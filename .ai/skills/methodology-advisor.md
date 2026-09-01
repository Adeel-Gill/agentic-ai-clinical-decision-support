# Skill — Research Methodology Advisor

**Load with:** [METHODOLOGY_RULES.md](../METHODOLOGY_RULES.md),
[EXPERIMENT_RULES.md](../EXPERIMENT_RULES.md), [DATASET_RULES.md](../DATASET_RULES.md),
[THESIS_STRUCTURE.md](../THESIS_STRUCTURE.md)

**Use when:** working on Chapter 3 methodology, design decisions, or reproducibility.

---

## Role

Ensure the research design actually answers the research questions, and that a competent
stranger could reproduce the work from the description alone.

## The frame is design science

The framework is the research artifact [hevner2004design]. Four activities: identify a problem,
design an artifact, demonstrate it on a realistic case, evaluate against the stated objectives.

Two consequences that must survive every edit:

- The contribution is **integrative**, not a new learning algorithm. Do not let methodology prose
  drift toward "we propose a novel model".
- The **demonstration** (Ch. 3 §3.7 worked patient trajectory) is a textual trace, not measured
  results. Never call it an experiment.

Design science is vulnerable to post-hoc rationalization — every choice looking inevitable in
hindsight. Chapter 3 guards against this by explicitly flagging the two components the original
design omitted (Data/Retrieval Agent, Memory-Manager) and arguing for them. **Preserve that
move.** It is what makes the chapter credible rather than merely coherent.

## Tense discipline

The rule most often broken. The Chapter 4 evaluation **has not been run**.

| Situation | Tense |
|---|---|
| Full evaluation, unbuilt components | "will be evaluated", "is designed to" |
| The pilot | "was measured", "the pilot found" |
| Implemented code | present/past, with scope stated |
| A cited paper's findings | present ("MedAgents reports") |

## Every design decision is a defended bet

State the decision, the alternative rejected, and why. The chapter already does this for
LangGraph vs linear chains, pgvector vs Qdrant, condition-triggered DAG vs fixed pipeline, and
dual-grounded vs external-only RAG.

Where a decision is genuinely uncertain, say so and point at
`04_Architecture/Technical_Feasibility.md`. "This is a bet under uncertainty" is stronger academic
writing than false confidence.

## Reproducibility requirements

- **Seeds** fixed for cohort sampling, bootstrap resampling, and stochastic decoding; recorded
  with each result.
- **Model and prompt versions pinned**; changing either starts a new result set.
- **Config-driven runs** — each baseline and ablation is one declarative config, so the ladder is
  a fair comparison rather than eight hand-tuned systems.
- **Fixed cohort manifest** — sampled once, reused verbatim by every configuration. This is the
  precondition for the paired statistical tests.
- **Determinism is imperfect** — LLM outputs vary; headline configs run multiple times and
  variability is reported.
- **No PHI in results.**

## Check the traceability chain

```
RQ → Objective → Gap → Methodology → Framework → Experiment → Result → Conclusion
```

For any methodology element, ask: which RQ does this serve? If none, it is out of scope or the
chain has a hole worth reporting.

## Scope boundaries

`07_Thesis/Chapter_1/Scope.md` commits to a conceptual framework plus a bounded prototype, and
explicitly excludes production hospital software, live EHR integration, and clinical trials.
`01_Admin/Timeline.md` names prototype scope as "the primary release valve" — if the schedule
slips, the prototype shrinks, not the writing. Methodology must not commit to work the timeline
cannot support.

## Ethics

PhysioNet credentialing + CITI training + DUA are prerequisites, and are `[IN PROGRESS]`. The
methodology must not assume access already granted. MIMIC-IV-Note is a separate request. The
pilot used the **open** demo — always state that distinction.

## Common defects

| Defect | Fix |
|---|---|
| Planned experiments in past tense | Future tense + `TODO: RUN EXPERIMENT` |
| The worked trace presented as evidence | Label it a demonstration |
| Cohort criteria that cannot be scripted | Express against documented columns |
| Label definitions without a clinical reference | Cite `singer2016sepsis3`, `vincent1996sofa` |
| Record-level splits | Patient-level only |
| Later stays used as features | Label information only (readmission) |
| Silent enrichment for rare positives | Record it |
| Cohort labels ≠ experiment tasks | Known defect D5 — reconcile once |

## Deliver

Which methodology elements were addressed, which design decisions were defended against a named
alternative, which reproducibility requirements are met and which are outstanding, and whether
the traceability chain holds.
