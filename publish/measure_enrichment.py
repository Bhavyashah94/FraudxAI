"""Measure fraud enrichment of a published batch against its spec reference.

Runs the identical computation three times over independently re-read bytes and prints
the spread, because the figures below get published and a silent regression in this
measurement would corrupt the dataset card's honesty claim.

Usage:
    python publish/measure_enrichment.py <master.csv[.gz]> <spec_file> <region>
"""
import gzip
import sys

import pandas as pd
import yaml


def load(path):
    opener = gzip.open if str(path).endswith(".gz") else open
    with opener(path, "rt", newline="") as fh:
        return pd.read_csv(fh, usecols=["amount", "is_fraud", "currency"])


def measure(df):
    fraud_rows = df[df["is_fraud"] == 1]
    total_value = df["amount"].sum()
    fraud_value = fraud_rows["amount"].sum()
    return {
        "rows": len(df),
        "fraud_rows": len(fraud_rows),
        "count_prevalence": float(df["is_fraud"].mean()),
        "value_share_bps": float(fraud_value / total_value * 10_000),
        "mean_fraud_amount": float(fraud_rows["amount"].mean()),
        "mean_all_amount": float(df["amount"].mean()),
        "currency": str(df["currency"].iloc[0]),
    }


def reference(spec_file, region):
    spec = yaml.safe_load(open(spec_file))
    targets = {}
    for profile in spec["profiles"]:
        for t in profile["targets"]:
            targets[t["id"]] = t
    return targets


def main():
    path, spec_file, region = sys.argv[1], sys.argv[2], sys.argv[3]
    targets = reference(spec_file, region)

    # Three independent passes over freshly re-read bytes.
    runs = [measure(load(path)) for _ in range(3)]

    keys = [k for k in runs[0] if isinstance(runs[0][k], float)]
    unstable = [k for k in keys if len({round(r[k], 9) for r in runs}) != 1]
    if unstable:
        print(f"UNSTABLE across repeats: {unstable}")
        return 1

    m = runs[0]
    ref_count = targets["fraud_prevalence"]["target"]
    ref_value = targets["fraud_value_share_bps"]["target"]
    ref_amount = targets[
        "mean_fraud_amount_inr" if region == "IN" else "mean_fraud_amount_usd"
    ]["target"]

    print(f"file     : {path}")
    print(f"region   : {region}   currency: {m['currency']}")
    print(f"rows     : {m['rows']:,}   fraud rows: {m['fraud_rows']:,}")
    print(f"repeats  : 3/3 identical")
    print()
    print(f"{'metric':26s} {'measured':>14s} {'spec ref':>12s} {'ratio':>9s}")
    for label, got, ref in (
        ("count prevalence", m["count_prevalence"], ref_count),
        ("value share (bps)", m["value_share_bps"], ref_value),
        ("mean fraud amount", m["mean_fraud_amount"], ref_amount),
    ):
        print(f"{label:26s} {got:14.4f} {ref:12.4f} {got / ref:8.0f}x")
    print()
    print(f"mean ticket overall  : {m['mean_all_amount']:.2f}")
    print(
        f"fraud ticket / mean ticket : {m['mean_fraud_amount'] / m['mean_all_amount']:.2f}x"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())