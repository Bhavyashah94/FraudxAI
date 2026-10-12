#!/usr/bin/env python3
"""Audit script for the 500k synthetic dataset to verify data quality and zero label leakage."""

import sys
from pathlib import Path
import polars as pl
import numpy as np
from sklearn.metrics import roc_auc_score, average_precision_score
import lightgbm as lgb

DATA_DIR = Path("/home/bshah/Projects/FraudxAI/staging_us_500k")
MASTER_FILE = DATA_DIR / "fraudxai_us_500k_seed42.csv"

def audit():
    print("[*] Starting rigorous data audit of 500k dataset...")
    
    # 1. File existence and row counts
    views = [
        "fraudxai_us_500k_seed42.csv",
        "fraudxai_us_500k_seed42_auth_stream.csv",
        "fraudxai_us_500k_seed42_gateway_telemetry.csv",
        "fraudxai_us_500k_seed42_clearing_settlement.csv",
        "fraudxai_us_500k_seed42_dispute_recovery.csv",
        "fraudxai_us_500k_seed42_threat_intel_graph.csv",
    ]
    
    for v in views:
        p = DATA_DIR / v
        if not p.exists():
            print(f"[FAIL] Missing file: {p}")
            sys.exit(1)
        with open(p, "rb") as f:
            lines = sum(1 for _ in f) - 1 # minus header
        print(f"  [OK] {v}: {lines:,} rows")
        if lines != 500000:
            print(f"[FAIL] Row count mismatch in {v}: expected 500,000, got {lines}")
            sys.exit(1)
            
    # 2. Master file invariants
    print("\n[*] Auditing master file invariants...")
    df = pl.read_csv(MASTER_FILE)
    
    fraud_count = df["is_fraud"].sum()
    fraud_rate = fraud_count / len(df)
    print(f"  Fraud count: {fraud_count:,} ({fraud_rate*100:.3f}%)")
    if fraud_rate < 0.015 or fraud_rate > 0.025:
        print(f"[FAIL] Fraud rate out of expected bounds: {fraud_rate}")
        sys.exit(1)
        
    t_min = df["timestamp_utc"].min()
    t_max = df["timestamp_utc"].max()
    print(f"  Time window: {t_min} to {t_max}")
    
    # Check monotonicity of time
    tx_times = df["tx_time_seconds"].to_numpy()
    if np.any(np.diff(tx_times) < 0):
        print("[FAIL] Time is not monotonically non-decreasing!")
        sys.exit(1)
    print("  [OK] Time sequence is monotonically non-decreasing.")
    
    # Check positive amounts
    amounts = df["amount"].to_numpy()
    if np.any(amounts <= 0):
        print("[FAIL] Zero or negative transaction amounts detected!")
        sys.exit(1)
    print(f"  [OK] Amounts strictly positive: min=${amounts.min():.2f}, max=${amounts.max():.2f}, mean=${amounts.mean():.2f}")
    
    # 3. Label quarantine check in modular views
    print("\n[*] Checking target label quarantine across modular views...")
    forbidden = {"is_fraud", "scenario_tag", "syndicate_id", "botnet_cluster_id", "mule_ring_id"}
    
    auth_cols = set(pl.read_csv(DATA_DIR / "fraudxai_us_500k_seed42_auth_stream.csv", n_rows=1).columns)
    gw_cols = set(pl.read_csv(DATA_DIR / "fraudxai_us_500k_seed42_gateway_telemetry.csv", n_rows=1).columns)
    settle_cols = set(pl.read_csv(DATA_DIR / "fraudxai_us_500k_seed42_clearing_settlement.csv", n_rows=1).columns)
    
    for name, cols in [("auth_stream", auth_cols), ("gateway_telemetry", gw_cols), ("clearing_settlement", settle_cols)]:
        leaks = cols.intersection(forbidden)
        if leaks:
            print(f"[FAIL] Label leakage in {name}: found {leaks}")
            sys.exit(1)
        print(f"  [OK] {name} has zero forbidden target labels.")
        
    # 4. Single-column shortcut check (ROC-AUC < 0.95)
    print("\n[*] Running single-column shortcut tripwire (ROC-AUC < 0.95)...")
    auth = pl.read_csv(DATA_DIR / "fraudxai_us_500k_seed42_auth_stream.csv")
    gw = pl.read_csv(DATA_DIR / "fraudxai_us_500k_seed42_gateway_telemetry.csv")
    disp = pl.read_csv(DATA_DIR / "fraudxai_us_500k_seed42_dispute_recovery.csv")
    
    joined = auth.join(gw.drop(["timestamp_utc", "merchant_id"]), on="transaction_id").join(disp.select(["transaction_id", "is_fraud"]), on="transaction_id")
    y = joined["is_fraud"].to_numpy()
    
    drop_cols = {
        "transaction_id", "card_id", "pan_masked", "merchant_id", "mid", "tid",
        "timestamp_utc", "client_ip", "device_canvas_hash", "auth_code", "is_fraud"
    }
    
    feature_cols = [c for c in joined.columns if c not in drop_cols]
    
    max_auc = 0.0
    top_col = ""
    for col in feature_cols:
        s = joined[col]
        if s.dtype == pl.String:
            s = s.cast(pl.Categorical).to_physical()
        vals = s.cast(pl.Float64, strict=False).fill_null(-1.0).to_numpy()
        if len(np.unique(vals)) < 2:
            continue
        auc = roc_auc_score(y, vals)
        if auc < 0.5:
            auc = 1.0 - auc
        if auc > max_auc:
            max_auc = auc
            top_col = col
        if auc >= 0.95:
            print(f"[FAIL] Single-column shortcut detected on {col}: ROC-AUC = {auc:.4f} >= 0.95")
            sys.exit(1)
            
    print(f"  [OK] Max single-column ROC-AUC: {max_auc:.4f} ({top_col}) - well below 0.95 gate.")
    
    # 5. Out-of-time pre-decision model PR-AUC benchmark
    print("\n[*] Evaluating out-of-time pre-decision LightGBM benchmark (80/20 temporal split)...")
    split_idx = int(len(joined) * 0.8)
    train_df = joined.slice(0, split_idx)
    test_df = joined.slice(split_idx, len(joined) - split_idx)
    
    cat_cols = [c for c in ["product_id", "cohort_id", "mti", "pos_entry_mode", "pos_condition_code", 
                            "trans_status_3ds", "currency", "channel_type", "avs_match_code", 
                            "cvv_match_flag", "asn_type", "gateway_provider"] if c in feature_cols]
    num_cols = [c for c in feature_cols if c not in cat_cols]
    
    X_train_num = train_df.select(num_cols).fill_null(-1.0).to_numpy()
    X_test_num = test_df.select(num_cols).fill_null(-1.0).to_numpy()
    
    cat_exprs = [pl.col(c).cast(pl.String).cast(pl.Categorical).to_physical().fill_null(-1) for c in cat_cols]
    X_train_cat = train_df.select(cat_exprs).to_numpy()
    X_test_cat = test_df.select(cat_exprs).to_numpy()
    
    X_train = np.hstack([X_train_num, X_train_cat])
    X_test = np.hstack([X_test_num, X_test_cat])
    y_train = train_df["is_fraud"].to_numpy()
    y_test = test_df["is_fraud"].to_numpy()
    
    clf = lgb.LGBMClassifier(n_estimators=100, learning_rate=0.05, random_state=42, verbose=-1)
    clf.fit(X_train, y_train)
    
    preds = clf.predict_proba(X_test)[:, 1]
    test_roc = roc_auc_score(y_test, preds)
    test_pr = average_precision_score(y_test, preds)
    
    print(f"  Out-of-time ROC-AUC: {test_roc:.4f}")
    print(f"  Out-of-time PR-AUC:  {test_pr:.4f}")
    
    if test_pr < 0.20 or test_pr > 0.97:
        print(f"[FAIL] Out-of-time PR-AUC {test_pr:.4f} out of valid bounds [0.20, 0.97]")
        sys.exit(1)
    print("  [OK] Out-of-time model PR-AUC is realistic and strictly within bounds.")
    
    print("\n[SUCCESS] All data audit and leakage gates PASSED with zero defects!")

if __name__ == "__main__":
    audit()
