# Pillar 1 scored against real payment data

**Status:** measurement, not a certification. **Date:** 2026-10-10. **Region graded against:** US (spec/09 reference).

## Why this was run

Pillar 1 of the certification grader (`spec/18_benchmark_reporting.yaml`) compares our
synthetic stream against reference distributions taken from payment-rail sources. The
benchmark currently reports `NON_CERTIFIED_FAIL`, with pillar 1 among the failing
pillars. A failing grade has two possible causes the report cannot tell apart:

1. our generator is off, or
2. the reference does not describe real card traffic either.

`scripts/score_external_corpus.py` runs the **grader's own function**
(`UnifiedBenchmarkRunner._evaluate_data_fidelity`) on other corpora, so every row in the
table below is produced by identical code against thresholds read from `spec/18`. The
only thing that differs between columns is the data.

## Command

```bash
python scripts/score_external_corpus.py \
  --reference-control 1500 \
  --synthetic 1500 --synthetic 50000 \
  --ulb /tmp/opencode/corpora/creditcard.arff \
  --ulb-legit /tmp/opencode/corpora/creditcard.arff \
  --csv /tmp/opencode/corpora/banksim.csv --amount-col amount --time-col step \
       --time-unit hours --label-col fraud \
  --json /tmp/opencode/pillar1_scorecard.json
```

## Corpora

| column | what it is | source | sha256 |
|---|---|---|---|
| FraudxAI synthetic | this repo's engine, seed 42, `fraud_prevalence=0.07` | `fraudx_synthesizer.engine.SimulationEngine` | n/a (generated) |
| ULB real | 284,807 real European card transactions, 2 days, 0.1727% flagged fraud | OpenML dataset 1597, file 1673544 (`https://openml.org/data/v1/download/1673544/creditcard.arff`) | `fdaf12730dc1fc426f318b71349f24f5c5fd00aa1152940be7e7509ae3d89d2a` |
| BankSim | 594,643 rows from a competing agent-based simulator (López-Rojas et al.), calibrated on a Spanish bank's aggregates | `https://raw.githubusercontent.com/atavci/fraud-detection-on-banksim-data/master/Data/synthetic-data-from-a-financial-payment-system/bs140513_032310.csv` | `e37006f76d993bfaec3a02d717b4f0bdc1ebfa5d36449e91fb7c07e225278377` |
| reference-sampler control | **not a generator**: amounts and inter-arrivals drawn from the reference itself | this script | n/a |

Both downloads were unauthenticated; no account was used.

## Results

| metric | limit | control n=1,500 | ours n=1,500 | ours n=50,000 | ULB real (all) | ULB real (legit) | BankSim |
|---|---|---|---|---|---|---|---|
| log10(1+amount) Wasserstein | ≤ 0.150 | 0.0000 **PASS** | 0.1508 FAIL | 0.1525 FAIL | **0.3745 FAIL** | 0.3740 FAIL | 0.2649 FAIL |
| log10(1+Δt seconds) Wasserstein | ≤ 0.150 | 0.0016 **PASS** | 0.2295 FAIL | 0.1161 **PASS** | 0.1716 FAIL | 0.1715 FAIL | 3.2941 FAIL |
| MCC Jensen-Shannon | ≤ 0.050 | n/a | 0.0747 FAIL | 0.0869 FAIL | n/a | n/a | n/a |
| channel Jensen-Shannon | ≤ 0.050 | n/a | 0.0131 **PASS** | 0.0707 FAIL | n/a | n/a | n/a |
| correlation Frobenius error | ≤ 1.250 | n/a | 0.0808 **PASS** | 0.0892 **PASS** | n/a | n/a | n/a |
| **verdict** (comparable metrics) | | **PASS** | **FAIL** | **FAIL** | **FAIL** | **FAIL** | **FAIL** |

Corpus detail as printed by the run:

| corpus | n | span | median amount | dt_min | dt_med |
|---|---|---|---|---|---|
| ours n=1,500 | 1,500 | 10.39 d | 30.33 USD | 0.3 s | 228.53 s |
| ours n=50,000 | 50,000 | 51.75 d | 37.82 USD | 0.01 s | 45.91 s |
| ULB real (all) | 284,807 | 2.00 d | 22.00 EUR | 1 s | 1 s |
| BankSim | 594,643 | 7.46 d | 26.90 (currency unlabelled) | **3600 s** | **3600 s** |
| reference-sampler control | 1,500 | 12.00 d | 42.65 USD | 0.13 s | 496.56 s |

`n/a` = the corpus does not carry that metric's inputs, so the metric is excluded from
the verdict instead of being scored on the grader's per-row defaults (`mcc` → 5411,
`pos_entry_mode` → "01", correlation columns → 0.0, each of which makes its own metric
trivially 0).

## What the numbers say

1. **Real data fails the amount gate, and fails it worse than we do.** ULB scores
   0.3745 against a 0.150 limit — 2.5× our 0.1508. Dropping ULB's fraud rows changes
   nothing (0.3740), so it is not fraud enrichment. The gate measures distance to the
   hardcoded `lognormal(mu=3.75, sigma=0.85)` USD reference, and on this corpus real
   card amounts are not that distribution: ULB's median is 22 against the reference's
   42.65, with a heavier right tail.

2. **The gate is gameable by construction.** The control draws straight from the
   reference and scores 0.0000 / 0.0016 → PASS, while being nothing like card traffic.
   Distance to the reference is therefore not evidence of realism.

3. **The inter-arrival gate conflates arrival shape with clock resolution.** BankSim's
   3.2941 is dominated by its hourly `step` (dt_min = dt_med = 3600 s), not by its
   arrival process; ULB's timestamps are whole seconds and its median Δt is 1 s, so the
   grader's `Δt > 0` filter drops every same-second pair and biases its score upward;
   our own Δt floor is 0.01–0.3 s. Three corpora, three clocks — the number is not
   comparable across them without the dt_min column.

4. **Sample size moves the verdicts at the grader's default n=1,500.** Our
   inter-arrival score goes 0.2295 (FAIL) → 0.1161 (PASS) at n=50,000, and channel JSD
   goes 0.0131 (PASS) → 0.0707 (FAIL): the JSD gates compare against a *uniform*
   distribution and are biased downward for small samples, so small runs are graded
   easier. The amount score is stable (0.1508 → 0.1525).

5. **Two gates cannot be run on any corpus but our own.** MCC and channel JSD are
   distances to uniform over the categories we emit; neither ULB nor BankSim carries
   MCC or POS-entry-mode codes, and the Frobenius gate needs our own five feature
   columns (`tx_count_1h`, `haversine_velocity_kph`, …). Those three gates are
   self-referential to our schema — they can fail us, but no external data can
   validate them.

## What this does and does not establish

**Does:** pillar 1's continuous gates do not rank data by resemblance to real
transactions. On the only real corpus obtainable without an account, real transactions
fail the amount gate harder than our synthetic output, and a sampler of the reference
passes trivially. Closing pillar 1 by tuning the generator to the reference would move
the generator *away* from this real corpus.

**Does not:** that the reference itself is wrong. ULB is one European bank's 2-day,
fraud-flagged, EUR-denominated extract and BankSim is calibrated on a Spanish bank;
neither is the Federal Reserve's US card population, so "real data fails" is
directional, not conclusive. It also says nothing about pillars 2–4: the pillar 4
relative-attribution-error failure is an internal-consistency result and is untouched
by this measurement.

**Not measured here:** pillar 1's remaining gates on external data (impossible for the
reasons in finding 5), and any corpus behind Kaggle authentication — IEEE-CIS would be
the natural second real corpus and needs an API key.

## Proposed next step (a decision for the slice owner, not taken here)

Re-derive pillar 1 against a real corpus instead of a hardcoded lognormal: grade
generators on distance-to-real (with the same clock and sample size on both sides),
keep a size-corrected statistic, and record the reference corpus and its hash in
`spec/18` the way thresholds are already recorded there. Until then, pillar 1's FAIL
should be read as "differs from the Fed lognormal", not "less realistic than real
data".
