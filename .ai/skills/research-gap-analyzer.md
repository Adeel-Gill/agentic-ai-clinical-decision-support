# Skill — Research Gap Analyzer

**Load with:** [LITERATURE_REVIEW.md](../LITERATURE_REVIEW.md),
[THESIS_STRUCTURE.md](../THESIS_STRUCTURE.md), [RESEARCH_INTEGRITY.md](../RESEARCH_INTEGRITY.md)

**Use when:** testing, restating, or defending the research gap.

---

## Role

Be the person most likely to destroy the gap claim, so an examiner cannot.

## The gap must emerge from the literature

Never manufacture a gap to justify the thesis. The original claim in this project — "no unified
framework integrates everything" — was correctly rejected by the examiner as weak: integration is
not novelty, and the comparative table contradicted it.

A legitimate gap statement identifies six things:

1. what existing systems already solve;
2. what they partially solve;
3. what remains unresolved;
4. why the unresolved problem matters;
5. how the proposed framework addresses it;
6. what remains outside the scope.

`02_Research/Research_Gap.md` does all six. It is the standard to match.

## The current gap, in three parts

1. **Evaluation data.** The strongest medical agent systems are measured almost entirely on
   static examination QA (MedQA, MedMCQA, PubMedQA) or on generated patients. A real ICU stay is
   noisy, longitudinal, incompletely documented, and internally contradictory. High USMLE accuracy
   says little about tracking a deteriorating patient across days of MIMIC-IV observations.
2. **What retrieval is grounded in.** Medical RAG grounds in guidelines, textbooks, and
   literature — not in the specific patient. What is missing is retrieval anchored to the patient
   timeline: prior labs, prior admissions, and the trend of a given vital as first-class evidence.
3. **Verification and auditability as evaluated components.** Rarely is there a dedicated step
   checking a generated recommendation against retrieved patient evidence, and more rarely is the
   audit trail's faithfulness itself *measured*. "The panel of agents agreed" is not "this
   recommendation is entailed by the retrieved evidence, and here is the trace."

## The three derived questions

These are **evaluation sub-questions derived from RQ2/RQ3/RQ4** — never a competing RQ scheme.
Presenting them as a second set of research questions is a documented HIGH-severity
inconsistency.

## Stress-testing procedure

Run this whenever the gap is restated, and whenever new literature lands:

1. **Name the strongest counter-system.** Currently CliCARE — it grounds LLMs in longitudinal
   cancer EHRs including a MIMIC-IV cohort, with guideline alignment and an expert-validated
   judge.
2. **State honestly what it does.** Do not minimize.
3. **State the specific difference.** For CliCARE: offline TKG *compression* rather than
   query-time timestamp-aware retrieval; no recommendation-level verification gate; no audit
   trail and no measured citation faithfulness; no human-in-the-loop operational workflow.
4. **Ask whether that difference matters clinically.** If it does not, the gap is cosmetic.
5. **Ask whether it is testable.** If no experiment could falsify it, it is not a research gap.
6. **Check the other four longitudinal systems** — Traj-CoA, TrajOnco, TIMER, RGAR.
7. **Check the 2025–2026 benchmarks** — MedAgentBench (synthetic records), HealthBench
   (conversations), revisited MIMIC-IV (one-shot prediction), COMPOSER-LLM (one narrow
   prospective task).

If a new paper closes part of the gap, **narrow the claim**. Do not defend territory that has
been taken.

## Keep three things separate

| | Answers | Lives in |
|---|---|---|
| Research Gap | What the field has not done | Ch. 2 §2.9, `02_Research/Research_Gap.md` |
| Contribution | What this thesis does about it | Ch. 1, Ch. 5 §5.2 (C1–C6) |
| Future Work | What remains after this thesis | Ch. 5 §5.5 |

## The novelty claim this gap supports

**Instrumented integration** — timestamp-aware retrieval from the patient's own timeline coupled
to recommendation-level verification, with an audit trail whose faithfulness is measured, on real
longitudinal ICU records. Bounded by "within the literature reviewed for this study", and
falsifiable: if the ablations show the components do not improve grounded decision quality, the
thesis fails honestly.

## Never

- Claim a gap without checking P021–P050.
- Use "no existing system…" without saying which systems you checked.
- Downplay a competitor to preserve the claim.
- Present the three gap questions as a competing RQ scheme.
- Restate "integration is the novelty".

## Deliver

The gap statement, the strongest counter-system and why it does not close it, the falsification
condition, and whether the claim needed narrowing.
