# FraudxAI: Grounded Multi-Agent Payment Fraud Simulation & Causal XAI Benchmark

[![Python](https://img.shields.io/badge/python-3.9%20%7C%203.10%20%7C%203.11%20%7C%203.12%20%7C%203.13-blue.svg)]()
[![Tests](https://img.shields.io/badge/pytest-54%20passed-brightgreen.svg)]()
[![Invariants](https://img.shields.io/badge/invariants-37%2F37%20verified-brightgreen.svg)]()
[![Standard](https://img.shields.io/badge/rails-ISO%208583%20%7C%20RBI%20AFA%20%7C%20Visa%20VCR-orange.svg)]()
[![Anti-Astronaut](https://img.shields.io/badge/grounding-Anti--Astronaut%20Certified-darkgreen.svg)](AGENTS.md)

**FraudxAI** is an open-source, mathematically rigorous **Discrete-Event Multi-Agent Simulation (DES-MAS)** platform and **Causal Explainable AI (XAI)** evaluation benchmark for payment card fraud detection.

Unlike synthetic data generators that rely on ungrounded statistical distributions or toy column schemas, FraudxAI synthesizes authentic **institutional banking feeds** calibrated to official payment network operating regulations (Visa Core Rules, Mastercard Rules), statutory central bank mandates (Reserve Bank of India Master Directions), and empirical cybercrime research.

---

## Key Capabilities

### 1. Dual-Region Payment Rail Ecosystems
* **US Dual-Message Rails (USD Cents)**:
  * Two-stage lifecycle: Authorization Request (`MTI 0100` $\to$ `0110`) followed by Financial Presentment/Clearing (`MTI 0200` $\to$ `0210`) with 24–72 hour settlement delays.
  * Real-world pre-auth mechanics: Automated Fuel Dispenser (AFD, MCC 5542) \$175 hold vs. final nozzle cutoff; Dining (MCC 5812) post-auth 10–20% tip tolerances; Hotel/Lodging (MCC 7011) incidental hold windows.
  * Stand-In Processing (STIP) floor limits when issuer cores timeout ($> 2.0\,\text{s}$).
  * Address Verification Service (AVS) numeric street + ZIP matrix adjudication (`Y`, `A`, `Z`, `N`, `U`).
* **Indian Payment Rails (INR Paisa)**:
  * Mandatory Additional Factor of Authentication (AFA/OTP) on domestic CNP e-commerce.
  * Contactless NFC tap-and-pay limits (₹5,000 ceiling without PIN, requiring PIN challenge or chip fallback after 5 consecutive taps).
  * RuPay Credit Cards on UPI QR code rails (POS Entry Mode `031`).
  * Card-on-File Tokenization (CoFT, `RBI/2021-22/96`) network tokenization flows.
  * Indian card product taxonomy: Kisan Credit Card (KCC), PMJDY RuPay Debit, FD-Backed Entry Cards, Salaried Prime Rewards, and Super-Premium HNI cards.

### 2. Multi-Agent Closed-Loop Feedback
* **Cardholder Agents**:
  * Calibrated to the Federal Reserve Diary of Consumer Payment Choice (DCPC) and BLS surveys across 7 verified demographic cohorts.
  * Continuous 24-hour circular circadian arrival intensity on $\mathbb{S}^1$ (von Mises mixture modeling lunch, dinner, and nocturnal sleep lull suppression).
  * Multi-modal discovery latency survival models: instant push notification (10–60s) vs. daily banking app checks (12–36h) vs. monthly billing statement reviews (30–45d).
  * Authentic hard negatives: legitimate home relocations and cross-border vacation travel that exhibit high spend/velocity anomalies but carry valid EMV chip cryptograms.
* **Adaptive Fraudster Syndicates**:
  * Closed-loop adaptation to bank responses: bisection amount decay on `ISO 51` (Insufficient Funds), gateway hopping to lower-tier acquirers on `3DS Challenge`, velocity backoff on `ISO 59` (Suspected Fraud), and darknet warranty replacement on `ISO 05/14/54`.
  * Grounded attack playbooks: Micro-auth card testing probes (AVS `Z` ZIP bypass), Account Takeover (ATO) with 14-day silent dormancy baking, synthetic sleeper bust-outs with ACH float exploitation, Apple Pay "Yellow Path" token provisioning, distributed PAN Enumeration Attacks (PEA additive guessing), triangulation fraud, reverse-proxy vishing, and malicious Android APK SMS stealers.
* **Bank Decision Engine**:
  * Multi-tier issuer authorization switch enforcing ISO 8583 response codes (`00` Approved, `05` Do Not Honor, `10` Partial Approval, `14` Invalid Card, `51` Insufficient Funds, `57` Transaction Not Permitted, `59` Suspected Fraud, `63` Security Violation, `65` Activity Limit Exceeded, `82` Invalid CVV).
  * Visa Account Attack Intelligence (VAAI) defense scoring against distributed card testing.

### 3. Four Partitioned Institutional Banking Feeds
Real financial institutions do not maintain a single flat table with toy column names (`amount`, `is_fraud`). FraudxAI partitions synthetic outputs into the four distinct feeds that production data warehouses actually store:

| Feed File | Schema Standard | Description |
| :--- | :--- | :--- |
| `auth_stream.csv` | ISO 8583 / ISO 20022 | Real-time authorization switch feed containing MTI, STAN, RRN, Auth Code, Response Code, POS Entry Mode, ECI, 3DS status, available balances, and minor currency units. |
| `gateway_telemetry.csv` | Payment Gateway Risk | Network & device telemetry containing Client IP, ASN type, geo risk scores, canvas Murmur3 hashes, AVS codes, CVV match flags, and cross-border flags. |
| `clearing_settlement.csv` | Dual-Message Settlement | Financial presentment feed (`MTI 0200`) with 24–72h delay windows, actual captured amounts (AFD pump vs hold, dining tips), and interchange fees. |
| `dispute_recovery.csv` | Scheme & Statutory Disputes | Chargeback logs with reason codes (Visa 10.4, RBI unauthorized debit), Visa CE 3.0 pre-dispute deflection, arbitration fees, RBI Customer Limited Liability Tiers (`RBI/2017-18/15`), and CFCFRMS 1930 golden hour cyber-liens. |

### 4. Ground-Truth Causal Counterfactuals & Shapley XAI Benchmarking
* **Pearl's Structural Counterfactual Twins**:
  For every fraudulent transaction $\mathbf{x}_{\text{obs}}$, the engine computes the unperturbed counterfactual twin $\mathbf{x}_{\text{cf}}$ the cardholder would have produced in the absence of the adversary:
  $$\mathbf{\phi}^*_{\text{input}} = \mathbf{x}_{\text{obs}} - \mathbf{x}_{\text{cf}}$$
* **Exact Analytical Shapley Attribution**:
  Provides closed-form game-theoretic Shapley attributions with zero residual efficiency error ($\sum_i \phi_i = f(\mathbf{x}) - \mathbb{E}[f]$), allowing post-hoc explainers (TreeSHAP, KernelSHAP) to be benchmarked against genuine ground truth.
* **Quantitative XAI Evaluator (`GroundTruthXAIEvaluator`)**:
  Computes Precision@k, Recall@k, Kendall's $\tau_b$, Spearman's $\rho$, and Relative Attribution Error (RAE).

### 5. Physical & Kinematic Invariants
* **Space-Time Velocity Limits**: Great-circle Haversine metrics with antipodal numerical stability guarantee that card-present transactions never exceed physical transport velocities ($< 900\,\text{km/h}$).
* **Temporal Monotonicity**: 64-bit microsecond priority queue with stable sequence tie-breaking guarantees strict global chronological order ($t_0 \le t_1 \le \dots \le t_N$).
* **Online Streaming Ledger**: Strictly point-in-time state updates using Welford's algorithm for online mean and variance tracking, completely eliminating future lookahead bias.

---

## Architecture Overview

```
                           +-------------------------------------+
                           | DiscreteEventEngine (Priority Queue)|
                           | 64-bit microsecond monotonic clock  |
                           +------------------+------------------+
                                              |
                     +------------------------+------------------------+
                     |                                                 |
                     v                                                 v
    +--------------------------------+                +--------------------------------+
    |       Cardholder Profile       |                |     AdaptiveFraudsterAgent     |
    |  - Fed DCPC Persona Clusters   |                |  - 10 Empirical Playbooks      |
    |  - Circadian von Mises simplex |                |  - Bisection Decay on ISO 51   |
    |  - Multi-modal discovery curve |                |  - Gateway Hop on 3DS (Tier C) |
    |  - Sub-mach kinematic bounds   |                |  - Nocturnal window targeting  |
    +----------------+---------------+                +----------------+---------------+
                     |                                                 |
                     +------------------------+------------------------+
                                              |
                                              v
                           +-------------------------------------+
                           |      BankDecisionEngine (Switch)    |
                           |  - ISO 8583 response codes          |
                           |  - RBI AFA / OTP verification       |
                           |  - INR 5k contactless ceiling       |
                           |  - Visa VAAI anti-enumeration       |
                           +------------------+------------------+
                                              |
                                              v
                           +-------------------------------------+
                           |     StreamingLedger (Point-in-Time) |
                           |  - Online Welford mean/variance     |
                           |  - 5-Way geo mismatch scoring       |
                           |  - Device canvas Murmur3 hash       |
                           +------------------+------------------+
                                              |
                                              v
                           +-------------------------------------+
                           |    Structural Causal Engine (SCM)   |
                           |  - Counterfactual twin generation   |
                           |  - Exact analytical Shapley values  |
                           +------------------+------------------+
                                              |
                     +------------------------+------------------------+
                     |                        |                        |
                     v                        v                        v
            [auth_stream.csv]      [gateway_telemetry.csv]  [clearing_settlement.csv]
            (ISO 8583 Protocol)    (Gateway Risk & Device)   (Dual-Message Presentment)
                                              |
                                              v
                                   [dispute_recovery.csv]
                                   (Chargebacks & 1930 Liens)
```

---

## Quick Start

### Installation

```bash
git clone https://github.com/bhavy/FraudxAI.git
cd FraudxAI
pip install -e .
```

### Command-Line Interface (CLI)

#### 1. Synthesize US Dual-Message Transactions
```bash
# Generates 5,000 US transactions partitioned into 4 institutional feeds
python -m fraudx_synthesizer.cli generate \
    -n 5000 \
    --cards 1000 \
    --merchants 150 \
    --region US \
    --fraud-rate 0.03 \
    --days 30 \
    --seed 42 \
    -o data/us_production.csv \
    --include-disputes \
    --export-institutional-views
```

#### 2. Synthesize Indian Payment Rail Transactions (RBI AFA / RuPay / CoFT)
```bash
# Generates 5,000 Indian transactions with RBI liability tiers and 1930 cyber-liens
python -m fraudx_synthesizer.cli generate \
    -n 5000 \
    --cards 1000 \
    --merchants 150 \
    --region IN \
    --fraud-rate 0.03 \
    --days 30 \
    --seed 42 \
    -o data/india_production.csv \
    --include-disputes \
    --export-institutional-views
```

### Python API

```python
from fraudx_synthesizer import SimulationEngine

# Initialize simulation engine for Indian payment ecosystem
engine = SimulationEngine(
    n_cards=500,
    n_merchants=100,
    region="IN",
    seed=42,
)

# Generate batch of 1,000 transactions
records = engine.generate_batch(
    n_transactions=1000,
    fraud_prevalence=0.04,
    time_span_days=14,
)

print(f"Synthesized {len(records)} transactions.")
sample = records[0]
print(f"TX ID: {sample['transaction_id']} | MTI: {sample['mti']} | ISO Field 39: {sample['response_code']}")
print(f"Amount: {sample['amount']} {sample['currency']} (Minor Units: {sample['amount_minor']})")
print(f"Dominant Causal Driver: {sample['dominant_causal_driver']}")
```

### Benchmarking an XAI Model Against Ground Truth

```python
import numpy as np
from fraudx_synthesizer import GroundTruthXAIEvaluator

evaluator = GroundTruthXAIEvaluator()

# Ground truth Shapley vector from StructuralCausalEngine
phi_true = np.array([0.45, 0.30, 0.15, 0.05, 0.05])

# Attribution vector predicted by a black-box explainer (e.g. KernelSHAP)
phi_pred = np.array([0.40, 0.35, 0.10, 0.08, 0.07])

# Evaluate fidelity metrics
metrics = evaluator.evaluate_explanation(
    phi_true=phi_true,
    phi_pred=phi_pred,
    feature_names=["velocity", "amount_ratio", "geo_risk", "hour", "mcc"],
    top_k=3,
)

print(f"Top-3 Precision: {metrics['precision_at_k']:.3f}")
print(f"Kendall Tau Rank Correlation: {metrics['kendall_tau']:.3f}")
print(f"Relative Attribution Error (RAE): {metrics['relative_attribution_error']:.3f}")
```

---

## Repository Structure

```
FraudxAI/
├── fraudx_synthesizer/              # Core Simulation & Causal Benchmark Engine
│   ├── agents.py                   # Cardholders, Adaptive Fraudsters & Bank Decision Engine
│   ├── causal_scm.py               # Structural Causal Model & Analytical Shapley Decomposition
│   ├── cli.py                      # Production CLI supporting dual regions & feed exports
│   ├── engine.py                   # Monotonic Priority Queue Discrete-Event Engine
│   ├── evaluation.py               # GroundTruthXAIEvaluator (Precision@k, Kendall Tau, RAE)
│   ├── invariants.py               # Antipodal Haversine kinematics & monetary conservation
│   ├── ledger.py                   # StreamingLedger with point-in-time Welford tracking
│   └── world.py                    # Spatial merchant topologies & MCC taxonomies
├── spec/                           # Grounded Living Specifications (Single Source of Truth)
│   ├── 01_financial_instruments.yaml # 11 Global + 5 Indian card product definitions
│   ├── 02_human_personas.yaml       # 7 Fed DCPC cohorts & circadian arrival simplexes
│   ├── 03_payment_rail_gaps.yaml    # AFD holds, tip tolerances, STIP, AVS, Visa CE 3.0
│   ├── 04_adversarial_playbooks.yaml# 10 Grounded cybercrime attack playbooks
│   ├── 05_india_payment_rails.yaml  # RBI AFA, RuPay on UPI, CoFT, and 1930 cyber-liens
│   └── research_notes/              # Subagent census dossiers citing official manuals
├── scripts/
│   ├── verify_grounded_invariants.py # 37-Scenario Grounded Verification Engine
│   └── inspect_generated_data.py    # Statistical inspection of synthesized batches
├── tests/                           # Deterministic Automated PyTest Suite
│   └── test_synthesizer/            # 39 Unit tests certifying all engine invariants
├── AGENTS.md                        # Anti-Astronaut Grounding Mandate
└── pyproject.toml
```

---

## Verification & Test Results

FraudxAI enforces strict, deterministic verification across the entire stack:

### 1. PyTest Unit & Integration Suite (39 / 39 Passed)
```bash
python -m pytest tests/ -v
```
Certifies:
* Analytical Shapley efficiency in probability and log-odds spaces.
* Geodesic antipodal stability and sub-mach commercial velocity limits.
* Closed-loop multi-agent feedback (ISO 51 amount decay, 3DS gateway hopping, card freezes).
* Strict global temporal monotonicity under concurrent microsecond arrivals.
* Zero deterministic target label leakage in AVS and billing/shipping fields.
* Dual-region institutional schema conformance (USD cents vs. INR paisa, ISO 8583 syntax, MTI 0200 clearing presentment, Visa CE 3.0 deflection, RBI limited liability tiers).

### 2. Grounded 37-Scenario Invariant Verification (100% Passed)
```bash
python scripts/verify_grounded_invariants.py
```
Validates 37 formal operational scenarios across:
* **Part A (Adversarial Playbooks)**: Micro-auth probing, 14-day silent ATO baking, sleeper bust-outs, Apple Pay yellow-path tokenization, nocturnal sleep suppression, reverse-proxy vishing, and APK SMS stealers.
* **Part B (Payment Rail Plumbing)**: AFD \$175 pre-auth nozzle cutoffs, hotel incidental folios, dining 20% tip adjustments, STIP 2.0s SLA outages, AVS matrix adjudication, and India ₹5,000 contactless limits.
* **Part C (Consumer Dynamics & Quirks)**: Dhanteras gold splitting (Rule 114B ₹2L cap), fuel surcharge waivers, no-cost EMI discounts, forgotten subscription churn, and multi-modal discovery latencies.
* **Part D (Merchant Risk & Disputes)**: PEA additive guessing, triangulation fraud multipliers, Visa CE 3.0 pre-dispute deflection, \$500 network arbitration veto, RBI Circular `RBI/2017-18/15` limited liability tiers, and CFCFRMS Helpline 1930 golden hour races.

---

## Grounding Mandate (Anti-Astronaut Policy)

This repository adheres strictly to the **Anti-Astronaut Grounding Mandate** codified in [`AGENTS.md`](AGENTS.md):
1. **Zero Theoretical Buzzwords**: No speculative, non-implementable concepts (no quantum computing, neuromorphic hardware, or zero-knowledge rollups unless backed by executable Python code).
2. **Physical & Financial Units**: Every parameter has concrete units (USD cents, INR paisa, seconds, km/h, probabilities in $[0.0, 1.0]$).
3. **Real-World Banking Plumbing**: Models reflect actual payment networks, ISO 8583 response codes, AVS matrices, 3DS 2.x rules, and statutory circulars.
4. **Specification-First Lifecycle**: `spec/` $\to$ Deterministic Tests $\to$ Minimal Implementation $\to$ Raw Data Inspection.

---

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.
