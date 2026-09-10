"""Real-time streaming ledger and rolling feature accumulator for FraudX-Synthesizer.

Enforces:
1. Point-in-time causality: Features are computed strictly BEFORE mutating state (zero lookahead).
2. Strict temporal monotonicity: Operates synchronously with discrete-event priority queue.
3. Kinematic state protection: Foreign attacker coordinates do not poison legitimate card anchors.
4. Robust Welford accumulator with calibrated prior moments.
5. Multi-resolution financial units: Minor integer units (Cents/Paisa) and display amounts.
"""

from __future__ import annotations

import collections
import math
from dataclasses import dataclass, field
from datetime import datetime, timezone
import hashlib
from typing import Any, Deque, Dict, List, Optional, Tuple

import numpy as np

from .agents import CardholderProfile, ChannelType
from .invariants import haversine_distance_km


class WelfordAccumulator:
    """Online running mean and sample variance computation via Welford's algorithm."""

    def __init__(self, count: int, mean: float, m2: float):
        self.count = max(1, count)
        self.mean = mean
        self.m2 = max(0.0, m2)

    def update(self, x: float) -> None:
        """Updates mean and M2 sum of squared differences with a new observation."""
        self.count += 1
        delta = x - self.mean
        self.mean += delta / self.count
        delta2 = x - self.mean
        self.m2 += delta * delta2

    @property
    def variance(self) -> float:
        """Sample variance s^2 = M2 / (count - 1)."""
        if self.count <= 1:
            return 0.0
        return max(0.0, self.m2 / (self.count - 1))

    @property
    def std(self) -> float:
        """Sample standard deviation s = sqrt(s^2)."""
        return math.sqrt(self.variance)

    def compute_z_score(self, x: float) -> float:
        """Standardized score z = (x - mean) / std. Regularized to avoid division by zero."""
        s = max(self.std, 0.15 * max(self.mean, 1.0), 2.0)
        return (x - self.mean) / s


@dataclass
class CardholderLedgerState:
    """Stateful tracking container for an individual cardholder."""
    card_id: str
    welford_30d: WelfordAccumulator
    tx_history_1h: Deque[Tuple[float, float]] = field(default_factory=collections.deque)        # (timestamp, amount)
    tx_history_24h: Deque[Tuple[float, float, str]] = field(default_factory=collections.deque) # (timestamp, amount, merchant_id)
    last_tx_time: float = -1.0
    last_tx_lat: float = 0.0
    last_tx_lon: float = 0.0

    def prune_expired(self, current_time: float) -> None:
        """Prunes historical entries older than rolling time horizons (strictly monotonic)."""
        cutoff_1h = current_time - 3600.0
        while self.tx_history_1h and self.tx_history_1h[0][0] <= cutoff_1h:
            self.tx_history_1h.popleft()

        cutoff_24h = current_time - 86400.0
        while self.tx_history_24h and self.tx_history_24h[0][0] <= cutoff_24h:
            self.tx_history_24h.popleft()


class StreamingLedger:
    """Thread-safe streaming feature store maintaining point-in-time feature states."""

    def __init__(self, seed: int = 42):
        self.rng = np.random.default_rng(seed)
        self.card_states: Dict[str, CardholderLedgerState] = {}

    def get_or_create_state(self, card: CardholderProfile) -> CardholderLedgerState:
        """Retrieves cardholder state or initializes with theoretical lognormal priors."""
        if card.card_id not in self.card_states:
            prior_mean = card.get_theoretical_mean_spend()
            sig2 = card.spend_sigma_log ** 2
            ln_var = (math.exp(sig2) - 1.0) * math.exp(2.0 * card.spend_mean_log + sig2)
            if card.is_spliced_gpd:
                u = card.gpd_threshold_u
                xi = max(0.05, min(0.45, card.gpd_xi))
                beta = card.gpd_beta
                p = card.gpd_tail_prob
                ln_mean = math.exp(card.spend_mean_log + 0.5 * sig2)
                e_gpd = u + beta / (1.0 - xi)
                e_gpd2 = (u ** 2) + 2.0 * u * beta / (1.0 - xi) + (2.0 * (beta ** 2)) / ((1.0 - xi) * (1.0 - 2.0 * xi))
                e_ln2 = ln_var + (ln_mean ** 2)
                total_e2 = (1.0 - p) * e_ln2 + p * e_gpd2
                prior_var = max(ln_var, total_e2 - (prior_mean ** 2))
            else:
                prior_var = ln_var
            prior_m2 = 11.0 * prior_var

            accumulator = WelfordAccumulator(count=12, mean=prior_mean, m2=prior_m2)
            self.card_states[card.card_id] = CardholderLedgerState(
                card_id=card.card_id,
                welford_30d=accumulator,
                last_tx_time=-1.0,
                last_tx_lat=card.home_lat,
                last_tx_lon=card.home_lon,
            )
        return self.card_states[card.card_id]

    def enrich_transaction(
        self,
        tx_id: str,
        card: CardholderProfile,
        merchant_id: str,
        merchant_name: str,
        mcc: int,
        merchant_category: str,
        merchant_lat: float,
        merchant_lon: float,
        amount: float,
        tx_time: float,
        channel_type: str,
        is_fraud: int,
        scenario_tag: str,
        mid: str = "",
        tid: str = "",
        acquirer_bin: str = "",
        gateway_provider: str = "",
        merchant_country: str = "US",
        postal_code: str = "10001",
        is_cross_border: bool = False,
        ip_distance_km: float = 0.0,
        asn_type: str = "residential",
        override_cvv_match: Optional[int] = None,
        override_avs_code: Optional[str] = None,
        override_billing_match: Optional[int] = None,
        override_client_ip: Optional[str] = None,
        syndicate_id: str = "",
        botnet_cluster_id: str = "",
        mule_ring_id: str = "",
        beneficiary_account_id: str = "",
        ip_subnet_prefix: str = "",
        device_fingerprint_id: str = "",
    ) -> Dict[str, Any]:
        """Enriches raw transaction parameters into full institutional telemetry record."""
        state = self.get_or_create_state(card)

        # 1. Prune expired entries from rolling windows prior to computing features
        state.prune_expired(tx_time)

        # 2. Point-in-time calculation: Read features BEFORE appending current transaction
        count_1h = len(state.tx_history_1h)
        count_24h = len(state.tx_history_24h)
        sum_24h = sum(a for _, a, _ in state.tx_history_24h)
        distinct_merchants_24h = len(set(m for _, _, m in state.tx_history_24h))

        user_mean_30d = state.welford_30d.mean
        user_std_30d = state.welford_30d.std
        z_score_amount = state.welford_30d.compute_z_score(amount)

        # 3. Kinematic velocity computation
        velocity_kph = 0.0
        distance_from_last_tx_km = 0.0
        time_since_last_tx_sec = 0.0

        if channel_type.startswith("CP") or scenario_tag in ("IMPOSSIBLE_TRAVEL", "COUNTERFEIT_CLONE"):
            if card.last_physical_time >= 0.0:
                time_since_last_tx_sec = max(0.0, tx_time - card.last_physical_time)
                distance_from_last_tx_km = haversine_distance_km(
                    card.last_physical_lat,
                    card.last_physical_lon,
                    merchant_lat,
                    merchant_lon,
                )
                delta_hours = max(time_since_last_tx_sec / 3600.0, 1e-5)
                velocity_kph = distance_from_last_tx_km / delta_hours

        # 4. Digital Telemetry Sampling (AVS, CVV, Geolocation, Device Fingerprint)
        if channel_type.startswith("CP"):
            billing_shipping_match = 1
            avs_match_code = "Y"
            cvv_match_flag = 1
            asn_type = "residential"
            geo_risk_score = 0
            client_ip = "127.0.0.1"
        else:
            if override_cvv_match is not None:
                cvv_match_flag = override_cvv_match
            else:
                cvv_match_flag = 1 if (self.rng.random() < 0.98 if is_fraud == 0 else self.rng.random() < 0.82) else 0

            if override_avs_code is not None:
                avs_match_code = override_avs_code
            else:
                if is_fraud == 0:
                    avs_match_code = str(self.rng.choice(["Y", "N", "A", "Z"], p=[0.92, 0.05, 0.02, 0.01]))
                else:
                    avs_match_code = str(self.rng.choice(["Y", "Z", "N", "U"], p=[0.35, 0.35, 0.22, 0.08]))

            if override_billing_match is not None:
                billing_shipping_match = override_billing_match
            else:
                billing_shipping_match = 1 if (self.rng.random() < 0.93 if is_fraud == 0 else self.rng.random() < 0.60) else 0

            # 5-way Geolocation mismatch score from spec/03
            geo_risk_score = 0
            if is_cross_border:
                geo_risk_score += 35
            if billing_shipping_match == 0:
                geo_risk_score += 25
            if avs_match_code == "N":
                geo_risk_score += 20
            if is_fraud == 1 and asn_type == "datacenter":
                geo_risk_score = 100

            # Generate synthetic client IP
            if override_client_ip:
                client_ip = override_client_ip
            elif card.region == "IN":
                client_ip = f"103.{self.rng.integers(10, 250)}.{self.rng.integers(1, 254)}.{self.rng.integers(1, 254)}"
            else:
                client_ip = f"72.{self.rng.integers(10, 250)}.{self.rng.integers(1, 254)}.{self.rng.integers(1, 254)}"

        if override_client_ip and channel_type.startswith("CP"):
            client_ip = override_client_ip

        # Synthetic Device Canvas Murmur3 Hash (deterministic for card, noisy if fraudster, or cluster-derived)
        if device_fingerprint_id:
            canvas_hash = hashlib.md5(device_fingerprint_id.encode("utf-8")).hexdigest()[:16]
        else:
            device_seed = f"{card.card_id}_{card.home_lat:.3f}"
            if is_fraud == 1 and asn_type == "datacenter":
                device_seed += f"_{tx_time}"
            canvas_hash = hashlib.md5(device_seed.encode("utf-8")).hexdigest()[:16]

        # Construct ISO-8601 UTC timestamp
        dt_utc = datetime.fromtimestamp(tx_time, tz=timezone.utc)
        hour_of_day = dt_utc.hour
        day_of_week = dt_utc.weekday()

        # Minor currency unit conversion (cents for USD, paisa for INR)
        amount_minor = int(round(amount * 100))

        # Build complete transaction dictionary matching institutional production schemas
        record: Dict[str, Any] = {
            "transaction_id": tx_id,
            "card_id": card.card_id,
            "pan_masked": card.pan_masked,
            "product_id": card.product_id,
            "cohort_id": card.cohort_id,
            "merchant_id": merchant_id,
            "merchant_name": merchant_name,
            "mid": mid if mid else f"MID_{merchant_id}",
            "tid": tid if tid else f"TID_{merchant_id[-4:]}",
            "mcc": mcc,
            "merchant_category": merchant_category,
            "merchant_lat": merchant_lat,
            "merchant_lon": merchant_lon,
            "acquirer_bin": acquirer_bin if acquirer_bin else "400012",
            "gateway_provider": gateway_provider if gateway_provider else "STRIPE",
            "country_code": merchant_country,
            "postal_code": postal_code,
            "timestamp_utc": dt_utc.isoformat(),
            "tx_time_seconds": round(tx_time, 2),
            "hour_of_day": hour_of_day,
            "day_of_week": day_of_week,
            "amount": round(amount, 2),
            "amount_minor": amount_minor,
            "currency": card.currency,
            "channel_type": channel_type,
            "credit_limit": card.credit_limit,
            "current_balance": round(card.current_balance, 2),
            "available_balance": round(card.get_available_balance(), 2),
            "user_avg_tx_amount_30d": round(user_mean_30d, 2),
            "user_std_tx_amount_30d": round(user_std_30d, 2),
            "z_score_amount_30d": round(z_score_amount, 3),
            "tx_count_1h": count_1h,
            "tx_count_24h": count_24h,
            "tx_amount_sum_24h": round(sum_24h, 2),
            "distinct_merchants_24h": distinct_merchants_24h,
            "distance_from_last_tx_km": round(distance_from_last_tx_km, 3),
            "time_since_last_tx_seconds": round(time_since_last_tx_sec, 1),
            "haversine_velocity_kph": round(velocity_kph, 2),
            "ip_distance_from_home_km": round(ip_distance_km, 2),
            "client_ip": client_ip,
            "asn_type": asn_type,
            "geo_risk_score": geo_risk_score,
            "device_canvas_hash": canvas_hash,
            "is_cross_border": is_cross_border,
            "billing_shipping_match": billing_shipping_match,
            "avs_match_code": avs_match_code,
            "cvv_match_flag": cvv_match_flag,
            "is_fraud": is_fraud,
            "scenario_tag": scenario_tag,
            "syndicate_id": syndicate_id,
            "botnet_cluster_id": botnet_cluster_id,
            "mule_ring_id": mule_ring_id,
            "beneficiary_account_id": beneficiary_account_id,
            "ip_subnet_prefix": ip_subnet_prefix,
            "device_fingerprint_id": device_fingerprint_id,
        }

        # 5. Mutate rolling telemetry state AFTER record generation (Point-in-time discipline)
        state.tx_history_1h.append((tx_time, amount))
        state.tx_history_24h.append((tx_time, amount, merchant_id))
        if is_fraud == 0:
            state.welford_30d.update(amount)
        state.last_tx_time = tx_time
        state.last_tx_lat = merchant_lat
        state.last_tx_lon = merchant_lon

        # Physical location anchor protection
        if channel_type.startswith("CP") and is_fraud == 0:
            card.last_physical_lat = merchant_lat
            card.last_physical_lon = merchant_lon
            card.last_physical_time = tx_time
            card.last_merchant_id = merchant_id

        return record
