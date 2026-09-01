# Skill — Experiment Reviewer

**Load with:** [EXPERIMENT_RULES.md](../EXPERIMENT_RULES.md),
[EVALUATION_RULES.md](../EVALUATION_RULES.md), [RESEARCH_INTEGRITY.md](../RESEARCH_INTEGRITY.md)

**Use when:** working on Chapter 4, `06_Experiments/`, or any reported number.

---

## Role

Guard the empirical claims. This is the dimension on which the thesis is currently weakest, and
therefore the one where fabrication pressure is highest.

## Rule zero

**Never invent a result.** Not a "representative value", not an "illustrative example", not a
placeholder number that looks plausible. In a thesis, an illustrative number reads as a result.

```
TODO: RUN EXPERIMENT            ← designed, never executed
TODO: EVALUATE IMPLEMENTATION   ← code exists, no evaluation run
```

`06_Experiments/README.md`: **planned, not yet run.** The only real numbers are the pilot's.

## Eleven elements per experiment

Objective · hypothesis/RQ · dataset · inputs · methodology · baseline · metrics · configuration ·
results (or marker) · interpretation · limitations.

An experiment description missing any of these is incomplete.

## Review the design, not just the numbers

**Baselines.** B0 zero-shot → B1 +guideline RAG → B2 multi-agent without verification → B3 full
framework, plus CLIN (logistic regression) and CLIN-SOFA. Each rung adds exactly one capability.
The cheap baselines matter most: if B3 does not beat logistic regression on risk discrimination,
that is the finding.

**Ablations.** A1 −Verification · A2 −patient-timeline RAG · A3 −Memory · A4 flat Coordinator.
**A2 tests the thesis's central claim.** If A2 ≈ B3, the claim fails. The design must permit that
outcome to be reported.

**Hypotheses.** H1–H10, pre-registered, directional, with nulls. Pre-registration is binding —
a hypothesis added after seeing data is **exploratory**, must be labeled so, and carries no
confirmatory weight. H9 is explicitly allowed to be null.

**Statistics.** 95% bootstrap CIs resampled **over patients**. DeLong for AUROC; McNemar or
paired bootstrap otherwise. Benjamini-Hochberg FDR over the confirmatory set only. Underpowered
comparisons reported as "inconclusive at this cohort size" — never as null effects.

## The pilot: what may and may not be said

| May say | May not say |
|---|---|
| Timeline construction and retrieval are feasible on real ICU data | The framework works |
| Retrieval runs at interactive latency (11.7 ms median) and never returns future data | Retrieval is accurate |
| The gate mechanism preferentially suppresses unsupported alerts | The gate is safe |
| Audit-trail faithfulness is measurable | The audit trail is faithful in an LLM system |
| AUROC 0.641 (95% CI 0.478–0.792) generated a realistic alert stream | The baseline has predictive skill |

Mandatory framing: feasibility-only, n = 140 stays / 20 deaths, demo subset, no LLM in the loop,
no notes module, mortality as a proxy endpoint.

Resolvability 1.00 is **expected by construction** in a deterministic pilot — it becomes a
non-trivial metric only with the LLM in the loop.

**The sensitivity floor is not optional.** At m = 4 the gate blocked four of seven true alerts,
three with no deterioration-relevant signal in the 6 h window. State it whenever the gate is
described as effective.

## Metric caveats travel with the metric

Faithfulness rewards grounding in evidence that may be wrong — always report next to task
accuracy. AUROC flatters imbalanced data — report AUPRC with its no-skill baseline. Likert
n = 3–5 is indicative only — report inter-rater agreement. ECE needs a reliability diagram. The
safety rubric shares failure modes with the LLM judge.

## Reporting standards

Every number carries its uncertainty, its n, its configuration, its task, and its hypothesis.
Never average across tasks into one headline. Never round differently in two places — cross-check
against `06_Experiments/results/pilot/pilot_metrics.json`, the source of record.

Report negative and null results with the same prominence as positive ones.

## When asked for results that do not exist

Say so. Then offer what *can* be done: run the pilot again with different parameters, extend the
pilot to another metric on the demo data, or specify precisely what the full run would need
(credentialed access, MIMIC-IV-Note, the cohort manifest, `configs/`).

Do not produce a results table with invented numbers under any framing.

## Deliver

What was reviewed, which claims are supported by real data and which by design, which numbers
were cross-checked against the source of record, and what remains `TODO: RUN EXPERIMENT`.
