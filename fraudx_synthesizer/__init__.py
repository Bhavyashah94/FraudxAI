"""FraudX-Synthesizer: Sovereign Multi-Agent Financial Transaction & Attack Simulation Framework.

An independent, publication-grade benchmark library for synthesizing payment transaction
histories, adversarial fraud topologies, and closed-form causal Shapley ground truths.
"""

from .agents import (
    AdaptiveFraudsterAgent,
    BankDecisionEngine,
    CardholderProfile,
    CardholderState,
    ChannelType,
    FraudScenario,
    FraudsterAgent,
    ISO8583Response,
)
from .causal_scm import (
    CausalGroundTruth,
    CounterfactualCausalEngine,
    StructuralCausalEngine,
)
from .engine import (
    DiscreteEventEngine,
    SimulationEngine,
)
from .evaluation import (
    GroundTruthXAIEvaluator,
    XAIBenchmarkResult,
)
from .invariants import (
    EARTH_RADIUS_KM,
    haversine_distance_km,
    verify_transaction_invariants,
)
from .ledger import (
    CardholderLedgerState,
    StreamingLedger,
    WelfordAccumulator,
)
from .syndicates import (
    BotnetCluster,
    MuleRing,
    SyndicateEntity,
    SyndicateRegistry,
)
from .world import (
    MCC_TAXONOMY,
    MerchantProfile,
    WorldEnvironment,
)

__version__ = "0.2.0"

__all__ = [
    "DiscreteEventEngine",
    "SimulationEngine",
    "StreamingLedger",
    "WorldEnvironment",
    "CardholderProfile",
    "CardholderState",
    "MerchantProfile",
    "AdaptiveFraudsterAgent",
    "FraudsterAgent",
    "BankDecisionEngine",
    "ISO8583Response",
    "FraudScenario",
    "ChannelType",
    "StructuralCausalEngine",
    "CounterfactualCausalEngine",
    "CausalGroundTruth",
    "GroundTruthXAIEvaluator",
    "XAIBenchmarkResult",
    "WelfordAccumulator",
    "CardholderLedgerState",
    "verify_transaction_invariants",
    "haversine_distance_km",
    "EARTH_RADIUS_KM",
    "MCC_TAXONOMY",
    "BotnetCluster",
    "MuleRing",
    "SyndicateEntity",
    "SyndicateRegistry",
]

