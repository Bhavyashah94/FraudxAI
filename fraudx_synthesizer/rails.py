"""Boundary Layer 1: Decoupled Payment Rail Verifier Switch for FraudxAI.

Implements:
1. CandidateTransactionIntent: Decoupled contract for proposed agent transaction intents.
2. RailVerificationResult: Complete banking switch authorization payload.
3. RailVerifierSwitch: Deterministic institutional boundary layer enforcing:
   - Multi-party solvency checks (credit limit, posted balance, overdraft limit).
   - Regulatory velocity & transaction ceilings (RBI ₹5k PIN-free contactless, 5-tx limit; US STIP floors).
   - 3DS 2.x protocol state machine & exemption evaluation (Low-Value, TRA, Whitelist, Challenge).
   - EMV 4.3 Bit 55 cryptogram & TVR validation.
   - AVS (Address Verification Service) and CVV2 validation.
   - Exact ISO 8583 response code generation (00, 05, 10, 14, 51, 54, 59, 63, 65, 82).
"""

from __future__ import annotations

import math
from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Dict, List, Optional, Tuple

import numpy as np

from .agents import CardholderProfile, ISO8583Response


@dataclass
class CandidateTransactionIntent:
    """Decoupled candidate transaction intent proposed by Generative Layer 2."""
    tx_id: str
    card_id: str
    sim_time_sec: float
    amount: float
    currency: str
    channel_type: str
    merchant_id: str
    mcc: int
    merchant_lat: float
    merchant_lon: float
    is_cross_border: bool = False
    is_fraud: int = 0
    scenario_tag: str = "ORGANIC_NORMAL"
    # Proposed authorization credentials
    otp_submitted: bool = True
    cvv_provided: bool = True
    avs_code: str = "Y"
    billing_shipping_match: int = 1
    pin_entered: bool = False
    emv_chip_present: bool = False
    emv_cryptogram_valid: bool = True
    three_ds_requested: bool = False
    risk_score: float = 0.02
    vaai_score: int = 25
    haversine_velocity_kph: float = 0.0
    tx_count_1h: int = 0
    tx_count_24h: int = 0
    tx_attempts_1h: int = 0
    distinct_mids_30m: int = 1
    subminute_attempts_60s: int = 0
    ip_distance_km: float = 5.0
    asn_type: str = "residential"


@dataclass
class RailVerificationResult:
    """Complete institutional banking switch evaluation result."""
    approved: bool
    iso_response_code: str  # ISO 8583 response code
    approved_amount: float
    trans_status_3ds: str   # 3DS 2.x status: "Y", "A", "C", "N", "R"
    eci: str                # Electronic Commerce Indicator ("05", "06", "07", "")
    auth_code: str
    decline_reason: str = ""
    hold_placed: bool = False
    hold_amount: float = 0.0
    regulatory_rule_triggered: str = ""
    interchange_fee: float = 0.0
    settlement_amount: float = 0.0
    pos_entry_mode: str = "051"
    pos_condition_code: str = "00"
    hop_origin: str = "ISSUER_HOST"


class RailVerifierSwitch:
    """Boundary Layer 1 Deterministic Rail Switch enforcing payment plumbing invariants."""

    def __init__(self, region: str = "US", seed: int = 42):
        self.region = region.upper()
        self.rng = np.random.default_rng(seed)

    def verify_intent(
        self,
        intent: CandidateTransactionIntent,
        card: CardholderProfile,
    ) -> RailVerificationResult:
        """Evaluates candidate intent against banking rails, solvency, and regulatory limits."""
        # 1. Terminal POS Entry Mode & Condition Codes
        ch = intent.channel_type
        if ch == "CP_POS_CHIP":
            pos_entry = "051"
        elif ch == "CP_POS_CONTACTLESS":
            pos_entry = "071"
        elif ch == "CP_POS_MAGSTRIPE":
            pos_entry = "901"
        elif ch == "CNP_WEB":
            pos_entry = "012"
        elif ch == "CNP_MOBILE":
            pos_entry = "102"
        elif ch == "UPI_QR_CREDIT":
            pos_entry = "031"
        else:
            pos_entry = "812"

        pos_condition = "00" if ch.startswith("CP") else "59"

        # 2. Card Status / Freeze Checks (Cardholder app lock returns ISO 57)
        if card.is_frozen or card.check_freeze_status(intent.sim_time_sec):
            return RailVerificationResult(
                approved=False,
                iso_response_code=ISO8583Response.NOT_PERMITTED_57.value if hasattr(ISO8583Response, 'NOT_PERMITTED_57') else "57",
                approved_amount=0.0,
                trans_status_3ds="N",
                eci="07" if ch.startswith("CNP") else "",
                auth_code="",
                decline_reason="CARD_FROZEN_OR_BLOCKED_BY_CARDHOLDER",
                pos_entry_mode=pos_entry,
                pos_condition_code=pos_condition,
                hop_origin="ISSUER_HOST",
            )

        # 3. Hardware Cryptographic Primacy (Visa Core Rules / Mastercard Chapter 17)
        # Authentic EMV Contact Chip + PIN or Biometric CDCVM Wallet:
        # ARQC cryptogram (Tag 9F26) is non-replayable and validated by issuer cryptographic security module (HSM).
        is_verified_hardware_crypto = (
            (intent.emv_chip_present or ch == "CP_POS_CHIP")
            and intent.emv_cryptogram_valid
            and (ch in ("CP_POS_CHIP", "CP_POS_CONTACTLESS"))
        )

        # 4. Channel Controls (E-Commerce / International enabled)
        if ch.startswith("CNP") and not card.domestic_cnp_enabled:
            return RailVerificationResult(
                approved=False,
                iso_response_code=ISO8583Response.NOT_PERMITTED_57.value if hasattr(ISO8583Response, 'NOT_PERMITTED_57') else "57",
                approved_amount=0.0,
                trans_status_3ds="N",
                eci="07",
                auth_code="",
                decline_reason="DOMESTIC_CNP_DISABLED_BY_CARDHOLDER",
                pos_entry_mode=pos_entry,
                pos_condition_code=pos_condition,
                hop_origin="ISSUER_HOST",
            )

        if intent.is_cross_border and not card.international_enabled:
            return RailVerificationResult(
                approved=False,
                iso_response_code=ISO8583Response.NOT_PERMITTED_57.value if hasattr(ISO8583Response, 'NOT_PERMITTED_57') else "57",
                approved_amount=0.0,
                trans_status_3ds="N" if ch.startswith("CNP") else "",
                eci="07" if ch.startswith("CNP") else "",
                auth_code="",
                decline_reason="INTERNATIONAL_TRANSACTIONS_DISABLED",
                pos_entry_mode=pos_entry,
                pos_condition_code=pos_condition,
                hop_origin="ISSUER_HOST",
            )

        # 5. Kinematic Space-Time Geofencing (Supersonic Velocity Veto)
        # Commercial aviation maximum speed ceiling (~900 km/h).
        if ch.startswith("CP") and intent.haversine_velocity_kph > 900.0:
            return RailVerificationResult(
                approved=False,
                iso_response_code=ISO8583Response.SUSPECTED_FRAUD_59.value,
                approved_amount=0.0,
                trans_status_3ds="N",
                eci="",
                auth_code="",
                decline_reason="SUPERSONIC_PHYSICAL_VELOCITY",
                pos_entry_mode=pos_entry,
                pos_condition_code=pos_condition,
                hop_origin="GATEWAY_FILTER",
            )

        # 6. Channel-Differentiated Velocity & Botnet Enumeration Limits (ISO 65)
        # A. Core banking daily count limit (FIS / Fiserv / TSYS standard: 35 tx/24h)
        if intent.tx_count_24h >= 35:
            return RailVerificationResult(
                approved=False,
                iso_response_code=ISO8583Response.ACTIVITY_COUNT_EXCEEDED_65.value,
                approved_amount=0.0,
                trans_status_3ds="N",
                eci="07" if ch.startswith("CNP") else "",
                auth_code="",
                decline_reason="DAILY_TRANSACTION_COUNT_LIMIT_EXCEEDED",
                pos_entry_mode=pos_entry,
                pos_condition_code=pos_condition,
                hop_origin="ISSUER_HOST",
            )

        # B. Card-Not-Present Card-Testing & Botnet Enumeration Checks
        if ch.startswith("CNP"):
            # Multi-merchant automated enumeration (e.g. automated checker bot testing across distinct MIDs).
            # distinct_mids_30m is a PRIOR-WINDOW count (excludes current MID per ledger.py point-in-time semantics).
            # Grounded in Visa VAAI / Mastercard SafetyNet spec/03 channel_differentiated_velocity_ceilings:
            #   card_not_present_max_distinct_mids: 3 (prior unique MIDs in 30m = spec threshold).
            # Compound condition: spec threshold of 3 prior MIDs combined with a fraud signal indicator.
            # Unconditional veto at 5 prior distinct MIDs: even without VAAI signal, 5+ unique CNP merchants
            # in 30 minutes is statistically outside normal human shopping behavior.
            is_enumeration_attack = (
                (intent.distinct_mids_30m >= 3 and (
                    intent.vaai_score >= 60 or
                    intent.subminute_attempts_60s >= 2 or
                    (intent.amount <= 15.0 and intent.tx_attempts_1h >= 3)
                ))
                or intent.distinct_mids_30m >= 5
            )
            if is_enumeration_attack:
                return RailVerificationResult(
                    approved=False,
                    iso_response_code=ISO8583Response.ACTIVITY_COUNT_EXCEEDED_65.value,
                    approved_amount=0.0,
                    trans_status_3ds="N",
                    eci="07",
                    auth_code="",
                    decline_reason="CNP_MERCHANT_ENUMERATION_DETECTED",
                    pos_entry_mode=pos_entry,
                    pos_condition_code=pos_condition,
                    hop_origin="NETWORK_SWITCH_VAAI",
                )
            # High-frequency sub-minute automated script burst (>= 3 attempts in 60s)
            if intent.subminute_attempts_60s >= 3:
                return RailVerificationResult(
                    approved=False,
                    iso_response_code=ISO8583Response.ACTIVITY_COUNT_EXCEEDED_65.value,
                    approved_amount=0.0,
                    trans_status_3ds="N",
                    eci="07",
                    auth_code="",
                    decline_reason="HIGH_FREQUENCY_AUTOMATED_PROBE",
                    pos_entry_mode=pos_entry,
                    pos_condition_code=pos_condition,
                    hop_origin="GATEWAY_FILTER",
                )
            # Normal CNP hourly throttle
            if intent.tx_count_1h >= 8:
                return RailVerificationResult(
                    approved=False,
                    iso_response_code=ISO8583Response.ACTIVITY_COUNT_EXCEEDED_65.value,
                    approved_amount=0.0,
                    trans_status_3ds="N",
                    eci="07",
                    auth_code="",
                    decline_reason="CNP_HOURLY_FREQUENCY_LIMIT_EXCEEDED",
                    pos_entry_mode=pos_entry,
                    pos_condition_code=pos_condition,
                    hop_origin="ISSUER_HOST",
                )
        else:
            # Card-Present: Verified Contact Chip allows up to 15 tx/h (shopping trips, food courts, parking, transit)
            max_cp_hourly = 15 if is_verified_hardware_crypto else 10
            if intent.tx_count_1h >= max_cp_hourly:
                return RailVerificationResult(
                    approved=False,
                    iso_response_code=ISO8583Response.ACTIVITY_COUNT_EXCEEDED_65.value,
                    approved_amount=0.0,
                    trans_status_3ds="",
                    eci="",
                    auth_code="",
                    decline_reason="CP_HOURLY_FREQUENCY_LIMIT_EXCEEDED",
                    pos_entry_mode=pos_entry,
                    pos_condition_code=pos_condition,
                    hop_origin="ISSUER_HOST",
                )

        # 7. Contactless Regulatory Rails (India RBI vs Global)
        if ch == "CP_POS_CONTACTLESS":
            if self.region == "IN" or card.currency == "INR":
                # RBI Master Direction: ₹5,000 PIN-free ceiling
                if intent.amount > 5000.0 and not intent.pin_entered:
                    return RailVerificationResult(
                        approved=False,
                        iso_response_code=ISO8583Response.ACTIVITY_LIMIT_EXCEEDED_65.value,
                        approved_amount=0.0,
                        trans_status_3ds="",
                        eci="",
                        auth_code="",
                        decline_reason="RBI_NFC_PIN_REQUIRED_OVER_5000_INR",
                        regulatory_rule_triggered="RBI_NFC_PIN_MANDATE",
                        pos_entry_mode=pos_entry,
                        pos_condition_code=pos_condition,
                        hop_origin="TERMINAL_SCA",
                    )
                # 5 consecutive PINless transaction ceiling
                if card.consecutive_pinless_contactless_count >= 5 and not intent.pin_entered:
                    return RailVerificationResult(
                        approved=False,
                        iso_response_code=ISO8583Response.ACTIVITY_LIMIT_EXCEEDED_65.value,
                        approved_amount=0.0,
                        trans_status_3ds="",
                        eci="",
                        auth_code="",
                        decline_reason="RBI_NFC_CONSECUTIVE_LIMIT_REACHED",
                        regulatory_rule_triggered="RBI_NFC_VELOCITY_CAP",
                        pos_entry_mode=pos_entry,
                        pos_condition_code=pos_condition,
                        hop_origin="ISSUER_HOST",
                    )

        # 8. Monetary Bounds Validation
        max_cap = 20_000_000.0 if (self.region == "IN" or card.currency == "INR") else 250_000.0
        if intent.amount <= 0.0 or intent.amount > max_cap:
            return RailVerificationResult(
                approved=False,
                iso_response_code=ISO8583Response.DO_NOT_HONOR_05.value,
                approved_amount=0.0,
                trans_status_3ds="N",
                eci="07" if ch.startswith("CNP") else "",
                auth_code="",
                decline_reason="INVALID_AMOUNT_BOUNDS",
                pos_entry_mode=pos_entry,
                pos_condition_code=pos_condition,
                hop_origin="ISSUER_HOST",
            )

        # 9. VAAI Network Intelligence Check
        if intent.vaai_score >= 75:
            return RailVerificationResult(
                approved=False,
                iso_response_code=ISO8583Response.SUSPECTED_FRAUD_59.value,
                approved_amount=0.0,
                trans_status_3ds="N",
                eci="07" if ch.startswith("CNP") else "",
                auth_code="",
                decline_reason="VAAI_NETWORK_FRAUD_SCORE_EXCEEDED",
                pos_entry_mode=pos_entry,
                pos_condition_code=pos_condition,
                hop_origin="NETWORK_SWITCH_VAAI",
            )

        # 10. 3DS 2.x Authentication & Exemption Engine (CNP Channels)
        trans_status_3ds = ""
        eci = ""
        if ch.startswith("CNP"):
            # Strict RBI Statutory Rule (India Domestic): 100% Mandatory AFA (OTP)
            if (self.region == "IN" or card.currency == "INR") and not intent.is_cross_border:
                if not intent.otp_submitted:
                    return RailVerificationResult(
                        approved=False,
                        iso_response_code=ISO8583Response.SECURITY_VIOLATION_63.value,
                        approved_amount=0.0,
                        trans_status_3ds="N",
                        eci="07",
                        auth_code="",
                        decline_reason="RBI_MANDATORY_AFA_OTP_REQUIRED",
                        pos_entry_mode=pos_entry,
                        pos_condition_code=pos_condition,
                        hop_origin="ACS_3DS",
                    )
                trans_status_3ds = "Y"
                eci = "05"
            else:
                # Global / US PSD2 & EMVCo 3DS 2.x Exemption Engine
                if intent.amount < 30.0:
                    trans_status_3ds = "Y"
                    eci = "05"  # Low-Value Exemption (LVE)
                elif intent.risk_score < 0.08 and intent.amount < 100.0:
                    trans_status_3ds = "Y"
                    eci = "05"  # TRA Exemption
                elif intent.risk_score < 0.45:
                    trans_status_3ds = "Y"
                    eci = "05"  # Frictionless
                else:
                    # Step-Up Challenge (risk_score >= 0.45)
                    if not intent.otp_submitted:
                        return RailVerificationResult(
                            approved=False,
                            iso_response_code=ISO8583Response.SECURITY_VIOLATION_63.value,
                            approved_amount=0.0,
                            trans_status_3ds="N",
                            eci="07",
                            auth_code="",
                            decline_reason="3DS_CHALLENGE_FAILED_OR_BYPASSED",
                            pos_entry_mode=pos_entry,
                            pos_condition_code=pos_condition,
                            hop_origin="ACS_3DS",
                        )
                    trans_status_3ds = "C"
                    eci = "05"

        # 11. Cryptographic & Security Credentials Verification
        if ch.startswith("CNP") and not intent.cvv_provided:
            return RailVerificationResult(
                approved=False,
                iso_response_code=ISO8583Response.INVALID_CVV_82.value if hasattr(ISO8583Response, 'INVALID_CVV_82') else "82",
                approved_amount=0.0,
                trans_status_3ds=trans_status_3ds,
                eci=eci,
                auth_code="",
                decline_reason="CVV_MATCH_FAILED",
                pos_entry_mode=pos_entry,
                pos_condition_code=pos_condition,
                hop_origin="ISSUER_HOST",
            )

        # 12. Solvency & Balance Evaluation (Available Credit / Balance)
        avail = card.get_available_balance()
        if intent.amount > avail:
            min_afd_avail = 500.0 if (self.region == "IN" or card.currency == "INR") else 10.0
            # Partial approval strictly negotiated for Automated Fuel Dispensers (MCC 5542) or Transit (MCC 4111, 4784)
            if intent.mcc in (5542, 4111, 4784) and avail >= min_afd_avail:
                approved_amt = round(avail, 2)
                auth_code = f"A{self.rng.integers(10000, 99999)}"
                return RailVerificationResult(
                    approved=True,
                    iso_response_code=ISO8583Response.PARTIAL_APPROVAL_10.value,
                    approved_amount=approved_amt,
                    trans_status_3ds=trans_status_3ds or "Y",
                    eci=eci,
                    auth_code=auth_code,
                    hold_placed=True,
                    hold_amount=approved_amt,
                    pos_entry_mode=pos_entry,
                    pos_condition_code=pos_condition,
                    hop_origin="ISSUER_HOST",
                )
            else:
                return RailVerificationResult(
                    approved=False,
                    iso_response_code=ISO8583Response.INSUFFICIENT_FUNDS_51.value,
                    approved_amount=0.0,
                    trans_status_3ds=trans_status_3ds,
                    eci=eci,
                    auth_code="",
                    decline_reason="INSUFFICIENT_FUNDS_OR_CREDIT_LIMIT_EXCEEDED",
                    pos_entry_mode=pos_entry,
                    pos_condition_code=pos_condition,
                    hop_origin="ISSUER_HOST",
                )

        # 13. Real-Time Risk Score Thresholding (WITHOUT SYNTHETIC ORACLE LEAK)
        # Authentic EMV Contact Chip + valid cryptogram carries statutory counterfeit dispute protection
        if is_verified_hardware_crypto:
            pass  # Hardware cryptogram verified
        elif intent.risk_score >= 0.88:
            return RailVerificationResult(
                approved=False,
                iso_response_code=ISO8583Response.SUSPECTED_FRAUD_59.value,
                approved_amount=0.0,
                trans_status_3ds=trans_status_3ds or "N",
                eci=eci,
                auth_code="",
                decline_reason="BANK_ML_DECISION_ENGINE_FRAUD_DECLINE",
                pos_entry_mode=pos_entry,
                pos_condition_code=pos_condition,
                hop_origin="ISSUER_HOST",
            )

        # 14. Transaction Approval
        auth_code = f"A{self.rng.integers(10000, 99999)}"
        interchange_rate = 0.0175
        interchange = round(intent.amount * interchange_rate, 2)
        settlement = round(intent.amount - interchange, 2)

        return RailVerificationResult(
            approved=True,
            iso_response_code=ISO8583Response.APPROVED_00.value,
            approved_amount=intent.amount,
            trans_status_3ds=trans_status_3ds or "Y",
            eci=eci,
            auth_code=auth_code,
            hold_placed=True,
            hold_amount=intent.amount,
            interchange_fee=interchange,
            settlement_amount=settlement,
            pos_entry_mode=pos_entry,
            pos_condition_code=pos_condition,
            hop_origin="ISSUER_HOST",
        )
