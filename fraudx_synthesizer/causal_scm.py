"""Feature Risk Attribution & Baseline Reference Engine.

Provides:
1. Parametric risk scoring combining linear feature shifts and multi-feature interaction synergies.
2. Baseline feature delta calculation against the uncompromised cardholder's 30-day history:
   delta_x = x_observed - x_baseline
3. Feature risk attributions:
   - Logit space: Owen multilinear attribution for linear + interaction terms.
   - Probability space: 128-point numerical path integration (Aumann-Shapley / Integrated Gradients)
     with normalized sum matching the total probability delta.
"""

from __future__ import annotations

import math
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Tuple

import numpy as np


@dataclass
class CausalGroundTruth:
    """Rigorous ground-truth risk attribution and contrastive explanation for a transaction."""
    is_fraud: int
    scenario_tag: str
    risk_score: float
    base_risk: float
    logit_z: float
    base_logit: float
    analytical_shapley_log_odds: Dict[str, float] = field(default_factory=dict)
    analytical_shapley_probability: Dict[str, float] = field(default_factory=dict)
    counterfactual_input_deltas: Dict[str, float] = field(default_factory=dict)
    dominant_causal_driver: str = "baseline"
    active_causal_parents: List[str] = field(default_factory=list)
    counterfactual_mode: str = "CONTRASTIVE_PROFILE_FOIL"
    counterfactual_twin: Dict[str, Any] = field(default_factory=dict)
    normative_baseline: Dict[str, Any] = field(default_factory=dict)
    explanation_narrative: str = ""

    def __post_init__(self) -> None:
        if not self.normative_baseline and self.counterfactual_twin:
            self.normative_baseline = self.counterfactual_twin
        elif not self.counterfactual_twin and self.normative_baseline:
            self.counterfactual_twin = self.normative_baseline


class StructuralCausalEngine:
    """Evaluates structural causal risk and derives exact counterfactual attributions."""

    def __init__(self, base_prevalence: float = 0.0020):
        self.base_prevalence = max(1e-5, min(0.999, base_prevalence))
        self.base_logit = math.log(self.base_prevalence / (1.0 - self.base_prevalence))

        # Baseline expected values for normal transactions E[X_i]
        self.feature_baselines: Dict[str, float] = {
            "haversine_velocity_kph": 15.0,
            "amount_to_mean_ratio_30d": 1.0,
            "tx_count_1h": 0.3,
            "tx_count_24h": 2.5,
            "tx_amount_sum_24h_ratio": 0.25,
            "ip_distance_from_home_km": 8.0,
            "is_cross_border_tx": 0.02,
            "avs_mismatch_flag": 0.08,
            "billing_shipping_mismatch": 0.08,
            "cvv_mismatch_flag": 0.01,
            "is_high_risk_mcc": 0.04,
            "is_night_tx": 0.05,
        }

        # Structural causal DAG weights (log-odds impact per unit deviation)
        self.structural_weights: Dict[str, float] = {
            "haversine_velocity_kph": 0.0055,
            "amount_to_mean_ratio_30d": 0.65,
            "tx_count_1h": 0.85,
            "tx_count_24h": 0.20,
            "tx_amount_sum_24h_ratio": 1.10,
            "ip_distance_from_home_km": 0.0018,
            "is_cross_border_tx": 1.75,
            "avs_mismatch_flag": 1.95,
            "billing_shipping_mismatch": 1.80,
            "cvv_mismatch_flag": 2.80,
            "is_high_risk_mcc": 1.40,
            "is_night_tx": 0.90,
        }

        # Grounded multi-feature synergy interaction kernels
        self.pairwise_synergies: List[Tuple[str, str, float]] = [
            ("haversine_velocity_kph", "ip_distance_from_home_km", 0.00004),
            ("is_night_tx", "amount_to_mean_ratio_30d", 0.45),
            ("is_night_tx", "is_cross_border_tx", 1.20),
            ("amount_to_mean_ratio_30d", "is_high_risk_mcc", 0.55),
            ("tx_count_1h", "tx_amount_sum_24h_ratio", 0.75),
            ("avs_mismatch_flag", "cvv_mismatch_flag", 1.85),
        ]

        self.three_way_synergies: List[Tuple[str, str, str, float]] = [
            ("is_night_tx", "is_cross_border_tx", "amount_to_mean_ratio_30d", 0.35),
        ]

        # 128-point Gauss-Legendre quadrature nodes and weights for exact Aumann-Shapley path attribution
        x_nodes, w_weights = np.polynomial.legendre.leggauss(128)
        self._gl_t = 0.5 * (x_nodes + 1.0)
        self._gl_wt = 0.5 * w_weights

    def _logistic(self, z: float) -> float:
        """Numerically stable standard sigmoid."""
        if z >= 35.0:
            return 1.0
        elif z <= -35.0:
            return 0.0
        return 1.0 / (1.0 + math.exp(-z))

    def evaluate(
        self,
        record: Dict[str, Any],
        scenario_tag: str = "ORGANIC_NORMAL",
    ) -> CausalGroundTruth:
        """Evaluates causal risk and constructs exact counterfactual twin and attributions."""
        amount = float(record.get("amount", 25.0))
        mean_30d = float(record.get("user_avg_tx_amount_30d", 25.0))
        ratio_30d = amount / max(mean_30d, 1.0)

        velocity_kph = float(record.get("haversine_velocity_kph", 0.0))
        channel = str(record.get("channel_type", ""))

        if not channel.startswith("CP") and scenario_tag != "COUNTERFEIT_CLONE" and scenario_tag != "IMPOSSIBLE_TRAVEL":
            effective_velocity = 0.0
        else:
            effective_velocity = velocity_kph

        count_1h = float(record.get("tx_count_1h", 0))
        count_24h = float(record.get("tx_count_24h", 0))
        sum_24h = float(record.get("tx_amount_sum_24h", 0.0))
        credit_limit = float(record.get("credit_limit", 5000.0))
        sum_ratio = sum_24h / max(credit_limit, 500.0)

        ip_dist = float(record.get("ip_distance_from_home_km", 0.0))
        cross_border = 1.0 if bool(record.get("is_cross_border", False)) else 0.0

        avs_code = str(record.get("avs_match_code", "Y"))
        avs_mismatch = 1.0 if avs_code in ("N", "U") else 0.0

        bill_ship = int(record.get("billing_shipping_match", 1))
        bill_mismatch = 1.0 if bill_ship == 0 else 0.0

        cvv_flag = int(record.get("cvv_match_flag", 1))
        cvv_mismatch = 1.0 if cvv_flag == 0 else 0.0

        mcc = int(record.get("mcc", 5411))
        is_high_risk = 1.0 if mcc in (5094, 6051, 5732, 7995, 8398) else 0.0

        hour = int(record.get("hour_of_day", 14))
        is_night = 1.0 if (1 <= hour <= 5) else 0.0

        feature_vector: Dict[str, float] = {
            "haversine_velocity_kph": effective_velocity,
            "amount_to_mean_ratio_30d": ratio_30d,
            "tx_count_1h": count_1h,
            "tx_count_24h": count_24h,
            "tx_amount_sum_24h_ratio": sum_ratio,
            "ip_distance_from_home_km": ip_dist,
            "is_cross_border_tx": cross_border,
            "avs_mismatch_flag": avs_mismatch,
            "billing_shipping_mismatch": bill_mismatch,
            "cvv_mismatch_flag": cvv_mismatch,
            "is_high_risk_mcc": is_high_risk,
            "is_night_tx": is_night,
        }

        # 1. Compute Logit-Space Feature Attributions via Owen Multilinear Formula
        deltas: Dict[str, float] = {}
        for feat_name in self.structural_weights:
            x_val = feature_vector[feat_name]
            base_val = self.feature_baselines[feat_name]
            deltas[feat_name] = max(0.0, x_val - base_val)

        # Linear component A_{i,0}
        A_0 = {
            feat_name: self.structural_weights[feat_name] * deltas[feat_name]
            for feat_name in self.structural_weights
        }
        c1 = sum(A_0.values())

        # Pairwise interaction components A_{i,1}
        A_1 = {feat_name: 0.0 for feat_name in self.structural_weights}
        c2 = 0.0
        for f1, f2, weight in self.pairwise_synergies:
            term = weight * deltas[f1] * deltas[f2]
            if term > 0.0:
                A_1[f1] += term
                A_1[f2] += term
                c2 += term

        # 3-way interaction components A_{i,2}
        A_2 = {feat_name: 0.0 for feat_name in self.structural_weights}
        c3 = 0.0
        for f1, f2, f3, weight in self.three_way_synergies:
            term = weight * deltas[f1] * deltas[f2] * deltas[f3]
            if term > 0.0:
                A_2[f1] += term
                A_2[f2] += term
                A_2[f3] += term
                c3 += term

        # Feature attributions in logit space: phi_i^logit = A_{i,0} + 1/2 A_{i,1} + 1/3 A_{i,2}
        raw_phi_logit = {
            feat_name: A_0[feat_name] + 0.5 * A_1[feat_name] + (1.0 / 3.0) * A_2[feat_name]
            for feat_name in self.structural_weights
        }
        total_logit_shift = c1 + c2 + c3
        logit_z = self.base_logit + total_logit_shift
        risk_score = self._logistic(logit_z)
        base_risk = self.base_prevalence

        # Clean unrounded or minimally rounded logit attributions with exact mathematical efficiency: sum == total_logit_shift
        shapley_logit = {k: round(v, 6) for k, v in raw_phi_logit.items()}

        # 2. Probability Space Attributions (Numerical Path Integration via 128-Point Quadrature)
        # Along straight-line path x(t) = x_0 + t * delta_x:
        # z(t) = base_logit + c1 * t + c2 * t^2 + c3 * t^3
        # phi_i^AS = A_{i,0} M0 + A_{i,1} M1 + A_{i,2} M2
        # where Mm = int_0^1 t^m sigma'(z(t)) dt
        z_t = self.base_logit + c1 * self._gl_t + c2 * (self._gl_t ** 2) + c3 * (self._gl_t ** 3)
        sig = 1.0 / (1.0 + np.exp(-np.clip(z_t, -35.0, 35.0)))
        sig_prime = sig * (1.0 - sig)

        M0 = float(np.sum(self._gl_wt * sig_prime))
        M1 = float(np.sum(self._gl_wt * self._gl_t * sig_prime))
        M2 = float(np.sum(self._gl_wt * (self._gl_t ** 2) * sig_prime))

        # Path-integrated attributions (normalized to ensure sum_i phi_i == delta_p)
        delta_p = risk_score - base_risk
        raw_psi = {
            feat_name: A_0[feat_name] * M0 + A_1[feat_name] * M1 + A_2[feat_name] * M2
            for feat_name in self.structural_weights
        }
        sum_psi = sum(raw_psi.values())
        if sum_psi > 1e-12 and delta_p > 1e-12:
            scale_factor = delta_p / sum_psi
            shapley_prob = {feat_name: round(v * scale_factor, 6) for feat_name, v in raw_psi.items()}
        elif delta_p <= 1e-12:
            shapley_prob = {feat_name: 0.0 for feat_name in self.structural_weights}
        else:
            shapley_prob = {feat_name: round(v, 6) for feat_name, v in raw_psi.items()}

        # 3. Grounded Normative Baseline & Contrastive Attribution Construction
        is_fraud = int(record.get("is_fraud", 0))
        normative_baseline = dict(record)
        cf_input_deltas: Dict[str, float] = {}

        baseline_amount = round(mean_30d, 2)
        normative_baseline["amount"] = baseline_amount
        normative_baseline["is_fraud"] = 0
        normative_baseline["scenario_tag"] = "ORGANIC_NORMAL"
        normative_baseline["haversine_velocity_kph"] = 0.0
        normative_baseline["ip_distance_from_home_km"] = 0.0
        normative_baseline["is_cross_border"] = False
        normative_baseline["avs_match_code"] = "Y"
        normative_baseline["billing_shipping_match"] = 1
        normative_baseline["cvv_match_flag"] = 1

        if is_fraud == 1:
            counterfactual_mode = "ADVERSARIAL_INSERTION"
            cf_input_deltas["amount"] = round(amount - baseline_amount, 2)
            cf_input_deltas["haversine_velocity_kph"] = round(effective_velocity, 2)
            cf_input_deltas["ip_distance_from_home_km"] = round(ip_dist - 0.0, 2)
            cf_input_deltas["billing_shipping_mismatch"] = float(bill_mismatch)
            cf_input_deltas["avs_mismatch_flag"] = float(avs_mismatch)
            cf_input_deltas["cvv_mismatch_flag"] = float(cvv_mismatch)
        else:
            counterfactual_mode = "ORGANIC_BASELINE"
            cf_input_deltas["amount"] = round(amount - baseline_amount, 2)
            cf_input_deltas["haversine_velocity_kph"] = round(effective_velocity, 2)
            cf_input_deltas["ip_distance_from_home_km"] = round(ip_dist - 0.0, 2)
            cf_input_deltas["billing_shipping_mismatch"] = float(bill_mismatch)
            cf_input_deltas["avs_mismatch_flag"] = float(avs_mismatch)
            cf_input_deltas["cvv_mismatch_flag"] = float(cvv_mismatch)

        # 4. Active Causal Drivers
        active_parents: List[str] = []
        best_driver = "baseline"
        max_contrib = 0.0

        for feat_name, phi_p in shapley_prob.items():
            if phi_p > 0.005:
                active_parents.append(feat_name)
            if phi_p > max_contrib:
                max_contrib = phi_p
                best_driver = feat_name

        # 5. Narrative Explanation Generation
        narrative = self._generate_narrative(
            scenario_tag=scenario_tag,
            is_fraud=is_fraud,
            driver=best_driver,
            active_parents=active_parents,
            amount=amount,
        )

        return CausalGroundTruth(
            is_fraud=is_fraud,
            scenario_tag=scenario_tag,
            risk_score=round(risk_score, 6),
            base_risk=round(base_risk, 6),
            logit_z=round(logit_z, 4),
            base_logit=round(self.base_logit, 4),
            analytical_shapley_log_odds=shapley_logit,
            analytical_shapley_probability=shapley_prob,
            counterfactual_input_deltas=cf_input_deltas,
            dominant_causal_driver=best_driver,
            active_causal_parents=active_parents,
            counterfactual_mode=counterfactual_mode,
            counterfactual_twin=normative_baseline,
            normative_baseline=normative_baseline,
            explanation_narrative=narrative,
        )

    def _generate_narrative(
        self,
        scenario_tag: str,
        is_fraud: int,
        driver: str,
        active_parents: List[str],
        amount: float,
    ) -> str:
        """Generates clear, analyst-readable causal narrative."""
        if is_fraud == 0:
            if "HARD_NEGATIVE" in scenario_tag:
                return (
                    f"Legitimate high-ticket or travel outlier (${amount:.2f}). "
                    f"Elevated features ({', '.join(active_parents) if active_parents else driver}) "
                    f"are mitigated by authentic EMV cryptographic verification."
                )
            return "Routine cardholder transaction consistent with historical behavioral baseline."

        if scenario_tag == "CARD_TESTING_BURST":
            return (
                f"Automated card testing probe (${amount:.2f}). Attacker probed card validity "
                f"at a low-friction merchant; primary causal driver: {driver}."
            )
        elif scenario_tag == "ACCOUNT_TAKEOVER":
            return (
                f"Account Takeover exploitation (${amount:.2f}). Transaction initiated from an anomalous "
                f"offshore IP; primary causal driver: {driver}."
            )
        elif scenario_tag == "COUNTERFEIT_CLONE" or scenario_tag == "IMPOSSIBLE_TRAVEL":
            return (
                f"Counterfeit magstripe clone (${amount:.2f}). Terminal swipe executed at remote POS "
                f"concurrent with local cardholder activity; primary causal driver: {driver}."
            )
        elif scenario_tag == "SLEEPER_BUST_OUT":
            return (
                f"Credit line bust-out (${amount:.2f}). High-utilization balance drain; "
                f"primary causal driver: {driver}."
            )
        return f"Adversarial attack ({scenario_tag}, ${amount:.2f}) driven by {driver}."


# Backward compatibility alias
CounterfactualCausalEngine = StructuralCausalEngine
