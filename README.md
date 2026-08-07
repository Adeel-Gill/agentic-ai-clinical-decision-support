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
| `paper/` | W-category paper draft (introduction, related work, methodology, discussion) |
| `REVIEW/` | External examiner report, prioritized TODO, viva questions, style guide |
| `Reports/` | Generated progress reports (literature update report) |

## Status (as of 2026-08-05)
- Literature: 2025–2026 update complete — 25 new papers (P021–P045) with PDFs, notes
  (`02_Research/Notes/`), matrix rows, taxonomy mapping, and BibTeX entries; Chapter 2 gained
  Section 2.11 (Recent Advances 2025–2026).
- W-category paper: draft assembled in `paper/` (deadline 2026-08-10), now including a pilot
  feasibility study (Section 5) run on the open MIMIC-IV demo — code in
  `05_Source_Code/src/acdss/pilot/`, aggregate results in `06_Experiments/results/pilot/`.
- Chapters 1–2: drafted (under revision for citations + de-AI'd prose).
- Chapter 3 (framework/methodology): drafted in `07_Thesis/Chapter_3/`.
- Chapter 4 (experimental design): planned in `07_Thesis/Chapter_4/` + `06_Experiments/`.
- Chapter 5: outline.
- Prototype (`05_Source_Code/`): clinician platform implemented (React + FastAPI, synthetic
  data) and the `acdss.pilot` package runnable; the LLM agent loop remains a scaffold.
- Dataset (`03_Dataset/`): access + cohort + dictionary specified; extraction not yet run.

## Running the app (clinician platform)

Research prototype — synthetic data only, not for clinical use.

**Prerequisites:** Python 3.11+ with `fastapi` and `uvicorn` (`pip install fastapi uvicorn`),
and Node.js 18+.

**1. Start the backend** (FastAPI, port 8000):

```bash
cd 05_Source_Code/src
python -m uvicorn acdss.api.app_dashboard:app --reload --port 8000
```

**2. Start the frontend** (React + Vite, port 5173) in a second terminal:

```bash
cd 05_Source_Code/frontend
npm install
npm run dev
```

**3. Open** http://localhost:5173 — six screens: Unit Overview, Patient Timeline (with the
"replay what was knowable" cursor), Recommendation Review (approve/modify/reject),
Alerts & Verification Gate, Audit Trail, Agent Monitor. API docs: http://localhost:8000/docs.

Notes: the frontend proxies `/api` to port 8000, so start the backend first. The gate
operating curve and agent health metrics are served from the real pilot results in
`06_Experiments/results/pilot/` when present. To (re)generate those from the open
MIMIC-IV demo, see `05_Source_Code/README.md` §6. A static, no-install design prototype
of the same screens is at `04_Architecture/UI_Prototype/acdss_ui_prototype.html`.

## Data access & ethics
MIMIC-IV and MIMIC-IV-Note require PhysioNet credentialing (CITI "Data or Specimens
Only Research" training) and acceptance of the PhysioNet Credentialed Health Data Use
Agreement. No patient data is committed to this repository. See `03_Dataset/README.md`.

## Reproducing the bibliography
References live in `02_Research/References.bib`. Entries flagged `TODO-VERIFY` must be
checked against the publisher of record before submission.
