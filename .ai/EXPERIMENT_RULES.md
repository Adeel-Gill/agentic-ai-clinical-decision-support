# EXPERIMENT RULES

Governs `06_Experiments/`, Chapter 4, and every reported number.

---

## 1. Never invent results

If results do not exist, write the marker — not a plausible number, not a "representative
value", not an "illustrative example".

```
TODO: RUN EXPERIMENT            ← designed, never executed
TODO: EVALUATE IMPLEMENTATION   ← code exists, no evaluation run
```

`06_Experiments/README.md` states it plainly: **planned, not yet run**. The only real numbers in
this repository come from the pilot on the open MIMIC-IV demo.

## 2. Every experiment carries eleven elements

An experiment description is incomplete without all of these:

1. **Objective** — what question it settles
2. **Hypothesis or research question** — directional, with the null a negative result confirms
3. **Dataset** — which cohort, which split, which manifest
4. **Inputs** — what each configuration receives
5. **Methodology** — the procedure, reproducibly
6. **Baseline** — what it is compared against
7. **Metrics** — defined in `Evaluation_Metrics.md`
8. **Configuration** — model, prompt version, retrieval sources, active agents, seeds
9. **Results** — or the marker
10. **Interpretation** — what it means, including what it does not mean
11. **Limitations** — construct, internal, external validity

## 3. The baseline ladder

Each rung adds exactly one capability, so gaps isolate contributions. Do not reorder or merge.

| Config | Retrieval | Multi-agent | Verification | Memory | Coordinator | Isolates |
|---|---|---|---|---|---|---|
| **B0** single LLM zero-shot | none | no | no | no | — | accuracy floor |
| **B1** LLM + guideline RAG | guidelines | no | no | no | — | value of retrieval (RQ4) |
| **B2** MedAgents-style | guidelines | yes | **no** | no | flat | value of multi-agent reasoning (RQ2/RQ3) |
| **B3** full framework | guidelines + **patient timeline** | yes | yes | yes | orchestrated | verification + remaining components |
| **CLIN** logistic regression | structured features | — | — | — | — | strong cheap risk baseline |
| **CLIN-SOFA** severity score | — | — | — | — | — | clinical risk comparator [vincent1996sofa] |

CLIN and CLIN-SOFA apply to risk tasks T1–T4 only.

The cheap baselines matter most. If B3 does not beat logistic regression on risk discrimination,
that is the finding — report it.

## 4. Ablations — one component removed from B3

| Config | Change | Question |
|---|---|---|
| **A1** −Verification | Verification agent off | Does the safety layer reduce unsafe recommendations? (RQ3) |
| **A2** −patient-timeline RAG | guideline-only retrieval | Does patient-specific grounding change outputs? (RQ4) |
| **A3** −Memory | persistent memory off | Does long-term context help longitudinal tasks? (RQ2) |
| **A4** flat Coordinator | fixed sequence, no delegation | Does orchestration earn its overhead? (RQ2) |

A2 is the ablation that tests the thesis's central novelty claim. If A2 ≈ B3, the claim fails —
and that must be reportable, not designed around.

Every baseline and ablation runs across all applicable tasks. **Component value is reported per
task, never averaged into one headline figure.**

## 5. Tasks

| ID | Task | Type | Reference standard |
|---|---|---|---|
| T1 | In-hospital mortality | Binary | Recorded outcome |
| T2 | ICU transfer / escalation | Binary | Recorded outcome |
| T3 | Sepsis onset | Binary | Sepsis-3 operational definition [singer2016sepsis3] |
| T4 | 30-day readmission | Binary | Recorded outcome |
| T5 | Diagnosis support | Ranked differential | Recorded discharge diagnoses (imperfect) |
| T6 | Treatment recommendation | Open-ended | Guideline concordance + safety rubric + clinician review |
| C1 | MedQA (accuracy control) | Multiple choice | Answer key [jin2021medqa] |

T5's reference standard is acknowledged as noisy — that is why C1 is reported alongside.
Known defect D5: T2 has no matching cohort label; prolonged LOS has no task. Reconcile.

## 6. Pre-registered hypotheses

H1–H10 are confirmatory and corrected together under Benjamini-Hochberg FDR
[benjamini1995controlling]. Each has a directional prediction and a null a negative result
confirms.

| ID | Hypothesis | Comparison | RQ | Primary metric |
|---|---|---|---|---|
| H1 | Guideline retrieval improves grounding over zero-shot | B1 > B0 | RQ4 | Faithfulness |
| H2 | Multi-agent reasoning improves accuracy over single-LLM retrieval | B2 > B1 | RQ2 | Top-k / MRR (T5) |
| H3 | Verification reduces unsafe recommendations | B3 < B2 | RQ3 | Unsafe-rate (T6) |
| H4 | Full framework improves grounding over unverified multi-agent | B3 > B2 | RQ4 | Faithfulness |
| H5 | Framework matches or beats logistic regression on risk | B3 ≥ CLIN | RQ5 | AUROC/AUPRC |
| H6 | Ablating verification raises unsafe-recommendation rate | A1 > B3 | RQ3 | Unsafe-rate (T6) |
| H7 | Patient-timeline retrieval changes/improves outputs | B3 vs A2 | RQ4 | Faithfulness, accuracy |
| H8 | Persistent memory improves longitudinal performance | B3 > A3 | RQ2 | AUROC/AUPRC (T4) |
| H9 | Orchestration improves outcomes over flat coordination (may be null) | B3 vs A4 | RQ2 | Accuracy, latency |
| H10 | Framework produces more complete/better-calibrated trust signals | B3 vs B0–B2 | RQ3 | ECE, audit completeness |

**Pre-registration is binding.** Hypotheses are fixed before running so results cannot be
reverse-engineered afterward. Adding a hypothesis after seeing data makes it **exploratory** —
label it so, report it separately, and give it no confirmatory weight.

H9 is explicitly allowed to be null. Design that admits a null result is stronger than design
that cannot fail.

## 7. Statistical plan

- 95% bootstrap CIs, resampled **over patients** (not predictions), on every headline metric.
- Paired tests on the shared cohort: DeLong for AUROC [delong1988comparing]; McNemar or paired
  bootstrap for classification and faithfulness [dietterich1998approximate].
- Benjamini-Hochberg FDR over the **confirmatory set only**; exploratory p-values reported
  uncorrected and labeled.
- Underpowered comparisons are reported as **"inconclusive at this cohort size"** — never as
  null effects.
- Headline configurations run multiple times; LLM output variability is reported, not hidden.

## 8. Reproduction workflow

1. Obtain credentialed PhysioNet access.
2. Build the cohort once; write the manifest and patient-level splits to `cohort/`. Seeded.
3. Select a configuration from `configs/` (a baseline or ablation).
4. Run over the manifest; write outputs, audit trace, per-case predictions, latency, and cost to
   `results/<config-name>/`.
5. Score with `Evaluation_Metrics.md`. Automated metrics compute directly; the clinician Likert
   study and safety adjudication need the human review step.
6. Analyze: bootstrap CIs, paired tests, FDR over the confirmatory set.

`configs/` and `cohort/` do not exist yet — they are part of the intended layout.

## 9. The pilot: what it is and is not

`06_Experiments/results/pilot/` holds the only real numbers.

**Established:**

| Result | Value |
|---|---|
| ICU stays | 140 (100 patients, MIMIC-IV demo v2.2) |
| Timeline construction | 2.9 s for all stays; median 438 events/stay (IQR 236–798) |
| Retrieval latency at 24 h, k=10 | 11.7 ms median / 17.9 ms p95; 100% returned full k |
| Early-warning baseline | AUROC 0.641, **95% CI 0.478–0.792**, 5-fold CV, 23 features |
| Alerts at top-20% risk | 28 (7 true positive, 21 false positive) |
| Gate at m = 4 | true-alert pass rate 0.43, false-alert pass rate 0.14 → 22/28 blocked |
| Audit trail | 183 evidence references, 183 re-resolved, resolvability **1.00** |

**Not established:** predictive skill (the CI crosses 0.5 — expected at n = 140 with 20 events);
anything about the LLM loop; anything about notes; anything prospective; anything about clinical
benefit.

**Mandatory framing every time the pilot is cited:**

- feasibility-only, n = 140, 20 deaths;
- AUROC always with its CI, never as predictive skill;
- resolvability 1.00 is **expected by construction** in a deterministic pilot — it becomes a
  non-trivial metric only once the LLM is in the loop;
- the **sensitivity floor** is stated: at m = 4 the gate blocked four of seven true alerts, three
  of which had no deterioration-relevant signal in the 6 h window. Evidence-gating trades
  sensitivity for specificity; the window length is a tunable safety parameter that clinical
  governance, not engineering, must set.

## 10. Reporting results

- Report the metric with its uncertainty, always.
- Report n and the denominator.
- Report negative and null results with the same prominence as positive ones.
- Report the pre-registered hypothesis each result addresses.
- Report cost and latency alongside accuracy — a configuration that improves faithfulness at
  many times the cost of B1 may be clinically impractical.
- Never average across tasks to produce a single flattering number.
- Cross-check any repeated figure against `pilot_metrics.json`, the source of record.
