#!/usr/bin/env python
"""Generate the B.E. Major Project I synopsis figures from reproducible sources.

Why a script and not hand-drawn images
--------------------------------------
The previous synopsis shipped figures that contradicted the repository: a Gantt
labelling the platform "10 Playbooks" (it has 13), an architecture diagram
advertising "64,000+ events/sec" (measured: 2,015-2,626 events/sec, see
`docs/PROJECT_CONTEXT.md` 7.11), and a concordance chart annotated with numbers no
command reproduces. Every figure this script writes is derived either from the
repository's own artefacts or from a live measurement, and Figure 10.2 refuses to
draw unless the fresh harness run reproduces the published Table 10.1 row.

Outputs (default `--out /tmp/opencode/synopsisdocs/figures_build/`):

  fig_6_1_architecture.png   Chapter 6 - system architecture (regenerated)
  fig_9_1_context.png        Chapter 9 - context level diagram / Level-0 DFD
  fig_9_2_dfd_l1.png         Chapter 9 - Level-1 DFD           (from the original docx, unchanged)
  fig_9_3_sequence.png       Chapter 9 - 7-hop lifecycle       (from the original docx, unchanged)
  fig_9_4_er.png             Chapter 9 - E-R diagram           (from the original docx, unchanged)
  fig_9_5_control_flow.png   Chapter 9 - control flow          (from the original docx, unchanged)
  fig_10_1_dashboard.png     Chapter 10 - dashboard screenshot (repository GUI asset)
  fig_10_2_concordance.png   Chapter 10 - explainer vs ground truth (live LightGBM run)
  fig_11_1_gantt.png         Chapter 11 - Gantt chart          (regenerated)

The four "from the original docx" files and the logo are extracted by the caller
(`--asset-dir`); this script only regenerates what was wrong or unverifiable.

Usage:
    .venv/bin/python scripts/generate_synopsis_figures.py \
        --out /tmp/opencode/synopsisdocs/figures_build \
        --asset-dir /tmp/opencode/synopsisdocs/original_extract/word/media

The synopsis is printed in black and white: add `--grayscale` to emit every
figure (regenerated and copied) in print-safe grays.
"""

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch, Rectangle

# spec/18 universal colorblind-safe palette (Paul Tol muted/bright)
BLUE = "#4477AA"
LIGHT_BLUE = "#66CCEE"
GREEN = "#228833"
AMBER = "#CCBB44"
RED = "#EE6677"
PURPLE = "#AA3377"
GREY = "#BBBBBB"

GRAYSCALE = False

# Print-safe grayscale substitutes, chosen so that adjacent columns of the
# architecture figure keep distinct luminance steps when the synopsis is
# printed in black and white.
PRINT_GRAY = {
    "#4477AA": "#3a3a3a",  # BLUE
    "#66CCEE": "#c9c9c9",  # LIGHT_BLUE
    "#228833": "#545454",  # GREEN
    "#CCBB44": "#6e6e6e",  # AMBER
    "#EE6677": "#9a9a9a",  # RED
    "#AA3377": "#1f1f1f",  # PURPLE
    "#BBBBBB": "#cfcfcf",  # GREY
    "#5B8FC9": "#3f3f3f",  # Gantt semester VII bars
    "#8F8F8F": "#b0b0b0",  # Gantt semester VIII bars
    "#7A2F3A": "#4a4a4a",  # concordance ground-truth bar edge
    "#E8F0F7": "#f0f0f0",  # pale tint fills
    "#F7F3E2": "#f0f0f0",
    "#E6F2E8": "#f0f0f0",
    "#F2E6F0": "#f0f0f0",
}


def shade(color: str) -> str:
    """Map a design color to its print-safe grayscale when --grayscale is on."""
    if not GRAYSCALE:
        return color
    return PRINT_GRAY.get(color.upper(), color)


def enable_grayscale() -> None:
    """Rebind the palette constants to their print-safe grayscale substitutes."""
    global BLUE, LIGHT_BLUE, GREEN, AMBER, RED, PURPLE, GREY, GRAYSCALE
    GRAYSCALE = True
    BLUE, LIGHT_BLUE, GREEN, AMBER, RED, PURPLE, GREY = tuple(
        PRINT_GRAY[c] for c in (BLUE, LIGHT_BLUE, GREEN, AMBER, RED, PURPLE, GREY)
    )

# The published Table 10.1 row this script verifies against before annotating
# any figure (docs/SYNOPSIS_MASTER_CONTENT.md, regenerated 2026-10-16).
PUBLISHED_LIGHTGBM = {
    "kendall_tau": 0.3106,
    "spearman_rho": 0.3726,
    "precision_at_3": 0.3627,
    "rae": 1.6927,
    "pr_auc": 0.9118,
    "roc_auc": 0.9861,
}

TOLERANCE = 5e-4


def _wrap(ax, x, y, text, width, **kwargs):
    import textwrap

    ax.text(x, y, "\n".join(textwrap.wrap(text, width)), **kwargs)


def text_width_inches(s: str, size: float, weight: str = "normal") -> float:
    """Measured width of `s` in inches when set at `size` pt in DejaVu Sans."""
    from matplotlib.font_manager import FontProperties
    from matplotlib.textpath import TextPath

    prop = FontProperties(family="DejaVu Sans", weight=weight)
    tp = TextPath((0, 0), s, size=size, prop=prop)
    return tp.get_extents().width / 72.0


def fit_size(s: str, max_in: float, start: float, floor: float = 7.0,
             weight: str = "normal") -> float:
    """Largest size at or below `start` that keeps `s` within `max_in` inches."""
    size = start
    while size > floor and text_width_inches(s, size, weight) > max_in:
        size -= 0.2
    return round(size, 1)


def fit_wrap(s: str, size: float, max_in: float) -> list[str]:
    """Wrap bullet text so every rendered line stays within `max_in` inches."""
    import textwrap

    width = int(max_in / (size * 0.5 / 72.0))
    while width > 6:
        lines = textwrap.wrap("\u2022 " + s, width)
        if all(text_width_inches(line, size) <= max_in for line in lines):
            return lines
        width -= 1
    return ["\u2022 " + s]


def figure_architecture(out: Path) -> Path:
    """Figure 6.1: the four-stage fraud simulation pipeline, sized for print.

    Designed at final print size: 1 data unit = 1 inch, figure saved ~6.6 in
    wide, so when it is placed at full text width in the synopsis the 9 pt
    bullet text below is close to the size the reader sees on paper. Bullet
    lists are trimmed and every rendered line is measured so nothing
    overflows; the full detail lives in the Chapter 6 text.
    """
    fig = plt.figure(figsize=(6.6, 3.9), dpi=300)
    ax = fig.add_axes((0.0, 0.0, 1.0, 1.0))
    ax.set_xlim(0, 6.6)
    ax.set_ylim(0, 3.9)
    ax.axis("off")

    columns = [
        {
            "title": "Multi-Agent Simulation",
            "color": BLUE,
            "groups": [
                ("Normal Cardholders", [
                    "Calibrated India & US lifecycle",
                    "Home geography (haversine velocity)",
                ]),
                ("Adaptive Adversaries", [
                    "13 grounded playbooks (8 US + 5 India)",
                    "Back-off or decay after declines",
                ]),
                ("Microsecond Engine", [
                    "64-bit monotonic priority queue",
                    "Zero future lookahead by construction",
                ]),
            ],
        },
        {
            "title": "Banking Rails & Switch",
            "color": AMBER,
            "groups": [
                ("Payment Switch (<50 ms)", [
                    "ISO 8583 dual-message pair",
                    "MTI 0100 auth / 0200 clearing",
                ]),
                ("Regulatory Guards", [
                    "RBI AFA OTP step-up",
                    "US ECOA adverse actions",
                ]),
                ("Physical Invariants", [
                    ">900 km/h impossible travel blocked",
                    "Strict double-entry balance",
                ]),
            ],
        },
        {
            "title": "Operations & Supervision",
            "color": GREEN,
            "groups": [
                ("Human Investigator Desk", [
                    "Daily alert review capacity limits",
                    "Alert precision@K and recall",
                ]),
                ("Dispute & Chargeback Lag", [
                    "30-90 day customer dispute delay",
                    "Settlement feed (T+1 to T+3)",
                ]),
                ("Zero-Leakage Streaming", [
                    "Inference feed (day 0)",
                    "Decision excludes its own outcome",
                ]),
            ],
        },
        {
            "title": "Ground-Truth XAI Audits",
            "color": PURPLE,
            "groups": [
                ("Known Attack Cause (\u0394x)", [
                    "Pearlian counterfactual twins",
                    "Structural causal simulation",
                ]),
                ("Model Benchmarking", [
                    "TreeSHAP vs ground truth \u03c6*",
                    "Kendall \u03c4, Spearman \u03c1, RAE, P@k",
                ]),
                ("Pillar Audits", [
                    "Data fidelity & privacy robustness",
                    "Verdicts and violations published",
                ]),
            ],
        },
    ]

    x0, width, gap = 0.05, 1.5625, 0.10
    for ci, col in enumerate(columns):
        left = x0 + ci * (width + gap)
        # header band
        ax.add_patch(FancyBboxPatch((left, 3.52), width, 0.30,
                                    boxstyle="round,pad=0.015,rounding_size=0.05",
                                    facecolor=col["color"], edgecolor="none"))
        ax.text(left + width / 2, 3.67, col["title"], ha="center", va="center",
                fontsize=fit_size(col["title"], 1.44, start=8.8, weight="bold"),
                fontweight="bold", color="white")
        y = 3.42
        for gname, bullets in col["groups"]:
            ax.text(left + 0.05, y, gname, va="top",
                    fontsize=fit_size(gname, 1.44, start=9.0, weight="bold"),
                    fontweight="bold", color=col["color"])
            y -= 0.17
            for b in bullets:
                for line in fit_wrap(b, 9.0, 1.44):
                    ax.text(left + 0.08, y, line, fontsize=9.0, color="#222222", va="top")
                    y -= 0.15
                y -= 0.04
            y -= 0.05

    # measured facts strip
    ax.add_patch(Rectangle((0.05, 0.10), 6.50, 0.42, facecolor="#f0f0f0",
                           edgecolor="#5a5a5a", linewidth=0.9))
    ax.text(3.30, 0.31,
            "Measured: 2,015-2,626 events/s \u00b7 1.5 GB peak RSS \u00b7 410 automated tests",
            ha="center", va="center", fontsize=8.5, color="#222222")

    # flow arrows between column headers
    for ci in range(len(columns) - 1):
        x = x0 + (ci + 1) * width + ci * gap + gap / 2
        ax.add_patch(FancyArrowPatch((x - 0.032, 3.67), (x + 0.032, 3.67),
                                     arrowstyle="-|>", mutation_scale=7,
                                     linewidth=1.0, color="#555555"))

    path = out / "fig_6_1_architecture.png"
    fig.savefig(path, bbox_inches="tight", pad_inches=0.04, facecolor="white")
    plt.close(fig)
    return path


def figure_context_dfd(out: Path) -> Path:
    """Figure 9.1: Level-0 context diagram with the true 13-playbook count."""
    fig, ax = plt.subplots(figsize=(9.6, 6.6), dpi=170)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 68)
    ax.axis("off")

    def box(x, y, w, h, title, lines, color):
        ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.4,rounding_size=1.0",
                                    facecolor="white", edgecolor=color, linewidth=1.6))
        ax.text(x + w / 2, y + h - 2.6, title, ha="center", va="top",
                fontsize=9.6, fontweight="bold", color="#1a1a1a")
        for i, ln in enumerate(lines):
            ax.text(x + w / 2, y + h - 5.2 - i * 2.4, ln, ha="center", va="top",
                    fontsize=8.2, color="#333333")

    box(28, 58, 44, 9.2, "Cardholder Agents",
        ["Legitimate personas: diurnal spend, travel,", "merchant loyalty patterns"], BLUE)
    box(3, 27, 24, 12.5, "Adversarial Entities",
        ["13 attack playbooks", "(8 US + 5 India)", "closed-loop adaptation"], RED)
    box(73, 27, 24, 12.5, "Merchant Terminals",
        ["MCC taxonomy, POS channels,", "3DS access control,", "lat/lon coordinates"], GREEN)
    box(34, 27, 32, 12.5, "FRAUDXAI ENGINE",
        ["Simulation core: Hawkes event queue,", "ISO 8583 rails, SCM causal core"], PURPLE)
    box(28, 2, 44, 10, "Banking Switches & Regulators",
        ["Issuers, acquirers, compliance FIU;", "ISO 8583 streams & adverse reason codes"], BLUE)

    def arrow(x1, y1, x2, y2):
        ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2), arrowstyle="-|>",
                                     mutation_scale=15, linewidth=1.4, color="#555555"))

    arrow(50, 58, 50, 40.0)
    ax.text(50.8, 52.5, "card present / online swipes", fontsize=8.0, color="#444444")
    arrow(27, 33.2, 34, 33.2)
    ax.text(30.5, 34.6, "playbook\ninjections", ha="center", va="bottom",
            fontsize=7.6, color="#444444", linespacing=1.1)
    arrow(66, 33.2, 73, 33.2)
    arrow(73, 36.4, 66, 36.4)
    ax.text(69.5, 38.2, "auth requests", ha="center", va="bottom", fontsize=7.6, color="#444444")
    ax.text(69.5, 31.4, "results (00/05)", ha="center", va="top", fontsize=7.6, color="#444444")
    arrow(50, 27, 50, 12.5)
    ax.text(50.8, 21.5, "ISO 8583 streams & adverse reason codes", fontsize=8.0, color="#444444")

    fig.tight_layout()
    path = out / "fig_9_1_context.png"
    fig.savefig(path, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    return path


def figure_concordance(out: Path) -> Path:
    """Figure 10.2: TreeSHAP vs ground truth, drawn only from a verified live run."""
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
    from fraudx_synthesizer.benchmark import XAIBenchmarkHarness
    from fraudx_synthesizer.causal_contract import feature_names

    harness = XAIBenchmarkHarness(n_transactions=2000, fraud_prevalence=0.05, region="US", seed=42)
    summary = harness.run_benchmark("lightgbm")

    measured = {
        "kendall_tau": round(summary.mean_kendall_tau, 4),
        "spearman_rho": round(summary.mean_spearman_rho, 4),
        "precision_at_3": round(summary.mean_precision_at_3, 4),
        "rae": round(summary.mean_relative_attribution_error, 4),
        "pr_auc": round(summary.pr_auc, 4),
        "roc_auc": round(summary.auc_roc, 4),
    }
    for key, published in PUBLISHED_LIGHTGBM.items():
        if abs(measured[key] - published) > TOLERANCE:
            raise SystemExit(
                f"Figure 10.2 refused: fresh run gives {key}={measured[key]:.4f}, "
                f"published Table 10.1 says {published:.4f}. Update the table or the figure, "
                "never annotate a figure with numbers the command does not reproduce."
            )

    # Re-run the attribution loop of `benchmark.py::run_benchmark` to obtain the
    # per-feature shares the summary does not expose (same data, same model, same
    # split -- verified above by reproducing every published scalar).
    import lightgbm as lgb
    import shap

    X, y, GT, _records = harness.generate_and_prepare_dataset()
    n_train = int(len(X) * 0.70)
    model = lgb.LGBMClassifier(n_estimators=60, max_depth=4, random_state=42, verbose=-1)
    model.fit(X[:n_train], y[:n_train])
    explainer = shap.TreeExplainer(model)
    shap_values = harness._positive_class_shap(explainer.shap_values(X[n_train:]))
    y_test = y[n_train:]
    GT_test = GT[n_train:]
    fraud_idx = [i for i, label in enumerate(y_test) if label == 1][:50]

    abs_shap = np.abs(shap_values[fraud_idx])
    shap_shares = np.mean(abs_shap / np.maximum(abs_shap.sum(axis=1, keepdims=True), 1e-12), axis=0)
    abs_gt = np.abs(GT_test[fraud_idx])
    gt_shares = np.mean(abs_gt / np.maximum(abs_gt.sum(axis=1, keepdims=True), 1e-12), axis=0)

    cols = list(feature_names())
    order = np.argsort(-(shap_shares + gt_shares))
    labels = [cols[j] for j in order]
    emp = shap_shares[order]
    gt = gt_shares[order]

    fig = plt.figure(figsize=(13.6, 6.2), dpi=170)
    ax1 = fig.add_axes([0.06, 0.16, 0.50, 0.70])
    ax2 = fig.add_axes([0.63, 0.04, 0.35, 0.86], projection="polar")

    yy = np.arange(len(labels))
    h = 0.38
    ax1.barh(yy - h / 2, emp, height=h, color=BLUE, label="Empirical TreeSHAP |share|")
    ax1.barh(yy + h / 2, gt, height=h, color=RED, hatch="///", edgecolor=shade("#7a2f3a"),
             label="Ground truth \u03c6* (SCM)")
    ax1.set_yticks(yy)
    ax1.set_yticklabels(labels, fontsize=8.4)
    ax1.invert_yaxis()
    ax1.set_xlabel("Mean normalised feature attribution share", fontsize=9.5)
    ax1.set_title("Attribution fidelity: explainer vs causal ground truth",
                  fontsize=11.5, fontweight="bold", loc="left")
    ax1.legend(fontsize=8.5, loc="lower right", frameon=False)
    ax1.grid(axis="x", color=GREY, alpha=0.35, linewidth=0.6)
    ax1.set_axisbelow(True)
    for s in ("top", "right"):
        ax1.spines[s].set_visible(False)
    ax1.annotate(
        f"Kendall \u03c4_b = {measured['kendall_tau']:.4f}   "
        f"Spearman \u03c1 = {measured['spearman_rho']:.4f}\n"
        f"Precision@3 = {measured['precision_at_3']:.4f}   "
        f"RAE = {measured['rae']:.4f}   n = {summary.n_evaluated_samples} "
        "(LightGBM, seed 42, n=2000)",
        xy=(0.0, -0.19), xycoords="axes fraction", fontsize=8.6, color="#333333",
    )

    theta = np.linspace(0, 2 * np.pi, len(labels), endpoint=False)
    theta_closed = np.concatenate([theta, theta[:1]])
    for vals, color, name, style in ((emp, BLUE, "TreeSHAP", "-"), (gt, RED, "Ground truth \u03c6*", "--")):
        v = np.concatenate([vals, vals[:1]])
        ax2.plot(theta_closed, v, color=color, linewidth=1.7, label=name, linestyle=style)
        ax2.fill(theta_closed, v, color=color, alpha=0.12)
    ax2.set_xticks(theta)
    ax2.set_xticklabels(labels, fontsize=6.6)
    ax2.tick_params(pad=1)
    ax2.set_title("Attribution geometry", fontsize=11.5, fontweight="bold", pad=16)
    ax2.grid(color=GREY, alpha=0.5, linewidth=0.6)

    path = out / "fig_10_2_concordance.png"
    fig.savefig(path, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    return path


def figure_gantt(out: Path) -> Path:
    """Figure 11.1: two-semester Gantt with the true playbook count."""
    tasks = [
        ("1. Literature Survey & Statutory Spec", [(0, 1.0)]),
        ("2. Hawkes Monotonic Simulation Engine", [(1, 2.0)]),
        ("3. Dual-Region Rails & 13 Playbooks", [(2, 2.0)]),
        ("4. SCM Causal Ground Truth Prototype", [(3, 2.0)]),
        ("5. Synopsis & Sem VII Defense", [(4, 1.0)]),
        ("6. Multi-Agent Intent Mesh Scaling", [(6, 2.0)]),
        ("7. Prequential Streaming Delay Queues", [(7, 2.0)]),
        ("8. Real-Time Web Telemetry Dashboard", [(8, 2.0)]),
        ("9. External Benchmark Audits (BAF/CIS)", [(9, 2.0)]),
        ("10. Final Thesis & University Defense", [(10, 1.0)]),
    ]
    months = ["Jul", "Aug", "Sep", "Oct", "Nov", "Dec", "Jan", "Feb", "Mar", "Apr", "May"]

    fig, ax = plt.subplots(figsize=(12.4, 5.8), dpi=170)
    ax.set_xlim(-7.8, 11)
    ax.set_ylim(-2.6, len(tasks) + 0.4)
    ax.invert_yaxis()
    ax.axis("off")

    # semester header bands (months occupy x in [0, 11]; task names live left of 0)
    ax.add_patch(Rectangle((0, -2.5), 6, 1.15, facecolor=shade("#e8f0f7"), edgecolor=BLUE, linewidth=1.0))
    ax.add_patch(Rectangle((6, -2.5), 5, 1.15, facecolor=shade("#f2e6f0"), edgecolor=PURPLE, linewidth=1.0))
    ax.text(3, -1.925, "BE PROJECT PART I (SEM VII)", ha="center", va="center",
            fontsize=10, fontweight="bold", color=BLUE)
    ax.text(8.5, -1.925, "BE PROJECT PART II (SEM VIII)", ha="center", va="center",
            fontsize=10, fontweight="bold", color=PURPLE)
    for mi, m in enumerate(months):
        ax.text(mi + 0.5, -0.75, m, ha="center", va="center", fontsize=8.6, color="#333333")
    ax.text(-7.6, -0.9, "TASK / MILESTONE", ha="left", va="center",
            fontsize=10, fontweight="bold", color="#1a1a1a")

    for ti, (name, spans) in enumerate(tasks):
        y = ti + 0.5
        ax.add_patch(Rectangle((-7.8, ti), 18.8, 1.0,
                               facecolor="#fafafa" if ti % 2 else "white",
                               edgecolor="#dddddd", linewidth=0.6))
        ax.text(-7.6, y, name, ha="left", va="center", fontsize=9.0, color="#1a1a1a")
        for start, dur in spans:
            ax.add_patch(FancyBboxPatch((start + 0.08, ti + 0.22), dur - 0.16, 0.56,
                                        boxstyle="round,pad=0.02,rounding_size=0.18",
                                        facecolor=shade("#5b8fc9") if start < 6 else shade("#8f8f8f"),
                                        edgecolor="none", alpha=0.95))

    # month gridlines
    for mi in range(12):
        ax.plot([mi, mi], [0, len(tasks)], color="#e6e6e6", linewidth=0.7, zorder=0)
    ax.plot([0, 0], [-2.5, len(tasks)], color="#888888", linewidth=1.0, zorder=1)
    ax.plot([6, 6], [-2.5, len(tasks)], color="#888888", linewidth=1.2, zorder=1)

    fig.tight_layout()
    path = out / "fig_11_1_gantt.png"
    fig.savefig(path, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    return path


def _convert_gray(path: Path) -> None:
    """Rewrite a copied raster in grayscale for the B/W-printed synopsis."""
    from PIL import Image

    img = Image.open(path)
    gray = img.convert("L")
    img.close()
    gray.save(path)


def copy_assets(out: Path, asset_dir: Path, repo_root: Path) -> list[Path]:
    """Copy unchanged originals (diagrams, logo) and the dashboard screenshot."""
    copied = []
    mapping = {
        "image6.png": "fig_9_2_dfd_l1.png",
        "image5.png": "fig_9_3_sequence.png",
        "image7.png": "fig_9_4_er.png",
        "image10.png": "fig_9_5_control_flow.png",
        "image2.png": "college_logo.png",
    }
    for src, dst in mapping.items():
        s = asset_dir / src
        if s.exists():
            shutil.copyfile(s, out / dst)
            if GRAYSCALE and dst != "college_logo.png":
                _convert_gray(out / dst)
            copied.append(out / dst)
    dashboard = repo_root / "gui" / "screenshots" / "3_screen_xai_desktop.png"
    if dashboard.exists():
        shutil.copyfile(dashboard, out / "fig_10_1_dashboard.png")
        if GRAYSCALE:
            _convert_gray(out / "fig_10_1_dashboard.png")
        copied.append(out / "fig_10_1_dashboard.png")
    return copied


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--out", type=Path, default=Path("/tmp/opencode/synopsisdocs/figures_build"))
    ap.add_argument("--asset-dir", type=Path,
                    default=Path("/tmp/opencode/synopsisdocs/original_extract/word/media"))
    ap.add_argument("--skip-concordance", action="store_true",
                    help="Skip Figure 10.2 (the only figure that trains a model)")
    ap.add_argument("--grayscale", action="store_true",
                    help="Emit every figure in print-safe grayscale (B/W report)")
    args = ap.parse_args()
    if args.grayscale:
        enable_grayscale()
    args.out.mkdir(parents=True, exist_ok=True)
    repo_root = Path(__file__).resolve().parents[1]

    written = [figure_architecture(args.out), figure_context_dfd(args.out)]
    if not args.skip_concordance:
        written.append(figure_concordance(args.out))
    written.append(figure_gantt(args.out))
    written.extend(copy_assets(args.out, args.asset_dir, repo_root))

    for p in written:
        print(p)


if __name__ == "__main__":
    main()
