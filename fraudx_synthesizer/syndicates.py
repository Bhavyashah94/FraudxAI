"""Adversarial Syndicate Graph Topologies & Persistent Infrastructure Entities.

Models real-world cybercrime underground infrastructure:
- Botnet proxy clusters sharing residential/datacenter ASN subnets and spoofed device canvas fingerprints across multiple compromised cardholders.
- Mule banking rings receiving layered cash-out transactions across multiple victims.
- Persistent syndicates enabling realistic bipartite and hypergraph link analysis for GNN and fraud ring detection benchmarks.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple
import numpy as np


@dataclass
class BotnetCluster:
    """Represents a distributed botnet or residential proxy pool executing coordinated attacks."""
    cluster_id: str
    subnet_prefix: str
    asn: str
    device_fingerprints: List[str]
    ip_pool: List[str]

    def sample_ip_and_device(self, rng: np.random.Generator) -> Tuple[str, str]:
        """Draws an IP and device fingerprint from the cluster pool."""
        ip = str(rng.choice(self.ip_pool))
        device = str(rng.choice(self.device_fingerprints))
        return ip, device


@dataclass
class MuleRing:
    """Represents a coordinated money-mule laundering network receiving fraudulent proceeds."""
    ring_id: str
    liquidation_channel: str
    beneficiary_accounts: List[str]
    layering_hop_latency_seconds: float = 300.0

    def sample_beneficiary(self, rng: np.random.Generator) -> str:
        """Draws a target mule beneficiary account."""
        return str(rng.choice(self.beneficiary_accounts))


@dataclass
class SyndicateEntity:
    """A persistent cybercrime syndicate operating coordinated campaigns across accounts."""
    syndicate_id: str
    name: str
    primary_playbook: str
    botnets: List[BotnetCluster] = field(default_factory=list)
    mule_rings: List[MuleRing] = field(default_factory=list)

    def sample_telemetry(self, rng: np.random.Generator) -> Dict[str, str]:
        """Samples persistent technical markers for an attack event."""
        res: Dict[str, str] = {
            "syndicate_id": self.syndicate_id,
            "botnet_cluster_id": "",
            "ip_subnet_prefix": "",
            "client_ip": "",
            "device_fingerprint_id": "",
            "mule_ring_id": "",
            "beneficiary_account_id": "",
        }

        if self.botnets:
            botnet = rng.choice(self.botnets)
            ip, dev = botnet.sample_ip_and_device(rng)
            res["botnet_cluster_id"] = botnet.cluster_id
            res["ip_subnet_prefix"] = botnet.subnet_prefix
            res["client_ip"] = ip
            res["device_fingerprint_id"] = dev

        if self.mule_rings:
            ring = rng.choice(self.mule_rings)
            res["mule_ring_id"] = ring.ring_id
            res["beneficiary_account_id"] = ring.sample_beneficiary(rng)

        return res


class SyndicateRegistry:
    """Initializes and manages persistent cybercrime syndicates for the simulation environment."""

    def __init__(self, region: str = "US", seed: int = 42):
        self.region = region.upper()
        self.rng = np.random.default_rng(seed)
        self.syndicates: List[SyndicateEntity] = []
        self._playbook_to_syndicate: Dict[str, SyndicateEntity] = {}
        self._initialize_syndicates()

    def _initialize_syndicates(self) -> None:
        """Instantiates grounded cybercrime organizations with realistic technical assets."""
        if self.region == "IN":
            apk_botnet = BotnetCluster(
                cluster_id="BOTNET_IN_APK_01",
                subnet_prefix="103.251.167.0/24",
                asn="AS55836",
                device_fingerprints=[f"DEV_APK_SPOOF_{i:03d}" for i in range(12)],
                ip_pool=[f"103.251.167.{i}" for i in range(10, 50)],
            )
            vishing_mule = MuleRing(
                ring_id="MULE_IN_RENT_RING_01",
                liquidation_channel="CRED_HOUSING_RENT_PORTAL",
                beneficiary_accounts=[f"MULE_ACC_SBIN_{i:05d}" for i in range(100, 108)],
                layering_hop_latency_seconds=180.0,
            )
            syn_in_1 = SyndicateEntity(
                syndicate_id="SYN_IN_MEWAT_VISH",
                name="Mewat Remote Vishing & APK Syndicate",
                primary_playbook="IN_ADV_REVERSE_PROXY_VISHING",
                botnets=[apk_botnet],
                mule_rings=[vishing_mule],
            )
            self.syndicates.append(syn_in_1)
            self._playbook_to_syndicate["IN_ADV_REVERSE_PROXY_VISHING"] = syn_in_1
            self._playbook_to_syndicate["IN_ADV_APK_SMS_STEALER"] = syn_in_1
            self._playbook_to_syndicate["IN_ADV_SIM_SWAP_ESIM_HIJACK"] = syn_in_1
            self._playbook_to_syndicate["ADV_INDIAN_VISHING_OTP"] = syn_in_1
            self._playbook_to_syndicate["ADV_INDIAN_APK_FORWARDER"] = syn_in_1

            intl_botnet = BotnetCluster(
                cluster_id="BOTNET_IN_PROXY_02",
                subnet_prefix="185.220.101.0/24",
                asn="AS9009",
                device_fingerprints=[f"DEV_RES_CHROME_{i:03d}" for i in range(8)],
                ip_pool=[f"185.220.101.{i}" for i in range(1, 30)],
            )
            syn_in_2 = SyndicateEntity(
                syndicate_id="SYN_IN_INTL_BYPASS",
                name="Foreign Gateway Non-3DS Bypass Syndicate",
                primary_playbook="IN_ADV_INTL_NON_3DS_BYPASS",
                botnets=[intl_botnet],
                mule_rings=[],
            )
            self.syndicates.append(syn_in_2)
            self._playbook_to_syndicate["IN_ADV_INTL_NON_3DS_BYPASS"] = syn_in_2
            self._playbook_to_syndicate["ADV_INDIAN_INTL_BYPASS"] = syn_in_2

            rent_mule = MuleRing(
                ring_id="MULE_IN_P2P_02",
                liquidation_channel="RENT_PORTAL_CASH_OUT",
                beneficiary_accounts=[f"MULE_ACC_HDFC_{i:05d}" for i in range(200, 206)],
                layering_hop_latency_seconds=360.0,
            )
            syn_in_3 = SyndicateEntity(
                syndicate_id="SYN_IN_RENT_DRAIN",
                name="Credit-to-Bank Rent Portal Ring",
                primary_playbook="IN_ADV_RENT_PORTAL_CASHOUT",
                botnets=[apk_botnet],
                mule_rings=[rent_mule],
            )
            self.syndicates.append(syn_in_3)
            self._playbook_to_syndicate["IN_ADV_RENT_PORTAL_CASHOUT"] = syn_in_3
            self._playbook_to_syndicate["ADV_CREDIT_LINE_CASH_OUT"] = syn_in_3

        else:
            carding_botnet = BotnetCluster(
                cluster_id="BOTNET_US_CARDING_01",
                subnet_prefix="198.54.130.0/24",
                asn="AS16509",
                device_fingerprints=[f"DEV_BOT_HEADLESS_{i:03d}" for i in range(15)],
                ip_pool=[f"198.54.130.{i}" for i in range(10, 60)],
            )
            syn_us_1 = SyndicateEntity(
                syndicate_id="SYN_US_CARDING_BOT",
                name="Automated Micro-Auth Probing Syndicate",
                primary_playbook="ADV_MICRO_AUTH_PROBE",
                botnets=[carding_botnet],
                mule_rings=[],
            )
            self.syndicates.append(syn_us_1)
            self._playbook_to_syndicate["ADV_MICRO_AUTH_PROBE"] = syn_us_1
            self._playbook_to_syndicate["ADV_DISTRIBUTED_BIN_ENUMERATION"] = syn_us_1
            self._playbook_to_syndicate["ADV_NOCTURNAL_BURST"] = syn_us_1
            self._playbook_to_syndicate["ADV_MICRO_AUTH_CARDING"] = syn_us_1

            bustout_mule = MuleRing(
                ring_id="MULE_US_ACH_RING_01",
                liquidation_channel="ACH_KITING_WHOLESALE",
                beneficiary_accounts=[f"MULE_CHASE_{i:05d}" for i in range(500, 508)],
                layering_hop_latency_seconds=900.0,
            )
            syn_us_2 = SyndicateEntity(
                syndicate_id="SYN_US_SYNTHETIC_BUSTOUT",
                name="Synthetic Identity Sleeper Bust-Out Ring",
                primary_playbook="ADV_SLEEPER_BUST_OUT",
                botnets=[],
                mule_rings=[bustout_mule],
            )
            self.syndicates.append(syn_us_2)
            self._playbook_to_syndicate["ADV_SLEEPER_BUST_OUT"] = syn_us_2
            self._playbook_to_syndicate["ADV_COLLUSIVE_BUST_OUT_MID"] = syn_us_2

            ato_botnet = BotnetCluster(
                cluster_id="BOTNET_US_ATO_02",
                subnet_prefix="142.250.190.0/24",
                asn="AS15169",
                device_fingerprints=[f"DEV_ATO_SPOOF_{i:03d}" for i in range(10)],
                ip_pool=[f"142.250.190.{i}" for i in range(20, 50)],
            )
            ato_mule = MuleRing(
                ring_id="MULE_US_CRYPTO_02",
                liquidation_channel="P2P_CRYPTO_ESCROW",
                beneficiary_accounts=[f"MULE_BOA_{i:05d}" for i in range(600, 606)],
                layering_hop_latency_seconds=450.0,
            )
            syn_us_3 = SyndicateEntity(
                syndicate_id="SYN_US_ATO_SYNDICATE",
                name="Account Takeover & Token Hijack Syndicate",
                primary_playbook="ADV_ATO_SILENT_BAKING",
                botnets=[ato_botnet],
                mule_rings=[ato_mule],
            )
            self.syndicates.append(syn_us_3)
            self._playbook_to_syndicate["ADV_ATO_SILENT_BAKING"] = syn_us_3
            self._playbook_to_syndicate["ADV_ACCOUNT_TAKEOVER"] = syn_us_3
            self._playbook_to_syndicate["ADV_APPLE_PAY_YELLOW_PATH"] = syn_us_3
            self._playbook_to_syndicate["ADV_TRIANGULATION_FRAUD"] = syn_us_3
            self._playbook_to_syndicate["ADV_TOKEN_PROVISIONING_FRAUD"] = syn_us_3

    def get_syndicate_for_playbook(self, playbook: str) -> Optional[SyndicateEntity]:
        """Returns the syndicate responsible for the specified playbook, if configured."""
        if playbook in self._playbook_to_syndicate:
            return self._playbook_to_syndicate[playbook]
        if self.syndicates:
            return self.syndicates[0]
        return None
