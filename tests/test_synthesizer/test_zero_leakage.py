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


def test_authorization_feed_has_zero_target_labels():
    """AUTH_STREAM_COLUMNS must strictly exclude is_fraud and scenario_tag."""
    from fraudx_synthesizer.cli import AUTH_STREAM_COLUMNS, THREAT_INTEL_GRAPH_COLUMNS

    assert "is_fraud" not in AUTH_STREAM_COLUMNS, "Authorization feed must NOT leak target label is_fraud"
    assert "scenario_tag" not in AUTH_STREAM_COLUMNS, "Authorization feed must NOT leak scenario_tag"
    assert "syndicate_id" not in AUTH_STREAM_COLUMNS, "Authorization feed must NOT leak syndicate_id"

    # Threat intel graph columns must contain syndicate graph entities
    assert "syndicate_id" in THREAT_INTEL_GRAPH_COLUMNS
    assert "botnet_cluster_id" in THREAT_INTEL_GRAPH_COLUMNS


def test_classifier_non_trivial_roc_auc():
    """Linear classifier trained on point-in-time features must achieve realistic separability (0.80 - 0.99) without 1.0 leakage."""
    import numpy as np
    from sklearn.linear_model import LogisticRegression
    from sklearn.metrics import roc_auc_score

    engine = SimulationEngine(n_cards=200, n_merchants=50, seed=42)
    records = engine.generate_batch(n_transactions=1500, fraud_prevalence=0.06)

    X = []
    y = []
    for r in records:
        X.append([
            float(r["amount"]),
            float(r.get("tx_count_1h", 0)),
            float(r.get("tx_count_24h", 0)),
            float(r.get("haversine_velocity_kph", 0)),
            float(r.get("ip_distance_from_home_km", 0)),
            1.0 if r.get("is_cross_border") else 0.0,
            1.0 if str(r.get("avs_match_code", "Y")) in ("N", "U") else 0.0,
            1.0 if int(r.get("billing_shipping_match", 1)) == 0 else 0.0,
            float(r.get("cvv_match_flag", 1)),
            float(r.get("emv_arqc_verified", 0)),
            float(r.get("three_ds_authenticated", 0)),
        ])
        y.append(int(r["is_fraud"]))

    X = np.array(X)
    y = np.array(y)

    split = 1000
    clf = LogisticRegression(max_iter=1000)
    clf.fit(X[:split], y[:split])
    test_probs = clf.predict_proba(X[split:])[:, 1]
    auc = roc_auc_score(y[split:], test_probs)

    assert 0.80 <= auc <= 0.99, f"Expected realistic ROC-AUC in [0.80, 0.99], got {auc:.4f}"
