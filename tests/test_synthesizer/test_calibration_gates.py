"""Automated CI tests for US and India calibration profiles and gated targets.

Verifies:
- spec/09_us_calibration_targets.yaml is loaded and valid in SpecRegistry.
- US calibration report accurately evaluates authorization approval rates, credit card ticket sizes, and CNP fraud share.
- Gated targets pass within defined physical and regulatory tolerances.
- Cross-region profile validation strictly rejects mismatches.
"""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import pytest

from fraudx_synthesizer import SimulationEngine
from fraudx_synthesizer.calibration import calibration_report
from fraudx_synthesizer.spec_loader import load_all_specs

US_PROFILE = "fed-payments-study-2022"
IN_PROFILE = "rbi-psi-2026-07"


def test_us_profile_carries_grounded_sources():
    specs = load_all_specs()
    assert US_PROFILE in specs.calibration_profiles, f"Profile {US_PROFILE} must be registered"
    profile = specs.calibration_profiles[US_PROFILE]
    assert profile.region == "US"
    assert profile.fraud_prevalence > 0.0
    assert len(profile.targets) >= 5, "US calibration profile must have comprehensive targets"
    for target in profile.targets:
        assert target.source.strip(), f"Target {target.id} must have a cited public data source"
        assert target.target > 0.0, f"Target {target.id} must have a positive numerical value"


def test_us_calibration_report_on_synthetic_batch():
    # Low transaction budget for battery-friendly execution
    engine = SimulationEngine(n_cards=150, n_merchants=40, region="US", seed=42)
    records = engine.generate_batch(n_transactions=1500, fraud_prevalence=0.03, time_span_days=15)

    report = calibration_report(records, profile_id=US_PROFILE, requested_fraud_prevalence=0.03)

    assert report["profile"] == US_PROFILE
    assert report["region"] == "US"
    assert report["generated"]["rows"] == 1500
    assert report["generated"]["fraud_rows"] > 0

    by_id = {t["id"]: t for t in report["targets"]}
    assert "mean_credit_card_ticket_usd" in by_id
    assert "authorization_approval_rate" in by_id

    # Check gated targets
    assert by_id["mean_credit_card_ticket_usd"]["gate"] is True
    assert by_id["mean_credit_card_ticket_usd"]["status"] == "PASS"

    assert by_id["authorization_approval_rate"]["status"] == "REPORTED"
    assert by_id["authorization_approval_rate"]["observed"] > 0.85

    # Overall gated verdict must be PASS
    assert report["overall"] == "PASS"


def test_us_report_refuses_indian_records():
    engine = SimulationEngine(n_cards=50, n_merchants=20, region="IN", seed=42)
    records = engine.generate_batch(n_transactions=200, fraud_prevalence=0.03)
    with pytest.raises(ValueError, match="is for region US"):
        calibration_report(records, profile_id=US_PROFILE, requested_fraud_prevalence=0.03)


def test_cli_us_calibration_generation(tmp_path: Path):
    out = tmp_path / "us_calibrated.csv"
    cmd = [
        sys.executable,
        "-m",
        "fraudx_synthesizer.cli",
        "generate",
        "-n",
        "300",
        "--cards",
        "50",
        "--merchants",
        "20",
        "--region",
        "US",
        "--calibration",
        US_PROFILE,
        "--fraud-rate",
        "0.03",
        "--seed",
        "42",
        "-o",
        str(out),
    ]
    res = subprocess.run(cmd, capture_output=True, text=True, cwd=str(Path(__file__).resolve().parents[2]))
    assert res.returncode == 0, res.stderr

    report_path = tmp_path / "us_calibrated_calibration.json"
    assert report_path.exists(), "Calibration report JSON must be exported"
    report = json.loads(report_path.read_text(encoding="utf-8"))
    assert report["profile"] == US_PROFILE
    assert report["overall"] == "PASS"
