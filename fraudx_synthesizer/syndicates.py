"""Adversarial Syndicate Graph Topologies & Persistent Infrastructure Entities.

Models real-world cybercrime underground infrastructure:
- Multi-threat syndicate ecology: IABs, Card Checkers, ATO crews, Synthetic Bust-outs, Reship/Gift drain, and FinCEN mule pipelines.
- Multi-ASN residential, mobile, and datacenter proxy pools with authentic ISP allocations (Comcast, AT&T, Charter, Jio, Airtel).
- FoxIO JA4 TLS signatures and passive p0f TCP stack telemetry for cross-layer anomaly modeling.
- 3-tier FinCEN/FATF money mule layering DAGs: Tier 1 Smurfing -> Tier 2 Aggregator LLCs -> Tier 3 Crypto Off-Ramp.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Dict, List, Optional, Tuple
import numpy as np


class MuleTier(str, Enum):
    TIER_1_SMURF = "TIER_1_SMURF"
    TIER_2_AGGREGATOR = "TIER_2_AGGREGATOR"
    TIER_3_OFFRAMP = "TIER_3_OFFRAMP"


@dataclass
class BotnetCluster:
    """Represents a distributed botnet or residential proxy pool executing coordinated attacks."""
    cluster_id: str
    name: str
    subnet_prefix: str
    asn: str
    isp: str
    proxy_type: str  # "RESIDENTIAL_STICKY", "MOBILE_4G_5G", "DATACENTER_ROTATING"
    ja4_signature: str
    tcp_os_profile: str  # "Windows_11", "Linux_Container", "macOS_Darwin", "Android_Linux"
    device_fingerprints: List[str]
    ip_pool: List[str]

    def sample_ip_and_device(self, rng: np.random.Generator) -> Tuple[str, str, Dict[str, Any]]:
        """Draws an IP, device fingerprint, and network telemetry from the cluster pool."""
        ip = str(rng.choice(self.ip_pool))
        device = str(rng.choice(self.device_fingerprints))
        telemetry = {
            "asn": self.asn,
            "isp": self.isp,
            "proxy_type": self.proxy_type,
            "ja4_signature": self.ja4_signature,
            "tcp_os_profile": self.tcp_os_profile,
        }
        return ip, device, telemetry


@dataclass
class MuleRing:
    """Represents a coordinated money-mule laundering network receiving fraudulent proceeds."""
    ring_id: str
    tier: MuleTier
    account_type: str  # "PERSONAL_CHECKING", "COMMERCIAL_SHELL_LLC", "P2P_CRYPTO_ESCROW"
    liquidation_channel: str
    beneficiary_accounts: List[str]
    bank_routing: str
    fee_cut_ratio: float = 0.10
    layering_hop_latency_seconds: float = 300.0
    is_frozen: bool = False

    def sample_beneficiary(self, rng: np.random.Generator) -> str:
        """Draws a target mule beneficiary account."""
        return str(rng.choice(self.beneficiary_accounts))


@dataclass
class SyndicateEntity:
    """A persistent cybercrime syndicate operating specialized campaigns across accounts."""
    syndicate_id: str
    name: str
    archetype: str
    primary_playbooks: List[str]
    target_mccs: List[int] = field(default_factory=list)
    credential_tiers: List[str] = field(default_factory=list)
    botnets: List[BotnetCluster] = field(default_factory=list)
    mule_rings: List[MuleRing] = field(default_factory=list)

    def sample_telemetry(self, rng: np.random.Generator) -> Dict[str, Any]:
        """Samples persistent technical markers and mule destination for an attack event."""
        res: Dict[str, Any] = {
            "syndicate_id": self.syndicate_id,
            "syndicate_name": self.name,
            "syndicate_archetype": self.archetype,
            "botnet_cluster_id": "",
            "ip_subnet_prefix": "",
            "client_ip": "",
            "device_fingerprint_id": "",
            "asn": "",
            "isp": "",
            "ja4_signature": "",
            "mule_ring_id": "",
            "mule_tier": "",
            "beneficiary_account_id": "",
            "liquidation_channel": "",
        }

        if self.botnets:
            botnet = rng.choice(self.botnets)
            ip, dev, net_tel = botnet.sample_ip_and_device(rng)
            res["botnet_cluster_id"] = botnet.cluster_id
            res["ip_subnet_prefix"] = botnet.subnet_prefix
            res["client_ip"] = ip
            res["device_fingerprint_id"] = dev
            res["asn"] = net_tel["asn"]
            res["isp"] = net_tel["isp"]
            res["ja4_signature"] = net_tel["ja4_signature"]

        if self.mule_rings:
            ring = rng.choice(self.mule_rings)
            res["mule_ring_id"] = ring.ring_id
            res["mule_tier"] = ring.tier.value
            res["beneficiary_account_id"] = ring.sample_beneficiary(rng)
            res["liquidation_channel"] = ring.liquidation_channel

        return res


class SyndicateRegistry:
    """Initializes and manages persistent cybercrime syndicates for the simulation environment."""

    def __init__(self, region: str = "US", seed: int = 42):
        self.region = region.upper()
        self.rng = np.random.default_rng(seed)
        self.syndicates: List[SyndicateEntity] = []
        self._syndicate_by_id: Dict[str, SyndicateEntity] = {}
        self._playbook_to_syndicates: Dict[str, List[SyndicateEntity]] = {}
        self._initialize_syndicates()

    def _initialize_syndicates(self) -> None:
        """Instantiates grounded cybercrime organizations with realistic technical assets."""
        if self.region == "IN":
            self._init_india_syndicates()
        else:
            self._init_us_syndicates()

        for syn in self.syndicates:
            self._syndicate_by_id[syn.syndicate_id] = syn
            for pb in syn.primary_playbooks:
                if pb not in self._playbook_to_syndicates:
                    self._playbook_to_syndicates[pb] = []
                self._playbook_to_syndicates[pb].append(syn)

    def _init_us_syndicates(self) -> None:
        """Configures 6 empirical US cybercrime threat actors grounded in DOJ/FinCEN reports."""
        # Common Mule Infrastructure: Tier 1 Smurf & Tier 2 Aggregator
        ato_mule_t1 = MuleRing(
            ring_id="MULE_US_SMURF_CHASE_01",
            tier=MuleTier.TIER_1_SMURF,
            account_type="PERSONAL_CHECKING",
            liquidation_channel="INSTANT_P2P_SMURF",
            beneficiary_accounts=[f"MULE_CHASE_{i:05d}" for i in range(100, 115)],
            bank_routing="021000021",
            fee_cut_ratio=0.10,
            layering_hop_latency_seconds=300.0,
        )
        ato_mule_t2 = MuleRing(
            ring_id="MULE_US_AGGREGATOR_LLC_02",
            tier=MuleTier.TIER_2_AGGREGATOR,
            account_type="COMMERCIAL_SHELL_LLC",
            liquidation_channel="SAME_DAY_ACH_CONSOLIDATION",
            beneficiary_accounts=[f"MULE_BOA_CORP_{i:05d}" for i in range(200, 208)],
            bank_routing="026009593",
            fee_cut_ratio=0.15,
            layering_hop_latency_seconds=1200.0,
        )

        # 1. SYN_US_CARDING_BOT: Automated micro-auth card testing botnet
        checker_botnet = BotnetCluster(
            cluster_id="BOTNET_US_CHECKER_01",
            name="OpenBullet High-Throughput Checker Pool",
            subnet_prefix="198.54.130.0/24",
            asn="AS16509",
            isp="Amazon AWS",
            proxy_type="DATACENTER_ROTATING",
            ja4_signature="t13d1516h2_8daaf6152771_e562703ab853",
            tcp_os_profile="Linux_Container",
            device_fingerprints=[f"DEV_CHECKER_BOT_{i:03d}" for i in range(25)],
            ip_pool=[f"198.54.130.{i}" for i in range(10, 100)],
        )
        syn_carding = SyndicateEntity(
            syndicate_id="SYN_US_CARDING_BOT",
            name="Automated Micro-Auth Probing Syndicate",
            archetype="CARD_CHECKER_BOTNET",
            primary_playbooks=[
                "ADV_MICRO_AUTH_PROBE",
                "ADV_DISTRIBUTED_BIN_ENUMERATION",
                "ADV_NOCTURNAL_BURST",
                "INTENT_OMEGA_PROBE",
            ],
            target_mccs=[8398, 4899, 5815],
            credential_tiers=["TIER_TRACK_2_DUMP", "TIER_CNP_FULLZ"],
            botnets=[checker_botnet],
            mule_rings=[ato_mule_t1],  # Connects card checking hits to smurf ingress
        )

        # 2. SYN_US_ATO_SYNDICATE: Account Takeover & Session Hijacking Syndicate
        ato_botnet_comcast = BotnetCluster(
            cluster_id="BOTNET_US_RES_COMCAST_02",
            name="Comcast Xfinity Residential SOCKS5 Pool",
            subnet_prefix="73.162.10.0/24",
            asn="AS7922",
            isp="Comcast Cable Communications",
            proxy_type="RESIDENTIAL_STICKY",
            ja4_signature="t13d1516h2_dfa4a7752771_c212703ab899",
            tcp_os_profile="Windows_11",
            device_fingerprints=[f"DEV_RES_CHROME_WIN_{i:03d}" for i in range(20)],
            ip_pool=[f"73.162.10.{i}" for i in range(10, 60)],
        )
        ato_botnet_att = BotnetCluster(
            cluster_id="BOTNET_US_RES_ATT_03",
            name="AT&T Fiber Residential SOCKS5 Pool",
            subnet_prefix="108.204.45.0/24",
            asn="AS7018",
            isp="AT&T Services",
            proxy_type="RESIDENTIAL_STICKY",
            ja4_signature="t13d1516h2_dfa4a7752771_c212703ab899",
            tcp_os_profile="Windows_11",
            device_fingerprints=[f"DEV_RES_EDGE_WIN_{i:03d}" for i in range(20)],
            ip_pool=[f"108.204.45.{i}" for i in range(10, 60)],
        )
        syn_ato = SyndicateEntity(
            syndicate_id="SYN_US_ATO_SYNDICATE",
            name="Account Takeover & High-Ticket Retail Syndicate",
            archetype="ATO_RETAIL_CREW",
            primary_playbooks=[
                "ADV_ATO_SILENT_BAKING",
                "ADV_ACCOUNT_TAKEOVER",
                "ADV_APPLE_PAY_YELLOW_PATH",
                "ADV_TOKEN_PROVISIONING_FRAUD",
                "INTENT_OMEGA_HARVEST",
            ],
            target_mccs=[5732, 5311, 5944],
            credential_tiers=["TIER_SESSION_COOKIE", "TIER_PHISHED_OTP", "TIER_DEVICE_TOKEN"],
            botnets=[ato_botnet_comcast, ato_botnet_att],
            mule_rings=[ato_mule_t1, ato_mule_t2],
        )

        # 3. SYN_US_SYNTHETIC_BUSTOUT: Synthetic Identity Sleeper Bust-Out & ACH Float Syndicate
        bustout_mule_t2 = MuleRing(
            ring_id="MULE_US_BUSTOUT_WF_03",
            tier=MuleTier.TIER_2_AGGREGATOR,
            account_type="COMMERCIAL_SHELL_LLC",
            liquidation_channel="ACH_KITING_WHOLESALE",
            beneficiary_accounts=[f"MULE_WELLS_CORP_{i:05d}" for i in range(300, 310)],
            bank_routing="121000247",
            fee_cut_ratio=0.18,
            layering_hop_latency_seconds=1800.0,
        )
        syn_bustout = SyndicateEntity(
            syndicate_id="SYN_US_SYNTHETIC_BUSTOUT",
            name="Synthetic Identity Sleeper Bust-Out Ring",
            archetype="SYNTHETIC_BUSTOUT_RING",
            primary_playbooks=[
                "ADV_SLEEPER_BUST_OUT",
                "ADV_COLLUSIVE_BUST_OUT_MID",
                "INTENT_OMEGA_INCUBATE",
            ],
            target_mccs=[6051, 5944, 5732],
            credential_tiers=["TIER_CNP_FULLZ"],
            botnets=[ato_botnet_comcast],
            mule_rings=[bustout_mule_t2],
        )

        # 4. SYN_US_RESHIP_GIFT: CNP Reship & Gift Card Drain Ring
        reship_botnet = BotnetCluster(
            cluster_id="BOTNET_US_RES_CHARTER_04",
            name="Charter Spectrum Residential SOCKS5 Pool",
            subnet_prefix="68.114.88.0/24",
            asn="AS20115",
            isp="Charter Communications",
            proxy_type="RESIDENTIAL_STICKY",
            ja4_signature="t13d1415h2_08a3f8541249_4387201bc910",
            tcp_os_profile="macOS_Darwin",
            device_fingerprints=[f"DEV_RES_MAC_SAFARI_{i:03d}" for i in range(15)],
            ip_pool=[f"68.114.88.{i}" for i in range(10, 50)],
        )
        reship_mule = MuleRing(
            ring_id="MULE_US_GIFT_LIQUIDATION_04",
            tier=MuleTier.TIER_1_SMURF,
            account_type="PERSONAL_CHECKING",
            liquidation_channel="SECONDARY_GIFT_CARD_P2P",
            beneficiary_accounts=[f"MULE_USAA_{i:05d}" for i in range(400, 408)],
            bank_routing="314074269",
            fee_cut_ratio=0.25,
            layering_hop_latency_seconds=600.0,
        )
        syn_reship = SyndicateEntity(
            syndicate_id="SYN_US_RESHIP_GIFT",
            name="CNP Reship Logistics & Gift Card Drain Ring",
            archetype="RESHIP_GIFT_DRAIN",
            primary_playbooks=[
                "ADV_TRIANGULATION_FRAUD",
                "INTENT_OMEGA_BISECT_DRAIN",
            ],
            target_mccs=[5947, 5310, 5732],
            credential_tiers=["TIER_CNP_FULLZ", "TIER_TRACK_2_DUMP"],
            botnets=[reship_botnet],
            mule_rings=[reship_mule],
        )

        # 5. SYN_US_IAB_STEALER: Initial Access Broker & Stealer Log Distributor
        stealer_botnet = BotnetCluster(
            cluster_id="BOTNET_US_MALWARE_C2_05",
            name="Infostealer C2 Exfiltration Gateway",
            subnet_prefix="185.220.101.0/24",
            asn="AS9009",
            isp="Offshore Bulletproof Hosting",
            proxy_type="DATACENTER_ROTATING",
            ja4_signature="t12i1212h1_7caa04519921_b124802fc712",
            tcp_os_profile="Linux_Container",
            device_fingerprints=[f"DEV_MALWARE_DROPPER_{i:03d}" for i in range(10)],
            ip_pool=[f"185.220.101.{i}" for i in range(5, 45)],
        )
        syn_iab = SyndicateEntity(
            syndicate_id="SYN_US_IAB_STEALER",
            name="Initial Access Broker & Stealer Log Distributor",
            archetype="IAB_STEALER_BROKER",
            primary_playbooks=["ADV_STEALER_LOG_TRIAGE", "ADV_INITIAL_ACCESS_DROP"],
            target_mccs=[5815, 8398],
            credential_tiers=["TIER_SESSION_COOKIE", "TIER_CNP_FULLZ"],
            botnets=[stealer_botnet],
            mule_rings=[ato_mule_t1],
        )

        # 6. SYN_US_FINCEN_MULE_NET: Multi-Tier Layering & Crypto Off-Ramp Network
        fincen_crypto_offramp = MuleRing(
            ring_id="MULE_US_CRYPTO_OFFRAMP_05",
            tier=MuleTier.TIER_3_OFFRAMP,
            account_type="P2P_CRYPTO_ESCROW",
            liquidation_channel="BINANCE_BYBIT_P2P_USDT_TRC20",
            beneficiary_accounts=[f"MULE_CRYPTO_USDT_{i:05d}" for i in range(500, 515)],
            bank_routing="P2P_TRON_USDT",
            fee_cut_ratio=0.05,
            layering_hop_latency_seconds=900.0,
        )
        syn_fincen_mule = SyndicateEntity(
            syndicate_id="SYN_US_FINCEN_MULE_NET",
            name="FinCEN 3-Tier Layering & Crypto Off-Ramp Network",
            archetype="FINCEN_MULE_NETWORK",
            primary_playbooks=["ADV_MULTI_HOP_LAYERING", "ADV_CRYPTO_SEVERANCE"],
            target_mccs=[6051, 6012],
            credential_tiers=["TIER_SESSION_COOKIE", "TIER_DEVICE_TOKEN"],
            botnets=[ato_botnet_att],
            mule_rings=[ato_mule_t1, ato_mule_t2, fincen_crypto_offramp],
        )

        self.syndicates = [
            syn_carding,
            syn_ato,
            syn_bustout,
            syn_reship,
            syn_iab,
            syn_fincen_mule,
        ]

    def _init_india_syndicates(self) -> None:
        """Configures 5 empirical India cybercrime threat actors grounded in I4C/CFCFRMS reports."""
        # 1. SYN_IN_MEWAT_VISH: Mewat Remote Vishing & APK Trojan Ring
        apk_botnet = BotnetCluster(
            cluster_id="BOTNET_IN_JIO_APK_01",
            name="Reliance Jio 4G Mobile Botnet Pool",
            subnet_prefix="103.251.167.0/24",
            asn="AS55836",
            isp="Reliance Jio Infocomm",
            proxy_type="MOBILE_4G_5G",
            ja4_signature="t13d1516h2_apk_android_dalvik",
            tcp_os_profile="Android_Linux",
            device_fingerprints=[f"DEV_APK_SPOOF_JIO_{i:03d}" for i in range(20)],
            ip_pool=[f"103.251.167.{i}" for i in range(10, 80)],
        )
        mewat_mule_t1 = MuleRing(
            ring_id="MULE_IN_SMURF_SBI_01",
            tier=MuleTier.TIER_1_SMURF,
            account_type="PERSONAL_CHECKING",
            liquidation_channel="INSTANT_UPI_P2P",
            beneficiary_accounts=[f"MULE_SBI_{i:05d}" for i in range(100, 115)],
            bank_routing="SBIN0001234",
            fee_cut_ratio=0.10,
            layering_hop_latency_seconds=120.0,
        )
        syn_mewat = SyndicateEntity(
            syndicate_id="SYN_IN_MEWAT_VISH",
            name="Mewat Remote Vishing & APK Trojan Syndicate",
            archetype="REMOTE_VISHING_APK",
            primary_playbooks=[
                "IN_ADV_REVERSE_PROXY_VISHING",
                "IN_ADV_APK_SMS_STEALER",
                "IN_ADV_SIM_SWAP_ESIM_HIJACK",
                "ADV_INDIAN_VISHING_OTP",
                "ADV_INDIAN_APK_FORWARDER",
                "INTENT_OMEGA_PROBE",
            ],
            target_mccs=[4899, 8398, 5815],
            credential_tiers=["TIER_PHISHED_OTP", "TIER_TRACK_2_DUMP"],
            botnets=[apk_botnet],
            mule_rings=[mewat_mule_t1],
        )

        # 2. SYN_IN_JAMTARA_VISH: Jamtara Telephony Social Engineering Crew
        airtel_botnet = BotnetCluster(
            cluster_id="BOTNET_IN_AIRTEL_02",
            name="Bharti Airtel Mobile SOCKS5 Pool",
            subnet_prefix="49.32.12.0/24",
            asn="AS45609",
            isp="Bharti Airtel Limited",
            proxy_type="MOBILE_4G_5G",
            ja4_signature="t13d1516h2_dfa4a7752771_c212703ab899",
            tcp_os_profile="Android_Linux",
            device_fingerprints=[f"DEV_AIRTEL_MOB_{i:03d}" for i in range(15)],
            ip_pool=[f"49.32.12.{i}" for i in range(10, 50)],
        )
        syn_jamtara = SyndicateEntity(
            syndicate_id="SYN_IN_JAMTARA_VISH",
            name="Jamtara Social Engineering & KYC Phishing Crew",
            archetype="TELEPHONY_SOCIAL_ENGINEERING",
            primary_playbooks=["IN_ADV_KYC_EXPIRY_PHISHING", "IN_ADV_LOTTERY_PRIZE_SCAM"],
            target_mccs=[5311, 5732],
            credential_tiers=["TIER_PHISHED_OTP", "TIER_CNP_FULLZ"],
            botnets=[airtel_botnet],
            mule_rings=[mewat_mule_t1],
        )

        # 3. SYN_IN_RENT_DRAIN: Credit-to-Bank Rent Portal Arbitrage Ring
        rent_mule_t2 = MuleRing(
            ring_id="MULE_IN_RENT_HDFC_02",
            tier=MuleTier.TIER_2_AGGREGATOR,
            account_type="COMMERCIAL_SHELL_LLC",
            liquidation_channel="CRED_HOUSING_RENT_PORTAL",
            beneficiary_accounts=[f"MULE_HDFC_CORP_{i:05d}" for i in range(200, 210)],
            bank_routing="HDFC0000456",
            fee_cut_ratio=0.12,
            layering_hop_latency_seconds=180.0,
        )
        syn_rent = SyndicateEntity(
            syndicate_id="SYN_IN_RENT_DRAIN",
            name="Credit-to-Bank Rent Portal Arbitrage Ring",
            archetype="RENT_PORTAL_DRAIN",
            primary_playbooks=[
                "IN_ADV_RENT_PORTAL_CASHOUT",
                "ADV_CREDIT_LINE_CASH_OUT",
                "INTENT_OMEGA_BISECT_DRAIN",
                "INTENT_OMEGA_HARVEST",
            ],
            target_mccs=[6513, 5311, 5732],
            credential_tiers=["TIER_CNP_FULLZ", "TIER_DEVICE_TOKEN"],
            botnets=[apk_botnet],
            mule_rings=[rent_mule_t2],
        )

        # 4. SYN_IN_P2P_MULE_HERDER: P2P Crypto Laundering Ring
        crypto_mule_t3 = MuleRing(
            ring_id="MULE_IN_P2P_CRYPTO_03",
            tier=MuleTier.TIER_3_OFFRAMP,
            account_type="P2P_CRYPTO_ESCROW",
            liquidation_channel="BINANCE_P2P_USDT_ESCROW",
            beneficiary_accounts=[f"MULE_USDT_TRC_{i:05d}" for i in range(300, 312)],
            bank_routing="P2P_TRON_USDT",
            fee_cut_ratio=0.06,
            layering_hop_latency_seconds=600.0,
        )
        syn_p2p_crypto = SyndicateEntity(
            syndicate_id="SYN_IN_P2P_MULE_HERDER",
            name="P2P USDT Crypto Off-Ramp Herder Network",
            archetype="P2P_CRYPTO_OFFRAMP",
            primary_playbooks=["IN_ADV_P2P_CRYPTO_LAUNDERING", "ADV_CRYPTO_SEVERANCE"],
            target_mccs=[6051, 6012],
            credential_tiers=["TIER_CNP_FULLZ"],
            botnets=[airtel_botnet],
            mule_rings=[mewat_mule_t1, rent_mule_t2, crypto_mule_t3],
        )

        # 5. SYN_IN_INTL_BYPASS: Foreign Non-3DS Gateway Bypass Syndicate
        intl_botnet = BotnetCluster(
            cluster_id="BOTNET_IN_INTL_PROXY_03",
            name="Offshore Foreign Gateway Proxy Pool",
            subnet_prefix="185.220.101.0/24",
            asn="AS9009",
            isp="Offshore Bulletproof Hosting",
            proxy_type="DATACENTER_ROTATING",
            ja4_signature="t13d1516h2_dfa4a7752771_c212703ab899",
            tcp_os_profile="Linux_Container",
            device_fingerprints=[f"DEV_INTL_CHROME_{i:03d}" for i in range(12)],
            ip_pool=[f"185.220.101.{i}" for i in range(1, 35)],
        )
        syn_intl = SyndicateEntity(
            syndicate_id="SYN_IN_INTL_BYPASS",
            name="Foreign Gateway Non-3DS Bypass Syndicate",
            archetype="INTL_NON_3DS_BYPASS",
            primary_playbooks=[
                "IN_ADV_INTL_NON_3DS_BYPASS",
                "ADV_INDIAN_INTL_BYPASS",
                "INTENT_OMEGA_INCUBATE",
            ],
            target_mccs=[4722, 5999, 7011],
            credential_tiers=["TIER_CNP_FULLZ"],
            botnets=[intl_botnet],
            mule_rings=[],
        )

        self.syndicates = [
            syn_mewat,
            syn_jamtara,
            syn_rent,
            syn_p2p_crypto,
            syn_intl,
        ]

    def get_syndicate_by_id(self, syndicate_id: str) -> Optional[SyndicateEntity]:
        """Returns the syndicate entity with the given ID, if known."""
        return self._syndicate_by_id.get(syndicate_id)

    def get_syndicate_for_intent(
        self,
        macro_option: str,
        mcc: int,
        amount: float,
        credential_tier: str = "",
        playbook_name: str = "",
    ) -> SyndicateEntity:
        """Dynamically attributes a candidate fraud transaction to the most specialized syndicate.
        
        Eliminates the monopolistic 2-syndicate baseline by evaluating the target MCC,
        ticket size, credential tier, and attack macro-option.
        """
        # If explicit legacy playbook matches exactly one syndicate (and is not an INTENT scenario tag), prioritize it
        if playbook_name and not playbook_name.startswith("INTENT_OMEGA_") and playbook_name in self._playbook_to_syndicates:
            candidates = self._playbook_to_syndicates[playbook_name]
            if len(candidates) == 1:
                return candidates[0]

        if self.region == "IN":
            if macro_option == "OMEGA_PROBE" or mcc in (8398, 4899, 5815):
                # Probing is shared between Mewat remote testing and Jamtara vishing testers
                return self._syndicate_by_id["SYN_IN_JAMTARA_VISH"] if self.rng.random() < 0.35 else self._syndicate_by_id["SYN_IN_MEWAT_VISH"]
            elif mcc in (6513, 5311) or amount > 25000.0:
                return self._syndicate_by_id["SYN_IN_RENT_DRAIN"]
            elif mcc in (6051, 6012) or amount > 50000.0:
                return self._syndicate_by_id["SYN_IN_P2P_MULE_HERDER"]
            elif mcc in (4722, 7011):
                return self._syndicate_by_id["SYN_IN_INTL_BYPASS"]
            else:
                # Weighted distribution across active India syndicates
                weights = [0.35, 0.20, 0.25, 0.15, 0.05]
                return self.rng.choice(self.syndicates, p=weights)

        # US Region Logic
        if macro_option == "OMEGA_PROBE" or (mcc in (8398, 4899, 5815) and amount <= 10.0):
            # Probing is shared between card-checking botnets (75%) and Initial Access Brokers (25%)
            if self.rng.random() < 0.25:
                return self._syndicate_by_id["SYN_US_IAB_STEALER"]
            return self._syndicate_by_id["SYN_US_CARDING_BOT"]

        if mcc == 5947 or mcc == 5310:
            # Gift card liquidation and department store drains
            return self._syndicate_by_id["SYN_US_RESHIP_GIFT"]

        if mcc in (6051, 6012):
            # Cryptocurrency purchase and financial off-ramps
            return self._syndicate_by_id["SYN_US_FINCEN_MULE_NET"]

        if amount >= 1500.0 and mcc in (5732, 5944):
            # High-ticket electronics and luxury goods bust-outs or ATO
            p_bustout = 0.45 if credential_tier == "TIER_CNP_FULLZ" else 0.20
            if self.rng.random() < p_bustout:
                return self._syndicate_by_id["SYN_US_SYNTHETIC_BUSTOUT"]
            return self._syndicate_by_id["SYN_US_ATO_SYNDICATE"]

        if macro_option == "OMEGA_BISECT_DRAIN":
            # Bisect drains span between ATO retail crews and Reship/Gift rings
            return self.rng.choice([
                self._syndicate_by_id["SYN_US_ATO_SYNDICATE"],
                self._syndicate_by_id["SYN_US_RESHIP_GIFT"],
            ])

        # General harvest: distributed across the 4 exploitation syndicates
        candidate_pool = [
            self._syndicate_by_id["SYN_US_ATO_SYNDICATE"],
            self._syndicate_by_id["SYN_US_RESHIP_GIFT"],
            self._syndicate_by_id["SYN_US_SYNTHETIC_BUSTOUT"],
            self._syndicate_by_id["SYN_US_FINCEN_MULE_NET"],
        ]
        weights = [0.40, 0.30, 0.15, 0.15]
        return self.rng.choice(candidate_pool, p=weights)

    def get_syndicate_for_playbook(self, playbook: str) -> Optional[SyndicateEntity]:
        """Returns a syndicate responsible for the specified playbook (backwards compatibility)."""
        if playbook in self._playbook_to_syndicates:
            matches = self._playbook_to_syndicates[playbook]
            return matches[0] if len(matches) == 1 else self.rng.choice(matches)
        if self.syndicates:
            return self.syndicates[0]
        return None
