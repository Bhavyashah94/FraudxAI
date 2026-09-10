"""Tests verifying complete elimination of deterministic target label leakage."""

import pytest
from fraudx_synthesizer import SimulationEngine


def test_zero_deterministic_label_leakage():
    """Verifies that avs_match_code and billing_shipping_match do not leak ground truth."""
    engine = SimulationEngine(n_cards=300, n_merchants=80, seed=42)
    records = engine.generate_batch(n_transactions=2000, fraud_prevalence=0.08)

    cnp_records = [r for r in records if not r["channel_type"].startswith("CP")]
    assert len(cnp_records) > 200, "Should have substantial CNP transactions"

    # 1. AVS Match Code Leakage Verification
    # Legitimate transactions must sometimes have AVS mismatches ('N', 'A', 'Z')
    legit_cnp = [r for r in cnp_records if r["is_fraud"] == 0]
    legit_avs_mismatches = [r for r in legit_cnp if r["avs_match_code"] != "Y"]
    assert len(legit_avs_mismatches) > 0, "Legitimate CNP transactions must experience realistic AVS mismatches"

    # Fraudulent transactions must sometimes have valid AVS matches ('Y')
    fraud_cnp = [r for r in cnp_records if r["is_fraud"] == 1]
    fraud_avs_matches = [r for r in fraud_cnp if r["avs_match_code"] == "Y"]
    assert len(fraud_avs_matches) > 0, "Fraudulent CNP transactions must realistically sometimes match AVS"

    # 2. Billing/Shipping Match Leakage Verification
    # Legitimate CNP should sometimes have different shipping addresses (e.g. gifts)
    legit_billing_mismatch = [r for r in legit_cnp if r["billing_shipping_match"] == 0]
    assert len(legit_billing_mismatch) > 0, "Legitimate users must sometimes have billing != shipping"

    # Fraudulent CNP should sometimes have matching shipping address
    fraud_billing_match = [r for r in fraud_cnp if r["billing_shipping_match"] == 1]
    assert len(fraud_billing_match) > 0, "Fraudsters must sometimes use matched addresses"

    # 3. Deterministic Leakage Check
    # Neither feature should have 100% mutual information with is_fraud
    # i.e., avs_match_code == 'N' should not guarantee is_fraud == 1
    avs_n_records = [r for r in cnp_records if r["avs_match_code"] == "N"]
    p_fraud_given_avs_n = sum(r["is_fraud"] for r in avs_n_records) / len(avs_n_records)
    assert p_fraud_given_avs_n < 1.0, f"avs_match_code == 'N' must not leak 100% fraud, got {p_fraud_given_avs_n}"
    assert p_fraud_given_avs_n > 0.0, "avs_match_code == 'N' must correlate with fraud risk"
