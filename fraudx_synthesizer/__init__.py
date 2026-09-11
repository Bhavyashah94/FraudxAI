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
from .benchmark import (
    AdversarialPrivacyEvaluator,
    AdversarialPrivacySummary,
    MLUtilityEvaluator,
    MLUtilitySummary,
    ModelBenchmarkSummary,
    StatisticalFidelityEvaluator,
    StatisticalFidelitySummary,
    TripartiteBenchmarkHarness,
    TripartiteBenchmarkSummary,
    XAIBenchmarkHarness,
    generate_tripartite_markdown_report,
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
    DoubleEntryWorldLedger,
    StreamingLedger,
    WelfordAccumulator,
)
from .rails import (
    CandidateTransactionIntent,
    RailVerificationResult,
    RailVerifierSwitch,
)
from .stream import (
    INFERENCE_ALLOWLIST,
    ZeroLeakageDataPartitioner,
)
from .syndicates import (
    BotnetCluster,
    MuleRing,
    SyndicateEntity,
    SyndicateRegistry,
)
from .hawkes import (
    ADVERSARY_HAWKES_PROFILES,
    PERSONA_HAWKES_PROFILES,
    HawkesParameters,
    RecursiveCircadianHawkesEngine,
)
from .invertible_flow import (
    AffineCouplingLayer,
    ConditionalRealNVPFlow,
    LatentAumannShapleyAttributor,
    TransactionFlowFeatureCodec,
)
from .world import (
    MCC_TAXONOMY,
    MerchantProfile,
    WorldEnvironment,
)
from .intent import (
    AnalyticalBeliefState,
    CandidateAction,
    ConstraintPruner,
    CredentialDossier,
    CredentialTier,
    InformationDirectedOptimizer,
    MacroOptionType,
    MultiHopSwitchEngine,
    SwitchHopResult,
    TokenBindingResult,
)
from .visualizer import (
    compile_simulation_data_bundle,
    generate_visualization_file,
    render_standalone_html,
)

__version__ = "0.3.0"

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
    "XAIBenchmarkHarness",
    "ModelBenchmarkSummary",
    "StatisticalFidelitySummary",
    "MLUtilitySummary",
    "AdversarialPrivacySummary",
    "TripartiteBenchmarkSummary",
    "StatisticalFidelityEvaluator",
    "MLUtilityEvaluator",
    "AdversarialPrivacyEvaluator",
    "TripartiteBenchmarkHarness",
    "generate_tripartite_markdown_report",
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
    "HawkesParameters",
    "RecursiveCircadianHawkesEngine",
    "PERSONA_HAWKES_PROFILES",
    "ADVERSARY_HAWKES_PROFILES",
    "ConditionalRealNVPFlow",
    "AffineCouplingLayer",
    "TransactionFlowFeatureCodec",
    "LatentAumannShapleyAttributor",
    "DoubleEntryWorldLedger",
    "CandidateTransactionIntent",
    "RailVerificationResult",
    "RailVerifierSwitch",
    "ZeroLeakageDataPartitioner",
    "INFERENCE_ALLOWLIST",
    "AnalyticalBeliefState",
    "CandidateAction",
    "ConstraintPruner",
    "CredentialDossier",
    "CredentialTier",
    "InformationDirectedOptimizer",
    "MacroOptionType",
    "MultiHopSwitchEngine",
    "SwitchHopResult",
    "TokenBindingResult",
    "compile_simulation_data_bundle",
    "generate_visualization_file",
    "render_standalone_html",
]

