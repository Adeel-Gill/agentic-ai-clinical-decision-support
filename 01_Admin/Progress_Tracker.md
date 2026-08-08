# Progress Tracker

Snapshot of where each chapter and artifact stands. Update at each supervisor check-in.
Last updated 2026-08-05.

| Chapter / Artifact | Status | % | Notes |
|---|---|---|---|
| Ch. 1 — Introduction | Drafted; revised | 85 | De-AI'd `Chapter_1_Revised.md` created with inline citations and continuous prose; awaiting supervisor sign-off to promote over the original. |
| Ch. 2 — Literature Review | Drafting; partial revision | 70 | 4 sections revised (Agentic AI, Trustworthy AI, CDSS, RAG); ~6 sections still need de-AI + citations (see `_Rewrite_Notes.md`). New Section 2.11 (Recent Advances 2025–2026) added 2026-08-05 with 25 new citations; 2.9 gap analysis updated. |
| Ch. 3 — Proposed Framework & Methodology | Drafting | 40 | Architecture + agents being written (other agent). Fix chapter-number cross-refs (framework = Ch. 3). |
| Ch. 4 — Experimental Design & Evaluation | Planned | 15 | Metrics/baselines/ablations outlined in `06_Experiments/`; not executed. Depends on cohort + prototype. |
| Ch. 5 — Conclusion & Future Work | Outline | 20 | Structured outline with prose stubs created; RQ answers pending Ch. 4 results. |
| Taxonomy of LLM-based agents | Drafted | 55 | Prose exists; needs critical framing + reconciliation with figure. |
| Research gap | Drafting | 50 | Owned by another agent; do not edit. |
| MIMIC-IV cohort / dataset | Specified | 30 | Cohort definition + data dictionary written; extraction not yet run; PhysioNet access required. |
| Prototype (`05_Source_Code/`) | Pilot implemented | 35 | Package skeleton in place; `acdss.pilot` fully implemented and run on the open MIMIC-IV demo (2026-08-07): timelines, retrieval, baseline, verification gate, measured audit trail. LLM agent loop still skeleton. |
| Pilot study (MIMIC-IV demo) | Done | 100 | 140 stays; retrieval ~12 ms; gate blocks 86% of false vs 57% of true alerts at m=4; trail resolvability 1.00. Results in `06_Experiments/results/pilot/`; write-up in `paper/05_Pilot_Study.md`. |
| Architecture diagrams (`04_Architecture/`) | Drafted | 60 | Diagrams exported; re-label any that use old Chapter 4 figure numbers. |
| References.bib | In progress | 80 | 70 entries after 2025–2026 update (25 added for P021–P045); canonical keys extended; `TODO-VERIFY` venue details outstanding for a handful of new entries; paper-ID reconciliation pending. |
| 2025–2026 literature update (P021–P045) | Done | 100 | 25 papers: PDFs, notes, matrix rows, taxonomy, bib entries, Section 2.11, framework refinements (2026-08-05). |
| W-category paper | Revised through 3 external review rounds | 90 | IEEE manuscript + pilot; 59 verified refs; novelty repositioned to instrumented integration; Table I status transparency; §4.5 safety subsection. Remaining: author block, venue, Turnitin (2026-08-08). |
| Longitudinal-EHR prior work (P046–P050) | In progress | 80 | CliCARE, Traj-CoA, TrajOnco, TIMER, RGAR: PDFs + bib + taxonomy done; notes + matrix rows landing (2026-08-08). |
| Defense deck (`08_Presentation/`) | Outline | 15 | `Defense_Outline.md` created; slides not built. |
| Front matter (abstract, etc.) | Not started | 0 | Write after full draft is stable. |

Overall thesis completion (rough weighted estimate): **~40%**.
