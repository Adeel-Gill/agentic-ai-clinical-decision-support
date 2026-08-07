# Pilot Feasibility Study — MIMIC-IV Demo (v2.2)

**Run date:** 2026-08-07 · **Code:** `05_Source_Code/src/acdss/pilot/` ·
**Data:** MIMIC-IV Clinical Database Demo v2.2 (PhysioNet, Open Data license — 100 patients,
140 ICU stays). Data files are NOT stored in this repository (see `03_Dataset/README.md`);
only aggregate metrics are committed (`pilot_metrics.json`).

**Purpose.** Exercise the non-LLM slice of the proposed framework on real (demo) ICU data:
timeline construction (memory layer), timestamp-aware retrieval, a classical early-warning
baseline to generate an alert stream, and the rule-based verification gate with a *measured*
audit trail. This is feasibility evidence, not a performance claim: n = 140 stays, 20 deaths.

To reproduce:

```bash
cd 05_Source_Code/src
python -m acdss.pilot.run_pilot --data <demo_root> --out ../../06_Experiments/results/pilot
```

## Results

### Timeline construction (memory layer)
| Metric | Value |
|---|---|
| ICU stays | 140 |
| Total construction time | 2.9 s (all stays) |
| Events per stay (median, IQR) | 438 (236–798) |
| Event mix | 75% vitals, 17% meds, 7% labs, prior admissions |
| Stays with ≥1 prior admission in timeline | 60/140 (43%) |

### Timestamp-aware retrieval (at 24 h after ICU admission, k = 10)
| Metric | Value |
|---|---|
| Query latency (median / p95) | 11.7 ms / 17.9 ms |
| Stays returning full k results | 100% |
| Stays with ≥1 deterioration-relevant abnormal signal | 138/140 |
| Distinct abnormal signals per stay (median) | see `pilot_metrics.json` |

### Early-warning baseline (first-24 h features → in-hospital mortality)
Logistic regression, 5-fold stratified CV, 23 features.
| Metric | Value |
|---|---|
| AUROC (cross-validated) | 0.641 |
| 95% bootstrap CI | 0.478 – 0.792 |
| Alerts raised (top 20% risk) | 28 (7 true positive, 21 false positive) |

The confidence interval crosses 0.5 — expected at n = 140 with 20 events; the baseline exists
to generate a realistic alert stream for the gate experiment, not to claim predictive skill.

### Verification gate (distinct deterioration signals in the 6 h before decision)
| Min. distinct signals | Pass rate, true alerts | Pass rate, false alerts | Blocked |
|---|---|---|---|
| 1 | 0.57 | 0.90 | 5/28 |
| 2 | 0.57 | 0.67 | 10/28 |
| 3 | 0.57 | 0.48 | 14/28 |
| **4** | **0.43** | **0.14** | 22/28 |
| 5 | 0.43 | 0.10 | 23/28 |
| 6 | 0.14 | 0.05 | 26/28 |

From ≥3 required signals onward the gate blocks false alerts at a higher rate than true
alerts (at m = 4: 86% of false alerts blocked vs 57% of true alerts retained). Note the
honest caveat visible at m = 1: three of seven true alerts had *no* recent abnormal signal in
the 6 h window, so evidence-gating imposes a sensitivity floor — the gate trades sensitivity
for specificity, and the window length is a tunable safety parameter.

### Audit trail (measured, not assumed)
| Metric | Value |
|---|---|
| Evidence references logged | 183 |
| References re-resolved against raw tables (source, row, timestamp, label) | 183 |
| **Trail resolvability** | **1.00** |

## Interpretation

1. **Feasibility established** for the memory and retrieval layers on real ICU data:
   construction is fast, retrieval is interactive-latency and never returns future data.
2. **The verification-gate mechanism behaves as designed** — requiring a concordant,
   recent, multi-signal evidence picture preferentially suppresses unsupported alerts.
3. **Audit-trail faithfulness can be measured**, and in this deterministic pilot it is
   perfect by construction; the LLM-based system will make this metric non-trivial, which
   is exactly why the framework treats it as an evaluation target.
4. **Limits:** 100-patient demo cohort, single site, no clinical notes module, no LLM in the
   loop, mortality as a proxy endpoint. Nothing here supports deployment claims; the full
   credentialed MIMIC-IV evaluation (Chapter 4) remains the substantive test.
