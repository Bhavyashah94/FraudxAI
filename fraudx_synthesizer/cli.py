"""Command-line interface for FraudX-Synthesizer."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path

from .engine import SimulationEngine


AUTH_STREAM_COLUMNS = [
    "transaction_id",
    "card_id",
    "pan_masked",
    "product_id",
    "cohort_id",
    "timestamp_utc",
    "tx_time_seconds",
    "mti",
    "stan",
    "rrn",
    "auth_code",
    "response_code",
    "auth_response_code",
    "pos_entry_mode",
    "pos_condition_code",
    "eci",
    "trans_status_3ds",
    "vaai_score",
    "amount",
    "amount_minor",
    "currency",
    "available_balance",
    "credit_limit",
    "mcc",
    "merchant_id",
]

THREAT_INTEL_GRAPH_COLUMNS = [
    "transaction_id",
    "card_id",
    "merchant_id",
    "syndicate_id",
    "botnet_cluster_id",
    "mule_ring_id",
    "beneficiary_account_id",
    "ip_subnet_prefix",
    "device_fingerprint_id",
]

GATEWAY_TELEMETRY_COLUMNS = [
    "transaction_id",
    "timestamp_utc",
    "merchant_id",
    "mid",
    "tid",
    "acquirer_bin",
    "gateway_provider",
    "client_ip",
    "asn_type",
    "ip_distance_from_home_km",
    "device_canvas_hash",
    "channel_type",
    "avs_match_code",
    "cvv_match_flag",
    "geo_risk_score",
    "is_cross_border",
]

CLEARING_SETTLEMENT_COLUMNS = [
    "transaction_id",
    "clearing_mti",
    "clearing_delay_hours",
    "amount",
    "amount_minor",
    "settled_amount",
    "settled_amount_minor",
    "currency",
    "interchange_fee_minor",
    "mcc",
    "merchant_id",
    "mid",
    "acquirer_bin",
]

DISPUTE_RECOVERY_COLUMNS = [
    "transaction_id",
    "card_id",
    "amount",
    "currency",
    "is_fraud",
    "scenario_tag",
    "dispute_status",
    "dispute_reason_code",
    "ce3_qualified",
    "arbitration_fee_usd",
    "rbi_liability_tier",
    "rbi_provisional_credit_mandate_days",
    "cfcfrms_1930_lien_status",
]

DISPUTE_EXCLUDE_COLUMNS = {
    "dispute_status",
    "dispute_reason_code",
    "ce3_qualified",
    "arbitration_fee_usd",
    "rbi_liability_tier",
    "rbi_provisional_credit_mandate_days",
    "cfcfrms_1930_lien_status",
}


def _export_csv_view(file_path: Path, records: list[dict], fieldnames: list[str]) -> None:
    """Helper to export a projected institutional view table."""
    with open(file_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(records)


def cmd_generate(args: argparse.Namespace) -> None:
    """Generates a batch of synthetic transactions and saves to CSV or JSON."""
    engine = SimulationEngine(
        n_cards=args.cards,
        n_merchants=args.merchants,
        region=args.region,
        seed=args.seed,
    )
    print(
        f"Generating {args.n} transactions (region={args.region}, fraud_prevalence={args.fraud_rate}, seed={args.seed})...",
        file=sys.stderr,
    )
    records = engine.generate_batch(
        n_transactions=args.n,
        fraud_prevalence=args.fraud_rate,
        time_span_days=args.days,
    )

    out_path = Path(args.output)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    # Master output formatting
    export_records = records
    if not args.include_disputes:
        export_records = [
            {k: v for k, v in r.items() if k not in DISPUTE_EXCLUDE_COLUMNS}
            for r in records
        ]

    if out_path.suffix == ".json":
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(export_records, f, indent=2)
    elif out_path.suffix == ".jsonl":
        with open(out_path, "w", encoding="utf-8") as f:
            for r in export_records:
                f.write(json.dumps(r) + "\n")
    else:  # CSV default
        if export_records:
            all_keys = list({k: None for r in export_records for k in r.keys()}.keys())
            with open(out_path, "w", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=all_keys, extrasaction="ignore")
                writer.writeheader()
                writer.writerows(export_records)

    print(f"Successfully wrote {len(export_records)} transactions to {out_path}", file=sys.stderr)

    # Export partitioned institutional views if requested
    if args.export_institutional_views and records:
        parent_dir = out_path.parent
        stem = out_path.stem

        views = [
            (parent_dir / f"{stem}_auth_stream.csv", AUTH_STREAM_COLUMNS, "Authorization Feed (ISO 8583)"),
            (parent_dir / f"{stem}_gateway_telemetry.csv", GATEWAY_TELEMETRY_COLUMNS, "Gateway Risk Telemetry"),
            (parent_dir / f"{stem}_clearing_settlement.csv", CLEARING_SETTLEMENT_COLUMNS, "Clearing & Settlement Presentment"),
            (parent_dir / f"{stem}_dispute_recovery.csv", DISPUTE_RECOVERY_COLUMNS, "Dispute & Chargeback Recovery"),
            (parent_dir / f"{stem}_threat_intel_graph.csv", THREAT_INTEL_GRAPH_COLUMNS, "Threat Intelligence Graph Enclave"),
        ]

        for path, cols, label in views:
            _export_csv_view(path, records, cols)
            print(f"Exported {label} -> {path}", file=sys.stderr)


def cmd_benchmark(args: argparse.Namespace) -> None:
    """Executes empirical XAI or Tripartite industrial benchmark evaluation."""
    import json
    from dataclasses import asdict
    from pathlib import Path

    if getattr(args, "tripartite", False):
        from .benchmark import TripartiteBenchmarkHarness, generate_tripartite_markdown_report

        harness = TripartiteBenchmarkHarness(
            n_transactions=args.samples,
            fraud_prevalence=args.fraud_rate,
            region=args.region,
            seed=args.seed,
        )
        print(f"Executing Tripartite Industrial Benchmark on {args.samples} transactions ({args.region})...", file=sys.stderr)
        summary = harness.run_tripartite_benchmark()

        if args.json:
            print(json.dumps(asdict(summary), indent=2))
        else:
            report = generate_tripartite_markdown_report(summary)
            print("\n" + report + "\n")

        if getattr(args, "output_report", None):
            report_content = generate_tripartite_markdown_report(summary)
            Path(args.output_report).write_text(report_content, encoding="utf-8")
            print(f"Report saved to {args.output_report}", file=sys.stderr)

    else:
        from .benchmark import XAIBenchmarkHarness

        harness = XAIBenchmarkHarness(
            n_transactions=args.samples,
            fraud_prevalence=args.fraud_rate,
            region=args.region,
            seed=args.seed,
        )
        print(f"Executing XAI Benchmark on {args.samples} transactions ({args.model})...", file=sys.stderr)
        summary = harness.run_benchmark(model_type=args.model)

        if args.json:
            print(json.dumps(asdict(summary), indent=2))
        else:
            print("\n" + "=" * 65)
            print("  FRAUDX-AI EMPIRICAL XAI BENCHMARK RESULTS")
            print("=" * 65)
            print(f"  Model Architecture:           {summary.model_name.upper()}")
            print(f"  Explainer Method:             {summary.explainer_name}")
            print(f"  Evaluated Fraud Samples:      {summary.n_evaluated_samples}")
            print(f"  Classifier ROC-AUC:           {summary.auc_roc:.4f}")
            print(f"  Classifier PR-AUC:            {summary.pr_auc:.4f}")
            print("-" * 65)
            print(f"  Ranking Concordance (Kendall Tau):      {summary.mean_kendall_tau:.4f}")
            print(f"  Rank Correlation (Spearman Rho):        {summary.mean_spearman_rho:.4f}")
            print(f"  Directional Cosine Similarity:          {summary.mean_cosine_similarity:.4f}")
            print(f"  Top-3 Support Recovery (Precision@3):   {summary.mean_precision_at_3:.4f}")
            print(f"  Relative Attribution Error (RAE):       {summary.mean_relative_attribution_error:.4f}")
            print("=" * 65 + "\n")


def main() -> None:
    parser = argparse.ArgumentParser(prog="fraudx-sim", description="FraudX-Synthesizer CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Generate subcommand
    p_gen = subparsers.add_parser("generate", help="Generate batch transactions")
    p_gen.add_argument("-n", type=int, default=5000, help="Number of transactions to synthesize")
    p_gen.add_argument("--cards", type=int, default=1000, help="Number of simulated cardholders")
    p_gen.add_argument("--merchants", type=int, default=150, help="Number of simulated merchants")
    p_gen.add_argument("--region", type=str, choices=["US", "IN"], default="US", help="Geographic banking ecosystem: US (USD dual-message) or IN (INR RBI AFA/RuPay/CoFT)")
    p_gen.add_argument("--fraud-rate", type=float, default=0.02, help="Fraud prevalence ratio")
    p_gen.add_argument("--days", type=int, default=30, help="Simulation duration in days")
    p_gen.add_argument("--seed", type=int, default=42, help="Deterministic random seed")
    p_gen.add_argument("-o", "--output", type=str, default="synthetic_transactions.csv", help="Output file (.csv, .json, .jsonl)")
    p_gen.add_argument("--include-disputes", action="store_true", default=False, help="Include post-authorization dispute and chargeback lifecycle columns in master output")
    p_gen.add_argument("--export-institutional-views", action="store_true", default=False, help="Export partitioned institutional banking warehouse feeds")
    p_gen.set_defaults(func=cmd_generate)

    # Benchmark subcommand
    p_bench = subparsers.add_parser("benchmark", help="Run empirical XAI or Tripartite benchmark")
    p_bench.add_argument("-n", "--samples", type=int, default=2000, help="Number of synthetic transactions")
    p_bench.add_argument("--model", type=str, choices=["lightgbm", "rf"], default="lightgbm", help="ML model architecture")
    p_bench.add_argument("--region", type=str, choices=["US", "IN"], default="US", help="Banking ecosystem region")
    p_bench.add_argument("--fraud-rate", type=float, default=0.05, help="Fraud prevalence ratio")
    p_bench.add_argument("--seed", type=int, default=42, help="Deterministic seed")
    p_bench.add_argument("--tripartite", action="store_true", default=False, help="Run complete Tripartite Industrial Benchmark Suite")
    p_bench.add_argument("--output-report", type=str, default=None, help="Path to write Markdown certification report")
    p_bench.add_argument("--json", action="store_true", help="Output benchmark metrics in JSON format")
    p_bench.set_defaults(func=cmd_benchmark)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
