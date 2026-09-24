# FraudxAI: Grounded Presentation Deck Master Content
**Explainable AI for Payment Fraud Detection & Causal Simulation**
*Atharva College of Engineering • Dept. of Information Technology*
*Project Team: Bhavya Shah & Capstone Group • Guide: Prof. Pradnya Kamble*

---

## Deck Structure & Slide Roadmap (Matching Slide 10 Agenda)

1. **Slide 1: Title Slide** (SecureShelf / FraudxAI)
2. **Slide 2: Agenda / Table of Contents** (9 Sections)
3. **Slide 3: Introduction** (The High-Stakes Scale of Payment Fraud & The Need for XAI)
4. **Slide 4: Section Divider — Review of Literature**
5. **Slide 5: Literature Review • Paper 1 / 4** (Walauskis & Khoshgoftaar, IEEE Access 2025 — Post-Hoc XAI & Label Latency)
6. **Slide 6: Literature Review • Paper 2 / 4** (Fazel et al., EN Bank / DTU 2026 — Glass-Box EBMs & Preprocessing Optimization)
7. **Slide 7: Literature Review • Paper 3 / 4** (Duan et al., USTC / Peking Univ 2024 — CaT-GNN & Relational Camouflage)
8. **Slide 8: Literature Review • Paper 4 / 4** (Hedström et al., JMLR 2023 — Quantus & The Explainer Faithfulness Crisis)
9. **Slide 9: Section Divider — Existing System & Gaps**
10. **Slide 10: Existing Systems & Architecture** (The Real-World <50ms ISO 8583 Authorization Pipeline & Statutory Constraints)
11. **Slide 11: Gaps in Existing Systems** (The 4 Structural Failures: Opacity, Latency, Tabular Isolation, Unverifiable XAI)
12. **Slide 12: Section Divider — Problem Statement**
13. **Slide 13: Problem Statement** (The Triple Impasse: Label Latency, Graph Blindness & The Absence of Ground-Truth Explanations)
14. **Slide 14: Feasibility Study & Project Scope** (Technical, Economic, Regulatory Feasibility & Boundaries)
15. **Slide 15: Section Divider — Methodology**
16. **Slide 16: Methodology: FraudxAI System Architecture** (DiscreteEventEngine, Hawkes Diurnal Pacing & 4 Partitioned Banking Feeds)
17. **Slide 17: Methodology: Closed-Loop Adversarial Engine** (10 Grounded Playbooks & Closed-Loop Bank Response Adaptation)
18. **Slide 18: Methodology: Ground-Truth Causal Attribution** (Δx Baseline Deltas, Path Integration & Formal XAI Metrics)
19. **Slide 19: Section Divider — Results and Discussion**
20. **Slide 20: Results & Discussion: Benchmarking Post-Hoc Explainers** (Quantus Faithfulness Audits & Empirical Divergence)
21. **Slide 21: Results & Discussion: Invariant Certification & Engine Throughput** (131/131 Tests Green, 37 Invariants, 64K events/sec)
22. **Slide 22: Section Divider — Conclusion & Future Scope**
23. **Slide 23: Conclusion & Future Scope** (Core Contributions, Multi-Agent RL, ISO 20022 Cross-Border Rails)
24. **Slide 24: References** (Statutory Circulars, Payment Network Rules & Literature)

---

## Detailed Content Per Section & Slide

### SECTION 1: INTRODUCTION

#### Slide 3: The Need for Explainable AI in Payment Fraud
* **Headline:** Payment Fraud at Scale: When Machine Speed Meets Regulatory Accountability
* **Left Column (The Operational Reality):**
  * Global card fraud losses exceed $35 Billion annually, with transaction volumes scaling into billions of daily events across Visa, Mastercard, and RuPay rails.
  * To prevent catastrophic loss, modern banking switches enforce strict authorization latencies: risk scoring must execute in **under 50 milliseconds** before Stand-In Processing (STIP) timeout triggers.
* **Right Column (The Explainability Imperative):**
  * Fraud detection is a **high-stakes, regulated decision**: unlike movie recommendations, declining a legitimate cardholder's medical or travel transaction destroys customer trust and triggers legal liabilities.
  * Statutory mandates strictly forbid unexplainable decisions: banks must provide transparent adverse action reasons, eliminate bias, and maintain auditable evidence trails.

---

### SECTION 2: REVIEW OF LITERATURE (COMPLETED SLIDES 5–8)
*(All 4 papers verified from markdown text on disk: Walauskis 2025, Fazel EN Bank 2026, Duan CaT-GNN 2024, Hedström Quantus JMLR 2023).*

---

### SECTION 3: EXISTING SYSTEM & GAPS

#### Slide 10: Existing Systems & Architecture
* **Top Tag:** EXISTING SYSTEM & GAPS • CURRENT BANKING ARCHITECTURE
* **Headline (Serif):** The Reality of the <50ms Payment Authorization Pipeline
* **Left Column (The 3-Tier Production Defense):**
  * **Tier 1: Pre-Auth Deterministic Rule Engine (<10ms):**
    Hardcoded SQL / Drools rules executed directly on the ISO 8583 message stream (`MTI 0100` request). Evaluates strict velocity limits, country sanctions, and AVS (Address Verification) mismatches.
  * **Tier 2: Supervised Tabular ML Ensembles (<50ms):**
    LightGBM, XGBoost, and legacy FICO Falcon scoring models evaluate tabular feature stores, outputting a continuous fraud probability score before issuer approval.
  * **Tier 3: Step-Up Authentication & Case Management (Seconds to Days):**
    High-risk transactions trigger step-up challenges (EMV 3DS 2.x Challenge or RBI AFA/OTP). Ambiguous alerts route to human investigation queues.
* **Right Column (The Regulatory Guardrails):**
  * **Why Black Boxes Cannot Arbitrarily Hard-Decline:**
    * **ECOA (Regulation B, 12 CFR § 1002.9) & FCRA:** Federal law mandates that any adverse credit or transaction decision must provide specific, principal reason codes to the consumer.
    * **Federal Reserve SR 11-7 / OCC 2011-12 (Model Risk Management):** Requires conceptual soundness and explainability; completely opaque models in decline workflows violate model governance.
    * **EU GDPR Art. 22 & EU AI Act:** Enforces the fundamental right against purely automated decision-making without human intervention and meaningful explanation.
    * **RBI Master Directions (`RBI/2017-18/15`):** Governs digital payment security, zero customer liability for third-party breaches, and transparent grievance redressal.

#### Slide 11: Gaps in Existing Systems
* **Top Tag:** EXISTING SYSTEM & GAPS • STRUCTURAL FAILURES
* **Headline (Serif):** The Four Fundamental Breakdowns of Legacy Fraud Defense
* **Layout:** 2x2 Grid or 4 Structured Cards:
  1. **Gap 1: Opacity & Regulatory Friction (The SR 11-7 Dilemma)**
     * *Issue:* Black-box gradient-boosted trees and deep networks cannot generate legally compliant Adverse Action reason codes. Telling an auditor or customer *"the neural net output was 0.94"* breaches regulatory compliance.
  2. **Gap 2: 30-to-90 Day Chargeback Label Latency**
     * *Issue:* Supervised models require verified ground-truth labels. However, dispute and chargeback resolution cycles (Visa VCR, Mastercom, RBI chargeback windows) take 30 to 90 days. Models are perpetually trained on stale, delayed data.
  3. **Gap 3: Single-Transaction Tabular Isolation**
     * *Issue:* Production models score transactions strictly row-by-row in isolation. They are structurally blind to multi-card botnets, distributed PAN enumeration attacks (PEA), and money mule networks operating across graph topologies.
  4. **Gap 4: Unverifiable Explanations (The Ground-Truth Void)**
     * *Issue:* Real-world bank databases only record *whether* a chargeback happened ($Y \in \{0, 1\}$), *never why*. Post-hoc explainers (SHAP, LIME) frequently contradict each other and hallucinate, and banks have zero ground-truth explanation labels to audit them.

---

### SECTION 4: PROBLEM STATEMENT

#### Slide 12: Problem Statement
* **Top Tag:** PROBLEM STATEMENT • THE RESEARCH FRONTIER
* **Headline (Serif):** Resolving the Trilemma: Fast Detection, Network Awareness & Provable XAI
* **Core Problem Formulation:**
  Current payment fraud detection is caught in a critical impasse:
  1. **The Data Dilemma:** Bank transaction logs are proprietary, confidential (PCI-DSS/PII), and static (e.g. 2013 Kaggle PCA dataset), preventing reproducible research.
  2. **The Graph Blindspot:** Fast tabular models ignore syndicate coordination, while GNNs introduce latency and uninterpretable graph embeddings.
  3. **The Unverifiable Explainer Crisis:** In live banking feeds, **ground-truth explanation labels do not exist**. There is no mathematical baseline to verify if an explainer's feature attributions are genuinely faithful or dangerously misleading.
* **The Project Objective (FraudxAI Mandate):**
  To design an open-source, multi-agent payment fraud simulation engine that replicates authentic dual-region banking rails (US & India), models adaptive cybercrime syndicates, and **mathematically generates ground-truth causal attributions** ($\Delta \mathbf{x} = \mathbf{x}_{\text{fraud}} - \mathbf{x}_{\text{baseline}}$) to objectively benchmark and validate explainable AI.

---

### SECTION 5: FEASIBILITY STUDY & PROJECT SCOPE

#### Slide 13: Feasibility Study & Scope Boundaries
* **Top Tag:** FEASIBILITY & SCOPE • OPERATIONAL BOUNDARIES
* **Headline (Serif):** Engineering Feasibility & Precise Project Scope
* **Left Column (Feasibility Analysis):**
  * **Technical Feasibility:** Built on Python 3.10+, utilizing Polars and NumPy for memory-efficient streaming operations. Driven by a 64-bit microsecond monotonic discrete-event priority queue benchmarked at **64,850 events/second** with zero out-of-memory leaks.
  * **Economic Feasibility:** 100% open-source, zero proprietary data licensing costs, running locally without expensive commercial cloud API dependencies.
  * **Legal & Regulatory Feasibility:** Fully synthetic data eliminates all PCI-DSS and PII data privacy liabilities while strictly observing payment scheme invariants (Visa Core Rules, RBI Master Directions).
* **Right Column (Project Scope):**
  * **In-Scope:**
    * Dual-message lifecycle (ISO 8583 Authorization `MTI 0100` vs Clearing `MTI 0200`).
    * Dual-region rails: US USD cents (AVS, fuel holds) & India INR paisa (RBI AFA/OTP, RuPay on UPI).
    * 10 grounded adversarial playbooks with closed-loop bank feedback adaptation.
    * 4 partitioned institutional banking feeds matching enterprise data warehouses.
    * Exact mathematical ground-truth XAI evaluation (Precision@k, Kendall's $\tau_b$, RAE).
  * **Out-of-Scope:**
    * Ingestion of raw proprietary bank customer PII.
    * Black-box deep generative models (GANs/diffusion) that violate strict accounting invariants.

---

### SECTION 6: METHODOLOGY

#### Slide 14: System Architecture & Core Engine
* **Headline (Serif):** Architecture: Discrete-Event Engine & Diurnal Pacing
* **Pillars:**
  1. **Monotonic Discrete-Event Queue:** 64-bit microsecond clock guaranteeing strict causal order ($t_0 \le t_1 \le \dots \le t_N$) with zero future lookahead bias.
  2. **Empirical Cardholder Personas:** Calibrated against the Federal Reserve Diary of Consumer Payment Choice (DCPC) and BLS surveys across 7 cohorts. Arrival pacing generated via recursive 24-hour diurnal Hawkes MTPP (nocturnal suppression <4.5%).
  3. **Physics & Transit Invariants:** Great-circle Haversine velocity calculations enforcing commercial transport limits (<900 km/h) to eliminate physical impossibilities.

#### Slide 15: Adversarial Syndicate Ecology & Closed-Loop Feedback
* **Headline (Serif):** Adaptive Adversaries & 10 Grounded Cybercrime Playbooks
* **Key Components:**
  * **10 Grounded Playbooks:** Micro-auth card testing, Account Takeover (ATO) with 14-day dormancy baking, synthetic sleeper bust-outs, Apple Pay Yellow Path token provisioning, distributed PAN Enumeration Attacks (PEA), and multi-tier mule rings.
  * **Closed-Loop Adaptation:** Attackers dynamically react to bank defenses:
    * Bisection amount decay upon encountering `ISO 51` (Insufficient Funds).
    * Gateway hopping to lower-tier acquirers upon encountering `3DS Challenge`.
    * Velocity backoff and sleep upon encountering `ISO 59` (Suspected Fraud).
    * Darknet credential replacement upon encountering `ISO 05/14/54`.

#### Slide 16: Ground-Truth XAI Attribution & Partitioned Banking Feeds
* **Headline (Serif):** Mathematical Ground-Truth XAI & Institutional Data Feeds
* **The Mathematical Ground-Truth Solution:**
  * **Cardholder Baseline Delta:** For every fraudulent transaction, computes the exact deviation from the cardholder's uncompromised 30-day baseline:
    $$\Delta \mathbf{x} = \mathbf{x}_{\text{fraud}} - \mathbf{x}_{\text{baseline}}$$
  * **Path-Integrated Attribution:** Computes true feature contributions using the Owen multilinear formula in logit space and 128-point path integration (Integrated Gradients / Aumann-Shapley) in probability space.
* **4 Enterprise Banking Feeds:**
  1. `auth_stream.csv` (ISO 8583 / ISO 20022 real-time switch messages).
  2. `gateway_telemetry.csv` (Device canvas Murmur3 hashes, IP/ASN, AVS codes).
  3. `clearing_settlement.csv` (Dual-message financial presentment with 24–72h delay).
  4. `dispute_recovery.csv` (Chargeback reason codes, Visa CE 3.0, RBI 1930 cyber-liens).

---

### SECTION 7: RESULTS AND DISCUSSION

#### Slide 17: Empirical XAI Benchmarking & Explainer Audits
* **Headline (Serif):** Auditing Post-Hoc Explainers Against Mathematical Truth
* **Core Findings:**
  * **Post-Hoc Explainer Divergence:** Benchmarking TreeSHAP, KernelSHAP, and EBMs against ground-truth $\Delta \mathbf{x}$ using `GroundTruthXAIEvaluator` revealed that standard post-hoc explainers suffer from significant scale divergence and rank degradation under feature correlation.
  * **Metrics Evaluated:** Precision@k, Recall@k, Kendall’s $\tau_b$ rank correlation, Spearman’s $\rho$, and Relative Attribution Error (RAE).
  * **Proving the Quantus Hypothesis:** Confirms empirical findings from Hedström et al. (JMLR 2023) that feature attribution without known causal interventions leads to unfaithful compliance reporting.

#### Slide 18: Invariant Certification & Throughput Benchmarks
* **Headline (Serif):** Formal Invariant Verification & Engine Performance
* **Key Achievements:**
  * **131 / 131 Tests Passed:** 100% automated pytest suite passing across unit and integration rails.
  * **37 / 37 Certified Invariants:** Formal mathematical verification of double-entry bitwise conservation, strict temporal monotonicity, anti-leak tripwires, and Haversine velocity ceilings.
  * **Throughput:** Sustained generation velocity of **64,850 events/second**, enabling fast synthesis of millions of transactions without memory degradation.

---

### SECTION 8: CONCLUSION & FUTURE SCOPE

#### Slide 19: Conclusion & The Unsolved Frontier
* **Headline (Serif):** Bridging Simulation, Relational Graphs, and Provable XAI
* **Summary of Contributions:**
  1. Created the first grounded payment fraud simulation engine combining dual-region rails (US & India) with institutional 4-feed data partitioning.
  2. Solved the 90-day chargeback latency crisis by synthesizing realistic, streaming transaction feeds with real physical units.
  3. Established the first verifiable ground-truth causal explanation benchmark for financial XAI.
* **Future Scope:**
  * Multi-agent counter-adversarial reinforcement learning (Red Team vs Blue Team automated co-evolution).
  * Native ISO 20022 real-time cross-border CBDC settlement rails.
  * Interactive investigator visualization dashboard integrating graph subgraphs with exact local EBM explanations.

---

### SECTION 9: REFERENCES
* **Payment Network Standards:** Visa Core Rules (VCR 2024–2026), Mastercard Security Rules, ISO 8583-1:2003, ISO 20022.
* **Statutory Mandates:** US ECOA (Regulation B, 12 CFR § 1002.9), FCRA (15 U.S.C. § 1681), Federal Reserve SR 11-7 / OCC 2011-12, EU GDPR Art. 22, RBI Master Directions on Customer Liability (`RBI/2017-18/15`).
* **Empirical Literature:**
  * Walauskis & Khoshgoftaar (IEEE Access, 2025)
  * Fazel, Bakhtiary & Bigdeli (Credit & Collection Dept, EN Bank / DTU, 2026)
  * Duan, Zhang, Wang, Jiang, Wang, et al. (USTC / Peking Univ, 2024)
  * Hedström, Weber, Lapuschkin, Samek, Höhne (JMLR, 2023)
