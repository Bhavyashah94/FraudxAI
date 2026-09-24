"""Deterministic Verification Suite for Day 5 (Slice 18): Camera-Ready Reporting & Unified Benchmark CLI."""

from __future__ import annotations

import json
from pathlib import Path
import tempfile
import pytest
import numpy as np

from fraudx_synthesizer.benchmark_reporter import (
    AdversarialPrivacyScorecard,
    BenchmarkReportCompiler,
    CausalXAIScorecard,
    DataFidelityScorecard,
    OperationalStreamingScorecard,
    PublicationPlotter,
    UnifiedBenchmarkReportData,
    UnifiedBenchmarkRunner,
)
from fraudx_synthesizer.evaluation import DailyStreamingMetrics


@pytest.fixture
def sample_report_data() -> UnifiedBenchmarkReportData:
    """Creates a deterministic reference benchmark report fixture."""
    return UnifiedBenchmarkReportData(
        schema_version="1.0.0",
        metadata={
            "timestamp_utc": "2026-09-24T12:00:00Z",
            "region": "US",
            "currency": "USD",
            "n_transactions": 2500,
            "seed": 42,
            "model_architecture": "HistGradientBoostingClassifier",
            "explainer_type": "Pearlian_SCM_vs_TreeSHAP",
        },
        system_provenance={
            "python_version": "3.13.0",
            "platform": "Windows-11",
            "cpu_count": 8,
            "runtime_seconds": 12.45,
        },
        fidelity=DataFidelityScorecard(
            wasserstein_amount_log=0.0821,
            wasserstein_arrival_log=0.0914,
            js_divergence_mcc=0.0312,
            js_divergence_channel=0.0185,
            spearman_frobenius_error=0.4210,
            passed=True,
        ),
        privacy=AdversarialPrivacyScorecard(
            dcr_5th_percentile=0.0652,
            nndr_mean=0.8415,
            mia_attack_roc_auc=0.5120,
            evasion_rate_macro_mean=0.1420,
            passed=True,
        ),
        streaming=OperationalStreamingScorecard(
            n_days_evaluated=4,
            w_train_days=3.0,
            w_test_days=1.0,
            delta_delay_days=1.5,
            mean_pr_auc=0.6840,
            mean_average_precision=0.6812,
            mean_p_at_k=0.7200,
            mean_cp_at_k=0.6500,
            mean_dollar_recall_at_k=0.8250,
            mean_dollar_precision_at_k=0.4120,
            total_cost_base=12540.50,
            total_cost_model=3420.25,
            overall_savings_ratio=0.7273,
            drift_detected_days_count=0,
            passed=True,
        ),
        xai=CausalXAIScorecard(
            mean_kendall_tau=0.7333,
            mean_spearman_rho=0.8857,
            mean_pearson_r=0.9240,
            mean_precision_at_3=1.0,
            mean_relative_attribution_error=0.1240,
            mean_causal_faithfulness=0.8800,
            passed=True,
        ),
        all_pillars_passed=True,
        certification_grade="TIER-1_GOLD",
        violations=[],
        daily_trajectory=[
            {"day_index": 0, "n_tx": 625, "n_fraud": 42, "pr_auc": 0.65, "p_at_k": 0.70, "cp_at_k": 0.60, "dollar_recall_at_k": 0.80, "savings_ratio": 0.71, "drift_detected": False},
            {"day_index": 1, "n_tx": 625, "n_fraud": 40, "pr_auc": 0.67, "p_at_k": 0.72, "cp_at_k": 0.64, "dollar_recall_at_k": 0.82, "savings_ratio": 0.72, "drift_detected": False},
            {"day_index": 2, "n_tx": 625, "n_fraud": 44, "pr_auc": 0.70, "p_at_k": 0.73, "cp_at_k": 0.67, "dollar_recall_at_k": 0.84, "savings_ratio": 0.74, "drift_detected": False},
            {"day_index": 3, "n_tx": 625, "n_fraud": 41, "pr_auc": 0.71, "p_at_k": 0.73, "cp_at_k": 0.69, "dollar_recall_at_k": 0.84, "savings_ratio": 0.74, "drift_detected": False},
        ],
        feature_attributions={
            "amount": 0.42,
            "haversine_velocity_kph": 0.28,
            "ip_distance_from_home_km": 0.16,
            "user_tx_count_1h": 0.08,
            "user_tx_count_24h": 0.04,
            "cvv_match_flag": 0.02,
        },
        ground_truth_phi={
            "amount": 0.45,
            "haversine_velocity_kph": 0.25,
            "ip_distance_from_home_km": 0.18,
            "user_tx_count_1h": 0.07,
            "user_tx_count_24h": 0.03,
            "cvv_match_flag": 0.02,
        },
    )


def test_camera_ready_figures_generation(tmp_path: Path):
    """Test 1: Verify all 5 publication figures are generated in PDF and PNG at 300 DPI."""
    plotter = PublicationPlotter(style="ieee")

    # Fig 1: Prequential Trajectory
    daily_objs = [
        DailyStreamingMetrics(
            day_index=i,
            t_start_seconds=i * 86400.0,
            t_end_seconds=(i + 1) * 86400.0,
            n_transactions=500,
            n_fraud_actual=35,
            pr_auc=0.65 + i * 0.02,
            average_precision=0.64 + i * 0.02,
            p_at_k=0.70,
            cp_at_k=0.60,
            dollar_recall_at_k=0.80,
            dollar_precision_at_k=0.05,
            cost_base=1000.0,
            cost_model=300.0,
            savings_ratio=0.70,
            n_train_admissible=200,
            drift_detected=False,
        )
        for i in range(4)
    ]
    p1 = plotter.plot_prequential_timeseries(daily_objs, output_path=tmp_path, formats=("png", "pdf"))
    assert p1["png"].exists() and p1["png"].stat().st_size > 1000
    assert p1["pdf"].exists() and p1["pdf"].stat().st_size > 1000

    # Fig 2: Operational Triage
    k_vals = [10, 25, 50, 100, 200]
    p_k = [0.85, 0.78, 0.70, 0.55, 0.38]
    cp_k = [0.75, 0.70, 0.65, 0.58, 0.45]
    p2 = plotter.plot_operational_triage_tradeoff(k_vals, p_k, cp_k, output_path=tmp_path, formats=("png", "pdf"))
    assert p2["png"].exists() and p2["png"].stat().st_size > 1000

    # Fig 3: Financial Savings
    s_ratios = [0.45, 0.68, 0.73, 0.70, 0.58]
    net_dollars = [4500.0, 6800.0, 7300.0, 7000.0, 5800.0]
    p3 = plotter.plot_financial_savings_utility(k_vals, s_ratios, net_dollars, output_path=tmp_path, formats=("png", "pdf"))
    assert p3["png"].exists() and p3["png"].stat().st_size > 1000

    # Fig 4: Streaming Drift Timeline
    days = [1, 2, 3, 4]
    ks_p = [0.65, 0.55, 0.42, 0.005]  # Day 4 has drift alarm
    psi_s = [0.02, 0.04, 0.08, 0.28]  # Day 4 has severe alarm
    p4 = plotter.plot_streaming_drift_timeline(days, ks_p, psi_s, output_path=tmp_path, formats=("png", "pdf"))
    assert p4["png"].exists() and p4["png"].stat().st_size > 1000

    # Fig 5: Ground-Truth XAI Comparison
    feats = ["amount", "velocity", "ip_dist", "tx_1h"]
    v_s = [0.45, 0.25, 0.20, 0.10]
    v_gt = [0.42, 0.28, 0.18, 0.12]
    p5 = plotter.plot_ground_truth_xai_comparison(feats, v_s, v_gt, pearson_r=0.98, spearman_rho=0.95, output_path=tmp_path, formats=("png", "pdf"))
    assert p5["png"].exists() and p5["pdf"].exists()


def test_benchmark_results_json_schema_validity(tmp_path: Path, sample_report_data: UnifiedBenchmarkReportData):
    """Test 2: Verify JSON serialization contains all required schema keys."""
    json_path = tmp_path / "benchmark_results.json"
    BenchmarkReportCompiler.compile_json(sample_report_data, json_path)

    assert json_path.exists()
    with open(json_path, "r", encoding="utf-8") as f:
        d = json.load(f)

    # Invariant: Must contain all 4 evaluation pillars and metadata
    assert d["schema_version"] == "1.0.0"
    assert "metadata" in d and d["metadata"]["region"] == "US"
    assert "system_provenance" in d and d["system_provenance"]["runtime_seconds"] > 0
    assert "fidelity" in d and d["fidelity"]["wasserstein_amount_log"] == 0.0821
    assert "privacy" in d and d["privacy"]["dcr_5th_percentile"] == 0.0652
    assert "streaming" in d and d["streaming"]["overall_savings_ratio"] == 0.7273
    assert "xai" in d and d["xai"]["mean_spearman_rho"] == 0.8857
    assert d["all_pillars_passed"] is True
    assert d["certification_grade"] == "TIER-1_GOLD"


def test_four_pillar_scorecard_computation():
    """Test 3: Verify UnifiedBenchmarkRunner executes simulation and evaluates all 4 pillars."""
    runner = UnifiedBenchmarkRunner(
        region="IN",
        n_transactions=600,
        time_span_days=10.0,
        k_daily=10,
        w_train_days=2.0,
        w_test_days=1.0,
        delta_delay_days=1.0,
        seed=101,
    )
    report = runner.run_benchmark()

    assert report.metadata["region"] == "IN"
    assert report.metadata["currency"] == "INR"
    assert report.fidelity.wasserstein_amount_log >= 0.0
    assert 0.0 <= report.fidelity.js_divergence_mcc <= 1.0
    assert report.privacy.dcr_5th_percentile >= 0.0
    assert 0.0 <= report.privacy.nndr_mean <= 1.0
    assert report.streaming.n_days_evaluated >= 1
    assert 0.0 <= report.streaming.mean_pr_auc <= 1.0
    assert report.streaming.overall_savings_ratio <= 1.0
    assert -1.0 <= report.xai.mean_spearman_rho <= 1.0
    assert report.certification_grade in ("TIER-1_GOLD", "TIER-2_SILVER", "NON_CERTIFIED_FAIL")


def test_offline_standalone_html_report_compilation(tmp_path: Path, sample_report_data: UnifiedBenchmarkReportData):
    """Test 4: Verify generated HTML report is 100% offline with zero external CDNs."""
    plotter = PublicationPlotter(style="ieee")
    fig_paths = {}

    daily_objs = [
        DailyStreamingMetrics(
            day_index=i, t_start_seconds=0.0, t_end_seconds=86400.0, n_transactions=100, n_fraud_actual=5,
            pr_auc=0.5, average_precision=0.5, p_at_k=0.5, cp_at_k=0.5, dollar_recall_at_k=0.5,
            dollar_precision_at_k=0.05, cost_base=100.0, cost_model=50.0, savings_ratio=0.5,
            n_train_admissible=50, drift_detected=False
        ) for i in range(2)
    ]
    fig_paths["fig1_prequential_timeseries"] = plotter.plot_prequential_timeseries(daily_objs, output_path=tmp_path)
    fig_paths["fig2_operational_triage_tradeoff"] = plotter.plot_operational_triage_tradeoff([10, 20], [0.8, 0.7], [0.6, 0.5], output_path=tmp_path)
    fig_paths["fig3_financial_savings_utility"] = plotter.plot_financial_savings_utility([10, 20], [0.5, 0.6], [500.0, 600.0], output_path=tmp_path)
    fig_paths["fig4_streaming_drift_timeline"] = plotter.plot_streaming_drift_timeline([1, 2], [0.5, 0.4], [0.02, 0.03], output_path=tmp_path)
    fig_paths["fig5_ground_truth_xai_comparison"] = plotter.plot_ground_truth_xai_comparison(
        ["amount", "velocity"], [0.6, 0.4], [0.55, 0.45], 0.95, 0.90, output_path=tmp_path
    )

    html_path = tmp_path / "benchmark_report.html"
    BenchmarkReportCompiler.compile_html(sample_report_data, fig_paths, html_path)

    assert html_path.exists()
    content = html_path.read_text(encoding="utf-8")

    # Invariants: Standalone self-contained HTML
    assert "data:image/png;base64," in content, "HTML report must embed figures as base64 images!"
    assert "http://" not in content, "Offline HTML must not reference external HTTP assets!"
    assert "https://" not in content, "Offline HTML must not reference external HTTPS assets!"
    assert "fonts.googleapis.com" not in content, "No external Google Fonts allowed in air-gapped forensic report!"


def test_cli_benchmark_run_end_to_end(tmp_path: Path):
    """Test 5: Verify CLI benchmark command with --unified and --camera-ready flags."""
    import argparse
    from fraudx_synthesizer.cli import cmd_benchmark

    out_dir = tmp_path / "run_out"
    args = argparse.Namespace(
        command="benchmark",
        samples=400,
        region="US",
        fraud_rate=0.06,
        seed=77,
        unified=True,
        camera_ready=True,
        output_dir=str(out_dir),
        conference_style="ieee",
        w_train=2.0,
        w_test=1.0,
        delta_delay=1.0,
        k_daily=10,
        output_report=None,
        json=False,
    )

    cmd_benchmark(args)

    assert (out_dir / "benchmark_results.json").exists()
    assert (out_dir / "BENCHMARK_REPORT.md").exists()
    assert (out_dir / "benchmark_report.html").exists()
    assert (out_dir / "figures" / "fig1_prequential_timeseries.png").exists()
    assert (out_dir / "figures" / "fig5_ground_truth_xai_comparison.png").exists()


def test_cli_benchmark_report_end_to_end(tmp_path: Path, sample_report_data: UnifiedBenchmarkReportData):
    """Test 6: Verify CLI report compilation from an existing benchmark_results.json."""
    import argparse
    from fraudx_synthesizer.cli import cmd_report

    # Save benchmark_results.json
    in_json = tmp_path / "benchmark_results.json"
    BenchmarkReportCompiler.compile_json(sample_report_data, in_json)

    out_dir = tmp_path / "compiled_reports"
    args = argparse.Namespace(
        command="report",
        input=str(in_json),
        output_dir=str(out_dir),
        format="json,md,html",
        conference_style="acm",
    )

    cmd_report(args)

    assert (out_dir / "benchmark_results.json").exists()
    assert (out_dir / "BENCHMARK_REPORT.md").exists()
    assert (out_dir / "benchmark_report.html").exists()
    assert (out_dir / "figures" / "fig2_operational_triage_tradeoff.png").exists()


def test_cli_generate_routing_without_arbitrary_threshold(tmp_path: Path, monkeypatch):
    """Test 7: Verify CLI generate command routes to discrete event engine for arbitrary N unless --parallel is passed."""
    import argparse
    from fraudx_synthesizer.cli import cmd_generate

    mock_records = [
        {"transaction_id": "TX_001", "amount": 100.0, "is_fraud": 0, "card_id": "C_01"}
    ]
    captured = {}

    def mock_generate_batch(self, n_transactions, fraud_prevalence, time_span_days):
        captured["n"] = n_transactions
        captured["prevalence"] = fraud_prevalence
        return mock_records

    from fraudx_synthesizer.engine import SimulationEngine
    monkeypatch.setattr(SimulationEngine, "generate_batch", mock_generate_batch)

    out_csv = tmp_path / "large_run.csv"
    args = argparse.Namespace(
        command="generate",
        n=150000,
        cards=100,
        merchants=20,
        region="US",
        fraud_rate=0.01,
        days=30,
        seed=42,
        output=str(out_csv),
        parallel=False,
        include_disputes=False,
        adversary_mode="intent",
        export_institutional_views=True,
        calibration=None,
    )

    cmd_generate(args)

    assert captured["n"] == 150000
    assert out_csv.exists()
    assert (tmp_path / "large_run_auth_stream.csv").exists()
    assert (tmp_path / "large_run_gateway_telemetry.csv").exists()

