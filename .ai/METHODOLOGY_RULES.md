# METHODOLOGY RULES

Governs Chapter 3 (`07_Thesis/Chapter_3/Chapter_3.md`) and anything describing how the research
was conducted.

---

## 1. The research design is design science

This thesis follows a design-science research process [hevner2004design]: the framework itself
is the primary research artifact, and the investigation is organized around four activities —
identify a problem, design an artifact, demonstrate it on a realistic case, evaluate whether the
demonstration meets the stated objectives.

Consequences that must be honored in every methodology sentence:

- The contribution is **integrative**, not a new learning algorithm. Do not write as if a novel
  model were being proposed.
- The **demonstration** is a worked patient trajectory carried end-to-end (Ch. 3 §3.7). It is a
  textual trace, not measured results. Never describe it as an experiment.
- The **evaluation** belongs to Chapter 4 and has not been executed.
- Design science is vulnerable to post-hoc rationalization. Chapter 3 guards against this by
  explicitly flagging two components the original design omitted (Data/Retrieval Agent,
  Memory-Manager) and arguing for them rather than folding them in silently. **Preserve that
  self-critical move** — it is what makes the chapter credible.

## 2. Tense discipline — the rule most often broken

| Situation | Correct tense |
|---|---|
| The full Chapter 4 evaluation | "**will be** evaluated", "**is designed to**" |
| Unbuilt components (RAG over notes, calibrated confidence, LLM agent loop) | future or conditional |
| The pilot study | "**was** measured", "the pilot **found**" |
| Implemented code (`acdss.pilot`, clinician platform) | present/past, with scope stated |
| A cited paper's findings | present ("MedAgents **reports**") |

Never write "we evaluated", "results show", "the framework achieved" about anything outside the
pilot. `06_Experiments/README.md` states plainly: **planned, not yet run.**

## 3. Every design decision is a defended bet

For each choice, state: the decision, the alternative you rejected, and why. The chapter already
does this for LangGraph vs linear chains, pgvector vs Qdrant, condition-triggered DAG vs fixed
pipeline, and dual-grounded vs external-only RAG. Extend rather than dilute.

Where a decision is genuinely uncertain, say so and point at the risk analysis
(`04_Architecture/Technical_Feasibility.md`). "This is a bet under uncertainty" is stronger
academic writing than false confidence.

## 4. What Chapter 3 must document

| Item | Where | Note |
|---|---|---|
| Research design (design science) | §3.1 | With the post-hoc-rationalization caveat |
| Dataset | §3.3.1 + `03_Dataset/` | Relative time only; provenance pointers |
| Cohort selection | `03_Dataset/Cohort_Definition.md` | 10 criteria, ordering matters |
| Preprocessing | `03_Dataset/Preprocessing_Pipeline.md` | Timeline construction |
| Feature extraction | `03_Dataset/` | Windowed features; leakage control |
| System architecture | §3.2, §3.3 | Six layers + cross-cutting trust layer |
| Agent design | §3.4 | Per-agent contract: inputs, tools, output schema, failure behavior |
| RAG pipeline | §3.6 | Dual grounding: patient timeline **and** external corpus |
| Memory mechanism | §3.5 | Four stores + Memory-Manager policy |
| Orchestration | §3.4 | Condition-triggered DAG; arbitration protocol |
| Evaluation methodology | Ch. 4 | Baselines, metrics, hypotheses |
| Limitations | §3.9 + Ch. 4 §4.8 + Ch. 5 §5.4 | Design limits belong in Ch. 3 too |

## 5. Reproducibility requirements

Anything described as a method must be reproducible from the description:

- **Seeds fixed** for cohort sampling, bootstrap resampling, and stochastic decoding; recorded
  with each result.
- **Model and prompt versions pinned** per run; changing either starts a new result set.
- **Config-driven runs** — each baseline and ablation is one declarative config file, so B0–B3
  and the ablations differ by configuration, not by hand-tuning. This is what makes the ladder a
  fair comparison.
- **Fixed cohort manifest** — sampled once, reused verbatim by every configuration. This is the
  precondition for the paired statistical tests.
- **Determinism is imperfect.** LLM outputs vary run to run; headline configurations are run
  multiple times and variability is reported, not hidden.
- **No PHI in results.** Only derived, non-identifying artifacts.

## 6. Bounded prototype, honestly bounded

The scope statement (`07_Thesis/Chapter_1/Scope.md`) commits to a conceptual framework plus a
bounded prototype, explicitly excluding production hospital software, live EHR integration, and
clinical trials. Do not let methodology prose drift beyond that boundary.

`01_Admin/Timeline.md` names prototype scope as "the primary release valve" — if the schedule
slips, the prototype shrinks, not the writing. Methodology text should never commit to
implementation work that the timeline does not support.

## 7. Ethics and approvals

- MIMIC-IV requires PhysioNet credentialing, CITI "Data or Specimens Only Research" training,
  and a signed Credentialed Health Data Use Agreement. MIMIC-IV-Note is a **separate** request.
- Credentialing status is `[IN PROGRESS]` (`REVIEW/TODO_Prioritized.md` H6) — the methodology
  must not assume access already granted.
- The pilot used the **open** MIMIC-IV Clinical Database Demo v2.2, which carries no
  credentialing requirement. State this distinction whenever the pilot is described.
- No IRB approval is required for retrospective analysis of de-identified MIMIC-IV under the
  DUA, but the DUA's terms (no re-identification, no redistribution) bind all work.

## 8. Common methodology defects to avoid

| Defect | Fix |
|---|---|
| Describing planned experiments in past tense | Future tense; add `TODO: RUN EXPERIMENT` |
| Presenting the worked trace as evidence | Label it a demonstration |
| Cohort criteria that cannot be scripted | Express every criterion against a documented column |
| Label definitions without a clinical reference | Cite `singer2016sepsis3`, `vincent1996sofa` |
| Splitting at the record level | Patient-level splits only — no patient in two partitions |
| Using later stays as features | Later stays are label information only (readmission) |
| Silent enrichment for rare positives | Record any enrichment so prevalences are not mistaken for population rates |
| Cohort labels that do not match experiment tasks | Known defect D5 — reconcile the four risk labels once |
