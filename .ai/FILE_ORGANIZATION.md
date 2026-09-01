# FILE ORGANIZATION

Respect the existing structure. Do not randomly create files; do not create a new top-level
directory; do not invent a parallel naming scheme.

---

## 1. Top-level layout

| Directory | Contents |
|---|---|
| `01_Admin/` | `Timeline.md`, `Progress_Tracker.md`, `Meeting_Notes.md`, `TODO.md` |
| `02_Research/` | Papers, per-paper notes, literature matrix, research gap, `References.bib` |
| `03_Dataset/` | MIMIC-IV cohort definition, data dictionary, preprocessing plan, `.gitignore` |
| `04_Architecture/` | Proposed framework, system design, technical feasibility, diagrams, UI prototype |
| `05_Source_Code/` | Prototype (backend, agents, RAG, MCP, pilot, frontend, docker, docs, tests) |
| `06_Experiments/` | Experimental design, evaluation metrics, results |
| `07_Thesis/` | Chapters 1–5, compiled build, images, references, formatting guide |
| `08_Presentation/` | Defense outline, slides, speaker notes, design guide, build scripts |
| `REVIEW/` | Examiner report, full audit, prioritized TODO, viva questions, style guide |
| `Reports/` | Generated progress reports |
| `paper/` | W-category manuscript |
| `.ai/` | This rules system |

## 2. Where new artifacts go

| Artifact | Location |
|---|---|
| A new paper PDF | `02_Research/Papers/<Category>/` |
| A paper note | `02_Research/Notes/Paper_nnn.md` |
| A literature matrix row | `02_Research/Literature_Matrix/Literature_Matrix.md` |
| A BibTeX entry | `02_Research/References.bib` (**and** the IEEE dict in `build_thesis_docx.py`) |
| Thesis chapter prose | `07_Thesis/Chapter_X/` |
| A compiled chapter | `07_Thesis/Compiled/` |
| A thesis figure | `07_Thesis/Images/` |
| A diagram spec | `04_Architecture/Diagrams/Diagram_Specs.md` |
| An exported diagram | `04_Architecture/Diagrams/` |
| Prototype code | `05_Source_Code/src/acdss/<layer>/` |
| Tests | `05_Source_Code/tests/` |
| An experiment config | `06_Experiments/configs/` (intended; not yet created) |
| A cohort manifest | `06_Experiments/cohort/` (intended; never data itself) |
| Run outputs | `06_Experiments/results/<config-name>/` |
| A review or audit | `REVIEW/` or `REVIEW/Full_Audit/` |
| A generated report | `Reports/` |
| Paper section prose | `paper/` |
| Temporary/scratch work | **outside the repository** — use the session scratchpad |

The six paper categories: `Agentic_AI`, `Clinical_Decision_Support`, `LLM_Healthcare`,
`Multi_Agent_Systems`, `RAG`, `Survey_Papers`.

## 3. Naming conventions

Follow what exists — do not introduce a new style.

| Type | Convention | Example |
|---|---|---|
| Paper PDF (early) | `YYYY_Title_With_Underscores.pdf` | `2022_ReAct_Synergizing_Reasoning_and_Acting_in_Language_Models.pdf` |
| Paper PDF (Pnnn era) | `Pnnn_Title_With_Underscores.pdf` | `P046_CliCARE_Grounding_LLMs_in_Clinical_Guidelines_for_Longitudinal_Cancer_EHRs.pdf` |
| Paper note | `Paper_nnn.md` (zero-padded to 3) | `Paper_046.md` |
| Citation key | `authorYYYYshortname` | `li2026clicare`, `jiang2025medagentbench` |
| Chapter section file | `Title_Case_With_Underscores.md` | `Trustworthy_AI_in_Clinical_Decision_Support.md` |
| Revised section | `<name>_Revised.md` | `Agentic_AI_Revised.md` |
| Rule/report doc | `SCREAMING_SNAKE.md` in `.ai/`, `Title_Case.md` elsewhere | `Citation_Audit.md` |
| Python module | `snake_case.py` | `run_pilot.py` |
| React component | `PascalCase.jsx` | `PatientTimeline.jsx` |

The paper ID `Pnnn` and the note number must match. Citation keys are lowercase, no underscores.

## 4. Change management

Before modifying an existing document:

1. **Read it** in full.
2. **Understand its purpose** — why it exists and who consumes it.
3. **Identify dependencies** — `grep -rn "<filename>" --include="*.md"` and check whether the
   build script reads it.
4. **Check for a canonical sibling** — a `_Revised.md` or `Compiled/` version may supersede it.
5. **Preserve useful content.** Improve rather than blindly replace.

After modifying:

- [ ] Consistency with related documents
- [ ] Citations still resolve
- [ ] Headings and numbering still correct
- [ ] Cross-references still point somewhere real
- [ ] Terminology unchanged
- [ ] File naming still conventional
- [ ] TODOs updated (added or closed) in the right tracker

## 5. Canonical vs superseded

Editing a superseded draft is the most common wasted-work failure here. Check first:

| Canonical | Superseded |
|---|---|
| `07_Thesis/Compiled/Chapter_1.md`, `Chapter_1/Chapter_1_Revised.md` | `Chapter_1/Chapter_1.md` and its pointer files |
| `07_Thesis/Compiled/Chapter_2.md`, `Chapter_2/*_Revised.md` | non-revised `Chapter_2/*.md` |
| `07_Thesis/Chapter_3/Chapter_3.md` | `04_Architecture/Proposed_Framework.md` |
| `07_Thesis/Chapter_2/Taxonomy_of_LLM_Based_Agents.md` | `04_Architecture/Taxonomy.md` |

One-line stubs (`Chapter_2/Taxonomy.md`, `Research_Gap.md`, `Proposed_Framework.md`,
`Literature_Review.md`) are placeholders. Do not extend them.

## 6. Generated files — never hand-edit

| File | Regenerate with |
|---|---|
| `paper/_body_generated.tex` | `python paper/tools/md2tex.py` |
| `paper/references.bib` | `python paper/tools/md2tex.py` |
| `paper/*.docx` | `python paper/tools/md2docx.py` |
| `07_Thesis/Thesis_Ch1_Ch2.docx` | `python 07_Thesis/Compiled/build_thesis_docx.py` |
| `07_Thesis/Images/superior_logo_vertical.png` | `python 07_Thesis/Images/make_vertical_logo.py` |
| `08_Presentation/*.pptx` | `python 08_Presentation/build_presentation.py` |

Edit the source, then regenerate. A hand-edited generated file is silently lost on the next build.

## 7. What must never be committed

- Any MIMIC-IV data, extract, cohort file, note text, or derived embedding
  (see [DATASET_RULES.md](DATASET_RULES.md))
- `.env` or any credential
- `node_modules/`, `__pycache__/`, `.venv/`, `dist/`, `build/`
- Draft manuscripts uploaded for similarity checking
- Scratch/temporary analysis files

Root `.gitignore` covers the build artifacts; `03_Dataset/.gitignore` covers data formats.
Verify with `git status` before every commit regardless.

## 8. Where TODOs live

Add new work items to the right tracker rather than only mentioning them in conversation:

| Tracker | Scope |
|---|---|
| `01_Admin/TODO.md` | Author-facing, supervisor-driven actions |
| `REVIEW/TODO_Prioritized.md` | Path to submission, H/M/L priority with impact and effort |
| `REVIEW/Full_Audit/TODO_Citations.md` | Citation defects |
| `REVIEW/Full_Audit/TODO_AI.md` | De-AI rewrite work |
| `REVIEW/Full_Audit/TODO_Plagiarism.md` | Similarity reduction |
| `REVIEW/Full_Audit/TODO_Writing.md` | Prose quality |
| `01_Admin/Progress_Tracker.md` | Status percentages — update at supervisor check-ins |
