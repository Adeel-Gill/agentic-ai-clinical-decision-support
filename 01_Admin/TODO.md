# TODO — Thesis Completion

Prioritized task list for finishing "An Agentic AI Framework for Intelligent Patient Monitoring
and Clinical Decision Support." Last updated 2026-07-22.

Legend: `[ ]` open · `[~]` in progress · `[x]` done.

## High priority (blocking submission)

- [~] Finalize Chapter 3 (Proposed Framework & Methodology) — architecture, agent roles, MIMIC-IV
  data flow. *(owned by another agent)*
- [ ] Chapter 4 (Experimental Design & Evaluation): lock metrics, baselines, ablations, cohort.
  *(owned by another agent)*
- [ ] Run the MIMIC-IV extraction against the finalized cohort definition (`03_Dataset/`).
- [ ] Build the bounded prototype in `05_Source_Code/` to the point where the Chapter 4 evaluation
  can run (agents, RAG, memory, HITL stub).
- [ ] Verify every `TODO-VERIFY` entry in `02_Research/References.bib` against publisher of record.
- [ ] Resolve all `[CITATION NEEDED]` markers across chapters.
- [ ] Reconcile paper IDs in the literature matrix: merge P016/P017, fix P018 → `jimenez2023trustworthy`,
  drop stray `P003s`, set MedAgents year = 2024.

## Medium priority (quality + consistency)

- [ ] Apply the de-AI'd rewrite to remaining Chapter 2 sections (see `07_Thesis/Chapter_2/_Rewrite_Notes.md`):
  AI_in_Healthcare, Large_Language_Models_in_Healthcare, LLM_Based_Agents, Agentic_AI_Frameworks,
  Taxonomy_of_LLM_Based_Agents, Chapter_Summary.
- [ ] Promote the `_Revised.md` chapter/section files to canonical once the supervisor approves.
- [ ] Fix all cross-references to the authoritative chapter numbering (framework = Chapter 3, not 4).
- [ ] Fill Chapter 5 prose stubs and answer RQ1–RQ5 once Chapter 4 results exist.
- [ ] Complete the defense deck from `08_Presentation/Defense_Outline.md`.
- [ ] Consistency pass: US spelling, terminology ("proposed framework", "agent", "module", "layer").
- [ ] Confirm all figures/diagrams are referenced and captioned; regenerate any mislabeled ones.

## Low priority (polish)

- [ ] Front matter: abstract, acknowledgments, list of figures/tables, abbreviations.
- [ ] Format bibliography to the required citation style; check DOIs/URLs.
- [ ] Proofread full manuscript end to end.
- [ ] Prepare viva questions and rehearse (see `REVIEW/`).
- [ ] Archive a reproducible snapshot of code + environment (Docker) for the appendix.
