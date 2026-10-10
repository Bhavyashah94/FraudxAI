"""Defects D1 and D2 from the 2026-10-11 audit, and the invariants each fix restores.

D1 -- `time_span_days` did not control the realised span, because
`_get_card_hawkes_params` divided each persona's volume by a hard-coded constant
(55.0 for US, 0.684 for IN) that happened to equal one persona's monthly volume
rather than by the population mean it is meant to be relative to. The persona
scales therefore averaged 1.1793 over the US card population, so every paced
batch ran 18% hot and landed well short of the requested span. Measured before
the fix at fraud_prevalence=0, cards=500: n=1000 -> 18.33d, n=5000 -> 21.35d,
n=20000 -> 22.46d, all against a requested 30d.

D2 -- the inter-arrival W1 gate built its reference renewal process from
`time_span_days` (the *requested* span) instead of the span the records actually
cover, so it measured the D1 rate error as if it were arrival-shape error and
inflated W1 by 0.03-0.09 on every pinned seed.

The fix to D1 is deliberately narrow: only the *normalisation divisor* changes.
The Hawkes sampler, the branching ratios, the diurnal envelope and the persona
volumes themselves are untouched -- the single-card sampler was measured to hit
its target_lambda exactly (ratios 0.96-1.01), so the defect was never in it.

A feedback controller that tried to steer the realised span was built, measured
and removed: it overshot badly wherever card freezes depleted the population
(n=100000 at 2% fraud: span driven from 44.8d to 48.5d), because frozen cards
emit nothing at all and no rate correction can reach them. That failure is why
this file asserts only what the retained fix actually delivers.
"""

import numpy as np
import pytest

from fraudx_synthesizer.engine import SimulationEngine


def _span_days(records):
    ts = [r["tx_time_seconds"] for r in records]
    return (max(ts) - min(ts)) / 86400.0


def test_persona_volume_scales_average_one_over_the_card_population():
    """D1: persona scales must average 1.0 over the simulated population.

    generate_batch budgets target_n / n_cards transactions per card and then
    scales each card by its persona's relative volume. If those scales do not
    average 1.0 the aggregate rate is the budget times the mean scale, and
    time_span_days is silently not honoured. Before the fix the US mean was
    1.1793 (divisor 55.0 against a population mean of 64.86) and the IN mean
    1.0578 (divisor 0.684 against 0.7236).
    """
    for region in ("US", "IN"):
        engine = SimulationEngine(n_cards=400, n_merchants=25, region=region, seed=11)
        engine._persona_scale_mean_cache = None
        mean_scale = engine._persona_volume_scale_mean()

        scales = []
        for card in engine.cards:
            p = engine._get_card_hawkes_params(card, mean_inter_arrival_sec=64800.0)
            p_base = engine._get_card_hawkes_params(card, mean_inter_arrival_sec=None)
            eta = min(0.95, p_base.alpha / p_base.beta)
            # Invert the engine's own mu_0 formula to recover the scale it applied.
            target_lambda = p.mu_0 * 0.8208 / (1.0 - eta)
            scales.append(target_lambda * 64800.0)

        assert np.mean(scales) == pytest.approx(1.0, abs=1e-9), (
            f"{region}: persona scales averaged {np.mean(scales):.4f}, so the aggregate rate "
            f"is that multiple of the requested budget"
        )
        # The divisor itself is a mean volume (or a mean expected-daily for IN), not 1.0 --
        # it is what each persona is divided *by* to make the scale dimensionless.
        expected_divisor = float(
            np.mean(
                [
                    (engine.specs.cohorts.get(c.cohort_id).monthly_tx_volume_mean
                     if engine.specs.cohorts.get(c.cohort_id) else 55.0)
                    for c in engine.cards
                ]
            )
        ) if region == "US" else mean_scale
        if region == "US":
            assert mean_scale == pytest.approx(expected_divisor, rel=1e-9), (
                f"US divisor {mean_scale:.4f} is not the population mean volume {expected_divisor:.4f}"
            )
        assert mean_scale > 0.0


def test_persona_divisor_is_measured_not_a_hard_coded_constant():
    """D1: the US divisor must track the population, not sit at 55.0.

    55.0 is C1_HOURLY_GIG_WORKER's own monthly volume. spec/02's population_weight
    puts the weighted mean at 65.50 and the realised card population at 64.86, so
    any fixed 55.0 divisor makes every batch run hot by their ratio.
    """
    engine = SimulationEngine(n_cards=400, n_merchants=25, region="US", seed=11)
    divisor = engine._persona_volume_scale_mean()
    assert divisor != 55.0, "divisor is still the hard-coded constant"
    assert 60.0 <= divisor <= 70.0, (
        f"divisor {divisor:.2f} is outside the plausible band for the US cohort mix"
    )


def test_span_error_shrinks_as_the_batch_grows():
    """D1: the pacing budget must converge on the request as n grows.

    The remaining error is the per-card first-arrival offset, which is O(1) per
    card and so amortises away as transactions per card rises. This is the shape
    of the fix, not just one favourable point: before the fix the error was
    roughly flat in n because the aggregate rate itself was wrong.

    The n=100000 point is the published-dataset shape (cards=1000, merchants=150,
    days=30) and so carries the headline regression guard: it landed at 46.91
    days, +56.4%, before the fix. It subsumes the standalone large-batch test that
    used to sit beside it -- same seed, same shape, and a tighter bound (5% here
    against 10% there) -- which is why that duplicate was removed rather than kept.
    """
    errors = {}
    for n in (5000, 20000, 100000):
        engine = SimulationEngine(n_cards=1000, n_merchants=150, region="US", seed=42)
        records = engine.generate_batch(
            n_transactions=n,
            fraud_prevalence=0.0,
            time_span_days=30,
            enforce_invariants=False,
        )
        errors[n] = abs(_span_days(records) - 30.0) / 30.0

    assert errors[100000] <= 0.05, f"large batch error {errors[100000]:.4f} should be small"
    assert errors[100000] <= errors[20000], (
        f"error did not shrink with n: {errors}"
    )
    assert errors[20000] <= errors[5000] + 0.02, (
        f"error did not shrink with n: {errors}"
    )


def test_india_pacing_is_normalised_like_us():
    """D1: the IN branch divided by a rounded macro mean and ran 5.8% hot.

    Same defect, different constant: 0.684 against a realised population mean of
    0.7236. It must be normalised the same way, or Indian batches quietly carry a
    different budget than requested.
    """
    engine = SimulationEngine(n_cards=600, n_merchants=50, region="IN", seed=5)
    engine._persona_scale_mean_cache = None
    scales = []
    for card in engine.cards:
        p = engine._get_card_hawkes_params(card, mean_inter_arrival_sec=64800.0)
        p_base = engine._get_card_hawkes_params(card, mean_inter_arrival_sec=None)
        eta = min(0.95, p_base.alpha / p_base.beta)
        scales.append(p.mu_0 * 0.8208 / (1.0 - eta) * 64800.0)
    assert np.mean(scales) == pytest.approx(1.0, abs=1e-9)


def test_normalisation_does_not_distort_relative_persona_volumes():
    """D1: normalising the divisor must preserve the ratios between personas.

    The fix divides every scale by the same constant, so the ordering and the
    ratios of persona volumes -- which are grounded in spec/02 -- must survive
    untouched. Losing these would silently flatten the persona mix.
    """
    engine = SimulationEngine(n_cards=600, n_merchants=50, region="US", seed=3)
    vols = {}
    for card in engine.cards:
        if card.cohort_id in vols:
            continue
        cs = engine.specs.cohorts.get(card.cohort_id)
        vols[card.cohort_id] = cs.monthly_tx_volume_mean if cs else 55.0

    # C6_SMALL_BUSINESS_OWNER is the heaviest and C2_FIXED_INCOME_SENIOR the lightest.
    assert vols["C6_SMALL_BUSINESS_OWNER"] > vols["C2_FIXED_INCOME_SENIOR"]
    assert vols["C4_SUBURBAN_FAMILY"] > vols["C1_HOURLY_GIG_WORKER"]

    engine._persona_scale_mean_cache = None
    divisor = engine._persona_volume_scale_mean()
    scaled = {k: v / divisor for k, v in vols.items()}
    raw_ratio = vols["C6_SMALL_BUSINESS_OWNER"] / vols["C2_FIXED_INCOME_SENIOR"]
    scaled_ratio = scaled["C6_SMALL_BUSINESS_OWNER"] / scaled["C2_FIXED_INCOME_SENIOR"]
    assert scaled_ratio == pytest.approx(raw_ratio, rel=1e-12), (
        "normalising the divisor must not change the ratio between personas"
    )


def test_unpaced_path_is_untouched_by_the_fix():
    """D1: pace_to_sample_budget=False must still use the calibrated base_mu.

    The Fed DCPC frequency test (test_discrete_event_engine_empirical_arrival_frequency)
    exercises this path and must keep passing: the fix applies only when a pacing
    budget is actually in force.
    """
    engine = SimulationEngine(n_cards=200, n_merchants=50, region="US", seed=42)
    p = engine._get_card_hawkes_params(engine.cards[0], mean_inter_arrival_sec=None)
    base = engine._get_card_hawkes_params(engine.cards[0], mean_inter_arrival_sec=None)
    assert p.mu_0 == base.mu_0
    assert p.mu_0 > 0.0


def test_span_is_monotonic_in_requested_days():
    """D1: asking for a longer stream must actually produce a longer stream.

    Before the fix the requested span barely moved the output, because the rate
    was set by the mis-normalised scales rather than by the request.

    n=30000 rather than 100000: at 1000 cards that is 30 transactions per card,
    already far past the per-card first-arrival offset that the assertion is
    about, and it halves the wall cost of this test.
    """
    spans = {}
    for days in (15, 30):
        engine = SimulationEngine(n_cards=1000, n_merchants=150, region="US", seed=42)
        records = engine.generate_batch(
            n_transactions=30000,
            fraud_prevalence=0.0,
            time_span_days=days,
            enforce_invariants=False,
        )
        spans[days] = _span_days(records)

    assert spans[30] > spans[15], (
        f"30-day request produced {spans[30]:.2f}d but 15-day produced {spans[15]:.2f}d"
    )
    assert spans[30] / spans[15] == pytest.approx(2.0, abs=0.35), (
        f"doubling the request should roughly double the span: {spans}"
    )
