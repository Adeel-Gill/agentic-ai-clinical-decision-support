# EVALUATION RULES

Metric definitions and reporting discipline. The authoritative source is
`06_Experiments/Evaluation_Metrics.md`; this file states the rules that govern its use.

---

## 1. Every metric must be recomputable

A metric is only admissible if it is defined precisely enough to be recomputed from a run's
output artifacts. Formula, tooling, and the exact aggregation unit must all be stated.

## 2. The metric grid

| Dimension | Metric | Tasks | RQ |
|---|---|---|---|
| Task accuracy | Top-k accuracy (k = 1, 3, 5), MRR; MedQA accuracy | T5; C1 | RQ1, RQ2 |
| Factual grounding | Faithfulness, RAGAS-style [es2024ragas] | T5, T6, C1 | RQ4 |
| Risk prediction | AUROC, AUPRC | T1–T4 | RQ5 |
| Safety | Unsafe-recommendation rate, pre/post verification | T6 | RQ3 |
| Explainability | Clinician Likert (faithfulness, usefulness), n = 3–5 | T5, T6 | RQ3 |
| Trustworthiness | ECE [guo2017calibration]; audit-log completeness | T1–T4; all | RQ3, RQ4 |
| Runtime | End-to-end latency (median, IQR, **p95**); cost per case | all | RQ2, RQ5 |

Runtime is a **first-class outcome**, not an afterthought — a configuration that is accurate but
slow and expensive may be clinically impractical.

## 3. Metric caveats that must travel with the number

Each of these is a construct-validity limitation recorded in `Evaluation_Metrics.md`. Reporting
the metric without its caveat is misleading.

| Metric | Caveat |
|---|---|
| **Faithfulness** | Rewards claims grounded in retrieved evidence **even when that evidence is wrong**. Always report next to task accuracy, never alone. |
| **Top-k accuracy (T5)** | Reference standard is recorded discharge diagnoses — imperfect. This is why MedQA (C1) is reported alongside. |
| **AUROC** | Flatters models on imbalanced data. AUPRC is reported explicitly, with the no-skill baseline (= positive prevalence) for context. |
| **Unsafe-recommendation rate** | The rubric shares failure modes with the LLM judge. An LLM pre-screen may triage, but must not decide the final label. |
| **Clinician Likert** | n = 3–5 is indicative only. It can surface gross differences and qualitative problems; it cannot support strong quantitative claims. Report inter-rater agreement (Krippendorff's α or weighted κ) [hayes2007krippendorff]. |
| **ECE** | Always accompanied by a reliability diagram. A confidence score that does not track true probability is dangerous regardless of AUROC. |
| **Audit-log completeness** | Automated schema check against a required-fields spec. In a deterministic pipeline it is near-trivially 1.00 — it becomes informative only with the LLM in the loop. |

## 4. LLM-as-judge rules

Faithfulness scoring uses an LLM judge for claim decomposition and entailment. Constraints:

- The judge follows a **fixed rubric**, versioned with the run.
- A **human spot-check subsample** validates the judge — always.
- The judge is never the sole arbiter of a safety label.
- Judge model and prompt version are pinned and reported; changing either starts a new result set.
- Judge failure modes (position bias, verbosity bias) are acknowledged. The pattern to follow is
  CliCARE's expert-validated ensemble with randomized presentation order and correlation against
  clinicians [li2026clicare].

## 5. Aggregation unit

- Bootstrap **over patients**, not over predictions — within-patient correlation is real.
- Splits are patient-level.
- A per-case metric averaged over cases is not the same as a per-patient metric; say which.

## 6. Reporting standards

Every reported number carries:

1. its **uncertainty** (CI, IQR, or explicit "point estimate, no CI computed");
2. its **n** and denominator;
3. its **configuration** (which baseline/ablation, which model version, which seed);
4. its **task** — never averaged across tasks into one headline;
5. its **hypothesis**, if confirmatory.

Forbidden:

- a metric without n;
- "significantly improves" without a test;
- selective reporting of the tasks where the framework wins;
- rounding a number differently in two places;
- averaging away a per-task result to produce a better-looking figure.

## 7. Negative and null results

Report them with the same prominence as positive ones. H9 (orchestration vs flat coordination) is
pre-registered as possibly null. If A2 (−patient-timeline RAG) matches B3, the thesis's central
claim is not supported — and the correct action is to report that, analyze why, and revise the
claim. `paper/04_Discussion.md` already commits to this: *"If the ablations show these components
do not improve grounded decision quality, the framework's thesis fails honestly."*

## 8. Safety evaluation is not optional

The quantity of interest for the Verification Agent is the **pre → post reduction**:

Δ_safety = Unsafe_pre − Unsafe_post

Report both the pre- and post-verification rate, not just the difference. And report the cost of
the reduction: the pilot showed evidence-gating imposes a **sensitivity floor**. Any gate
operating point must be reported with sensitivity alongside false-alert suppression, so the
trade-off is chosen deliberately rather than inherited from a default.

Suppression must never be silent. Blocked alerts remain visible and overridable in a dedicated
queue — the gate defers to clinical judgment, it does not replace it.

## 9. Benchmarks and comparators

| System | Capability | Covered by this evaluation? |
|---|---|---|
| AgentClinic [schmidgall2024agentclinic] | Interactive diagnostic dialogue in simulation | No — static snapshots only |
| EHRAgent [shi2024ehragent] | Code-generating queries over structured EHR | Partially |
| AMIE [tu2025amie] | Clinician-comparison dialogue at scale | No — out of scope/resourcing |
| MedAgentBench [jiang2025medagentbench] | FHIR-shaped task success | Comparator added post-proposal |
| HealthBench [arora2025healthbench] | Rubric grading of recommendation quality | Comparator added post-proposal |
| Revisited MIMIC-IV [lovon2025mimic] | One-shot prediction baselines | Comparator added post-proposal |

Stating what is **not** covered is part of the evaluation design, not an admission of weakness.

## 10. Threats to validity

Every results chapter names them explicitly, in three groups:

- **Internal** — reference-standard noise (T5), judge–rubric shared failure modes, LLM
  nondeterminism, cohort enrichment.
- **External** — single site, retrospective, critical-care only, bounded cohort of ~100–500
  patients, no prospective validation.
- **Construct** — faithfulness rewards grounding in wrong evidence; audit completeness measures
  schema conformance rather than truth; Likert n = 3–5 measures impression, not clinical outcome.
