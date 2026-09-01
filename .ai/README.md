# Thesis AI Skills & Rules

Operating manual for any AI assistant (Claude Code or otherwise) working in this repository.

**Thesis:** *An Agentic AI Framework for Intelligent Patient Monitoring and Clinical Decision
Support*
**Degree:** MS Artificial Intelligence — Superior University, Lahore
**Supervisor:** Dr. Fawad Nasim
**Primary dataset:** MIMIC-IV (PhysioNet, credentialed)

---

## Read this first

This is **not a software project**. It is a research repository under academic examination.
The success criterion is not "more output" — it is that every claim in the thesis is
**true, sourced, traceable, and defensible under viva questioning**.

Four failure modes are worse here than doing nothing at all:

1. **Fabricating** a citation, a result, an author, a DOI, or a dataset property.
2. **Silently upgrading status** — turning a *planned* experiment into a *completed* one,
   or a *designed* component into an *implemented* one.
3. **Overwriting** careful prior work (eight external review rounds are recorded in this
   repository) without reading and understanding it first.
4. **Breaking cross-chapter consistency** — the thesis has a documented consistency history;
   inconsistencies are examiner-visible in seconds.

If evidence is unavailable, write `[EVIDENCE REQUIRED]` or `[VERIFY SOURCE]`. Never invent.

---

## Directory map

| File | Governs |
|---|---|
| [RULES.md](RULES.md) | The non-negotiable core. Read before any task. |
| [WORKFLOW.md](WORKFLOW.md) | The nine-phase procedure for every substantial task. |
| [RESEARCH_INTEGRITY.md](RESEARCH_INTEGRITY.md) | Fabrication bans, status labels, uncertainty markers. |
| [ACADEMIC_WRITING.md](ACADEMIC_WRITING.md) | Voice, banned phrasing, paragraph discipline, de-AI rules. |
| [LITERATURE_REVIEW.md](LITERATURE_REVIEW.md) | Analytical (not descriptive) review; the 19-dimension note schema. |
| [CITATION_RULES.md](CITATION_RULES.md) | Canonical keys, bracket format, the two reference stores. |
| [THESIS_STRUCTURE.md](THESIS_STRUCTURE.md) | Authoritative chapter numbering, RQs, objectives, contributions. |
| [METHODOLOGY_RULES.md](METHODOLOGY_RULES.md) | Design-science framing, tense discipline, reproducibility. |
| [ARCHITECTURE_RULES.md](ARCHITECTURE_RULES.md) | Layers, agents, component justification test. |
| [DATASET_RULES.md](DATASET_RULES.md) | MIMIC-IV facts, module structure, PHI prohibition. |
| [TECHNICAL_RULES.md](TECHNICAL_RULES.md) | Prototype scope, implementation-claim discipline, stack. |
| [EXPERIMENT_RULES.md](EXPERIMENT_RULES.md) | Baselines, ablations, hypotheses; the "never invent results" rule. |
| [EVALUATION_RULES.md](EVALUATION_RULES.md) | Metric definitions and how results must be reported. |
| [REVIEWER_RULES.md](REVIEWER_RULES.md) | How to act as a hostile examiner. |
| [PUBLICATION_RULES.md](PUBLICATION_RULES.md) | W-category paper standards; what "novelty" may mean here. |
| [FORMATTING_RULES.md](FORMATTING_RULES.md) | Superior University / DOPS template compliance. |
| [FILE_ORGANIZATION.md](FILE_ORGANIZATION.md) | Where every artifact type belongs; naming conventions. |
| [QUALITY_CHECKLIST.md](QUALITY_CHECKLIST.md) | The gate every task passes before being called done. |
| [skills/](skills/) | Eleven role definitions (thesis writer, reviewer, editor, …). |

---

## The eleven roles

Load the matching skill file before working in that mode. Roles are in
[skills/](skills/):

| Role | File | Use when |
|---|---|---|
| Academic Thesis Writer | [thesis-writer.md](skills/thesis-writer.md) | Drafting or revising chapter prose. |
| AI Research Assistant / Literature Researcher | [literature-researcher.md](skills/literature-researcher.md) | Finding and verifying new papers. |
| Literature Review Assistant | [literature-reviewer.md](skills/literature-reviewer.md) | Writing or revising Chapter 2 sections. |
| Research Gap Analyzer | [research-gap-analyzer.md](skills/research-gap-analyzer.md) | Testing or restating the gap. |
| Research Methodology Advisor | [methodology-advisor.md](skills/methodology-advisor.md) | Chapter 3 methodology, design decisions. |
| Technical Architect | [architecture-reviewer.md](skills/architecture-reviewer.md) | Framework/component/diagram work. |
| Dataset Analyst | [dataset-analyst.md](skills/dataset-analyst.md) | Cohort, preprocessing, MIMIC-IV claims. |
| Experiment Reviewer | [experiment-reviewer.md](skills/experiment-reviewer.md) | Chapter 4, `06_Experiments/`, results. |
| Thesis Evaluator / Reviewer | [thesis-evaluator.md](skills/thesis-evaluator.md) | Adversarial review, viva prep. |
| Publication Assistant | [publication-writer.md](skills/publication-writer.md) | `paper/` — W-category manuscript. |
| Scientific Editor | [academic-editor.md](skills/academic-editor.md) | Line editing, de-AI pass, consistency sweep. |

---

## Repository state as of 2026-08-13

Facts an assistant must hold in mind before making any claim. Sources are the tracked files
named; if a file changes, re-derive rather than trusting this table.

| Item | State | Source |
|---|---|---|
| Chapters 1–2 | Drafted; `_Revised`/`Compiled` versions are the good ones | `01_Admin/Progress_Tracker.md` |
| Chapter 3 | Drafted, examiner-grade | `07_Thesis/Chapter_3/Chapter_3.md` |
| Chapter 4 | Design only — **no full evaluation has been run** | `06_Experiments/README.md` |
| Chapter 5 | Outline with prose stubs, `*(pending)*` markers | `07_Thesis/Chapter_5/Chapter_5.md` |
| Full MIMIC-IV evaluation | **NOT RUN.** PhysioNet credentialing outstanding | `REVIEW/TODO_Prioritized.md` H6 |
| Pilot feasibility study | **RUN** on the *open demo* (100 patients / 140 stays), 2026-08-07 | `06_Experiments/results/pilot/` |
| LLM agent loop | **Scaffold only** — `NotImplementedError` markers | `05_Source_Code/README.md` §6 |
| `acdss.pilot` package | Fully implemented and runnable | `05_Source_Code/README.md` §6 |
| Clinician platform (React + FastAPI) | Implemented, **synthetic data** | `05_Source_Code/README.md` |
| W-category paper | 100/100 SUBMIT verdict; author fields outstanding | `paper/SUBMISSION_CHECKLIST.md` |
| Literature | 52 IDs (P001–P052); **50 distinct papers** — P017 retired (duplicate of P016), P018 retired (empty slot); P051 SmartAlert and P052 MedHELM added 2026-08-13 | `02_Research/` |
| `References.bib` | 75 entries, 5 still `TODO-VERIFY` | `02_Research/References.bib` |

**The single most important line in this table:** the full evaluation has not been run.
Any sentence implying otherwise is a research-integrity violation.

---

## Known defects

Confirmed by inspection on 2026-08-13. Do not "discover" these again — fix them or leave them,
but do not write around them silently.

### Fixed

| # | Defect | Fix |
|---|---|---|
| D1 | `build_thesis_docx.py` IEEE dict held **45** keys against `References.bib`'s **75** — the 30 keys for P021–P050 were absent, so every Section 2.11 citation compiled to `[MISSING REFERENCE: key]`. | **Fixed 2026-08-13.** All 30 IEEE strings added, derived from their `References.bib` entries. Both stores now match key-for-key (75/75), verified programmatically. |
| D2 | `06_Experiments/results/pilot/README.md` said "86% of false alerts blocked vs **57% of true alerts retained**" at m = 4, contradicting its own table (true-alert pass rate **0.43**) and `paper/04_Discussion.md` §4.5 ("blocked four of the seven true alerts"). | **Fixed 2026-08-13.** Corrected to "86% of false alerts blocked, versus 43% of true alerts retained — that is, four of the seven true alerts were blocked." Verified against `pilot_metrics.json`. |
| D3 | The stale phrase "seven-agent" survived in `Chapter_3.md`, `System_Design.md`, `Technical_Feasibility.md`; the canonical count is **eight specialized agents + Coordinator + Memory-Manager module**. | **Fixed 2026-08-13.** All five occurrences updated to the eight-agent scheme; repo-wide grep confirms the remaining "seven" hits are benign (seven specific objectives in Ch1, "seventy percent" in 2.11) or accurate (`paper/` describes the seven-stub code scaffold and is at SUBMIT status — untouched). |
| D4 | `04_Architecture/Proposed_Framework.md` was the stale 7-agent original with zero citations and a literal `![alt text](image.png)`. | **Prose fixed 2026-08-13.** Data/Retrieval Agent and Memory-Manager sections added, §12 reframed as cross-cutting, canonical-status note added, audit-flagged claims cited (johnson2023mimic, yao2023react, lewis2020rag, gao2023rag, wu2025memory, rasheed2022explainable), placeholder replaced with a captioned figure. **Remaining: the embedded diagram export still shows seven agents — regeneration per `Diagrams/Diagram_Specs.md` spec 1 is open (M4), flagged in-file.** |

| D6 | Two **wall-clock** pilot figures disagreed with `pilot_metrics.json` (README/paper 2.9 s & 11.7/17.9 ms vs JSON 2.73 s & 9.62/15.01 ms). | **Resolved 2026-08-14 by author ruling** after an independent re-run on a fresh PhysioNet download reproduced **every deterministic figure exactly** (full gate curve, all counts/quantiles, trail 183/183) while wall-clock varied again (2.56 s, 8.18/13.8 ms). Ruling: prose stays as written; the committed JSON is the canonical artifact; timings are order-of-magnitude evidence. Variance note + three-run table appended to `06_Experiments/results/pilot/README.md`, including the `--min-evidence` invocation caveat (CLI default 2 vs `gate.py` default 3). |

### Open

| # | Defect | Evidence | Impact |
|---|---|---|---|
| D5 | Cohort labels (prolonged LOS) ≠ experiment tasks (T2 ICU transfer). | `Consistency_Report.md` §6 | T1–T4 do not map onto the four defined labels. Fold the fix into the cohort-manifest work (H3). |

---

## How to use this system

1. Open [RULES.md](RULES.md). It is short and binding.
2. Open the skill file for the role the task demands.
3. Follow [WORKFLOW.md](WORKFLOW.md) phases 1–9.
4. Gate the result through [QUALITY_CHECKLIST.md](QUALITY_CHECKLIST.md) before reporting done.

When a rule here conflicts with an instruction in the conversation, say so explicitly rather
than quietly picking one.
