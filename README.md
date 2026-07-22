# An Agentic AI Framework for Intelligent Patient Monitoring and Clinical Decision Support

MS thesis repository. The work designs a layered, multi-agent framework that combines
Large Language Model (LLM) agents, the ReAct reasoning paradigm, Retrieval-Augmented
Generation (RAG), persistent patient memory, and human-in-the-loop validation to support
clinicians, using the **MIMIC-IV** critical-care database as the data source.

## Repository layout

| Folder | Contents |
|---|---|
| `01_Admin/` | Timeline, progress tracker, meeting notes, TODO |
| `02_Research/` | Papers, per-paper notes, literature matrix, research gap, `References.bib` |
| `03_Dataset/` | MIMIC-IV cohort definition, data dictionary, ETL / preprocessing plan |
| `04_Architecture/` | Proposed framework, system design, technical feasibility, diagrams |
| `05_Source_Code/` | Prototype implementation (backend, agents, RAG, MCP, docker, docs) |
| `06_Experiments/` | Experimental design, baselines, ablations, metrics, results |
| `07_Thesis/` | Chapters 1–5, images, references |
| `08_Presentation/` | Defense slides / outline |
| `REVIEW/` | External examiner report, prioritized TODO, viva questions, style guide |

## Status (as of 2026-07-22)
- Chapters 1–2: drafted (under revision for citations + de-AI'd prose).
- Chapter 3 (framework/methodology): drafted in `07_Thesis/Chapter_3/`.
- Chapter 4 (experimental design): planned in `07_Thesis/Chapter_4/` + `06_Experiments/`.
- Chapter 5: outline.
- Prototype (`05_Source_Code/`): scaffold + design; not yet implemented.
- Dataset (`03_Dataset/`): access + cohort + dictionary specified; extraction not yet run.

## Data access & ethics
MIMIC-IV and MIMIC-IV-Note require PhysioNet credentialing (CITI "Data or Specimens
Only Research" training) and acceptance of the PhysioNet Credentialed Health Data Use
Agreement. No patient data is committed to this repository. See `03_Dataset/README.md`.

## Reproducing the bibliography
References live in `02_Research/References.bib`. Entries flagged `TODO-VERIFY` must be
checked against the publisher of record before submission.
