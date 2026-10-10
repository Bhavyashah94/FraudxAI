# Certification Grade Stability Across Runs

**Measured:** 2026-10-10 · **Commit:** `9895834` (pre-slice-23) for the sweep, plus the
pinning work described below · **Command:** `fraudx benchmark --unified` · **Verdict in every
one of 17 runs:** `NON_CERTIFIED_FAIL`

## What this report answers

The four-pillar benchmark reported **4 violations** on one invocation and **9** on another
from what looked like the same command. This report establishes, with numbers read from
stored `benchmark_results.json` files rather than remembered, why that happened and what
was changed so it cannot be mistaken again.

All counts below are printed by `scripts/report_grade_stability.py`, not transcribed:

```bash
.venv/bin/python scripts/report_grade_stability.py <each stored benchmark_results.json>
```

## Finding 1 — the grader itself is deterministic

Re-invoking the identical configuration produced byte-identical results in every group:

| configuration | independent invocations | verdict |
|---|---|---|
| `-n 400 --seed 42` | 3 | IDENTICAL (4 violations, 3 test days, PR-AUC 0.2120) |
| `-n 1000 --seed 42` | 2 | IDENTICAL (4 violations, 3 test days, PR-AUC 0.2614) |
| `-n 2000 --seed 42` | 3 | IDENTICAL (6 violations, 5 test days, PR-AUC 0.1273) |

So the spread is **not** a race, an unseeded RNG, or a floating-point difference. It is the
input the caller chose.

## Finding 2 — `spec/18` pinned the thresholds but not the run they were applied to

Before this slice, `spec/18_benchmark_reporting.yaml` contained the gate limits and nothing
about *which* run to grade: no sample size, no seed, no region, no stream length. `-n` was
therefore whatever the operator typed, and the README documented a different command
entirely (`fraudx benchmark -n 2000 --model lightgbm --seed 42`, the XAI-only harness, with
`--unified` never mentioned).

Across the 17 stored runs:

- violation counts: **4 to 9** (`4,4,4,4,4,4,4,5,5,6,6,6,6,6,6,8,9`)
- grades: `NON_CERTIFIED_FAIL x17`

The grade itself never moved — every run had at least three solid violations — but the
*violation count*, which is what gets quoted in prose, varied by a factor of two.

## Finding 3 — the gates that flip sit on very small denominators

| quantity | across the 17 runs | threshold |
|---|---|---|
| streaming test days evaluated | **2 – 8** | `min_days_evaluated: 2` (already in `spec/18`) |
| mean prequential PR-AUC | 0.0417 – 0.2614 | 0.1500 minimum |
| macro evasion rate (mean over attack sims) | 0.500 – 0.833 | pillar-2 maximum |

A gate evaluated on 2 test days, or on a handful of attack simulations, moves by large steps.
PR-AUC straddles its 0.1500 floor across the sweep, which is exactly why it flips.

## The tables

Produced by `scripts/report_grade_stability.py` over every stored run on disk:

| run | n | seed | violations | streaming test days | mean PR-AUC |
|---|---|---|---|---|---|
| `bench_check` | 400 | 42 | 4 | 3 | 0.2120 |
| `bench_dcr` | 1000 | 42 | 4 | 3 | 0.2614 |
| `bench_final` | 400 | 42 | 4 | 3 | 0.2120 |
| `bench_new` | 1000 | 42 | 4 | 3 | 0.2614 |
| `dig/bench_n2000` | 2000 | 42 | 6 | 5 | 0.1273 |
| `dig/bench_n400` | 400 | 42 | 4 | 3 | 0.2120 |
| `dig/seeds/n2000_s0` | 2000 | 0 | 6 | 7 | 0.1372 |
| `dig/seeds/n2000_s1` | 2000 | 1 | 9 | 8 | 0.1071 |
| `dig/seeds/n2000_s2` | 2000 | 2 | 5 | 8 | 0.0989 |
| `dig/seeds/n2000_s3` | 2000 | 3 | 4 | 6 | 0.1834 |
| `dig/seeds/n500_s0` | 500 | 0 | 6 | 3 | 0.1509 |
| `dig/seeds/n500_s1` | 500 | 1 | 6 | 2 | 0.0556 |
| `dig/seeds/n500_s2` | 500 | 2 | 4 | 2 | 0.1235 |
| `dig/seeds/n500_s3` | 500 | 3 | 5 | 4 | 0.2500 |
| `publish/bench_for_card` | 500 | 42 | 8 | 3 | 0.0417 |
| `stab/cr` *(after the pin)* | 2000 | 42 | 6 | 5 | 0.1273 |
| `stab/run1` *(after the pin)* | 2000 | 42 | 6 | 5 | 0.1273 |

*Paths abbreviated to their directory names; the script prints the full path. The `stab/*`
rows were run after `spec/18` gained the protocol block and reproduce the pre-pin
`n=2000 --seed 42` row exactly, so pinning changed no measurement.*

### Per-gate failures across those runs

| gate | failed in | reading |
|---|---|---|
| Pillar 1 (Data Fidelity): MCC Jensen-Shannon divergence | 17/17 | always |
| Pillar 1 (Data Fidelity): inter-arrival Wasserstein | 17/17 | always |
| Pillar 4 (Causal XAI Fidelity): relative attribution error | 17/17 | always |
| Pillar 1 (Data Fidelity): log-amount Wasserstein | 12/17 | FLIPS |
| Pillar 3 (Operational Streaming): prequential PR-AUC | 9/17 | FLIPS |
| Pillar 4 (Causal XAI Fidelity): Pearson linear r | 6/17 | FLIPS |
| Pillar 2 (Privacy & Robustness): macro evasion rate | 5/17 | FLIPS |
| Pillar 3 (Operational Streaming): net cost savings ratio | 4/17 | FLIPS |
| Pillar 3 (Operational Streaming): alert precision P@K | 3/17 | FLIPS |
| Pillar 2 (Privacy & Robustness): shadow MIA ROC-AUC | 1/17 | FLIPS |

**7 of 10 failing gates flip between runs.** Three are solid: inter-arrival Wasserstein,
MCC Jensen-Shannon divergence and relative attribution error failed every single run.

## What changed

1. **`spec/18` gained `evaluation_protocol` (§4)** — pins region, `n_transactions: 2000`,
   `seed: 42`, stream length, the four streaming window parameters, and
   `stability_seeds: [42, 0, 1, 2, 3]`. `n` and `seed` come from the command the README
   already documented; the window parameters are the grader's as-run defaults.
2. **The report records the protocol it was graded under.** `benchmark_results.json` now
   carries `pinned_protocol`, `run_protocol` and `protocol_mismatches`; a deviating run is
   marked **OFF-PROTOCOL** in the Markdown and HTML reports, with each deviation named, so
   its violation count cannot be presented as the pinned one.
3. **On-protocol runs publish a per-gate stability table instead of a single count**, by
   re-running every pinned seed (≈3 s each). Measured under the pin, across seeds
   `42, 0, 1, 2, 3` at `n=2000`:

   ```
   | gate                                                                        | failed in | reading         |
   | Pillar 1 (Data Fidelity): MCC Jensen-Shannon divergence # exceeds the maximum | 5/5     | solid failure   |
   | Pillar 1 (Data Fidelity): inter-arrival Wasserstein # exceeds the maximum    | 5/5     | solid failure   |
   | Pillar 4 (Causal XAI Fidelity): relative attribution error # exceeds the max | 5/5     | solid failure   |
   | Pillar 3 (Operational Streaming): prequential PR-AUC # falls below the min   | 4/5     | FLIPS WITH SEED |
   | Pillar 1 (Data Fidelity): log-amount Wasserstein # exceeds the maximum       | 3/5     | FLIPS WITH SEED |
   | Pillar 2 (Privacy & Robustness): macro evasion rate # exceeds the maximum    | 3/5     | FLIPS WITH SEED |
   | Pillar 4 (Causal XAI Fidelity): Pearson linear r # falls below the minimum   | 3/5     | FLIPS WITH SEED |
   | Pillar 3 (Operational Streaming): alert precision P@K # falls below the min  | 1/5     | FLIPS WITH SEED |
   | Pillar 3 (Operational Streaming): net cost savings ratio # falls below the m | 1/5     | FLIPS WITH SEED |
   ```

   Grades: `NON_CERTIFIED_FAIL x5`; violation counts 4–9; **the grade is stable across
   seeds**, the count is not.
4. **README documents the certification command** (`fraudx benchmark -n 2000 --unified
   --seed 42`) and says which numbers come from which invocation.

## Reproducing this

```bash
# the pinned certification run: one grade plus the 5-seed stability table
.venv/bin/python -m fraudx_synthesizer.cli benchmark -n 2000 --unified --seed 42 \
  --output-dir reports/benchmark

# the exploratory sweep behind the 4-9 range (the stored runs are a subset of this)
for n in 400 500 1000 2000; do for s in 42 0 1 2 3; do
  .venv/bin/python -m fraudx_synthesizer.cli benchmark -n "$n" --unified --seed "$s" \
    --output-dir "/tmp/grade-sweep/n${n}_s${s}" >/dev/null 2>&1
done; done

# every table in this report
.venv/bin/python scripts/report_grade_stability.py /tmp/grade-sweep/**/benchmark_results.json
```

The stored runs behind the tables above lived in a scratch directory and are not committed;
the tables are the record of them, and the loop regenerates an equivalent sweep.

## Not fixed, deliberately

- **The grade is still `NON_CERTIFIED_FAIL`.** Nothing here makes a failing gate pass; it
  makes *which* gates fail, and how reliably, visible.
- **The streaming floor is still `min_days_evaluated: 2`,** and observed test days are 2–8.
  Raising the floor alone would make pillar 3 fail on every run, because the pinned 12-day
  stream cannot produce more than ~8 test days. Doing this honestly means lengthening the
  stream first and re-measuring every pillar — a separate slice, not a number changed here.
- **`spec/17` disagrees with the grader's windows** (`default_w_train_days 30.0`,
  `default_delta_delay_days 14.0`, `default_k_daily 50` versus the as-run 3.0 / 1.5 / 15).
  A 30-day training window cannot run on a 12-day stream, so adopting `spec/17` requires the
  same stream-lengthening work. The conflict is recorded in `spec/18` §4 as an open
  divergence; neither side was silently changed to match the other.
