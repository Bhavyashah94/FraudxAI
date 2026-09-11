"""Real-time streaming daemon for FraudX-Synthesizer.

Provides high-throughput transaction streaming to REST endpoints or stdout
with zero PRISM-X coupling, asynchronous dispatch, and deterministic replaying.
"""

from __future__ import annotations

import argparse
import asyncio
from datetime import datetime, timezone
import json
import math
from pathlib import Path
import sys
import time
import urllib.request
import urllib.error
from typing import Any, Dict, List, Optional, Tuple

import numpy as np

from .engine import SimulationEngine


async def dispatch_transaction_async(
    endpoint: str,
    record: Dict[str, Any],
    timeout_sec: float = 2.0,
) -> Tuple[bool, int, float]:
    """Asynchronously dispatches a JSON transaction payload to a target REST endpoint."""
    loop = asyncio.get_running_loop()
    payload = json.dumps(record).encode("utf-8")
    req = urllib.request.Request(
        endpoint,
        data=payload,
        headers={"Content-Type": "application/json"},
        method="POST",
    )

    t0 = time.perf_counter()

    def _sync_post():
        try:
            with urllib.request.urlopen(req, timeout=timeout_sec) as resp:
                return True, resp.status
        except urllib.error.HTTPError as e:
            return False, e.code
        except Exception:
            return False, 0

    success, status_code = await loop.run_in_executor(None, _sync_post)
    elapsed_ms = (time.perf_counter() - t0) * 1000.0
    return success, status_code, elapsed_ms


async def run_stream_daemon(
    endpoint: Optional[str] = None,
    duration_sec: float = 60.0,
    target_tps: float = 5.0,
    fraud_prevalence: float = 0.02,
    seed: int = 42,
    to_stdout: bool = False,
) -> None:
    """Executes continuous streaming transaction emission loop."""
    engine = SimulationEngine(n_cards=500, n_merchants=100, seed=seed)
    print(
        f"[FraudX-Synthesizer Stream Daemon] Initialized (seed={seed}, target_tps={target_tps}, duration={duration_sec}s)",
        file=sys.stderr,
    )

    count = 0
    t_start = time.time()
    for record in engine.stream_continuous(
        duration_seconds=duration_sec,
        target_tps=target_tps,
        fraud_prevalence=fraud_prevalence,
    ):
        count += 1
        if to_stdout or endpoint is None:
            print(json.dumps(record))
            sys.stdout.flush()
        else:
            success, code, latency = await dispatch_transaction_async(endpoint, record)
            if not success:
                print(f"[WARN] Failed dispatch {record['transaction_id']} (HTTP {code})", file=sys.stderr)

        # Rate limiting sleep
        await asyncio.sleep(1.0 / max(target_tps, 0.1))

    total_time = time.time() - t_start
    print(
        f"[FraudX-Synthesizer Stream Daemon] Finished: {count} transactions in {total_time:.2f}s ({count / max(total_time, 0.01):.1f} TPS)",
        file=sys.stderr,
    )


def main():
    parser = argparse.ArgumentParser(description="FraudX-Synthesizer Streaming CLI")
    parser.add_argument("--endpoint", type=str, default=None, help="Target REST API URL (e.g. http://localhost:8000/api/v1/predict)")
    parser.add_argument("--duration", type=float, default=30.0, help="Stream duration in seconds")
    parser.add_argument("--tps", type=float, default=5.0, help="Target transactions per second")
    parser.add_argument("--fraud-rate", type=float, default=0.03, help="Adversarial fraud ratio (0.0 to 1.0)")
    parser.add_argument("--seed", type=int, default=42, help="Deterministic random seed")
    parser.add_argument("--stdout", action="store_true", help="Print transactions to stdout as JSON lines")

    args = parser.parse_args()
    asyncio.run(run_stream_daemon(
        endpoint=args.endpoint,
        duration_sec=args.duration,
        target_tps=args.tps,
        fraud_prevalence=args.fraud_rate,
        seed=args.seed,
        to_stdout=args.stdout,
    ))


INFERENCE_ALLOWLIST = {
    "transaction_id", "card_id", "pan_masked", "product_id", "cohort_id",
    "merchant_id", "merchant_name", "mid", "tid", "mcc", "merchant_category",
    "merchant_lat", "merchant_lon", "acquirer_bin", "gateway_provider",
    "country_code", "postal_code", "timestamp_utc", "tx_time_seconds",
    "hour_of_day", "day_of_week", "amount", "amount_minor", "currency",
    "channel_type", "credit_limit", "current_balance", "available_balance",
    "user_avg_tx_amount_30d", "user_std_tx_amount_30d", "z_score_amount_30d",
    "tx_count_1h", "tx_count_24h", "tx_amount_sum_24h", "distinct_merchants_24h",
    "distance_from_last_tx_km", "time_since_last_tx_seconds", "haversine_velocity_kph",
    "ip_distance_from_home_km", "client_ip", "asn_type", "geo_risk_score",
    "device_canvas_hash", "is_cross_border", "billing_shipping_match",
    "avs_match_code", "cvv_match_flag", "mti", "stan", "rrn", "auth_code",
    "response_code", "auth_response_code", "pos_entry_mode", "pos_condition_code",
    "eci", "trans_status_3ds", "vaai_score", "clearing_mti", "clearing_delay_hours",
    "settled_amount", "settled_amount_minor", "interchange_fee_minor",
    "hawkes_intensity_R",
}


class ZeroLeakageDataPartitioner:
    """Partitions unified synthetic transactions into 3 legally and architecturally isolated feeds."""

    def __init__(self, mean_chargeback_lag_days: float = 21.0, seed: int = 42):
        self.mean_chargeback_lag_days = mean_chargeback_lag_days
        self.rng = np.random.default_rng(seed)

    def partition_record(self, record: Dict[str, Any]) -> Tuple[Dict[str, Any], Dict[str, Any], Dict[str, Any]]:
        """Splits an individual record into (inference_feed, delayed_labels, threat_intel_graph_enclave)."""
        # 1. Inference Feed (strictly point-in-time, zero target labels, zero graph ids)
        inference_feed = {k: v for k, v in record.items() if k in INFERENCE_ALLOWLIST}

        # 2. Delayed Labels (empirical chargeback / dispute maturity lag)
        tx_time_sec = float(record.get("tx_time_seconds", 0.0))
        # Log-normal chargeback reporting lag (mean ~ 21 days, range 3 to 120 days)
        delay_days = float(self.rng.lognormal(mean=math.log(max(1.0, self.mean_chargeback_lag_days)), sigma=0.35))
        delay_days = max(3.0, min(120.0, delay_days))
        maturity_sec = tx_time_sec + delay_days * 86400.0
        maturity_dt = datetime.fromtimestamp(maturity_sec, tz=timezone.utc).isoformat()

        delayed_labels = {
            "transaction_id": record.get("transaction_id", ""),
            "card_id": record.get("card_id", ""),
            "is_fraud": int(record.get("is_fraud", 0)),
            "scenario_tag": str(record.get("scenario_tag", "")),
            "tx_timestamp_utc": record.get("timestamp_utc", ""),
            "label_maturity_timestamp_utc": maturity_dt,
            "chargeback_delay_days": round(delay_days, 1),
            "dispute_status": record.get("dispute_status", "NONE"),
            "dispute_reason_code": record.get("dispute_reason_code", ""),
            "rbi_liability_tier": record.get("rbi_liability_tier", ""),
        }

        # 3. Threat Intel Graph Enclave (isolated syndicate and network topology)
        threat_intel_graph_enclave = {
            "transaction_id": record.get("transaction_id", ""),
            "card_id": record.get("card_id", ""),
            "merchant_id": record.get("merchant_id", ""),
            "syndicate_id": record.get("syndicate_id", ""),
            "botnet_cluster_id": record.get("botnet_cluster_id", ""),
            "mule_ring_id": record.get("mule_ring_id", ""),
            "beneficiary_account_id": record.get("beneficiary_account_id", ""),
            "ip_subnet_prefix": record.get("ip_subnet_prefix", ""),
            "device_fingerprint_id": record.get("device_fingerprint_id", ""),
            "asn_type": record.get("asn_type", "residential"),
            "client_ip": record.get("client_ip", "127.0.0.1"),
            "is_fraud": int(record.get("is_fraud", 0)),
            "scenario_tag": str(record.get("scenario_tag", "")),
        }

        return inference_feed, delayed_labels, threat_intel_graph_enclave

    def partition_batch(
        self,
        records: List[Dict[str, Any]],
    ) -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]], List[Dict[str, Any]]]:
        """Partitions an entire batch of records into 3 feeds."""
        inf_batch: List[Dict[str, Any]] = []
        labels_batch: List[Dict[str, Any]] = []
        graph_batch: List[Dict[str, Any]] = []

        for r in records:
            inf, lbl, grp = self.partition_record(r)
            inf_batch.append(inf)
            labels_batch.append(lbl)
            graph_batch.append(grp)

        return inf_batch, labels_batch, graph_batch

    def export_partitioned_feeds(
        self,
        records: List[Dict[str, Any]],
        output_dir: str | Path,
    ) -> Dict[str, Path]:
        """Writes the 3 partitioned feeds to output directory as JSON lines."""
        out_path = Path(output_dir)
        out_path.mkdir(parents=True, exist_ok=True)

        inf_batch, labels_batch, graph_batch = self.partition_batch(records)

        paths = {
            "inference_feed": out_path / "inference_feed.jsonl",
            "delayed_labels": out_path / "delayed_labels.jsonl",
            "threat_intel_graph_enclave": out_path / "threat_intel_graph_enclave.jsonl",
        }

        for feed_name, file_path in paths.items():
            data = inf_batch if feed_name == "inference_feed" else (
                labels_batch if feed_name == "delayed_labels" else graph_batch
            )
            with open(file_path, "w", encoding="utf-8") as f:
                for row in data:
                    f.write(json.dumps(row) + "\n")

        return paths


if __name__ == "__main__":
    main()
