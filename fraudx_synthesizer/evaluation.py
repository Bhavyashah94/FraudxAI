"""Ground-Truth XAI Evaluation Suite for Transaction and Tabular Pipelines.

Implements closed-form benchmark metrics evaluating post-hoc explainers
(TreeSHAP, KernelSHAP, FastSHAP) against structural causal ground-truth vectors:
1. Support Recovery: Precision@k, Recall@k, F1@k
2. Ranking Fidelity: Kendall's tau-b and Spearman's rho
3. Attribution Error: Directional Cosine Similarity, normalized L1/L2 distance, Relative Attribution Error (RAE)
4. Counterfactual Deletion AUC and Causal Faithfulness
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Callable, Dict, List, Optional, Sequence, Set, Tuple

import numpy as np


@dataclass
class XAIBenchmarkResult:
    """Quantitative evaluation metrics for an explanation against ground truth."""
    precision_at_k: Dict[int, float]
    recall_at_k: Dict[int, float]
    f1_at_k: Dict[int, float]
    kendall_tau: float
    spearman_rho: float
    cosine_similarity: float
    normalized_l1_distance: float
    normalized_l2_distance: float
    relative_attribution_error: float
    causal_faithfulness: Optional[float] = None
    deletion_auc: Optional[float] = None


def compute_spearman_rho_pure_numpy(a: np.ndarray, b: np.ndarray) -> float:
    """Pure NumPy implementation of Spearman rank correlation."""
    if len(a) < 2 or np.all(a == a[0]) or np.all(b == b[0]):
        return 0.0
    rank_a = np.argsort(np.argsort(a)).astype(np.float64)
    rank_b = np.argsort(np.argsort(b)).astype(np.float64)
    mean_a = np.mean(rank_a)
    mean_b = np.mean(rank_b)
    diff_a = rank_a - mean_a
    diff_b = rank_b - mean_b
    denom = np.sqrt(np.sum(diff_a ** 2) * np.sum(diff_b ** 2))
    if denom <= 1e-12:
        return 0.0
    return float(np.sum(diff_a * diff_b) / denom)


def compute_kendall_tau_pure_numpy(a: np.ndarray, b: np.ndarray) -> float:
    """Pure NumPy implementation of Kendall's tau-b."""
    n = len(a)
    if n < 2:
        return 0.0
    concordant = 0
    discordant = 0
    ties_a = 0
    ties_b = 0
    for i in range(n):
        for j in range(i + 1, n):
            da = a[i] - a[j]
            db = b[i] - b[j]
            if da == 0 and db == 0:
                ties_a += 1
                ties_b += 1
            elif da == 0:
                ties_a += 1
            elif db == 0:
                ties_b += 1
            elif (da > 0 and db > 0) or (da < 0 and db < 0):
                concordant += 1
            else:
                discordant += 1

    total_pairs = n * (n - 1) / 2.0
    denom = math.sqrt((total_pairs - ties_a) * (total_pairs - ties_b))
    if denom <= 1e-12:
        return 0.0
    return float((concordant - discordant) / denom)


class GroundTruthXAIEvaluator:
    """Evaluates estimated attribution vectors against structural causal ground truth."""

    def __init__(self, eps: float = 1e-9, causal_threshold: float = 1e-4):
        self.eps = eps
        self.causal_threshold = causal_threshold

    def evaluate_instance(
        self,
        phi_hat: np.ndarray,
        phi_star: np.ndarray,
        k_values: Sequence[int] = (2, 3, 4),
        model_fn: Optional[Callable[[np.ndarray], np.ndarray]] = None,
        x_obs: Optional[np.ndarray] = None,
        x_cf: Optional[np.ndarray] = None,
    ) -> XAIBenchmarkResult:
        """Computes comprehensive evaluation metrics for a single explanation.

        Args:
            phi_hat: Estimated feature attribution vector (d,).
            phi_star: Ground-truth causal attribution vector (d,).
            k_values: Cutoff ranks for Precision@k and Recall@k.
            model_fn: Optional scoring function f(X).
            x_obs: Optional observed transaction vector.
            x_cf: Optional counterfactual twin transaction vector.
        """
        phi_h = np.asarray(phi_hat, dtype=np.float64).flatten()
        phi_s = np.asarray(phi_star, dtype=np.float64).flatten()
        d = len(phi_h)
        assert len(phi_s) == d, f"Dimension mismatch: phi_hat ({d}) != phi_star ({len(phi_s)})"

        # 1. Support Identification
        active_causal_indices = set(np.where(np.abs(phi_s) > self.causal_threshold)[0])
        ranked_hat_indices = np.argsort(-np.abs(phi_h))

        prec_at_k: Dict[int, float] = {}
        rec_at_k: Dict[int, float] = {}
        f1_at_k: Dict[int, float] = {}

        for k in k_values:
            k_clamped = min(k, d)
            top_k_hat = set(ranked_hat_indices[:k_clamped])
            true_positives = len(top_k_hat & active_causal_indices)

            p_k = true_positives / float(k_clamped) if k_clamped > 0 else 0.0
            prec_at_k[k] = round(p_k, 5)

            n_active = len(active_causal_indices)
            if n_active > 0:
                r_k = true_positives / float(n_active)
            else:
                r_k = 1.0 if len(top_k_hat) == 0 else 0.0
            rec_at_k[k] = round(r_k, 5)

            if (p_k + r_k) > 0.0:
                f1 = 2.0 * (p_k * r_k) / (p_k + r_k)
            else:
                f1 = 0.0
            f1_at_k[k] = round(f1, 5)

        # 2. Ranking Correlations
        abs_hat = np.abs(phi_h)
        abs_star = np.abs(phi_s)
        tau_b = compute_kendall_tau_pure_numpy(abs_hat, abs_star)
        rho = compute_spearman_rho_pure_numpy(abs_hat, abs_star)

        # 3. Continuous Attribution Error Metrics
        norm_hat_2 = float(np.linalg.norm(phi_h))
        norm_star_2 = float(np.linalg.norm(phi_s))

        # Directional Cosine Similarity
        if norm_hat_2 > self.eps and norm_star_2 > self.eps:
            cos_sim = float(np.dot(phi_h, phi_s) / (norm_hat_2 * norm_star_2))
        else:
            cos_sim = 1.0 if (norm_hat_2 <= self.eps and norm_star_2 <= self.eps) else 0.0

        # L1 Normalization (Total Variation Distance)
        l1_hat = float(np.sum(np.abs(phi_h)))
        l1_star = float(np.sum(np.abs(phi_s)))
        p_hat = phi_h / (l1_hat + self.eps)
        p_star = phi_s / (l1_star + self.eps)
        norm_l1_dist = float(0.5 * np.sum(np.abs(p_hat - p_star)))

        # L2 Normalization
        u_hat = phi_h / (norm_hat_2 + self.eps)
        u_star = phi_s / (norm_star_2 + self.eps)
        norm_l2_dist = float(np.linalg.norm(u_hat - u_star))

        # Relative Attribution Error (RAE)
        rae = float(np.linalg.norm(phi_h - phi_s) / (norm_star_2 + self.eps))

        # 4. Optional Faithfulness & Deletion Metrics
        causal_faithfulness: Optional[float] = None
        deletion_auc: Optional[float] = None

        if model_fn is not None and x_obs is not None and x_cf is not None:
            causal_faithfulness = self._compute_causal_faithfulness(model_fn, x_obs, x_cf, phi_h)
            deletion_auc = self._compute_deletion_auc(model_fn, x_obs, x_cf, ranked_hat_indices)

        return XAIBenchmarkResult(
            precision_at_k=prec_at_k,
            recall_at_k=rec_at_k,
            f1_at_k=f1_at_k,
            kendall_tau=round(tau_b, 5),
            spearman_rho=round(rho, 5),
            cosine_similarity=round(cos_sim, 5),
            normalized_l1_distance=round(norm_l1_dist, 5),
            normalized_l2_distance=round(norm_l2_dist, 5),
            relative_attribution_error=round(rae, 5),
            causal_faithfulness=round(causal_faithfulness, 5) if causal_faithfulness is not None else None,
            deletion_auc=round(deletion_auc, 5) if deletion_auc is not None else None,
        )

    def _compute_causal_faithfulness(
        self,
        model_fn: Callable[[np.ndarray], np.ndarray],
        x_obs: np.ndarray,
        x_cf: np.ndarray,
        phi_hat: np.ndarray,
    ) -> float:
        """Measures Pearson correlation between attribution and surgical score drop upon counterfactual restitution."""
        d = len(x_obs)
        delta_f = np.zeros(d, dtype=np.float64)
        base_pred = float(model_fn(x_obs.reshape(1, -1))[0])

        for i in range(d):
            if abs(x_obs[i] - x_cf[i]) < self.eps:
                delta_f[i] = 0.0
                continue
            x_pert = x_obs.copy()
            x_pert[i] = x_cf[i]
            pert_pred = float(model_fn(x_pert.reshape(1, -1))[0])
            delta_f[i] = base_pred - pert_pred

        if np.all(delta_f == 0.0) or np.all(phi_hat == 0.0):
            return 1.0 if np.all(delta_f == phi_hat) else 0.0

        mean_hat = np.mean(phi_hat)
        mean_delta = np.mean(delta_f)
        diff_hat = phi_hat - mean_hat
        diff_delta = delta_f - mean_delta
        denom = np.sqrt(np.sum(diff_hat ** 2) * np.sum(diff_delta ** 2))
        if denom <= 1e-12:
            return 0.0
        return float(np.sum(diff_hat * diff_delta) / denom)

    def _compute_deletion_auc(
        self,
        model_fn: Callable[[np.ndarray], np.ndarray],
        x_obs: np.ndarray,
        x_cf: np.ndarray,
        ranked_indices: np.ndarray,
    ) -> float:
        """Area under the prediction decay curve under counterfactual deletion."""
        d = len(x_obs)
        scores: List[float] = []
        x_curr = x_obs.copy()

        for step in range(d):
            idx = ranked_indices[step]
            x_curr[idx] = x_cf[idx]
            pred = float(model_fn(x_curr.reshape(1, -1))[0])
            scores.append(pred)

        return float(np.mean(scores))
