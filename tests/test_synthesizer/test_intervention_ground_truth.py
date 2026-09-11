"""Automated verification suite for zero synthetic leaks, EMV chip primacy, and intervention recovery.

Verifies:
1. Zero synthetic IP distance zeros (every attack scenario operates across realistic non-zero network distances >= 1.5 km).
2. Hardware cryptographic primacy: Authentic EMV Chip+PIN transactions never receive ISO 59 false declines.
3. Attack script intervention support recovery: TreeSHAP achieves high Precision@3 against canonical attack interventions.
4. Anti-leak tripwires: PR-AUC remains realistic (<= 0.96) with no single feature holding >70% attribution.
"""

import pytest
import numpy as np

from fraudx_synthesizer import (
    DiscreteEventEngine,
    XAIBenchmarkHarness,
)
from fraudx_synthesizer.agents import ISO8583Response


def test_zero_synthetic_ip_distance_leak():
    """Asserts that zero synthetic zeros exist for ip_distance_from_home_km across all fraud playbooks."""
    engine = DiscreteEventEngine(n_cards=300, n_merchants=50, region="US", seed=101)
    records = engine.generate_batch(n_transactions=2000, fraud_prevalence=0.06)

    fraud_records = [r for r in records if r["is_fraud"] == 1]
    assert len(fraud_records) >= 50, f"Insufficient fraud records generated: {len(fraud_records)}"

    fraud_ip_distances = [float(r["ip_distance_from_home_km"]) for r in fraud_records]
    min_fraud_ip = min(fraud_ip_distances)

    # Invariant: Min IP distance across all fraud attacks must be >= 1.5 km (no synthetic 0.0 leak)
    assert min_fraud_ip >= 1.5, f"Synthetic IP distance leak detected: min distance is {min_fraud_ip} km"

    # Invariant: A trivial threshold rule ip_distance <= 0.5 must capture exactly 0 fraud transactions
    trivial_split_frauds = [d for d in fraud_ip_distances if d <= 0.5]
    assert len(trivial_split_frauds) == 0, f"Trivial split <= 0.5 km captured {len(trivial_split_frauds)} frauds!"


def test_legitimate_hard_negatives_approval_primacy():
    """Asserts that authentic EMV Chip+PIN transactions maintain cryptographic primacy and are never falsely declined as ISO 59."""
    engine_in = DiscreteEventEngine(n_cards=300, n_merchants=50, region="IN", seed=202)
    # Generate batch during festive Diwali window with high-ticket gold transactions
    records_in = engine_in.generate_batch(
        n_transactions=1500,
        fraud_prevalence=0.03,
        active_macro_regime="DHANTERAS_DIWALI",
    )

    dhanteras_recs = [r for r in records_in if "DHANTERAS" in r.get("scenario_tag", "")]
    assert len(dhanteras_recs) > 0, "No Dhanteras gold splitting transactions generated"

    # All authentic EMV contact chip transactions must never be declined as ISO 59 (Suspected Fraud)
    chip_recs = [r for r in records_in if r.get("channel_type") == "CP_POS_CHIP" and r.get("is_fraud") == 0]
    iso_59_declines = [r for r in chip_recs if r.get("response_code") == ISO8583Response.SUSPECTED_FRAUD_59.value]
    assert len(iso_59_declines) == 0, f"EMV Chip+PIN received {len(iso_59_declines)} false ISO 59 declines!"

    # Overall approval rate for legitimate Chip transactions must be >= 85%
    # (Remaining declines are purely solvency-based ISO 51 Insufficient Funds from credit limits)
    approved_chip = [r for r in chip_recs if r.get("response_code") == ISO8583Response.APPROVED_00.value]
    chip_approval_rate = len(approved_chip) / len(chip_recs)
    assert chip_approval_rate >= 0.85, f"Legitimate Chip approval rate dropped to {chip_approval_rate:.3f}"


def test_treeshap_intervention_recovery_and_anti_leak_tripwires():
    """Asserts that TreeSHAP recovers attack script interventions and satisfies anti-leak tripwires."""
    harness = XAIBenchmarkHarness(
        n_transactions=1500,
        fraud_prevalence=0.06,
        region="US",
        seed=303,
    )
    summary = harness.run_benchmark(model_type="lightgbm")

    # 1. Anti-leak tripwire: PR-AUC must not be trivial 1.000 (realistic non-leaking data <= 0.96)
    assert summary.anti_leak_tripwire_passed is True, "Anti-leak tripwire failed!"
    assert summary.pr_auc <= 0.96, f"PR-AUC {summary.pr_auc:.4f} indicates synthetic leakage (> 0.96)"

    # 2. Intervention Support Recovery: Precision@3 must be >= 0.65 against attack script interventions
    assert summary.mean_intervention_precision_at_3 >= 0.65, (
        f"Intervention Precision@3 {summary.mean_intervention_precision_at_3:.4f} is below 0.65 threshold"
    )

    # 3. OpenXAI / Quantus metrics: Directional cosine similarity and Kendall tau positive
    assert summary.mean_cosine_similarity > 0.35, (
        f"Directional cosine similarity {summary.mean_cosine_similarity:.4f} is too low"
    )
    assert summary.mean_kendall_tau > 0.20, (
        f"Kendall tau ranking concordance {summary.mean_kendall_tau:.4f} is too low"
    )
