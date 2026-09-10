"""Autonomous agent models for cardholders, merchants, adversarial fraudsters, and banks.

Implements closed-loop behavioral dynamics:
1. CardholderProfile: 11 Global (Visa/MC) and 5 Indian (RBI/RuPay) card products,
   7 Fed DCPC cohorts, circadian NHPP arrivals, and authentic hard negatives.
2. AdaptiveFraudsterAgent: 10 grounded cybercrime playbooks (Global & India),
   including distributed additive BIN attacks, triangulation fraud, and silent baking.
3. BankDecisionEngine: Multi-tier authorization switch evaluating ISO 8583 syntax,
   RBI AFA/Card Controls, PSD2 SCA exemptions, STIP floor limits, and Visa VAAI scoring.
"""

from __future__ import annotations

import enum
import math
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Tuple

import numpy as np


class ISO8583Response(str, enum.Enum):
    APPROVED_00 = "00"
    DO_NOT_HONOR_05 = "05"
    PARTIAL_APPROVAL_10 = "10"
    INVALID_CARD_14 = "14"
    INSUFFICIENT_FUNDS_51 = "51"
    EXPIRED_CARD_54 = "54"
    NOT_PERMITTED_57 = "57"
    SUSPECTED_FRAUD_59 = "59"
    SECURITY_VIOLATION_63 = "63"
    ACTIVITY_COUNT_EXCEEDED_65 = "65"
    INVALID_CVV_82 = "82"


class FraudScenario(str, enum.Enum):
    ORGANIC_NORMAL = "ORGANIC_NORMAL"
    # Global Playbooks
    ADV_MICRO_AUTH_PROBE = "ADV_MICRO_AUTH_PROBE"
    ADV_ATO_SILENT_BAKING = "ADV_ATO_SILENT_BAKING"
    ADV_SLEEPER_BUST_OUT = "ADV_SLEEPER_BUST_OUT"
    ADV_APPLE_PAY_YELLOW_PATH = "ADV_APPLE_PAY_YELLOW_PATH"
    ADV_NOCTURNAL_BURST = "ADV_NOCTURNAL_BURST"
    ADV_DISTRIBUTED_BIN_ENUMERATION = "ADV_DISTRIBUTED_BIN_ENUMERATION"
    ADV_TRIANGULATION_FRAUD = "ADV_TRIANGULATION_FRAUD"
    ADV_COLLUSIVE_BUST_OUT_MID = "ADV_COLLUSIVE_BUST_OUT_MID"
    # India Playbooks
    IN_ADV_REVERSE_PROXY_VISHING = "IN_ADV_REVERSE_PROXY_VISHING"
    IN_ADV_APK_SMS_STEALER = "IN_ADV_APK_SMS_STEALER"
    IN_ADV_INTL_NON_3DS_BYPASS = "IN_ADV_INTL_NON_3DS_BYPASS"
    IN_ADV_RENT_PORTAL_CASHOUT = "IN_ADV_RENT_PORTAL_CASHOUT"
    IN_ADV_SIM_SWAP_ESIM_HIJACK = "IN_ADV_SIM_SWAP_ESIM_HIJACK"
    # Authentic Hard Negatives
    HARD_NEGATIVE_TRAVEL = "HARD_NEGATIVE_TRAVEL"
    HARD_NEGATIVE_RELOCATION = "HARD_NEGATIVE_RELOCATION"
    HARD_NEGATIVE_DHANTERAS_GOLD = "HARD_NEGATIVE_DHANTERAS_GOLD"
    HARD_NEGATIVE_EMERGENCY = "HARD_NEGATIVE_EMERGENCY"
    # Legacy aliases
    CARD_TESTING_BURST = "ADV_MICRO_AUTH_PROBE"
    VELOCITY_BLITZ = "ADV_MICRO_AUTH_PROBE"
    ACCOUNT_TAKEOVER = "ADV_ATO_SILENT_BAKING"
    SLEEPER_BUST_OUT = "ADV_SLEEPER_BUST_OUT"
    CNP_FULLZ_EXPLOIT = "ADV_ATO_SILENT_BAKING"
    COUNTERFEIT_CLONE = "ADV_APPLE_PAY_YELLOW_PATH"
    IMPOSSIBLE_TRAVEL = "HARD_NEGATIVE_TRAVEL"
    HARD_NEGATIVE = "HARD_NEGATIVE_TRAVEL"


class CardholderState(str, enum.Enum):
    HOMESTEAD = "HOMESTEAD"
    COMMUTING = "COMMUTING"
    SHOPPING_LOCAL = "SHOPPING_LOCAL"
    ACTIVE_SHOPPING_TRIP = "ACTIVE_SHOPPING_TRIP"
    RELOCATING = "RELOCATING"
    DOMESTIC_TRAVEL = "DOMESTIC_TRAVEL"
    INTL_TRAVEL = "INTL_TRAVEL"
    ALERTED = "ALERTED"
    FROZEN = "FROZEN"


class FraudsterState(str, enum.Enum):
    DUMP_INGESTION = "DUMP_INGESTION"
    MICRO_PROBING = "MICRO_PROBING"
    ATO_INFILTRATION = "ATO_INFILTRATION"
    SILENT_BAKING = "SILENT_BAKING"
    ACTIVE_CASHOUT = "ACTIVE_CASHOUT"
    AMOUNT_ADAPTATION = "AMOUNT_ADAPTATION"
    GATEWAY_HOP = "GATEWAY_HOP"
    VELOCITY_BACKOFF = "VELOCITY_BACKOFF"
    CARD_PURGE = "CARD_PURGE"
    BIN_ROTATION = "BIN_ROTATION"
    SUCCESS_HARVEST = "SUCCESS_HARVEST"


class ChannelType(str, enum.Enum):
    CP_POS_CHIP = "CP_POS_CHIP"
    CP_POS_CONTACTLESS = "CP_POS_CONTACTLESS"
    CP_POS_MAGSTRIPE = "CP_POS_MAGSTRIPE"
    CNP_WEB = "CNP_WEB"
    CNP_MOBILE = "CNP_MOBILE"
    CNP_API = "CNP_API"
    UPI_QR_CREDIT = "UPI_QR_CREDIT"


def sample_spliced_lognormal_gpd(
    rng: np.random.Generator,
    mu: float,
    sigma: float,
    u: float = 250.0,
    pi_u: float = 0.03,
) -> float:
    """Samples ticket spend from C^1 smoothly spliced LogNormal-GPD composite distribution."""
    z_u = (math.log(max(u, 1.0)) - mu) / max(sigma, 0.05)
    phi_z = (1.0 / math.sqrt(2.0 * math.pi)) * math.exp(-0.5 * z_u * z_u)
    f_ln_u = phi_z / (u * max(sigma, 0.05))

    beta = max(10.0, pi_u / max(f_ln_u, 1e-6))
    xi = max(0.05, min(0.40, (pi_u / (u * max(f_ln_u, 1e-6))) * (1.0 + (math.log(u) - mu) / (sigma ** 2)) - 1.0))

    draw = rng.uniform(0.0, 1.0)
    if draw <= (1.0 - pi_u):
        val = rng.lognormal(mean=mu, sigma=sigma)
        return float(np.clip(val, 1.50, u))
    else:
        uniform_tail = rng.uniform(0.0, 0.92)
        gpd_excess = (beta / xi) * (math.pow(1.0 - uniform_tail, -xi) - 1.0)
        return float(np.clip(u + gpd_excess, 1.50, u * 2.5))


@dataclass
class CardholderProfile:
    """Autonomous cardholder agent with BDI statechart, product limits, and regulatory controls.
    
    Fully grounded in canonical specifications (spec/01 - spec/05).
    """
    card_id: str
    home_lat: float
    home_lon: float
    work_lat: float
    work_lon: float
    is_commuter: bool
    credit_limit: float
    current_balance: float = 0.0
    spend_mean_log: float = 3.5
    spend_sigma_log: float = 0.65
    preferred_channels: List[str] = field(default_factory=lambda: ["CP_POS_CHIP", "CP_POS_CONTACTLESS", "CNP_WEB"])
    circadian_peak_hour: float = 14.0

    # Kinematics & Physical anchor tracking
    last_physical_lat: float = 0.0
    last_physical_lon: float = 0.0
    last_physical_time: float = -1.0

    # Behavioral state machine
    state: CardholderState = CardholderState.HOMESTEAD
    is_frozen: bool = False
    active_travel_until: float = -1.0
    travel_lat: float = 0.0
    travel_lon: float = 0.0
    unauthorized_alert_time: float = -1.0
    total_tx_count: int = 0
    consecutive_declines: int = 0

    # Shopping trip & Life-stage episode tracking
    active_trip_remaining_stops: int = 0
    active_trip_cluster_lat: float = 0.0
    active_trip_cluster_lon: float = 0.0
    relocation_until: float = -1.0

    # Institutional Banking Attributes
    product_id: str = "PROD_CLASSIC_REVOLVING"
    cohort_id: str = "C4_SUBURBAN_FAMILY"
    region: str = "US"
    currency: str = "USD"
    pan_masked: str = "414720******1234"
    domestic_cnp_enabled: bool = True
    international_enabled: bool = False
    contactless_enabled: bool = True
    consecutive_pinless_contactless_count: int = 0
    cumulative_pinless_contactless_amount: float = 0.0
    last_merchant_id: Optional[str] = None

    # Grounded Solvency & Billing Cycle Attributes
    posted_balance: float = 0.0
    pending_holds: float = 0.0
    overdraft_limit: float = 0.0
    active_holds: Dict[str, Tuple[float, float]] = field(default_factory=dict)
    billing_cycle_day: int = 15
    repayment_cohort: str = "TRANSACTOR"
    apr: float = 0.2199
    statement_balance: float = 0.0
    minimum_payment_due: float = 0.0
    payment_due_time: float = -1.0
    days_past_due: int = 0
    is_delinquent: bool = False

    # Grounded Spec Behavioral Elements
    dominant_mccs: List[int] = field(default_factory=list)
    channel_probabilities: Dict[str, float] = field(default_factory=dict)
    vigilance_weights: List[float] = field(default_factory=lambda: [0.35, 0.45, 0.12, 0.08])
    circadian_hourly_probs: np.ndarray = field(default_factory=lambda: np.ones(24) / 24.0)
    is_spliced_gpd: bool = False
    gpd_threshold_u: float = 250.0
    gpd_xi: float = 0.22
    gpd_beta: float = 95.0
    gpd_tail_prob: float = 0.03

    def __post_init__(self) -> None:
        if self.posted_balance == 0.0 and self.current_balance > 0.0:
            self.posted_balance = self.current_balance
        self.current_balance = self.posted_balance + self.pending_holds

    def get_theoretical_mean_spend(self) -> float:
        """Computes theoretical expected spend."""
        if not self.is_spliced_gpd:
            return math.exp(self.spend_mean_log + 0.5 * (self.spend_sigma_log ** 2))
        else:
            ln_mean = math.exp(self.spend_mean_log + 0.5 * (self.spend_sigma_log ** 2))
            gpd_mean = self.gpd_threshold_u + (self.gpd_beta / max(0.01, 1.0 - self.gpd_xi))
            return (1.0 - self.gpd_tail_prob) * ln_mean + self.gpd_tail_prob * gpd_mean

    def get_available_balance(self) -> float:
        """Computes real-time solvency balance based on instrument category."""
        if "DEBIT" in self.product_id:
            return max(0.0, (self.posted_balance + self.overdraft_limit) - self.pending_holds)
        elif any(k in self.product_id for k in ("PREPAID", "EBT", "HSA")):
            return max(0.0, self.posted_balance - self.pending_holds)
        elif "BNPL" in self.product_id:
            effective_limit = self.credit_limit * 1.15
            return max(0.0, effective_limit - (self.posted_balance + self.pending_holds))
        else:
            # Standard revolving credit
            return max(0.0, self.credit_limit - (self.posted_balance + self.pending_holds))

    def place_hold(self, tx_id: str, hold_amount: float, expire_time_sec: float) -> bool:
        """Places pre-authorization hold upon approval. ZERO effect on posted_balance."""
        self.pending_holds += hold_amount
        self.active_holds[tx_id] = (hold_amount, expire_time_sec)
        self.current_balance = self.posted_balance + self.pending_holds
        return True

    def release_hold(self, tx_id: str) -> float:
        """Releases hold upon decline, reversal, or expiry."""
        if tx_id in self.active_holds:
            hold_amt, _ = self.active_holds.pop(tx_id)
            self.pending_holds = max(0.0, self.pending_holds - hold_amt)
            self.current_balance = self.posted_balance + self.pending_holds
            return hold_amt
        return 0.0

    def settle_hold(self, tx_id: str, settled_amount: float) -> None:
        """Transitions pending hold into posted balance upon clearing presentment."""
        if tx_id in self.active_holds:
            hold_amt, _ = self.active_holds.pop(tx_id)
            self.pending_holds = max(0.0, self.pending_holds - hold_amt)
        self.posted_balance += settled_amount
        self.current_balance = self.posted_balance + self.pending_holds

    def prune_expired_holds(self, current_time_sec: float) -> List[str]:
        """Drops expired pre-auth holds that received no clearing presentment."""
        expired = [tx_id for tx_id, (_, exp_t) in self.active_holds.items() if current_time_sec >= exp_t]
        for tx_id in expired:
            self.release_hold(tx_id)
        return expired

    def close_billing_statement(self, current_time_sec: float) -> Tuple[float, float, float]:
        """Closes 30-day billing cycle, computes interest, and sets payment due date."""
        self.prune_expired_holds(current_time_sec)
        stmt_bal = self.posted_balance
        if stmt_bal > 0.0 and self.repayment_cohort == "REVOLVER":
            interest = round(stmt_bal * (self.apr / 365.0) * 30.0, 2)
            self.posted_balance += interest
            stmt_bal += interest

        if self.region == "IN":
            min_due = min(stmt_bal, max(500.0, round(0.05 * stmt_bal, 2)))
        else:
            min_due = min(stmt_bal, max(25.0, round(0.02 * stmt_bal, 2)))

        self.statement_balance = stmt_bal
        self.minimum_payment_due = min_due
        self.payment_due_time = current_time_sec + 25.0 * 86400.0  # Statutory 25-day grace period
        self.current_balance = self.posted_balance + self.pending_holds
        return stmt_bal, min_due, self.payment_due_time

    def execute_cohort_payment(self, sim_time: float, rng: np.random.Generator) -> float:
        """Executes repayment based on consumer financial cohort."""
        if self.posted_balance <= 0.0:
            return 0.0

        if self.repayment_cohort == "TRANSACTOR":
            payment = min(self.posted_balance, self.statement_balance)
            self.posted_balance = max(0.0, self.posted_balance - payment)
            self.days_past_due = 0
            self.is_delinquent = False

        elif self.repayment_cohort == "REVOLVER":
            if self.posted_balance <= self.minimum_payment_due:
                payment = self.posted_balance
            else:
                zeta = float(rng.beta(1.5, 4.5))
                discretionary = zeta * max(0.0, self.statement_balance - self.minimum_payment_due)
                payment = min(self.posted_balance, round(self.minimum_payment_due + discretionary, 2))
            self.posted_balance = max(0.0, self.posted_balance - payment)
            self.days_past_due = 0
            self.is_delinquent = False

        elif self.repayment_cohort == "DISTRESSED":
            if rng.random() < 0.50:
                self.days_past_due += 30
                self.is_delinquent = True
                late_fee = 750.0 if self.region == "IN" else 35.0
                self.posted_balance += late_fee
                payment = 0.0
                if self.days_past_due >= 60:
                    self.is_frozen = True
            else:
                payment = min(self.posted_balance, self.minimum_payment_due)
                self.posted_balance = max(0.0, self.posted_balance - payment)
        else:
            payment = min(self.posted_balance, self.statement_balance)
            self.posted_balance = max(0.0, self.posted_balance - payment)

        self.current_balance = self.posted_balance + self.pending_holds
        return payment

    def apply_payroll_deposit(self, deposit_amount: float) -> None:
        """Credits direct deposit payroll to checking deposit balance."""
        self.posted_balance += deposit_amount
        self.current_balance = self.posted_balance + self.pending_holds

    def apply_monthly_payment(self, payment_ratio: float = 0.90) -> None:
        """Simulates periodic credit balance settlement (backwards compatible)."""
        self.posted_balance = max(0.0, self.posted_balance * (1.0 - payment_ratio))
        self.current_balance = self.posted_balance + self.pending_holds

    def sample_spend_amount(self, rng: np.random.Generator) -> float:
        """Samples ticket amount according to cohort specification (LogNormal vs Spliced GPD)."""
        max_spend = self.credit_limit * 0.50 if self.credit_limit > 0 else 5000.0

        if not self.is_spliced_gpd:
            val = float(rng.lognormal(mean=self.spend_mean_log, sigma=self.spend_sigma_log))
        else:
            draw = float(rng.uniform(0.0, 1.0))
            if draw <= (1.0 - self.gpd_tail_prob):
                val = float(rng.lognormal(mean=self.spend_mean_log, sigma=self.spend_sigma_log))
                val = min(val, self.gpd_threshold_u)
            else:
                u_draw = float(rng.uniform(0.0, 0.95))
                xi = max(0.05, min(0.45, self.gpd_xi))
                gpd_excess = (self.gpd_beta / xi) * (math.pow(1.0 - u_draw, -xi) - 1.0)
                val = self.gpd_threshold_u + gpd_excess

        if self.currency == "INR":
            if self.spend_mean_log < 5.0:
                val *= 40.0
            return float(np.clip(val, 10.0, max_spend))
        else:
            return float(np.clip(val, 1.50, max_spend))

    def sample_preferred_mcc(self, rng: np.random.Generator) -> int:
        """Samples preferred MCC from cohort-specific distribution simplex."""
        if not self.dominant_mccs or rng.random() > 0.85:
            return int(rng.choice([5411, 5812, 5814, 5541, 5912, 5311, 5732, 5999]))
        return int(rng.choice(self.dominant_mccs))

    def sample_channel(self, rng: np.random.Generator) -> str:
        """Samples transaction channel using cohort channel distribution."""
        if not self.channel_probabilities:
            return "CP_POS_CHIP"
        channels = list(self.channel_probabilities.keys())
        weights = list(self.channel_probabilities.values())
        return str(rng.choice(channels, p=weights))

    def get_current_anchor_location(self, sim_time: float) -> Tuple[float, float, CardholderState]:
        """Calculates dynamic physical coordinates based on commute schedule, shopping trips, and travel state."""
        # 1. Travel State (Domestic or International)
        if self.active_travel_until > 0.0 and sim_time < self.active_travel_until:
            trav_state = CardholderState.INTL_TRAVEL if self.international_enabled else CardholderState.DOMESTIC_TRAVEL
            return self.travel_lat, self.travel_lon, trav_state

        if self.active_travel_until > 0.0 and sim_time >= self.active_travel_until:
            self.active_travel_until = -1.0
            self.state = CardholderState.HOMESTEAD

        # 2. Relocation Episode (72-hour moving window)
        if self.relocation_until > 0.0 and sim_time < self.relocation_until:
            return self.home_lat, self.home_lon, CardholderState.RELOCATING

        if self.relocation_until > 0.0 and sim_time >= self.relocation_until:
            self.relocation_until = -1.0
            self.state = CardholderState.HOMESTEAD

        # 3. Active Shopping Trip Chaining
        if self.active_trip_remaining_stops > 0:
            return self.active_trip_cluster_lat, self.active_trip_cluster_lon, CardholderState.ACTIVE_SHOPPING_TRIP

        # 4. Commuter / Homestead Dynamics
        day_of_week = int(sim_time // 86400) % 7
        if not self.is_commuter or day_of_week >= 5:
            return self.home_lat, self.home_lon, CardholderState.HOMESTEAD

        hour_of_day = ((sim_time % 86400.0) / 3600.0)

        # 07:30 - 09:00 Inbound Commute
        if 7.5 <= hour_of_day < 9.0:
            alpha = (hour_of_day - 7.5) / 1.5
            lat = (1.0 - alpha) * self.home_lat + alpha * self.work_lat
            lon = (1.0 - alpha) * self.home_lon + alpha * self.work_lon
            return lat, lon, CardholderState.COMMUTING

        # 09:00 - 17:00 Work Office
        elif 9.0 <= hour_of_day < 17.0:
            return self.work_lat, self.work_lon, CardholderState.SHOPPING_LOCAL

        # 17:00 - 18:30 Outbound Commute
        elif 17.0 <= hour_of_day < 18.5:
            alpha = (hour_of_day - 17.0) / 1.5
            lat = (1.0 - alpha) * self.work_lat + alpha * self.home_lat
            lon = (1.0 - alpha) * self.work_lon + alpha * self.home_lon
            return lat, lon, CardholderState.COMMUTING

        # 18:30 - 07:30 Homestead / Residential
        else:
            return self.home_lat, self.home_lon, CardholderState.HOMESTEAD

    def initiate_shopping_trip(self, cluster_lat: float, cluster_lon: float, num_stops: int) -> None:
        """Transitions cardholder into an active multi-stop shopping trip anchored to a commercial hub."""
        self.state = CardholderState.ACTIVE_SHOPPING_TRIP
        self.active_trip_remaining_stops = max(1, num_stops)
        self.active_trip_cluster_lat = cluster_lat
        self.active_trip_cluster_lon = cluster_lon

    def advance_shopping_trip(self) -> bool:
        """Advances shopping trip by one stop. Returns True if stops remain, False if trip concluded."""
        self.active_trip_remaining_stops -= 1
        if self.active_trip_remaining_stops <= 0:
            self.state = CardholderState.HOMESTEAD
            self.active_trip_remaining_stops = 0
            return False
        return True

    def initiate_relocation_episode(self, sim_time_sec: float, duration_sec: float = 259200.0) -> None:
        """Initiates 72-hour persistent home relocation episode."""
        self.state = CardholderState.RELOCATING
        self.relocation_until = sim_time_sec + duration_sec

    def initiate_travel(
        self,
        sim_time: float,
        duration_days: float,
        dest_lat: float,
        dest_lon: float,
        is_international: bool = False,
    ) -> None:
        """Transitions cardholder into multi-day domestic or international travel state."""
        self.active_travel_until = sim_time + duration_days * 86400.0
        self.travel_lat = dest_lat
        self.travel_lon = dest_lon
        self.state = CardholderState.INTL_TRAVEL if is_international else CardholderState.DOMESTIC_TRAVEL

    def trigger_unauthorized_alert(self, sim_time: float, rng: np.random.Generator) -> None:
        """Schedules cardholder fraud discovery based on calibrated vigilance survival distributions."""
        if self.is_frozen or self.unauthorized_alert_time >= 0.0:
            return

        tier_choice = rng.choice([1, 2, 3, 4], p=self.vigilance_weights)
        if tier_choice == 1:
            delay_sec = float(rng.lognormal(mean=5.2, sigma=0.85))
        elif tier_choice == 2:
            scale_sec = 36.0 * 3600.0
            delay_sec = float(scale_sec * ((-math.log(max(1e-6, rng.uniform(0.0, 1.0)))) ** (1.0 / 1.8)))
        elif tier_choice == 3:
            delay_sec = float(rng.uniform(3.0 * 86400.0, 45.0 * 86400.0))
        else:
            delay_sec = float(1e9)

        self.unauthorized_alert_time = sim_time + delay_sec
        self.state = CardholderState.ALERTED

    def check_freeze_status(self, sim_time: float) -> bool:
        """Checks whether notification delay elapsed and card should be permanently frozen."""
        if self.is_frozen:
            return True
        if self.unauthorized_alert_time >= 0.0 and sim_time >= self.unauthorized_alert_time:
            self.is_frozen = True
            self.state = CardholderState.FROZEN
            return True
        return False


@dataclass
class TargetCardAdversaryState:
    """Per-target adversary memory tracking discovered state and campaign lifecycle."""
    card_id: str
    fsm_state: FraudsterState = FraudsterState.DUMP_INGESTION
    current_probe_amount: float = 450.0
    consecutive_declines: int = 0
    last_response_code: Optional[ISO8583Response] = None
    target_mcc: int = 5732
    active_merchant_tier: str = "TIER_A"
    cooldown_until_sec: float = 0.0
    playbook_step: int = 0
    is_compromised: bool = True
    is_burned: bool = False
    is_dormant_until: float = 0.0
    discovered_limits: Dict[str, float] = field(default_factory=dict)


class AdaptiveFraudsterAgent:
    """Stateful adversarial agent executing closed-loop adaptive cybercrime playbooks with per-target memory."""

    def __init__(self, rng: np.random.Generator):
        self.rng = rng
        self.target_states: Dict[str, TargetCardAdversaryState] = {}
        # Global fallback trackers
        self.state = FraudsterState.DUMP_INGESTION
        self.current_amount = 450.0
        self.attack_interval_sec = 2.0
        self.consecutive_declines = 0
        self.active_merchant_tier = "TIER_A"
        self.cooldown_until_sec = 0.0

    def get_or_create_target(self, card: CardholderProfile) -> TargetCardAdversaryState:
        if card.card_id not in self.target_states:
            initial_amt = (
                float(self.rng.uniform(250.0, 650.0))
                if card.currency == "USD"
                else float(self.rng.uniform(20000.0, 50000.0))
            )
            self.target_states[card.card_id] = TargetCardAdversaryState(
                card_id=card.card_id,
                fsm_state=FraudsterState.DUMP_INGESTION,
                current_probe_amount=initial_amt,
                target_mcc=5732,
            )
        return self.target_states[card.card_id]

    def select_attack_playbook(
        self,
        card: CardholderProfile,
        sim_time_seconds: float,
        world_center_lat: float,
        world_center_lon: float,
        scenario_override: Optional[Any] = None,
    ) -> Dict[str, Any]:
        """Generates attack transaction parameters guided by per-target memory and stateful adaptation."""
        target = self.get_or_create_target(card)

        if scenario_override is not None:
            chosen_scenario = scenario_override
        else:
            if target.fsm_state == FraudsterState.MICRO_PROBING:
                chosen_scenario = FraudScenario.ADV_MICRO_AUTH_PROBE.value
            elif target.fsm_state == FraudsterState.ACTIVE_CASHOUT:
                chosen_scenario = FraudScenario.ADV_ATO_SILENT_BAKING.value
            elif target.fsm_state == FraudsterState.GATEWAY_HOP:
                chosen_scenario = FraudScenario.ADV_MICRO_AUTH_PROBE.value
            else:
                if card.region == "IN":
                    playbook_choices = [
                        FraudScenario.IN_ADV_REVERSE_PROXY_VISHING.value,
                        FraudScenario.IN_ADV_APK_SMS_STEALER.value,
                        FraudScenario.IN_ADV_INTL_NON_3DS_BYPASS.value,
                        FraudScenario.IN_ADV_RENT_PORTAL_CASHOUT.value,
                        FraudScenario.ADV_NOCTURNAL_BURST.value,
                    ]
                    playbook_weights = [0.30, 0.25, 0.20, 0.15, 0.10]
                else:
                    playbook_choices = [
                        FraudScenario.ADV_MICRO_AUTH_PROBE.value,
                        FraudScenario.ADV_ATO_SILENT_BAKING.value,
                        FraudScenario.ADV_SLEEPER_BUST_OUT.value,
                        FraudScenario.ADV_APPLE_PAY_YELLOW_PATH.value,
                        FraudScenario.ADV_NOCTURNAL_BURST.value,
                        FraudScenario.ADV_DISTRIBUTED_BIN_ENUMERATION.value,
                        FraudScenario.ADV_TRIANGULATION_FRAUD.value,
                    ]
                    playbook_weights = [0.20, 0.20, 0.15, 0.15, 0.10, 0.10, 0.10]
                chosen_scenario = str(self.rng.choice(playbook_choices, p=playbook_weights))

        scenario_val = chosen_scenario.value if hasattr(chosen_scenario, "value") else str(chosen_scenario)

        # 1. Micro-Auth Probe (Global)
        if scenario_val in (FraudScenario.ADV_MICRO_AUTH_PROBE.value, "VELOCITY_BLITZ", "CARD_TESTING_BURST"):
            target.fsm_state = FraudsterState.MICRO_PROBING
            amount = round(float(self.rng.uniform(0.50, 1.99)), 2)
            target.current_probe_amount = amount
            target.target_mcc = 8398
            return {
                "amount": amount,
                "channel_type": "CNP_WEB",
                "is_fraud": 1,
                "scenario_tag": FraudScenario.ADV_MICRO_AUTH_PROBE.value,
                "ip_distance_km": float(self.rng.uniform(250.0, 1500.0)),
                "preferred_mcc": 8398,
                "is_cross_border": False,
                "avs_code": "Z",
                "asn_type": "residential",
            }

        # 2. Account Takeover Silent Baking (Global)
        elif scenario_val in (FraudScenario.ADV_ATO_SILENT_BAKING.value, "ACCOUNT_TAKEOVER", "CNP_FULLZ_EXPLOIT"):
            if target.fsm_state == FraudsterState.AMOUNT_ADAPTATION:
                amount = round(target.current_probe_amount, 2)
            else:
                if card.currency == "INR":
                    low_b = min(card.credit_limit * 0.3, 30000.0)
                    high_b = max(low_b + 500.0, min(card.credit_limit * 0.85, 250000.0))
                else:
                    low_b = min(card.credit_limit * 0.35, 1500.0)
                    high_b = max(low_b + 25.0, min(card.credit_limit * 0.85, 8000.0))
                amount = round(float(self.rng.uniform(low_b, high_b)), 2)
                target.current_probe_amount = amount
            target.target_mcc = 5732
            return {
                "amount": amount,
                "channel_type": "CNP_WEB",
                "is_fraud": 1,
                "scenario_tag": FraudScenario.ADV_ATO_SILENT_BAKING.value,
                "ip_distance_km": float(self.rng.uniform(10.0, 25.0)),
                "preferred_mcc": 5732,
                "is_cross_border": False,
                "asn_type": "residential",
            }

        # 3. Sleeper Bust-Out (Global & India)
        elif scenario_val in (FraudScenario.ADV_SLEEPER_BUST_OUT.value, "SLEEPER_BUST_OUT"):
            remaining = max(100.0, card.credit_limit - card.current_balance)
            is_collusive_terminal = bool(self.rng.random() < 0.40)
            threshold = 2000000.0 if card.currency == "INR" else 25000.0
            if is_collusive_terminal or remaining <= threshold:
                amount = round(float(self.rng.uniform(0.90, 0.98) * remaining), 2)
            else:
                if card.currency == "INR":
                    split_target = min(remaining * 0.95, float(self.rng.uniform(1000000.0, 2000000.0)))
                else:
                    split_target = min(remaining * 0.95, float(self.rng.uniform(12000.0, 24500.0)))
                amount = round(split_target, 2)
            target.current_probe_amount = amount
            target.target_mcc = 5094
            return {
                "amount": amount,
                "channel_type": "CNP_WEB",
                "is_fraud": 1,
                "scenario_tag": FraudScenario.ADV_SLEEPER_BUST_OUT.value,
                "preferred_mcc": 5094,
                "is_cross_border": False,
                "asn_type": "residential",
            }

        # 4. Apple Pay Yellow Path (Global)
        elif scenario_val in (FraudScenario.ADV_APPLE_PAY_YELLOW_PATH.value, "COUNTERFEIT_CLONE"):
            amount = round(float(self.rng.uniform(500.0, 2500.0)), 2)
            target.current_probe_amount = amount
            target.target_mcc = 5732
            return {
                "amount": amount,
                "channel_type": "CP_POS_CONTACTLESS",
                "is_fraud": 1,
                "scenario_tag": FraudScenario.ADV_APPLE_PAY_YELLOW_PATH.value,
                "preferred_mcc": 5732,
                "is_cross_border": False,
                "override_lat": card.home_lat + float(self.rng.uniform(-0.05, 0.05)),
                "override_lon": card.home_lon + float(self.rng.uniform(-0.05, 0.05)),
                "asn_type": "residential",
            }

        # 5. Nocturnal Carding Burst (Global & India)
        elif scenario_val == FraudScenario.ADV_NOCTURNAL_BURST.value:
            amount = round(float(self.rng.uniform(150.0, 650.0)), 2)
            target.current_probe_amount = amount
            target.target_mcc = 5311
            return {
                "amount": amount,
                "channel_type": "CNP_WEB",
                "is_fraud": 1,
                "scenario_tag": FraudScenario.ADV_NOCTURNAL_BURST.value,
                "preferred_mcc": 5311,
                "is_cross_border": True,
                "asn_type": "datacenter",
            }

        # 6. Distributed BIN Enumeration (PEA Additive Probing)
        elif scenario_val == FraudScenario.ADV_DISTRIBUTED_BIN_ENUMERATION.value:
            amount = round(float(self.rng.uniform(1.00, 3.50)), 2)
            target.current_probe_amount = amount
            target.target_mcc = 8398
            return {
                "amount": amount,
                "channel_type": "CNP_WEB",
                "is_fraud": 1,
                "scenario_tag": FraudScenario.ADV_DISTRIBUTED_BIN_ENUMERATION.value,
                "preferred_mcc": 8398,
                "is_cross_border": False,
                "asn_type": "residential",
                "vaai_score": int(self.rng.integers(70, 95)),
            }

        # 7. Triangulation Fraud
        elif scenario_val == FraudScenario.ADV_TRIANGULATION_FRAUD.value:
            amount = round(float(self.rng.uniform(250.0, 650.0)), 2)
            target.current_probe_amount = amount
            target.target_mcc = 5732
            return {
                "amount": amount,
                "channel_type": "CNP_WEB",
                "is_fraud": 1,
                "scenario_tag": FraudScenario.ADV_TRIANGULATION_FRAUD.value,
                "preferred_mcc": 5732,
                "is_cross_border": False,
                "asn_type": "residential",
            }

        # 8. India: Reverse-Proxy Vishing & Digital Arrest
        elif scenario_val == FraudScenario.IN_ADV_REVERSE_PROXY_VISHING.value:
            amount = round(float(self.rng.uniform(50000.0, 350000.0)), 2)
            target.current_probe_amount = amount
            target.target_mcc = 6051
            return {
                "amount": amount,
                "channel_type": "CNP_WEB",
                "is_fraud": 1,
                "scenario_tag": FraudScenario.IN_ADV_REVERSE_PROXY_VISHING.value,
                "preferred_mcc": 6051,
                "is_cross_border": False,
                "otp_submitted": True,
                "asn_type": "residential",
            }

        # 9. India: Malicious APK SMS Stealer
        elif scenario_val == FraudScenario.IN_ADV_APK_SMS_STEALER.value:
            amount = round(float(self.rng.uniform(25000.0, 150000.0)), 2)
            target.current_probe_amount = amount
            target.target_mcc = 6513
            return {
                "amount": amount,
                "channel_type": "CNP_MOBILE",
                "is_fraud": 1,
                "scenario_tag": FraudScenario.IN_ADV_APK_SMS_STEALER.value,
                "preferred_mcc": 6513,
                "is_cross_border": False,
                "otp_submitted": True,
                "asn_type": "mobile",
            }

        # 10. India: International Non-3DS Bypass
        elif scenario_val == FraudScenario.IN_ADV_INTL_NON_3DS_BYPASS.value:
            amount_usd = round(float(self.rng.uniform(200.0, 1200.0)), 2)
            amount_inr = round(amount_usd * 83.5, 2)
            target.current_probe_amount = amount_inr
            target.target_mcc = 5732
            return {
                "amount": amount_inr,
                "channel_type": "CNP_WEB",
                "is_fraud": 1,
                "scenario_tag": FraudScenario.IN_ADV_INTL_NON_3DS_BYPASS.value,
                "preferred_mcc": 5732,
                "is_cross_border": True,
                "eci": "07",
                "asn_type": "datacenter",
            }

        # 11. India: Rent Portal Liquidation
        elif scenario_val == FraudScenario.IN_ADV_RENT_PORTAL_CASHOUT.value:
            remaining = max(10000.0, card.credit_limit - card.current_balance)
            amount = round(float(self.rng.uniform(0.70, 0.95) * remaining), 2)
            target.current_probe_amount = amount
            target.target_mcc = 6513
            return {
                "amount": amount,
                "channel_type": "CNP_WEB",
                "is_fraud": 1,
                "scenario_tag": FraudScenario.IN_ADV_RENT_PORTAL_CASHOUT.value,
                "preferred_mcc": 6513,
                "is_cross_border": False,
                "otp_submitted": True,
                "asn_type": "residential",
            }

        # Fallback
        target.current_probe_amount = 250.0
        return {
            "amount": 250.0,
            "channel_type": "CNP_WEB",
            "is_fraud": 1,
            "scenario_tag": scenario_val,
        }

    def receive_feedback(
        self,
        response_code: ISO8583Response,
        trans_status_3ds: Optional[str],
        sim_time_seconds: float,
        card_id: Optional[str] = None,
    ) -> None:
        """Adapts adversarial policy with per-target memory and stateful closed-loop updates."""
        target = self.target_states.get(card_id) if card_id else None

        if response_code in (ISO8583Response.APPROVED_00, ISO8583Response.PARTIAL_APPROVAL_10):
            self.consecutive_declines = 0
            if target:
                target.consecutive_declines = 0
                target.last_response_code = response_code
                if target.fsm_state == FraudsterState.MICRO_PROBING:
                    target.fsm_state = FraudsterState.ACTIVE_CASHOUT
                    target.current_probe_amount = float(self.rng.uniform(450.0, 1600.0))
                else:
                    target.fsm_state = FraudsterState.SUCCESS_HARVEST
            if self.state == FraudsterState.MICRO_PROBING:
                self.state = FraudsterState.ACTIVE_CASHOUT
                self.current_amount = float(self.rng.uniform(450.0, 1600.0))
            else:
                self.state = FraudsterState.SUCCESS_HARVEST
                self.current_amount = max(50.0, self.current_amount * 0.85)

        elif response_code == ISO8583Response.INSUFFICIENT_FUNDS_51:
            if target:
                target.consecutive_declines += 1
                target.fsm_state = FraudsterState.AMOUNT_ADAPTATION
                target.last_response_code = response_code
                target.current_probe_amount = max(25.0, round(target.current_probe_amount * 0.70, 2))
                target.cooldown_until_sec = sim_time_seconds + 30.0
            self.consecutive_declines += 1
            self.state = FraudsterState.AMOUNT_ADAPTATION
            self.current_amount = max(25.0, round(self.current_amount * 0.70, 2))

        elif trans_status_3ds == "C":
            if target:
                target.fsm_state = FraudsterState.GATEWAY_HOP
                target.last_response_code = response_code
                target.target_mcc = 5815
                target.current_probe_amount = min(target.current_probe_amount, 28.0)
            self.state = FraudsterState.GATEWAY_HOP
            self.active_merchant_tier = "TIER_C"

        elif response_code in (ISO8583Response.SUSPECTED_FRAUD_59, ISO8583Response.DO_NOT_HONOR_05):
            self.consecutive_declines += 1
            self.attack_interval_sec *= 2.5
            self.cooldown_until_sec = sim_time_seconds + self.attack_interval_sec
            self.state = FraudsterState.VELOCITY_BACKOFF
            if target:
                target.consecutive_declines += 1
                target.last_response_code = response_code
                if target.consecutive_declines >= 2:
                    target.is_burned = True
                    target.fsm_state = FraudsterState.CARD_PURGE
                else:
                    target.fsm_state = FraudsterState.VELOCITY_BACKOFF
                    target.cooldown_until_sec = sim_time_seconds + 300.0

        elif response_code in (ISO8583Response.INVALID_CARD_14, ISO8583Response.EXPIRED_CARD_54):
            self.state = FraudsterState.CARD_PURGE
            if target:
                target.is_burned = True
                target.fsm_state = FraudsterState.CARD_PURGE

    def inject_attack(
        self,
        scenario: Any,
        card: CardholderProfile,
        sim_time_seconds: float,
        world_center_lat: float,
        world_center_lon: float,
    ) -> Dict[str, Any]:
        """Backward-compatible inject_attack interface."""
        scen_str = scenario.value if hasattr(scenario, "value") else str(scenario)
        return self.select_attack_playbook(
            card=card,
            sim_time_seconds=sim_time_seconds,
            world_center_lat=world_center_lat,
            world_center_lon=world_center_lon,
            scenario_override=scen_str,
        )


FraudsterAgent = AdaptiveFraudsterAgent


class BankDecisionEngine:
    """Multi-tier issuer authorization switch implementing real-world ISO 8583 and regulatory rails."""

    def __init__(
        self,
        tau_decline: float = 0.85,
        tau_challenge: float = 0.45,
        max_speed_kmh: float = 900.0,
        max_hourly_velocity: int = 6,
    ):
        self.tau_decline = tau_decline
        self.tau_challenge = tau_challenge
        self.max_speed_kmh = max_speed_kmh
        self.max_hourly_velocity = max_hourly_velocity

    def evaluate_authorization(
        self,
        card: CardholderProfile,
        amount: float,
        channel: str,
        sim_time: float,
        velocity_kph: float,
        count_1h: int,
        cvv_valid: bool = True,
        is_card_format_valid: bool = True,
        is_expired: bool = False,
        ml_risk_score: float = 0.05,
        mcc: int = 5411,
        is_cross_border: bool = False,
        otp_provided: bool = True,
        vaai_score: int = 20,
    ) -> Tuple[ISO8583Response, Optional[str], Optional[float]]:
        """Evaluates authorization request and returns (ISO_Field_39, 3DS_trans_status, approved_amount)."""
        # 1. Syntax & Card Lifecycle Invariants
        if not is_card_format_valid:
            return ISO8583Response.INVALID_CARD_14, None, 0.0
        if is_expired:
            return ISO8583Response.EXPIRED_CARD_54, None, 0.0
        if card.is_frozen:
            return ISO8583Response.SUSPECTED_FRAUD_59, None, 0.0

        # 2. Network Attack Intelligence (Visa VAAI decline threshold 75)
        if vaai_score >= 75:
            return ISO8583Response.SUSPECTED_FRAUD_59, None, 0.0

        # 3. Indian Regulatory Rails (RBI Mandates)
        if card.region == "IN":
            if channel.startswith("CNP") and not is_cross_border and not card.domestic_cnp_enabled:
                return ISO8583Response.NOT_PERMITTED_57, None, 0.0
            if is_cross_border and not card.international_enabled:
                return ISO8583Response.NOT_PERMITTED_57, None, 0.0

            if channel.startswith("CNP") and not is_cross_border and not otp_provided:
                return ISO8583Response.SECURITY_VIOLATION_63, "N", 0.0

            if channel == "CP_POS_CONTACTLESS":
                if amount > 5000.0:
                    return ISO8583Response.DO_NOT_HONOR_05, "FORCE_CHIP_PIN", 0.0
                if card.consecutive_pinless_contactless_count >= 5 or (
                    card.cumulative_pinless_contactless_amount + amount > 15000.0
                ):
                    return ISO8583Response.DO_NOT_HONOR_05, "FORCE_CHIP_PIN", 0.0

        # 4. Security & Cryptographic Validation
        if not cvv_valid:
            return ISO8583Response.INVALID_CVV_82, None, 0.0

        # 5. Kinematic Speed Veto
        if channel.startswith("CP") and velocity_kph > self.max_speed_kmh:
            return ISO8583Response.SUSPECTED_FRAUD_59, None, 0.0

        # 6. Velocity Counter Veto
        if count_1h > self.max_hourly_velocity:
            return ISO8583Response.ACTIVITY_COUNT_EXCEEDED_65, None, 0.0

        # 7. Solvency & Credit Limit Check (evaluated on pre-auth available balance)
        available = card.get_available_balance()
        if amount > available:
            min_afd_avail = 500.0 if card.region == "IN" else 10.0
            if mcc == 5542 and available >= min_afd_avail:
                return ISO8583Response.PARTIAL_APPROVAL_10, "Y", available
            return ISO8583Response.INSUFFICIENT_FUNDS_51, None, 0.0

        # 8. Machine Learning Risk Thresholds & 3DS Challenges
        if ml_risk_score >= self.tau_decline:
            return ISO8583Response.SUSPECTED_FRAUD_59, None, 0.0

        if self.tau_challenge <= ml_risk_score < self.tau_decline:
            if channel.startswith("CNP"):
                return ISO8583Response.DO_NOT_HONOR_05, "C", 0.0
            else:
                return ISO8583Response.DO_NOT_HONOR_05, "N", 0.0

        # Successful Approval
        return ISO8583Response.APPROVED_00, "Y", amount
