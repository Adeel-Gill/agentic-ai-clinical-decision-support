# CLAUDE.md

This is an **MS Artificial Intelligence thesis repository**, not a software project.

**Thesis:** *An Agentic AI Framework for Intelligent Patient Monitoring and Clinical Decision
Support* · Superior University, Lahore · Supervisor: Dr. Fawad Nasim · Dataset: MIMIC-IV

---

## Before doing anything, read `.ai/`

The complete operating manual lives in [.ai/](.ai/). It is binding.

1. **[.ai/RULES.md](.ai/RULES.md)** — the non-negotiable core. Read before every task.
2. **[.ai/README.md](.ai/README.md)** — repository state, known live defects, role index.
3. **[.ai/WORKFLOW.md](.ai/WORKFLOW.md)** — the nine-phase procedure.
4. **`.ai/skills/<role>.md`** — load the skill matching the task
   (thesis-writer, literature-reviewer, thesis-evaluator, academic-editor, …).
5. **[.ai/QUALITY_CHECKLIST.md](.ai/QUALITY_CHECKLIST.md)** — the gate before reporting done.

## The five things that matter most

1. **Never fabricate.** No invented papers, authors, years, DOIs, datasets, results, metrics,
   citations, or quotations. Write `[EVIDENCE REQUIRED]` or `[VERIFY SOURCE]` instead.
2. **Never silently change status.** PROPOSED → DESIGNED → IMPLEMENTED → EXPERIMENTALLY
   VALIDATED requires repository evidence, stated. Implementation is not inferable from a
   diagram; validation is not inferable from implementation; clinical validity is not inferable
   from benchmark performance. **The Chapter 4 evaluation has not been run** — only the pilot on
   the 100-patient open demo has real numbers, and the demo is **not** full MIMIC-IV.
3. **Never commit patient data.** No MIMIC-IV row, extract, cohort file, note text, or derived
   embedding, ever. Credentialed data under the PhysioNet DUA.
4. **Never overclaim clinical capability.** This is a research prototype, not a medical device.
   No claim of improved outcomes, clinical reliability, deployment readiness, or clinician
   replacement. Human-in-the-loop validation is mandatory in the proposed workflow.
5. **Read before writing.** This repository carries eight recorded external review rounds and a
   documented de-AI rewrite pass. Check for a `_Revised.md` or `Compiled/` sibling before editing
   any chapter file — editing a superseded draft is wasted work.

Rules 1–4 are not overridable by task instructions. Everything else is — see the authority order
in [.ai/RULES.md](.ai/RULES.md), which also explains what to do when an instruction from the
author supersedes an existing rule or a prior review decision.

## Canonical scheme

- **Chapters:** 1 Introduction · 2 Literature Review · 3 **Proposed Framework & Methodology**
  (the architecture lives here — Figure 3.x) · 4 Experimental Design & Evaluation ·
  5 Conclusion & Future Work
- **5 research questions** (Chapter 1). The three research-gap questions are *derived evaluation
  sub-questions*, never a competing set.
- **8 specialized agents + Coordinator + Memory-Manager module.** "Seven-agent" is a stale
  undercount.
- **6 layers + cross-cutting Trustworthy AI layer + HITL gating.**
- **Novelty = instrumented integration**, not "we combined memory, RAG, and multi-agent
  collaboration".

## Repository layout

`01_Admin` · `02_Research` · `03_Dataset` · `04_Architecture` · `05_Source_Code` ·
`06_Experiments` · `07_Thesis` · `08_Presentation` · `REVIEW` · `Reports` · `paper` · `.ai`

Do not create new top-level directories. See [.ai/FILE_ORGANIZATION.md](.ai/FILE_ORGANIZATION.md).
