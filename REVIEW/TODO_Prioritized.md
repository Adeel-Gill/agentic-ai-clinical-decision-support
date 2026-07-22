# Prioritized TODO — Path to Submission

Impact and effort are rated Low / Med / High. Do all HIGH items before any examiner sees the thesis.

## 🔴 HIGH PRIORITY (blocking — a fail without these)

| # | Task | Impact | Effort | Notes |
|---|------|--------|--------|-------|
| H1 | Verify every `References.bib` entry against publisher of record; resolve all `TODO-VERIFY` | Critical | Med | Bibliography now exists; accuracy must be confirmed |
| H2 | Add inline citations throughout Ch1–Ch2 (adopt the `_Revised.md` versions) | Critical | High | Uncited claims fail IEEE/academic review |
| H3 | Build a bounded prototype (≥3 agents + RAG on ~100–500 MIMIC-IV patients) | Critical | High | The single biggest gap; without results this is a proposal |
| H4 | Run at least one experiment from Chapter 4 (baseline ladder + one ablation) and report real numbers | Critical | High | Turns the design into a thesis |
| H5 | Finalize Chapter 3 (formal architecture) inside the thesis | Critical | Med | Draft produced; refine + insert real figures |
| H6 | Obtain/record PhysioNet credentialing + DUA; confirm MIMIC-IV-Note access | Critical | Low | Notes-RAG depends on the separate Note module |
| H7 | Compile all chapters into ONE master thesis document (docx/LaTeX/md) | High | Med | Examiners need a continuous artifact |

## 🟡 MEDIUM PRIORITY

| # | Task | Impact | Effort | Notes |
|---|------|--------|--------|-------|
| M1 | Complete the de-AI rewrite for the remaining Chapter 2 section files | High | Med | See `Chapter_2/_Rewrite_Notes.md` |
| M2 | Run an AI-detector + similarity check; iterate until <15% overall, <2% single-source | High | Med | After citations + voice rewrite |
| M3 | Replace placeholder figure captions; regenerate framework figure at Ch3 numbering | Med | Low | "Figure 2.X" and `![alt text]` must go |
| M4 | Produce the missing diagrams from `Diagram_Specs.md` as final images | Med | Med | Sequence, RAG, memory, patient-journey, deployment |
| M5 | Add the recommended papers to the literature matrix + cite them in Ch2 | Med | Med | See `Recommended_Additional_Papers.md` |
| M6 | Write Chapter 5 findings once experiments are done | Med | Med | Outline exists |
| M7 | Add clinician-in-the-loop mini study (n=3–5) for explainability metric | Med | Med | Even small n strengthens the safety claim |

## 🟢 LOW PRIORITY

| # | Task | Impact | Effort | Notes |
|---|------|--------|--------|-------|
| L1 | Flesh out `05_Source_Code` skeletons into runnable modules | Med | High | Scaffold exists; implement as prototype grows |
| L2 | Build the defense deck from `08_Presentation/Defense_Outline.md` | Med | Med | |
| L3 | Keep `01_Admin` trackers current | Low | Low | Templates now in place |
| L4 | Add a data dictionary appendix to the thesis from `03_Dataset/Data_Dictionary.md` | Low | Low | |

## Suggested sequence
H6 → H1/H2 (in parallel) → H3 → H4 → H5 → H7 → M-series → L-series.
Rationale: credentialing unblocks data; citations and prototype can proceed in parallel; experiments depend on the prototype; compilation and polish come last.
