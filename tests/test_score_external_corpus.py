"""Tests for the external-corpus Pillar 1 scorer (scripts/score_external_corpus.py).

The script exists to answer one question honestly -- *does real payment data pass
the thresholds our synthetic data fails?* -- which is only a meaningful question
if two properties hold, and both are asserted here:

1. It grades with the certification grader's own code and thresholds, so a
   difference between two corpora is a difference in data and not in arithmetic.
2. A corpus that does not carry a metric's inputs is not graded on that metric.
   The grader substitutes per-row defaults for missing keys (``mcc`` -> 5411,
   ``pos_entry_mode`` -> "01"), each of which makes its divergence trivially 0;
   a corpus missing those columns would otherwise be handed a pass it did not earn.
"""

import importlib.util
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
_SCRIPT = REPO_ROOT / "scripts" / "score_external_corpus.py"


@pytest.fixture(scope="module")
def scorer():
    """Load scripts/score_external_corpus.py as a module (it is not a package)."""
    spec = importlib.util.spec_from_file_location("score_external_corpus", _SCRIPT)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def test_missing_columns_are_excluded_from_the_verdict(scorer):
    """A corpus without an MCC column is graded on 2 metrics, not 5."""
    records = [
        {"amount": 25.0, "tx_time_seconds": float(t)}
        for t in range(0, 100_000, 500)
    ]
    result = scorer.score("bare", records, {"n": len(records), "time_span_days": 100_000 / 86_400.0}, "US", 42)

    by_metric = {row["metric"]: row for row in result["metrics"]}
    assert by_metric["wasserstein_amount_log"]["comparable"] is True
    assert by_metric["wasserstein_arrival_log"]["comparable"] is True

    for metric in ("js_divergence_mcc", "js_divergence_channel", "spearman_frobenius_error"):
        assert by_metric[metric]["comparable"] is False, metric
        assert by_metric[metric]["pass"] is None, metric
        assert by_metric[metric]["missing_inputs"], metric

    assert result["comparable_metrics"] == 2
    assert result["verdict"] in {"PASS", "FAIL"}  # verdict covers the comparable subset only


def test_scorer_reproduces_the_graders_own_number(scorer):
    """Same seed, same batch: the script's figures equal the reporter's scorecard."""
    from fraudx_synthesizer.benchmark_reporter import UnifiedBenchmarkRunner

    n, region, seed = 400, "US", 7
    records, summary = scorer.generate_synthetic(n, region, seed)

    runner = UnifiedBenchmarkRunner(
        region=region, n_transactions=n, time_span_days=summary["time_span_days"], seed=seed
    )
    reference = runner._evaluate_data_fidelity(records)
    result = scorer.score("synthetic", records, summary, region, seed)

    by_metric = {row["metric"]: row for row in result["metrics"]}
    assert by_metric["wasserstein_amount_log"]["value"] == pytest.approx(reference.wasserstein_amount_log, abs=1e-9)
    assert by_metric["wasserstein_arrival_log"]["value"] == pytest.approx(reference.wasserstein_arrival_log, abs=1e-9)
    assert by_metric["js_divergence_mcc"]["value"] == pytest.approx(reference.js_divergence_mcc, abs=1e-9)
    assert all(row["comparable"] for row in result["metrics"])  # synthetic carries every input
    assert result["threshold_source"].endswith("spec/18_benchmark_reporting.yaml")


def test_reference_sampler_control_passes_the_continuous_gates(scorer):
    """A stream drawn from the reference itself must pass it -- that is the point.

    This documents what the two continuous gates measure: distance to the
    hardcoded reference. If this control ever *fails*, the control or the
    reference has drifted and the external scorecard should not be trusted.
    """
    records, summary = scorer.reference_control(4_000, "US", 42)
    result = scorer.score("control", records, summary, "US", 42)

    by_metric = {row["metric"]: row for row in result["metrics"]}
    assert by_metric["wasserstein_amount_log"]["pass"] is True
    assert by_metric["wasserstein_amount_log"]["value"] < 0.05
    assert by_metric["wasserstein_arrival_log"]["pass"] is True
    assert by_metric["wasserstein_arrival_log"]["value"] < 0.05
    assert result["verdict"] == "PASS"
