# FraudxAI Living Specification (`spec/`)

This directory is the **canonical Single Source of Truth (SSOT)** for the FraudxAI simulation platform.

## Purpose
To eliminate the gap between high-level research and executable reality, all domain knowledge (banking rules, human psychology, merchant friction, and fraudster playbooks) must be codified into typed specifications here **before** being implemented in code.

## Structure
- [`active_slice.yaml`](file:///c:/Users/bhavy/Documents/Projects/FraudxAI/spec/active_slice.yaml): The operational focus tracker. Read first in any session.
- `01_financial_instruments.yaml`: Card product tiers (Subprime, Prime, Ultra-High-Net-Worth, Corporate P-Cards, Debit, Virtual), limits, auth flows, and rail vulnerabilities.
- `02_human_personas.yaml`: Human lifestyle archetypes, circadian rhythms, notification fatigue, discovery latencies, and life quirks.
- `03_payment_rail_gaps.yaml`: Payment plumbing details (ISO 8583 codes, STIP, AVS, 3DS exemptions, dual-message settlement).
- `04_adversarial_playbooks.yaml`: Cybercrime playbooks (card testing, ATO baking, bust-out, BIN attacks, amount decay).

## Rules of Engagement
1. **Never write code without a spec.**
2. **Never put concepts in a spec that cannot run in Python/NumPy.**
3. **Every spec item must have test verification in `tests/`.**
