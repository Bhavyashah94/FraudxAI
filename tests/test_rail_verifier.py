"""Automated tests for Phase 3: Decoupled Rail Verifier Switch & Double-Entry World Ledger.

Validates:
1. Double-entry multi-party balance conservation (sum(Debits) == sum(Credits) to machine precision 1e-5).
2. Pre-auth hold lifecycle: hold placement, clearing settlement, hold release/expiry.
3. RBI contactless regulations (₹5,000 PIN-free ceiling, 5 consecutive PINless transaction cap).
4. Solvency invariants: zero balance mutation on insufficient funds / declines.
5. Kinematic space-time supersonic velocity veto (velocity > 900 km/h -> ISO 59).
6. 3DS 2.x exemption engine: Low-Value Exemption, TRA, and Step-Up Challenge flows.
7. EMV Contact Chip cryptographic primacy.
8. End-to-end integration through DiscreteEventEngine.
"""

from __future__ import annotations

import math
import pytest
import numpy as np

from fraudx_synthesizer.agents import CardholderProfile, CardholderState, ISO8583Response
from fraudx_synthesizer.engine import DiscreteEventEngine
from fraudx_synthesizer.ledger import DoubleEntryWorldLedger, StreamingLedger
from fraudx_synthesizer.rails import (
    CandidateTransactionIntent,
    RailVerificationResult,
    RailVerifierSwitch,
)


def create_test_card(
    card_id: str = "CARD_TEST_001",
    region: str = "US",
    credit_limit: float = 10000.0,
    current_balance: float = 1000.0,
) -> CardholderProfile:
    """Helper to instantiate a valid CardholderProfile for testing."""
    currency = "INR" if region == "IN" else "USD"
    lat = 40.7128 if region == "US" else 19.0760
    lon = -74.0060 if region == "US" else 72.8777
    return CardholderProfile(
        card_id=card_id,
        home_lat=lat,
        home_lon=lon,
        work_lat=lat + 0.05,
        work_lon=lon + 0.05,
        is_commuter=True,
        credit_limit=credit_limit,
        current_balance=current_balance,
        pan_masked="4000123456789010",
        product_id=f"{region}_PROD_STANDARD",
        cohort_id="C1_URBAN_TECH_PROFESSIONAL",
        region=region,
        currency=currency,
        spend_mean_log=3.8,
        spend_sigma_log=0.7,
        domestic_cnp_enabled=True,
        international_enabled=True,
    )


def test_double_entry_balance_conservation():
    """Verify bitwise multi-party balance conservation across hold, clearing, and release."""
    ledger = DoubleEntryWorldLedger()
    card_id = "CARD_DE_001"
    merchant_id = "MERCHANT_M001"

    # 1. Place pre-auth hold of $250.00
    ledger.place_pre_auth_hold(
        tx_id="TX_001",
        card_id=card_id,
        hold_amount=250.0,
        sim_time_sec=100.0,
    )

    # 2. Settle hold at clearing presentment ($245.00 actual, e.g. adjusted tip or fuel)
    m_net, interchange, net_fee = ledger.settle_hold(
        tx_id="TX_001",
        card_id=card_id,
        merchant_id=merchant_id,
        settled_amount=245.0,
        sim_time_sec=200.0,
    )
    assert math.isclose(m_net + interchange + net_fee, 245.0, abs_tol=1e-5)

    # 3. Place pre-auth hold of $150.00 and release upon reversal/expiry
    ledger.place_pre_auth_hold(
        tx_id="TX_002",
        card_id=card_id,
        hold_amount=150.0,
        sim_time_sec=300.0,
    )
    released_amt = ledger.release_hold(
        tx_id="TX_002",
        card_id=card_id,
        sim_time_sec=400.0,
    )
    assert released_amt == 150.0

    # 4. Global balance conservation assertion
    is_conserved, discrepancy = ledger.verify_global_balance_conservation()
    assert is_conserved, f"Double-entry balance conservation violated! Discrepancy: {discrepancy}"
    assert discrepancy < 1e-5


def test_rbi_contactless_regulations():
    """Verify RBI ₹5,000 PIN-free ceiling and 5 consecutive PINless transaction cap."""
    switch = RailVerifierSwitch(region="IN", seed=42)
    card = create_test_card(region="IN", credit_limit=100000.0, current_balance=5000.0)

    # Case A: Contactless spend > ₹5,000 without PIN must decline (ISO 65)
    intent_over_cap = CandidateTransactionIntent(
        tx_id="TX_NFC_001",
        card_id=card.card_id,
        sim_time_sec=100.0,
        amount=5500.0,
        currency="INR",
        channel_type="CP_POS_CONTACTLESS",
        merchant_id="M_NFC_001",
        mcc=5411,
        merchant_lat=card.home_lat,
        merchant_lon=card.home_lon,
        pin_entered=False,
    )
    res = switch.verify_intent(intent_over_cap, card)
    assert not res.approved
    assert res.iso_response_code == "65"
    assert "5000" in res.decline_reason or res.regulatory_rule_triggered == "RBI_NFC_PIN_MANDATE"

    # Case B: Contactless spend > ₹5,000 WITH PIN entered approves
    intent_over_cap_pin = CandidateTransactionIntent(
        tx_id="TX_NFC_002",
        card_id=card.card_id,
        sim_time_sec=105.0,
        amount=5500.0,
        currency="INR",
        channel_type="CP_POS_CONTACTLESS",
        merchant_id="M_NFC_001",
        mcc=5411,
        merchant_lat=card.home_lat,
        merchant_lon=card.home_lon,
        pin_entered=True,
    )
    res_pin = switch.verify_intent(intent_over_cap_pin, card)
    assert res_pin.approved
    assert res_pin.iso_response_code == "00"

    # Case C: 5 consecutive PINless transactions approved, 6th transaction blocked
    card.consecutive_pinless_contactless_count = 5
    intent_consecutive = CandidateTransactionIntent(
        tx_id="TX_NFC_003",
        card_id=card.card_id,
        sim_time_sec=110.0,
        amount=1500.0,
        currency="INR",
        channel_type="CP_POS_CONTACTLESS",
        merchant_id="M_NFC_001",
        mcc=5411,
        merchant_lat=card.home_lat,
        merchant_lon=card.home_lon,
        pin_entered=False,
    )
    res_consec = switch.verify_intent(intent_consecutive, card)
    assert not res_consec.approved
    assert res_consec.iso_response_code == "65"
    assert "CONSECUTIVE" in res_consec.decline_reason or res_consec.regulatory_rule_triggered == "RBI_NFC_VELOCITY_CAP"


def test_solvency_and_declines_zero_balance_mutation():
    """Verify that insufficient funds trigger ISO 51 and produce zero balance mutation."""
    switch = RailVerifierSwitch(region="US", seed=42)
    card = create_test_card(credit_limit=5000.0, current_balance=4800.0)
    avail_before = card.get_available_balance()
    assert avail_before == 200.0

    # Attempt to spend $350.00 (exceeds available balance)
    intent = CandidateTransactionIntent(
        tx_id="TX_SOLV_001",
        card_id=card.card_id,
        sim_time_sec=100.0,
        amount=350.0,
        currency="USD",
        channel_type="CNP_WEB",
        merchant_id="M_SOLV_001",
        mcc=5311,
        merchant_lat=card.home_lat,
        merchant_lon=card.home_lon,
        cvv_provided=True,
    )
    res = switch.verify_intent(intent, card)
    assert not res.approved
    assert res.iso_response_code == ISO8583Response.INSUFFICIENT_FUNDS_51.value

    # Balance and active holds must undergo ZERO mutation
    assert card.get_available_balance() == avail_before
    assert card.current_balance == 4800.0
    assert len(card.active_holds) == 0


def test_kinematic_supersonic_veto():
    """Verify that physical transactions with velocity > 900 km/h trigger ISO 59."""
    switch = RailVerifierSwitch(region="US", seed=42)
    card = create_test_card()

    intent = CandidateTransactionIntent(
        tx_id="TX_KIN_001",
        card_id=card.card_id,
        sim_time_sec=100.0,
        amount=120.0,
        currency="USD",
        channel_type="CP_POS_CHIP",
        merchant_id="M_KIN_001",
        mcc=5411,
        merchant_lat=card.home_lat,
        merchant_lon=card.home_lon,
        haversine_velocity_kph=1450.0,  # Supersonic travel velocity
    )
    res = switch.verify_intent(intent, card)
    assert not res.approved
    assert res.iso_response_code == ISO8583Response.SUSPECTED_FRAUD_59.value
    assert "SUPERSONIC" in res.decline_reason


def test_three_ds_frictionless_and_challenge_flows():
    """Verify 3DS 2.x Low-Value Exemption, TRA, and Step-Up Challenge mechanics."""
    switch = RailVerifierSwitch(region="US", seed=42)
    card = create_test_card()

    # Low-Value Exemption (< $30): Frictionless Authenticated (TransStatus 'Y', ECI '05')
    intent_lve = CandidateTransactionIntent(
        tx_id="TX_3DS_001",
        card_id=card.card_id,
        sim_time_sec=100.0,
        amount=18.50,
        currency="USD",
        channel_type="CNP_WEB",
        merchant_id="M_3DS_001",
        mcc=5815,
        merchant_lat=card.home_lat,
        merchant_lon=card.home_lon,
        cvv_provided=True,
    )
    res_lve = switch.verify_intent(intent_lve, card)
    assert res_lve.approved
    assert res_lve.iso_response_code == "00"
    assert res_lve.trans_status_3ds == "Y"
    assert res_lve.eci == "05"

    # High Risk with OTP Bypass / Failure: Step-up challenge failed -> ISO 63
    intent_challenge_fail = CandidateTransactionIntent(
        tx_id="TX_3DS_002",
        card_id=card.card_id,
        sim_time_sec=200.0,
        amount=450.0,
        currency="USD",
        channel_type="CNP_WEB",
        merchant_id="M_3DS_002",
        mcc=5732,
        merchant_lat=card.home_lat,
        merchant_lon=card.home_lon,
        risk_score=0.65,
        otp_submitted=False,
        cvv_provided=True,
    )
    res_fail = switch.verify_intent(intent_challenge_fail, card)
    assert not res_fail.approved
    assert res_fail.iso_response_code == ISO8583Response.SECURITY_VIOLATION_63.value

    # High Risk with Successful OTP Submission: Step-up challenge passed (TransStatus 'C', ECI '05')
    intent_challenge_pass = CandidateTransactionIntent(
        tx_id="TX_3DS_003",
        card_id=card.card_id,
        sim_time_sec=300.0,
        amount=450.0,
        currency="USD",
        channel_type="CNP_WEB",
        merchant_id="M_3DS_002",
        mcc=5732,
        merchant_lat=card.home_lat,
        merchant_lon=card.home_lon,
        risk_score=0.65,
        otp_submitted=True,
        cvv_provided=True,
    )
    res_pass = switch.verify_intent(intent_challenge_pass, card)
    assert res_pass.approved
    assert res_pass.iso_response_code == "00"
    assert res_pass.trans_status_3ds == "C"
    assert res_pass.eci == "05"


def test_emv_chip_primacy():
    """Verify that authentic EMV chip + PIN transactions have counterfeit dispute primacy."""
    switch = RailVerifierSwitch(region="US", seed=42)
    card = create_test_card()

    # Legitimate cardholder physical chip transaction with elevated anomaly score
    intent_chip = CandidateTransactionIntent(
        tx_id="TX_CHIP_001",
        card_id=card.card_id,
        sim_time_sec=100.0,
        amount=1200.0,
        currency="USD",
        channel_type="CP_POS_CHIP",
        merchant_id="M_CHIP_001",
        mcc=5944,  # Jewelry
        merchant_lat=card.home_lat,
        merchant_lon=card.home_lon,
        risk_score=0.92,
        is_fraud=0,  # Legitimate purchase
    )
    res_chip = switch.verify_intent(intent_chip, card)
    assert res_chip.approved
    assert res_chip.iso_response_code == ISO8583Response.APPROVED_00.value
    assert res_chip.pos_entry_mode == "051"


def test_end_to_end_engine_rails_and_ledger():
    """Verify that DiscreteEventEngine processes transactions through RailVerifierSwitch and DoubleEntryWorldLedger."""
    engine = DiscreteEventEngine(n_cards=50, n_merchants=20, region="US", seed=101)
    batch = engine.generate_batch(n_transactions=300, fraud_prevalence=0.05)

    assert len(batch) == 300
    for rec in batch:
        assert "response_code" in rec
        assert "auth_code" in rec
        assert "pos_entry_mode" in rec
        assert "pos_condition_code" in rec
        assert "settled_amount" in rec
        assert rec["response_code"] in [e.value for e in ISO8583Response]

    # Global double-entry balance conservation across the simulation batch
    is_conserved, discrepancy = engine.double_entry_ledger.verify_global_balance_conservation()
    assert is_conserved, f"Double-entry balance conservation violated across batch! Discrepancy: {discrepancy}"
    assert discrepancy < 1e-5
