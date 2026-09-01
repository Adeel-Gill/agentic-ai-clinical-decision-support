# ANNEXURE A — DATA DICTIONARY

> **Compile note (created 2026-08-13, L4 in `REVIEW/TODO_Prioritized.md`).** This annexure
> transcludes the canonical data dictionary at `03_Dataset/Data_Dictionary.md` — do not fork
> its content here; edit the canonical file and pull it in at final compile. Per
> `07_Thesis/Thesis_Formatting_Guide.md` §11 [DOPS]: placed at the very end after References;
> heading centered, 16 pt bold, ALL CAPS; any figures/tables numbered `Figure A.1` /
> `Table A.1`; body font/spacing/caption rules as the main text. The current
> `build_thesis_docx.py` covers Chapters 1–2 only — extend the build to append this annexure
> when the full-thesis compile is assembled (H7-era work).

**Content source:** `03_Dataset/Data_Dictionary.md` — the MIMIC-IV tables the proposed
framework consumes (module, key columns, role, volume caveats), keyed by `subject_id` /
`hadm_id` / `stay_id`. The dictionary documents only the subset this project reads
[johnson2023mimic; goldberger2000physiobank]; no table or extract is stored in this
repository, consistent with the PhysioNet DUA (R8).
