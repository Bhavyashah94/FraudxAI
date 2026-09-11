"""High-capacity streaming dataset storage, parallel simulation, and aggregations."""

from __future__ import annotations

import json
import math
import os
import sys
import time
from collections import Counter, defaultdict
from concurrent.futures import ProcessPoolExecutor, as_completed
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, Generator, Iterable, List, Optional, Tuple

import numpy as np
import polars as pl

# Institutional schema definitions
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


@dataclass
class SimulationAggregates:
    """Running global telemetry across arbitrary-scale transaction streams."""
    total_transactions: int = 0
    approved_count: int = 0
    declined_count: int = 0
    total_fraud_count: int = 0
    total_volume: float = 0.0
    total_fraud_volume: float = 0.0
    
    # 4-hop switch funnels
    hop_drops: Dict[str, int] = field(default_factory=lambda: defaultdict(int))
    iso_codes: Dict[str, int] = field(default_factory=lambda: defaultdict(int))
    macro_options: Dict[str, int] = field(default_factory=lambda: defaultdict(int))
    
    # Temporal distributions (24-hour diurnal bins)
    hourly_legit: List[int] = field(default_factory=lambda: [0] * 24)
    hourly_fraud: List[int] = field(default_factory=lambda: [0] * 24)
    
    # Threat graph clusters
    syndicates: Dict[str, int] = field(default_factory=lambda: defaultdict(int))
    botnets: Dict[str, int] = field(default_factory=lambda: defaultdict(int))
    merchants_fraud: Dict[str, float] = field(default_factory=lambda: defaultdict(float))
    mules_fraud: Dict[str, float] = field(default_factory=lambda: defaultdict(float))
    
    # Top sampled threat interactions for graph visualization (capped to avoid memory blowup)
    threat_edges: List[Dict[str, Any]] = field(default_factory=list)
    threat_nodes_map: Dict[str, Dict[str, Any]] = field(default_factory=dict)
    max_retained_nodes: int = 25000

    def update(self, records: List[Dict[str, Any]]) -> None:
        """Incrementally updates running aggregates from a batch of transaction records."""
        for r in records:
            self.total_transactions += 1
            amt = float(r.get("amount", 0.0))
            is_fraud = int(r.get("is_fraud", 0))
            resp = str(r.get("response_code", "00"))
            is_app = resp in ("00", "10", "ISO_00", "ISO_10") or resp.endswith("00") or resp.endswith("10")
            
            if is_app:
                self.approved_count += 1
            else:
                self.declined_count += 1
                
            self.total_volume += amt
            self.iso_codes[resp] += 1
            
            hop = str(r.get("hop_origin", "ISSUER_HOST"))
            self.hop_drops[hop] += 1
            
            macro = str(r.get("scenario_tag", "UNKNOWN"))
            self.macro_options[macro] += 1
            
            hr = int(r.get("hour_of_day", 0)) % 24
            if is_fraud:
                self.total_fraud_count += 1
                self.total_fraud_volume += amt
                self.hourly_fraud[hr] += 1
                
                # Threat network updates
                syn = str(r.get("syndicate_id", "SYN_UNASSIGNED"))
                bot = str(r.get("botnet_cluster_id", "BOT_UNASSIGNED"))
                mer = str(r.get("merchant_id", "MER_UNASSIGNED"))
                mule = str(r.get("mule_ring_id", "MULE_UNASSIGNED"))
                
                self.syndicates[syn] += 1
                self.botnets[bot] += 1
                self.merchants_fraud[mer] += amt
                self.mules_fraud[mule] += amt
                
                # Graph sampling for visualizer
                if len(self.threat_nodes_map) < self.max_retained_nodes:
                    card_id = str(r.get("card_id", "CARD_UNKNOWN"))
                    # Register nodes
                    if syn not in self.threat_nodes_map:
                        self.threat_nodes_map[syn] = {"id": syn, "type": "SYNDICATE", "label": syn, "volume": 0}
                    self.threat_nodes_map[syn]["volume"] += 1

                    if bot not in self.threat_nodes_map:
                        self.threat_nodes_map[bot] = {"id": bot, "type": "BOTNET", "label": bot, "volume": 0}
                    self.threat_nodes_map[bot]["volume"] += 1

                    if card_id not in self.threat_nodes_map:
                        self.threat_nodes_map[card_id] = {
                            "id": card_id,
                            "type": "CARD",
                            "label": card_id,
                            "tier": str(r.get("product_id", "CREDIT")),
                            "volume": 0,
                        }
                    self.threat_nodes_map[card_id]["volume"] += 1

                    if mer not in self.threat_nodes_map:
                        self.threat_nodes_map[mer] = {"id": mer, "type": "MERCHANT", "label": mer, "volume": 0}
                    self.threat_nodes_map[mer]["volume"] += 1

                    if mule not in self.threat_nodes_map:
                        self.threat_nodes_map[mule] = {"id": mule, "type": "MULE_RING", "label": mule, "volume": 0}
                    self.threat_nodes_map[mule]["volume"] += 1

                    # Register representative edges
                    if len(self.threat_edges) < self.max_retained_nodes * 2:
                        self.threat_edges.append({"source": syn, "target": bot, "type": "CONTROLS"})
                        self.threat_edges.append({"source": bot, "target": card_id, "type": "TARGETS"})
                        self.threat_edges.append({"source": card_id, "target": mer, "type": "PURCHASES"})
                        self.threat_edges.append({"source": mer, "target": mule, "type": "FUNNELS"})
            else:
                self.hourly_legit[hr] += 1

    def to_dict(self) -> Dict[str, Any]:
        """Serializes aggregates into a JSON-serializable dictionary."""
        return {
            "total_transactions": self.total_transactions,
            "approved_count": self.approved_count,
            "declined_count": self.declined_count,
            "approval_rate": self.approved_count / max(1, self.total_transactions),
            "total_fraud_count": self.total_fraud_count,
            "fraud_prevalence": self.total_fraud_count / max(1, self.total_transactions),
            "total_volume": round(self.total_volume, 2),
            "total_fraud_volume": round(self.total_fraud_volume, 2),
            "hop_drops": dict(self.hop_drops),
            "iso_codes": dict(self.iso_codes),
            "macro_options": dict(self.macro_options),
            "hourly_distribution": {
                "hours": list(range(24)),
                "legitimate": self.hourly_legit,
                "fraud": self.hourly_fraud,
            },
            "top_syndicates": dict(sorted(self.syndicates.items(), key=lambda x: x[1], reverse=True)[:20]),
            "top_botnets": dict(sorted(self.botnets.items(), key=lambda x: x[1], reverse=True)[:20]),
            "top_target_merchants": dict(sorted(self.merchants_fraud.items(), key=lambda x: x[1], reverse=True)[:20]),
            "top_mule_rings": dict(sorted(self.mules_fraud.items(), key=lambda x: x[1], reverse=True)[:20]),
            "graph_summary": {
                "nodes_count": len(self.threat_nodes_map),
                "edges_count": len(self.threat_edges),
            }
        }


class StreamingDatasetWriter:
    """Streams transactions to partitioned Parquet and/or CSV files with zero OOM risk."""

    def __init__(
        self,
        output_dir: str | Path,
        export_parquet: bool = True,
        export_csv: bool = False,
        chunk_size: int = 50000,
        max_retained_nodes: int = 25000,
    ):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.export_parquet = export_parquet
        self.export_csv = export_csv
        self.chunk_size = chunk_size
        
        self.aggregates = SimulationAggregates(max_retained_nodes=max_retained_nodes)
        self.chunk_idx = 0

        # Create table subdirectories
        self.tables = {
            "auth_stream": (self.output_dir / "auth_stream", AUTH_STREAM_COLUMNS),
            "threat_intel_graph": (self.output_dir / "threat_intel_graph", THREAT_INTEL_GRAPH_COLUMNS),
            "gateway_telemetry": (self.output_dir / "gateway_telemetry", GATEWAY_TELEMETRY_COLUMNS),
            "clearing_settlement": (self.output_dir / "clearing_settlement", CLEARING_SETTLEMENT_COLUMNS),
            "dispute_recovery": (self.output_dir / "dispute_recovery", DISPUTE_RECOVERY_COLUMNS),
        }
        for table_dir, _ in self.tables.values():
            table_dir.mkdir(parents=True, exist_ok=True)

    def write_chunk(self, records: List[Dict[str, Any]]) -> None:
        """Flushes a batch of transactions across all 5 institutional tables."""
        if not records:
            return

        # 1. Update running aggregates
        self.aggregates.update(records)

        # 2. Convert batch to Polars DataFrame (very fast Rust backing)
        df_batch = pl.DataFrame(records, strict=False)

        part_name = f"part_{self.chunk_idx:05d}"

        # 3. Write each institutional view table
        for table_name, (table_dir, cols) in self.tables.items():
            # Select available columns
            avail_cols = [c for c in cols if c in df_batch.columns]
            table_df = df_batch.select(avail_cols)

            if self.export_parquet:
                pq_path = table_dir / f"{part_name}.parquet"
                table_df.write_parquet(pq_path, compression="zstd")

            if self.export_csv:
                csv_path = table_dir / f"{part_name}.csv"
                table_df.write_csv(csv_path)

        self.chunk_idx += 1

    def finalize(self) -> Dict[str, Any]:
        """Saves metadata summary and returns consolidated telemetry."""
        meta = self.aggregates.to_dict()
        meta_path = self.output_dir / "simulation_metadata.json"
        with open(meta_path, "w", encoding="utf-8") as f:
            json.dump(meta, f, indent=2)

        # Also write sampled threat graph for direct visualization consumption
        graph_data = {
            "nodes": list(self.aggregates.threat_nodes_map.values()),
            "links": self.aggregates.threat_edges,
        }
        graph_path = self.output_dir / "threat_graph_sample.json"
        with open(graph_path, "w", encoding="utf-8") as f:
            json.dump(graph_data, f, indent=2)

        return meta


def _worker_simulation_task(
    worker_id: int,
    n_tx_target: int,
    region: str,
    output_dir: str,
    chunk_size: int,
    adversary_mode: str,
    seed: int,
) -> Dict[str, Any]:
    """Isolated worker simulation task generating a disjoint shard of transactions."""
    from fraudx_synthesizer.engine import DiscreteEventEngine

    worker_dir = Path(output_dir) / f"worker_{worker_id}"
    writer = StreamingDatasetWriter(
        output_dir=worker_dir,
        export_parquet=True,
        export_csv=False,
        chunk_size=chunk_size,
    )

    # Scale population proportionally with safe per-process memory caps
    n_cards = min(5000, max(500, n_tx_target // 20))
    n_merchants = min(500, max(50, n_tx_target // 200))

    engine = DiscreteEventEngine(
        n_cards=n_cards,
        n_merchants=n_merchants,
        region=region,
        adversary_mode=adversary_mode,
        seed=seed,
    )

    generated_so_far = 0
    while generated_so_far < n_tx_target:
        batch_to_gen = min(chunk_size, n_tx_target - generated_so_far)
        batch = engine.generate_batch(
            n_transactions=batch_to_gen,
            enforce_invariants=False,
            time_span_days=30,
        )
        writer.write_chunk(batch)
        generated_so_far += len(batch)

    summary = writer.finalize()
    return {
        "worker_id": worker_id,
        "generated": generated_so_far,
        "summary": summary,
        "worker_dir": str(worker_dir),
    }


class ParallelSimulationCoordinator:
    """Coordinates high-throughput simulation across CPU cores writing directly to disk."""

    def __init__(
        self,
        total_transactions: int = 1000000,
        num_workers: Optional[int] = None,
        region: str = "US",
        output_dir: str | Path = "data/simulation_run",
        chunk_size: int = 50000,
        adversary_mode: str = "intent",
        base_seed: int = 42,
    ):
        self.total_transactions = total_transactions
        self.num_workers = num_workers or max(1, min(14, os.cpu_count() or 4))
        self.region = region.upper()
        self.output_dir = Path(output_dir)
        self.chunk_size = chunk_size
        self.adversary_mode = adversary_mode
        self.base_seed = base_seed

    def run(self) -> Dict[str, Any]:
        """Executes parallel simulation pool and merges shard metadata."""
        self.output_dir.mkdir(parents=True, exist_ok=True)
        tx_per_worker = math.ceil(self.total_transactions / self.num_workers)

        t0 = time.perf_counter()
        print(f"[*] Starting Parallel Simulation: {self.total_transactions:,} transactions")
        print(f"   Workers: {self.num_workers} | Tx per worker: {tx_per_worker:,} | Chunk size: {self.chunk_size:,}")
        print(f"   Region: {self.region} | Mode: {self.adversary_mode} | Output: {self.output_dir}")

        worker_results = []
        with ProcessPoolExecutor(max_workers=self.num_workers) as executor:
            futures = [
                executor.submit(
                    _worker_simulation_task,
                    worker_id=w,
                    n_tx_target=tx_per_worker if w < self.num_workers - 1 else (self.total_transactions - tx_per_worker * (self.num_workers - 1)),
                    region=self.region,
                    output_dir=str(self.output_dir),
                    chunk_size=self.chunk_size,
                    adversary_mode=self.adversary_mode,
                    seed=self.base_seed + w * 1000,
                )
                for w in range(self.num_workers)
            ]

            completed = 0
            for future in as_completed(futures):
                res = future.result()
                worker_results.append(res)
                completed += res["generated"]
                elapsed = time.perf_counter() - t0
                rate = completed / max(0.001, elapsed)
                pct = (completed / self.total_transactions) * 100.0
                print(f"   -> [{completed:,} / {self.total_transactions:,}] ({pct:.1f}%) - {rate:,.0f} tx/sec - Elapsed: {elapsed:.1f}s")

        total_elapsed = time.perf_counter() - t0
        overall_throughput = completed / max(0.001, total_elapsed)
        print(f"\n[+] Simulation Complete!")
        print(f"   Total Transactions: {completed:,}")
        print(f"   Total Wall Time: {total_elapsed:.2f}s ({total_elapsed/60:.2f} minutes)")
        print(f"   Overall Throughput: {overall_throughput:,.1f} tx/sec")

        # Consolidate metadata
        consolidated = self._consolidate_worker_summaries(worker_results, total_elapsed, overall_throughput)
        
        # Save master metadata
        master_meta_path = self.output_dir / "master_simulation_metadata.json"
        with open(master_meta_path, "w", encoding="utf-8") as f:
            json.dump(consolidated, f, indent=2)

        return consolidated

    def _consolidate_worker_summaries(
        self,
        worker_results: List[Dict[str, Any]],
        wall_time_sec: float,
        throughput_tps: float,
    ) -> Dict[str, Any]:
        """Merges sharded worker summaries into a master institutional summary."""
        master = {
            "total_transactions": sum(r["generated"] for r in worker_results),
            "wall_time_seconds": round(wall_time_sec, 2),
            "throughput_tps": round(throughput_tps, 1),
            "num_workers": self.num_workers,
            "region": self.region,
            "adversary_mode": self.adversary_mode,
            "approved_count": 0,
            "declined_count": 0,
            "total_fraud_count": 0,
            "total_volume": 0.0,
            "total_fraud_volume": 0.0,
            "hop_drops": defaultdict(int),
            "iso_codes": defaultdict(int),
            "macro_options": defaultdict(int),
            "hourly_legitimate": [0] * 24,
            "hourly_fraud": [0] * 24,
            "top_syndicates": defaultdict(int),
            "top_botnets": defaultdict(int),
            "top_target_merchants": defaultdict(float),
            "top_mule_rings": defaultdict(float),
            "worker_shards": [r["worker_dir"] for r in worker_results],
        }

        for r in worker_results:
            s = r["summary"]
            master["approved_count"] += s.get("approved_count", 0)
            master["declined_count"] += s.get("declined_count", 0)
            master["total_fraud_count"] += s.get("total_fraud_count", 0)
            master["total_volume"] += s.get("total_volume", 0.0)
            master["total_fraud_volume"] += s.get("total_fraud_volume", 0.0)

            for k, v in s.get("hop_drops", {}).items():
                master["hop_drops"][k] += v
            for k, v in s.get("iso_codes", {}).items():
                master["iso_codes"][k] += v
            for k, v in s.get("macro_options", {}).items():
                master["macro_options"][k] += v

            h_dist = s.get("hourly_distribution", {})
            leg = h_dist.get("legitimate", [0]*24)
            frd = h_dist.get("fraud", [0]*24)
            for h in range(24):
                master["hourly_legitimate"][h] += leg[h]
                master["hourly_fraud"][h] += frd[h]

            for k, v in s.get("top_syndicates", {}).items():
                master["top_syndicates"][k] += v
            for k, v in s.get("top_botnets", {}).items():
                master["top_botnets"][k] += v
            for k, v in s.get("top_target_merchants", {}).items():
                master["top_target_merchants"][k] += v
            for k, v in s.get("top_mule_rings", {}).items():
                master["top_mule_rings"][k] += v

        master["approval_rate"] = master["approved_count"] / max(1, master["total_transactions"])
        master["fraud_prevalence"] = master["total_fraud_count"] / max(1, master["total_transactions"])
        master["total_volume"] = round(master["total_volume"], 2)
        master["total_fraud_volume"] = round(master["total_fraud_volume"], 2)
        master["hop_drops"] = dict(master["hop_drops"])
        master["iso_codes"] = dict(master["iso_codes"])
        master["macro_options"] = dict(master["macro_options"])
        master["top_syndicates"] = dict(sorted(master["top_syndicates"].items(), key=lambda x: x[1], reverse=True)[:25])
        master["top_botnets"] = dict(sorted(master["top_botnets"].items(), key=lambda x: x[1], reverse=True)[:25])
        master["top_target_merchants"] = dict(sorted(master["top_target_merchants"].items(), key=lambda x: x[1], reverse=True)[:25])
        master["top_mule_rings"] = dict(sorted(master["top_mule_rings"].items(), key=lambda x: x[1], reverse=True)[:25])

        return master
