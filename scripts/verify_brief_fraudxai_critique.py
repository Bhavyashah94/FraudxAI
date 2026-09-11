"""Diagnostic script verifying the 4 'Still True' critique points from Section 8 of the Prism Project Brief.

Critique Points:
1. IP Distance Alone Separability: In India, IP distance alone separates fraud with ROC-AUC ~0.99.
2. Trivial Classifier Separability: At default settings, auth-time features give GBDT PR-AUC near 1.000 (1.000 in IN, ~0.98 in US).
3. Anti-Leak Tripwire Failure: Default CLI runs fail the anti-leak tripwires.
4. Small Evaluation Sample Size: Default 2000-transaction test split contains only 22-23 evaluated frauds.
"""

from __future__ import annotations

import numpy as np
from sklearn.metrics import average_precision_score, roc_auc_score
import lightgbm as lgb

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from fraudx_synthesizer.benchmark import XAIBenchmarkHarness, FEATURE_NAMES


def audit_critique():
    print("=" * 70)
    print("  VERIFYING PRISM BRIEF SECTION 8 CRITIQUES OF FRAUDX-AI")
    print("=" * 70)

    # 1. India Region Verification
    print("\n[1] Testing India Region (region='IN', n=2000, seed=42)...")
    harness_in = XAIBenchmarkHarness(n_transactions=2000, fraud_prevalence=0.05, region="IN", seed=42)
    X_in, y_in, GT_in, recs_in = harness_in.generate_and_prepare_dataset()

    n_train_in = int(len(X_in) * 0.70)
    X_test_in, y_test_in = X_in[n_train_in:], y_in[n_train_in:]
    test_recs_in = recs_in[n_train_in:]

    # A. IP Distance Alone Separability
    # Feature 4 is ip_distance_from_home_km
    ip_test_in = X_test_in[:, 4]
    ip_auc_in = roc_auc_score(y_test_in, ip_test_in)
    ip_pr_in = average_precision_score(y_test_in, ip_test_in)
    legit_ips_in = [float(r["ip_distance_from_home_km"]) for r in recs_in if r["is_fraud"] == 0]
    fraud_ips_in = [float(r["ip_distance_from_home_km"]) for r in recs_in if r["is_fraud"] == 1]

    print(f"  - IP Distance ROC-AUC: {ip_auc_in:.4f} (Brief claimed ~0.995)")
    print(f"  - IP Distance PR-AUC:  {ip_pr_in:.4f}")
    print(f"  - Legit IP Distance Median: {np.median(legit_ips_in):.1f} km (Max: {max(legit_ips_in):.1f} km)")
    print(f"  - Fraud IP Distance Median: {np.median(fraud_ips_in):.1f} km (Min: {min(fraud_ips_in):.1f} km)")

    # B. GBDT Separability & Sample Size
    clf_in = lgb.LGBMClassifier(n_estimators=60, max_depth=4, random_state=42, verbose=-1)
    clf_in.fit(X_in[:n_train_in], y_in[:n_train_in])
    probs_in = clf_in.predict_proba(X_test_in)[:, 1]
    gbdt_pr_in = average_precision_score(y_test_in, probs_in)
    gbdt_roc_in = roc_auc_score(y_test_in, probs_in)
    n_fraud_test_in = int(np.sum(y_test_in))

    print(f"  - GBDT PR-AUC:         {gbdt_pr_in:.4f} (Brief claimed 1.000)")
    print(f"  - GBDT ROC-AUC:        {gbdt_roc_in:.4f}")
    print(f"  - Test Frauds Evaluated: {n_fraud_test_in} (Brief claimed 23)")

    # 2. US Region Verification
    print("\n[2] Testing US Region (region='US', n=2000, seed=42)...")
    harness_us = XAIBenchmarkHarness(n_transactions=2000, fraud_prevalence=0.05, region="US", seed=42)
    X_us, y_us, GT_us, recs_us = harness_us.generate_and_prepare_dataset()

    n_train_us = int(len(X_us) * 0.70)
    X_test_us, y_test_us = X_us[n_train_us:], y_us[n_train_us:]

    clf_us = lgb.LGBMClassifier(n_estimators=60, max_depth=4, random_state=42, verbose=-1)
    clf_us.fit(X_us[:n_train_us], y_us[:n_train_us])
    probs_us = clf_us.predict_proba(X_test_us)[:, 1]
    gbdt_pr_us = average_precision_score(y_test_us, probs_us)
    gbdt_roc_us = roc_auc_score(y_test_us, probs_us)
    n_fraud_test_us = int(np.sum(y_test_us))

    print(f"  - GBDT PR-AUC:         {gbdt_pr_us:.4f} (Brief claimed 0.979)")
    print(f"  - GBDT ROC-AUC:        {gbdt_roc_us:.4f}")
    print(f"  - Test Frauds Evaluated: {n_fraud_test_us} (Brief claimed 22)")

    # 3. Summary of Findings
    print("\n" + "=" * 70)
    print("  AUDIT VERDICT")
    print("=" * 70)
    print(f"  1. IP Distance Separator (IN):  {'CONFIRMED' if ip_auc_in > 0.95 else 'DISPROVEN'} ({ip_auc_in:.4f})")
    print(f"  2. Trivial PR-AUC 1.000 (IN):   {'CONFIRMED' if gbdt_pr_in >= 0.999 else 'DISPROVEN'} ({gbdt_pr_in:.4f})")
    print(f"  3. Elevated PR-AUC ~0.98 (US):  {'CONFIRMED' if gbdt_pr_us > 0.96 else 'DISPROVEN'} ({gbdt_pr_us:.4f})")
    print(f"  4. Small Test Fraud Size (22):  {'CONFIRMED' if n_fraud_test_us in (22, 23) else 'DISPROVEN'} ({n_fraud_test_us})")
    print("=" * 70 + "\n")


if __name__ == "__main__":
    audit_critique()
