"""Real-time streaming daemon for FraudX-Synthesizer.

Provides high-throughput transaction streaming to REST endpoints or stdout
with zero PRISM-X coupling, asynchronous dispatch, and deterministic replaying.
"""

from __future__ import annotations

import argparse
import asyncio
from dataclasses import dataclass
from datetime import datetime, timezone
from enum import Enum
import json
import math
from pathlib import Path
import sys
import time
import urllib.request
import urllib.error
from typing import Any, Dict, List, Optional, Sequence, Tuple, Union

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


class LabelSource(str, Enum):
    """Origin mechanism of the supervision label."""
    INVESTIGATOR_ALERT = "INVESTIGATOR_ALERT"
    CHARGEBACK_DISPUTE = "CHARGEBACK_DISPUTE"
    UNLABELLED = "UNLABELLED"
    UNREPORTED_DARK_FRAUD = "UNREPORTED_DARK_FRAUD"


class InvestigationStatus(str, Enum):
    """Operational queue triage status in the SecOps / FIU pipeline."""
    INVESTIGATED = "INVESTIGATED"
    QUEUED = "QUEUED"
    DROPPED_CAPACITY = "DROPPED_CAPACITY"
    UNREVIEWED = "UNREVIEWED"


class PriorityStrategy(str, Enum):
    """Triage ranking priority policy for investigator queues."""
    RISK_SCORE = "RISK_SCORE"
    VALUE_AT_RISK = "VALUE_AT_RISK"
    HYBRID = "HYBRID"


@dataclass(frozen=True)
class SupervisionRecord:
    """Immutable supervision record containing point-in-time delayed labels and provenance."""
    transaction_id: str
    card_id: str
    tx_time_seconds: float
    tx_timestamp_utc: str
    risk_score: float
    is_fraud_ground_truth: int
    label_source: LabelSource
    investigation_status: InvestigationStatus
    discovery_time_seconds: Optional[float]
    discovery_timestamp_utc: str
    investigation_delay_hours: Optional[float] = None
    chargeback_delay_days: Optional[float] = None
    discovered_label: Optional[int] = None
    priority_score: float = 0.0

    def is_label_available_at(self, query_time_seconds: float) -> Optional[int]:
        """Returns the point-in-time label known to the bank at query_time_seconds.

        Guarantees zero future temporal leakage:
        - Returns None if query_time_seconds < discovery_time_seconds or discovery_time is infinite.
        - Returns 1 if true positive fraud alert or chargeback confirmed on or before query_time.
        - Returns 0 if false positive alert cleared or legitimate transaction matured clean.
        """
        if self.discovery_time_seconds is None or math.isinf(self.discovery_time_seconds):
            return None
        if query_time_seconds < self.discovery_time_seconds:
            return None
        return self.discovered_label

    def to_dict(self) -> Dict[str, Any]:
        """Serializes supervision record to standard dictionary format."""
        return {
            "transaction_id": self.transaction_id,
            "card_id": self.card_id,
            "tx_time_seconds": self.tx_time_seconds,
            "tx_timestamp_utc": self.tx_timestamp_utc,
            "risk_score": self.risk_score,
            "is_fraud_ground_truth": self.is_fraud_ground_truth,
            "is_fraud": self.is_fraud_ground_truth,
            "label_source": self.label_source.value,
            "investigation_status": self.investigation_status.value,
            "discovery_time_seconds": None if (self.discovery_time_seconds is None or math.isinf(self.discovery_time_seconds)) else self.discovery_time_seconds,
            "discovery_timestamp_utc": self.discovery_timestamp_utc,
            "label_maturity_timestamp_utc": self.discovery_timestamp_utc,
            "investigation_delay_hours": self.investigation_delay_hours,
            "chargeback_delay_days": self.chargeback_delay_days,
            "discovered_label": self.discovered_label,
            "priority_score": self.priority_score,
        }


class SupervisionEngine:
    """Simulates the human investigator queue, daily capacity limits, bifurcated verification latencies,
    and dark fraud non-reporting curves for streaming payment transactions.
    Grounded in Dal Pozzolo et al. (IEEE TNNLS 2018), Carcillo et al. (AAAI 2018), and Visa/Mastercard dispute rules.
    """

    def __init__(
        self,
        k_daily: Optional[int] = None,
        alert_threshold: Optional[float] = None,
        priority_strategy: Optional[Union[str, PriorityStrategy]] = None,
        weibull_k: Optional[float] = None,
        weibull_scale_hours: Optional[float] = None,
        min_investigation_hours: Optional[float] = None,
        max_investigation_hours: Optional[float] = None,
        lognormal_mu_days: Optional[float] = None,
        lognormal_sigma: Optional[float] = None,
        min_chargeback_days: Optional[float] = None,
        max_chargeback_days: Optional[float] = None,
        v0_usd: Optional[float] = None,
        v0_inr: Optional[float] = None,
        dark_smoothness: Optional[float] = None,
        clean_maturity_days: Optional[float] = None,
        seed: int = 42,
    ):
        try:
            from .spec_loader import load_all_specs
            spec = load_all_specs().supervision
        except Exception:
            spec = None

        self.k_daily = max(0, int(k_daily if k_daily is not None else (spec.default_k_daily if spec else 50)))
        self.alert_threshold = float(alert_threshold if alert_threshold is not None else (spec.alert_threshold if spec else 0.70))
        strat = priority_strategy if priority_strategy is not None else (spec.default_priority_strategy if spec else PriorityStrategy.RISK_SCORE)
        self.priority_strategy = PriorityStrategy(strat)
        self.weibull_k = float(weibull_k if weibull_k is not None else (spec.weibull_k if spec else 1.35))
        self.weibull_scale_hours = float(weibull_scale_hours if weibull_scale_hours is not None else (spec.weibull_scale_hours if spec else 18.0))
        self.min_investigation_hours = float(min_investigation_hours if min_investigation_hours is not None else (spec.min_investigation_hours if spec else 0.5))
        self.max_investigation_hours = float(max_investigation_hours if max_investigation_hours is not None else (spec.max_investigation_hours if spec else 72.0))
        self.lognormal_mu_days = float(lognormal_mu_days if lognormal_mu_days is not None else (spec.lognormal_mu_days if spec else 3.40))
        self.lognormal_sigma = float(lognormal_sigma if lognormal_sigma is not None else (spec.lognormal_sigma if spec else 0.45))
        self.min_chargeback_days = float(min_chargeback_days if min_chargeback_days is not None else (spec.min_chargeback_days if spec else 3.0))
        self.max_chargeback_days = float(max_chargeback_days if max_chargeback_days is not None else (spec.max_chargeback_days if spec else 120.0))
        self.v0_usd = float(v0_usd if v0_usd is not None else (spec.v0_usd if spec else 15.0))
        self.v0_inr = float(v0_inr if v0_inr is not None else (spec.v0_inr if spec else 1250.0))
        self.dark_smoothness = float(dark_smoothness if dark_smoothness is not None else (spec.dark_smoothness if spec else 0.40))
        clean_mat = clean_maturity_days if clean_maturity_days is not None else (spec.clean_maturity_days if spec else 90.0)
        self.clean_maturity_days = float(clean_mat) if clean_mat is not None else None
        self.seed = seed
        self.rng = np.random.default_rng(seed)

        # Stateful online streaming tracking
        self._current_day: int = -1
        self._daily_investigated_count: int = 0

    def compute_priority_score(self, risk_score: float, amount: float) -> float:
        """Computes triage priority for alert ranking."""
        if self.priority_strategy == PriorityStrategy.RISK_SCORE:
            return float(risk_score)
        elif self.priority_strategy == PriorityStrategy.VALUE_AT_RISK:
            return float(risk_score * max(0.0, amount))
        elif self.priority_strategy == PriorityStrategy.HYBRID:
            norm_amount = min(1.0, max(0.0, amount) / 1000.0)
            return float(0.60 * risk_score + 0.40 * norm_amount)
        return float(risk_score)

    def _sample_investigation_delay_hours(self) -> float:
        """Samples analyst review latency from Weibull distribution within SLA bounds [0.5, 72.0] hours."""
        raw_hours = float(self.rng.weibull(self.weibull_k) * self.weibull_scale_hours)
        return float(np.clip(raw_hours, self.min_investigation_hours, self.max_investigation_hours))

    def _sample_chargeback_delay_days(self) -> float:
        """Samples dispute maturation latency from LogNormal distribution within scheme bounds [3.0, 120.0] days."""
        raw_days = float(self.rng.lognormal(mean=self.lognormal_mu_days, sigma=self.lognormal_sigma))
        return float(np.clip(raw_days, self.min_chargeback_days, self.max_chargeback_days))

    def _is_dark_fraud(self, amount: float, currency: str = "USD", scenario_tag: str = "") -> bool:
        """Determines whether an uninvestigated fraud transaction is withheld as dark fraud via sigmoidal non-reporting curve."""
        if scenario_tag in ("ADV_MICRO_AUTH_PROBE", "ADV_CARDING_MICRO_PROBE"):
            return bool(self.rng.random() < 0.99)
        threshold = self.v0_inr if currency == "INR" else self.v0_usd
        exponent = 1.0 / max(0.05, self.dark_smoothness)
        p_dark = 1.0 / (1.0 + math.pow(max(0.01, amount) / threshold, exponent))
        p_dark = float(np.clip(p_dark, 0.0001, 0.9999))
        return bool(self.rng.random() < p_dark)

    def process_batch(
        self,
        records: List[Dict[str, Any]],
        risk_scores: Optional[Sequence[float]] = None,
    ) -> List[SupervisionRecord]:
        """Processes an entire chronological batch with exact daily capacity allocation."""
        if not records:
            return []

        extracted_scores: List[float] = []
        for i, r in enumerate(records):
            if risk_scores is not None and i < len(risk_scores):
                score = float(risk_scores[i])
            else:
                score = float(r.get("risk_score", r.get("ml_risk_score", r.get("model_score", 0.0))))
            extracted_scores.append(score)

        # 1. Group records by simulation calendar day: day = floor(tx_time_seconds / 86400)
        day_groups: Dict[int, List[int]] = {}
        for idx, r in enumerate(records):
            t_sec = float(r.get("tx_time_seconds", 0.0))
            d_idx = int(t_sec // 86400.0)
            day_groups.setdefault(d_idx, []).append(idx)

        # 2. Determine investigated status per day
        investigated_indices: set[int] = set()
        dropped_indices: set[int] = set()

        for d_idx in sorted(day_groups.keys()):
            indices = day_groups[d_idx]
            candidates: List[Tuple[float, float, str, int]] = []
            for idx in indices:
                r = records[idx]
                score = extracted_scores[idx]
                amt = float(r.get("amount", 0.0))
                prio = self.compute_priority_score(score, amt)
                if score >= self.alert_threshold:
                    t_sec = float(r.get("tx_time_seconds", 0.0))
                    tx_id = str(r.get("transaction_id", ""))
                    # Higher priority first (-prio), then earliest time, tx_id, idx
                    candidates.append((-prio, t_sec, tx_id, idx))

            candidates.sort()
            allocated = candidates[: self.k_daily]
            overflow = candidates[self.k_daily :]

            for _, _, _, idx in allocated:
                investigated_indices.add(idx)
            for _, _, _, idx in overflow:
                dropped_indices.add(idx)

        # 3. Build SupervisionRecords
        results: List[SupervisionRecord] = []
        for idx, r in enumerate(records):
            tx_id = str(r.get("transaction_id", f"TX_{idx:08d}"))
            card_id = str(r.get("card_id", ""))
            tx_time_sec = float(r.get("tx_time_seconds", 0.0))
            tx_dt_utc = str(r.get("timestamp_utc", datetime.fromtimestamp(tx_time_sec, tz=timezone.utc).isoformat()))
            is_fraud = int(r.get("is_fraud", 0))
            scenario_tag = str(r.get("scenario_tag", "ORGANIC_NORMAL"))
            currency = str(r.get("currency", "USD"))
            amt = float(r.get("amount", 0.0))
            score = extracted_scores[idx]
            prio = self.compute_priority_score(score, amt)

            if idx in investigated_indices:
                inv_status = InvestigationStatus.INVESTIGATED
                label_src = LabelSource.INVESTIGATOR_ALERT
                delay_h = self._sample_investigation_delay_hours()
                disc_sec = tx_time_sec + delay_h * 3600.0
                disc_dt = datetime.fromtimestamp(disc_sec, tz=timezone.utc).isoformat()
                discovered_lbl = is_fraud  # Analyst verifies ground truth
                results.append(SupervisionRecord(
                    transaction_id=tx_id,
                    card_id=card_id,
                    tx_time_seconds=tx_time_sec,
                    tx_timestamp_utc=tx_dt_utc,
                    risk_score=score,
                    is_fraud_ground_truth=is_fraud,
                    label_source=label_src,
                    investigation_status=inv_status,
                    discovery_time_seconds=disc_sec,
                    discovery_timestamp_utc=disc_dt,
                    investigation_delay_hours=round(delay_h, 2),
                    chargeback_delay_days=None,
                    discovered_label=discovered_lbl,
                    priority_score=round(prio, 4),
                ))

            else:
                inv_status = (
                    InvestigationStatus.DROPPED_CAPACITY
                    if idx in dropped_indices
                    else InvestigationStatus.UNREVIEWED
                )

                if is_fraud == 1:
                    if self._is_dark_fraud(amt, currency=currency, scenario_tag=scenario_tag):
                        results.append(SupervisionRecord(
                            transaction_id=tx_id,
                            card_id=card_id,
                            tx_time_seconds=tx_time_sec,
                            tx_timestamp_utc=tx_dt_utc,
                            risk_score=score,
                            is_fraud_ground_truth=1,
                            label_source=LabelSource.UNREPORTED_DARK_FRAUD,
                            investigation_status=inv_status,
                            discovery_time_seconds=float("inf"),
                            discovery_timestamp_utc="",
                            investigation_delay_hours=None,
                            chargeback_delay_days=None,
                            discovered_label=None,
                            priority_score=round(prio, 4),
                        ))
                    else:
                        cb_days = self._sample_chargeback_delay_days()
                        disc_sec = tx_time_sec + cb_days * 86400.0
                        disc_dt = datetime.fromtimestamp(disc_sec, tz=timezone.utc).isoformat()
                        results.append(SupervisionRecord(
                            transaction_id=tx_id,
                            card_id=card_id,
                            tx_time_seconds=tx_time_sec,
                            tx_timestamp_utc=tx_dt_utc,
                            risk_score=score,
                            is_fraud_ground_truth=1,
                            label_source=LabelSource.CHARGEBACK_DISPUTE,
                            investigation_status=inv_status,
                            discovery_time_seconds=disc_sec,
                            discovery_timestamp_utc=disc_dt,
                            investigation_delay_hours=None,
                            chargeback_delay_days=round(cb_days, 1),
                            discovered_label=1,
                            priority_score=round(prio, 4),
                        ))
                else:
                    if self.clean_maturity_days is not None:
                        disc_sec = tx_time_sec + self.clean_maturity_days * 86400.0
                        disc_dt = datetime.fromtimestamp(disc_sec, tz=timezone.utc).isoformat()
                        disc_lbl: Optional[int] = 0
                    else:
                        disc_sec = float("inf")
                        disc_dt = ""
                        disc_lbl = None

                    results.append(SupervisionRecord(
                        transaction_id=tx_id,
                        card_id=card_id,
                        tx_time_seconds=tx_time_sec,
                        tx_timestamp_utc=tx_dt_utc,
                        risk_score=score,
                        is_fraud_ground_truth=0,
                        label_source=LabelSource.UNLABELLED,
                        investigation_status=inv_status,
                        discovery_time_seconds=disc_sec,
                        discovery_timestamp_utc=disc_dt,
                        investigation_delay_hours=None,
                        chargeback_delay_days=None,
                        discovered_label=disc_lbl,
                        priority_score=round(prio, 4),
                    ))

        return results

    def process_record(
        self,
        record: Dict[str, Any],
        risk_score: Optional[float] = None,
    ) -> SupervisionRecord:
        """Processes a single record in online streaming mode with active daily budget tracking."""
        score = (
            float(risk_score)
            if risk_score is not None
            else float(record.get("risk_score", record.get("ml_risk_score", 0.0)))
        )
        t_sec = float(record.get("tx_time_seconds", 0.0))
        d_idx = int(t_sec // 86400.0)

        # Reset daily budget counter on new day boundary
        if d_idx > self._current_day:
            self._current_day = d_idx
            self._daily_investigated_count = 0

        amt = float(record.get("amount", 0.0))
        currency = str(record.get("currency", "USD"))
        prio = self.compute_priority_score(score, amt)
        is_fraud = int(record.get("is_fraud", 0))
        scenario_tag = str(record.get("scenario_tag", "ORGANIC_NORMAL"))
        tx_id = str(record.get("transaction_id", ""))
        card_id = str(record.get("card_id", ""))
        tx_dt_utc = str(record.get("timestamp_utc", datetime.fromtimestamp(t_sec, tz=timezone.utc).isoformat()))

        # Check qualification & capacity
        if score >= self.alert_threshold:
            if self._daily_investigated_count < self.k_daily:
                self._daily_investigated_count += 1
                delay_h = self._sample_investigation_delay_hours()
                disc_sec = t_sec + delay_h * 3600.0
                disc_dt = datetime.fromtimestamp(disc_sec, tz=timezone.utc).isoformat()
                return SupervisionRecord(
                    transaction_id=tx_id,
                    card_id=card_id,
                    tx_time_seconds=t_sec,
                    tx_timestamp_utc=tx_dt_utc,
                    risk_score=score,
                    is_fraud_ground_truth=is_fraud,
                    label_source=LabelSource.INVESTIGATOR_ALERT,
                    investigation_status=InvestigationStatus.INVESTIGATED,
                    discovery_time_seconds=disc_sec,
                    discovery_timestamp_utc=disc_dt,
                    investigation_delay_hours=round(delay_h, 2),
                    chargeback_delay_days=None,
                    discovered_label=is_fraud,
                    priority_score=round(prio, 4),
                )
            else:
                inv_status = InvestigationStatus.DROPPED_CAPACITY
        else:
            inv_status = InvestigationStatus.UNREVIEWED

        if is_fraud == 1:
            if self._is_dark_fraud(amt, currency=currency, scenario_tag=scenario_tag):
                return SupervisionRecord(
                    transaction_id=tx_id,
                    card_id=card_id,
                    tx_time_seconds=t_sec,
                    tx_timestamp_utc=tx_dt_utc,
                    risk_score=score,
                    is_fraud_ground_truth=1,
                    label_source=LabelSource.UNREPORTED_DARK_FRAUD,
                    investigation_status=inv_status,
                    discovery_time_seconds=float("inf"),
                    discovery_timestamp_utc="",
                    investigation_delay_hours=None,
                    chargeback_delay_days=None,
                    discovered_label=None,
                    priority_score=round(prio, 4),
                )
            else:
                cb_days = self._sample_chargeback_delay_days()
                disc_sec = t_sec + cb_days * 86400.0
                disc_dt = datetime.fromtimestamp(disc_sec, tz=timezone.utc).isoformat()
                return SupervisionRecord(
                    transaction_id=tx_id,
                    card_id=card_id,
                    tx_time_seconds=t_sec,
                    tx_timestamp_utc=tx_dt_utc,
                    risk_score=score,
                    is_fraud_ground_truth=1,
                    label_source=LabelSource.CHARGEBACK_DISPUTE,
                    investigation_status=inv_status,
                    discovery_time_seconds=disc_sec,
                    discovery_timestamp_utc=disc_dt,
                    investigation_delay_hours=None,
                    chargeback_delay_days=round(cb_days, 1),
                    discovered_label=1,
                    priority_score=round(prio, 4),
                )
        else:
            if self.clean_maturity_days is not None:
                disc_sec = t_sec + self.clean_maturity_days * 86400.0
                disc_dt = datetime.fromtimestamp(disc_sec, tz=timezone.utc).isoformat()
                disc_lbl = 0
            else:
                disc_sec = float("inf")
                disc_dt = ""
                disc_lbl = None

            return SupervisionRecord(
                transaction_id=tx_id,
                card_id=card_id,
                tx_time_seconds=t_sec,
                tx_timestamp_utc=tx_dt_utc,
                risk_score=score,
                is_fraud_ground_truth=0,
                label_source=LabelSource.UNLABELLED,
                investigation_status=inv_status,
                discovery_time_seconds=disc_sec,
                discovery_timestamp_utc=disc_dt,
                investigation_delay_hours=None,
                chargeback_delay_days=None,
                discovered_label=disc_lbl,
                priority_score=round(prio, 4),
            )


class ZeroLeakageDataPartitioner:
    """Partitions unified synthetic transactions into 3 legally and architecturally isolated feeds."""

    def __init__(
        self,
        supervision_engine: Optional[SupervisionEngine] = None,
        mean_chargeback_lag_days: float = 21.0,
        k_daily: int = 50,
        alert_threshold: float = 0.70,
        seed: int = 42,
    ):
        self.supervision_engine = supervision_engine or SupervisionEngine(
            k_daily=k_daily,
            alert_threshold=alert_threshold,
            seed=seed,
        )
        self.mean_chargeback_lag_days = mean_chargeback_lag_days
        self.rng = np.random.default_rng(seed)

    def partition_record(self, record: Dict[str, Any]) -> Tuple[Dict[str, Any], Dict[str, Any], Dict[str, Any]]:
        """Splits an individual record into (inference_feed, delayed_labels, threat_intel_graph_enclave)."""
        # 1. Inference Feed (strictly point-in-time, zero target labels, zero graph ids)
        inference_feed = {k: v for k, v in record.items() if k in INFERENCE_ALLOWLIST}

        # 2. Delayed Labels via SupervisionEngine
        sup = self.supervision_engine.process_record(record)
        delayed_labels = sup.to_dict()
        delayed_labels["scenario_tag"] = record.get("scenario_tag", "")
        delayed_labels["dispute_status"] = record.get("dispute_status", "NONE")
        delayed_labels["dispute_reason_code"] = record.get("dispute_reason_code", "")
        delayed_labels["rbi_liability_tier"] = record.get("rbi_liability_tier", "")

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
        risk_scores: Optional[Sequence[float]] = None,
    ) -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]], List[Dict[str, Any]]]:
        """Partitions an entire batch of records into 3 feeds with exact daily capacity allocation."""
        inf_batch: List[Dict[str, Any]] = []
        labels_batch: List[Dict[str, Any]] = []
        graph_batch: List[Dict[str, Any]] = []

        sups = self.supervision_engine.process_batch(records, risk_scores=risk_scores)

        for r, sup in zip(records, sups):
            inf = {k: v for k, v in r.items() if k in INFERENCE_ALLOWLIST}
            lbl = sup.to_dict()
            lbl["scenario_tag"] = r.get("scenario_tag", "")
            lbl["dispute_status"] = r.get("dispute_status", "NONE")
            lbl["dispute_reason_code"] = r.get("dispute_reason_code", "")
            lbl["rbi_liability_tier"] = r.get("rbi_liability_tier", "")

            grp = {
                "transaction_id": r.get("transaction_id", ""),
                "card_id": r.get("card_id", ""),
                "merchant_id": r.get("merchant_id", ""),
                "syndicate_id": r.get("syndicate_id", ""),
                "botnet_cluster_id": r.get("botnet_cluster_id", ""),
                "mule_ring_id": r.get("mule_ring_id", ""),
                "beneficiary_account_id": r.get("beneficiary_account_id", ""),
                "ip_subnet_prefix": r.get("ip_subnet_prefix", ""),
                "device_fingerprint_id": r.get("device_fingerprint_id", ""),
                "asn_type": r.get("asn_type", "residential"),
                "client_ip": r.get("client_ip", "127.0.0.1"),
                "is_fraud": int(r.get("is_fraud", 0)),
                "scenario_tag": str(r.get("scenario_tag", "")),
            }

            inf_batch.append(inf)
            labels_batch.append(lbl)
            graph_batch.append(grp)

        return inf_batch, labels_batch, graph_batch

    def export_partitioned_feeds(
        self,
        records: List[Dict[str, Any]],
        output_dir: str | Path,
        risk_scores: Optional[Sequence[float]] = None,
    ) -> Dict[str, Path]:
        """Writes the 3 partitioned feeds to output directory as JSON lines."""
        out_path = Path(output_dir)
        out_path.mkdir(parents=True, exist_ok=True)

        inf_batch, labels_batch, graph_batch = self.partition_batch(records, risk_scores=risk_scores)

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

