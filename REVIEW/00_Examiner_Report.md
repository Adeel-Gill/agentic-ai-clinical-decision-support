# External Examiner's Report

**Thesis:** *An Agentic AI Framework for Intelligent Patient Monitoring and Clinical Decision Support*
**Reviewer role:** External MS examiner / IEEE reviewer
**Date:** 2026-07-22
**Verdict:** **Not approvable as a completed MS thesis in its current state.** It is a strong *proposal / literature-review-plus-design* milestone. The path to a pass is almost entirely execution: citations, Chapters 3–5, a prototype, and experiments. This report is companion to `TODO_Prioritized.md` and `Viva_Questions.md`.

---

## 1. Repository structure — 5/10

Only four of eight claimed top-level folders originally existed (`03_Dataset`, `05_Source_Code`, `06_Experiments`, `08_Presentation` were absent; several files were 0 bytes: `README.md`, `System_Design.md`, `Research_Gap.md`, all of `01_Admin/`, and `References.bib`). As part of this review pass those folders and files have been scaffolded/populated.

Remaining issues to watch:
- The thesis is still fragmented (Chapter 1 used "See X.md" pointers). A single compiled master document is needed for examination.
- Research-gap content lived in three places; now consolidated but keep it DRY.
- `Objectives.md` had its entire body duplicated (fixed).

## 2. Chapters — Ch1 6.5/10, Ch2 6/10; Ch3–5 absent (now drafted/outlined)

- Ch1 complete in structure, clean grammar, but promotional and uncited; fragmented across pointer files (a continuous revised version has been produced).
- Ch2 is the strongest original content (~11k words) but list-heavy, repetitive, and **entirely uncited** because `References.bib` was empty.
- **AI-generation risk is HIGH** across the prose (uniform paragraph length, triadic lists, formulaic openers). See `Style_And_Citation_Keys.md` for the de-AI rules applied to the revised chapters.

## 3. Literature review — 6/10

Good 20-paper matrix with rich columns and excellent per-paper notes. But it contained three defects, now corrected:
- **P018** described an irrelevant category-theory ("monoids") paper — mismatched with the actual stored PDF ("Toward Trustworthy AI in Healthcare"); the row has been corrected.
- **P016 = P017** (both "Towards Generalist Biomedical AI") — duplicate merged.
- Inconsistent IDs (`P003s`) and years (MedAgents 2023 vs 2024) — reconciled.
- Missing influential works added to `Recommended_Additional_Papers.md` (RAG originals, CoT/ToT/Reflexion, MIMIC-IV source paper, recent clinical agents EHRAgent/AgentClinic/AMIE).

Critically, the original comparative table showed *Agent Hospital ticking every column*, which undercut the novelty claim. The table now has differentiating columns (patient-timeline RAG, verification gate, longitudinal memory, real ICU data, faithful audit trail).

## 4. Research gap — was 5/10, rewritten

The original "no unified framework integrates everything" gap was weak (integration ≠ novelty) and contradicted by the comparative table. It has been rewritten around three defensible, testable questions:
1. Does retrieval over a patient's own longitudinal MIMIC-IV timeline (not just external literature) reduce hallucination versus guideline-only RAG?
2. Does a dedicated verification agent reduce unsafe recommendations versus a single-agent baseline, and at what latency cost?
3. Can the reasoning trace be rendered faithful enough for clinician validation?

**Why the thesis deserves to exist:** the clinical-agent literature has advanced on capability but lags on *safety-under-longitudinal-context and faithful auditability on real ICU data* — a concrete, under-served problem, provided the experiments are actually run.

## 5. Proposed framework — 6/10

Coherent six-layer + trustworthy-layer + HITL design with seven agents. Weaknesses (now addressed in the drafted Chapter 3 / System_Design): no formalism, black-box Coordinator, no conflict-resolution, "monitoring" without a streaming mechanism, undefined communication layer. Added: explicit Data/Retrieval Agent, Memory Manager, coordinator routing logic, arbitration protocol, and a feedback loop into memory.

## 6. Technical feasibility — implementable with real risks

Key risks (see `04_Architecture/Technical_Feasibility.md`): context-window overflow on ICU records (#1 risk), multi-minute latency for a 7-agent pipeline (MedAgents alone is ~40s/question), vector-DB and RAG-pipeline choices, cost per case, and the absence of an evaluation harness. All now have named mitigations and a recommended stack (LangGraph, pgvector, MCP tools).

## 7. Dataset — plan only (now specified)

Correct tables named. Two accuracy points that were missing and are now documented: clinical notes require the separate **MIMIC-IV-Note** module, and PhysioNet **credentialing/DUA** is mandatory. A cohort definition, data dictionary, and preprocessing/timeline pipeline have been scaffolded in `03_Dataset/`.

## 8. Experimental design — was absent (now drafted as Ch4)

No experiments existed. Chapter 4 now specifies a baseline ladder (single LLM → +guideline RAG → multi-agent w/o verification → full framework), ablations, and metrics for accuracy, hallucination/grounding, risk prediction (AUROC/AUPRC vs SOFA), safety, explainability (clinician Likert), trustworthiness (ECE, audit completeness), and runtime/cost.

## 9. Thesis level

**MS-level in ambition; below a complete MS thesis in execution.** Not PhD-level (no novel mechanism proven, no evaluation). As a *proposal* it is credible; as a *finished thesis* it needs Chapters 3–5 with a working prototype and real numbers.

| Category | Score |
|---|---|
| Novelty | 4/10 |
| Technical depth | 4/10 |
| Research contribution | 4/10 |
| Publication potential | 3/10 |
| Industrial impact | 3/10 |
| Clinical usefulness | 5/10 |

## 10. Missing diagrams

Sequence, agent-collaboration, RAG pipeline, memory architecture, patient-journey, DFD, deployment, verification/HITL flowchart, evaluation pipeline, methodology flowchart. Mermaid sources for these are provided in `04_Architecture/Diagrams/Diagram_Specs.md`.

## 11. Academic review

- **Citations:** zero resolved originally (empty `.bib`) — the single most damaging academic gap. `References.bib` is now populated (verify `TODO-VERIFY` entries).
- Figure captions are placeholders ("Figure 2.X"), images use literal `![alt text]`.
- Chapter-numbering inconsistency (framework called both Ch3 and Ch4) — standardized to **Chapter 3**.

## 12. Writing review

AI-detection risk HIGH. Prescription and banned-phrase list in `Style_And_Citation_Keys.md`; de-AI'd revised chapters produced. Plagiarism targets (<15% overall, <2% single source) are achievable only after real citations + voice rewrite + a similarity check.

## 13. Source code — was absent (now scaffolded)

No code existed. A clean Python scaffold (FastAPI + LangGraph + pgvector + MCP) mapping to the six layers and all agents is provided in `05_Source_Code/` as skeletons with docstrings/TODOs — a credible engineering plan, not a finished implementation.

---

## 14. Overall Score

| Dimension | Score |
|---|---|
| Architecture | 6/10 |
| Novelty | 4/10 |
| Writing | 5/10 |
| Literature | 6/10 |
| Methodology | 4/10 |
| Implementation | 1/10 |
| Publication Potential | 3/10 |
| Industrial Value | 3/10 |
| Clinical Relevance | 5/10 |
| **Overall** | **≈ 46 / 100** |

Interpretation: ~70% of a solid *proposal*; ~46% of a complete MS thesis.

---

## 17. Final recommendation

**I would not approve this as a completed thesis.** I would approve it *as a proposal / mid-candidature checkpoint.* Mandatory before submission:
1. Real bibliography + inline citations everywhere (done — verify entries).
2. Curated literature (P018/P016 fixed).
3. Sharpened, defensible gap (done).
4. Chapter 3 as formal architecture in the thesis (drafted).
5. **A working prototype + at least one bounded experiment with real numbers** (still outstanding — the biggest remaining item).
6. Chapter 5 (drafted as outline; needs real findings).
7. De-fragment into one document; adopt the de-AI'd revised prose; run a similarity check.
8. Populate/verify all scaffolded folders.

Brutally honest bottom line: you currently present *the design of an experiment you have not run and could not previously cite.* The citation and structural gaps are now closed by this pass; the **empirical gap (prototype + results) is what still stands between this and a pass.**
