# Prioritized TODO — Path to Submission

**Refreshed 2026-08-13 (second pass, end of working session).** The morning refresh listed
H1–H9 / M1–M8 / L1–L5; everything completable without data access, author-only actions, or
human participants was completed the same day — see "Done since last refresh". What remains
below is blocked on exactly three things: **author actions** (H1, H2, M7), **data access**
(H3–H6), and **larger build-outs** (M-series). Impact and effort rated Low / Med / High.

## 🔴 HIGH PRIORITY (blocking — a fail without these)

| # | Task | Impact | Effort | Notes |
|---|------|--------|--------|-------|
| ~~H1~~ | ~~Confirm the W-category paper submission status~~ | — | — | **Resolved 2026-08-14:** author confirms the paper went to the supervisor before the deadline; venue submission proceeds via the supervisor. Coined-term quote fixes applied post-submission with author approval. Keep the two camera-ready errata (shi2024ehragent pages; yehudai2025evaluation title) for the venue stage. |
| H2 | Obtain/record PhysioNet credentialing + DUA; confirm MIMIC-IV-Note access | Critical | Low | **CREDENTIALED 2026-08-22 (approved in 8 days).** Remaining: verify CITI training shows complete, sign the two DUAs (MIMIC-IV + MIMIC-IV-Note), selective download of the Data_Dictionary table subset to `C:\data\mimic-iv\`. Checklist updated. H3 unblocks the moment the DUAs are signed and data lands. |
| H3 | Extract the bounded MIMIC-IV cohort (~100–500 stays): seeded manifest + splits → `06_Experiments/cohort/` | Critical | Med | Depends on H2. Fix D5 (cohort labels ↔ T1–T4 mapping) while writing the manifest labels. |
| H4 | Complete the LLM agent loop (≥3 agents + dual-grounded RAG) to what Chapter 4 needs | Critical | High | `acdss.pilot` is done; the LLM loop is a scaffold. Keep scope bounded — the prototype is the schedule's release valve, not the writing. |
| H5 | Run the Chapter 4 evaluation (baseline ladder B0–B3 + ≥1 ablation), seeds + pinned models + repeated headline runs | Critical | High | Configs to write in `06_Experiments/configs/`. The pilot does **not** substitute (R8.1). |
| H6 | Write Chapter 4 from the actual result files, then Chapter 5 (RQ answers, interpretation vs literature) | Critical | High | Strictly after H5. |

## 🟡 MEDIUM PRIORITY

| # | Task | Impact | Effort | Notes |
|---|------|--------|--------|-------|
| M1 | Run the official Turnitin/iThenticate via supervisor/DOPS (bibliography + quotes excluded); iterate to <15% overall, <2% single-source | High | Med | **Author-run tool — the only remaining half.** Repo side done 2026-08-14: author approved and I applied the coined-term quote fixes (UNDCS phrase ×3 in `paper/` + 3 thesis-side occurrences; tex regenerated; `REVISION_REPORT.md` §C addendum records the decision change). |
| M2 | Produce the six remaining diagrams from `Diagrams/Diagram_Specs.md` (sequence, RAG, memory, patient journey, HITL flowchart, deployment/methodology); replace the still-fake `07_Thesis/Images/research_process.png` | Med | Med | **Figure 3.1 done 2026-08-14**: regenerated to the canonical eight-agent scheme (`Diagrams/framework_figure_3_1.svg` + 300-dpi PNG) and deployed over the fake `proposed_framework.png`. Taxonomy figure done earlier (Figure 2.1). |
| ~~M3~~ | ~~Decide D6 (pilot wall-clock figures)~~ | — | — | **Resolved 2026-08-14 by author ruling (variance-note option)** after a fresh-download re-run reproduced all deterministic figures exactly. Prose untouched; committed JSON canonical; three-run timing table + reproduction caveats appended to the pilot README. D6 moved to the Fixed table in `.ai/README.md`. |
| M4 | Clinician-in-the-loop mini study (n=3–5) for the explainability metric | Med | Med | Requires human participants. Optional but strengthens the safety claim. |
| ~~M5~~ | ~~Matrix scope decision~~ | — | — | **Resolved 2026-08-14 (recommended default adopted; reversible):** the matrix is scoped to the reviewed corpus (P001–P052); foundation citations stay bib-only. Scope note added to the matrix header. |
| ~~M6~~ | ~~Delete the 17 bannered superseded files~~ | — | — | **Done 2026-08-14 with author approval:** all 17 deleted after per-file banner verification; recoverable from git history; deletion record in `.ai/THESIS_STRUCTURE.md` §7. |

## 🟢 LOW PRIORITY

| # | Task | Impact | Effort | Notes |
|---|------|--------|--------|-------|
| ~~L1~~ | ~~Front matter per DOPS template~~ | — | — | **Verified largely done 2026-08-14:** the build already produces the full DOPS front-matter sequence; abstract corrected to the eight-agent roster and extended with pilot findings (358 words, in-window, R2-safe). Remaining slivers: Word caption fields for the auto-lists, DOPS confirmations, final abstract findings after Ch4. |
| L2 | Build the defense deck from `08_Presentation/Defense_Outline.md` | Med | Med | November window; results slides depend on Ch4, so a full draft is deliberately sequenced after H5. |
| ~~L3~~ | ~~P046–P050 notes + matrix rows~~ | — | — | **Verified done 2026-08-14:** all 52 IDs have matrix rows; the "landing" note was stale. |

## ❓ Supervisor / DOPS questions — ask, don't guess

1. Title-page wording for **MS Artificial Intelligence** (template specimen says "MASTER OF PHILOSOPHY").
2. Whether Chapter 4 may be renamed from the template's "DATA ANALYSIS AND RESULTS"; then reconcile chapter titles between the template and `.ai/RULES.md` R7.
3. Abstract word count if the Faculty overrides 300–400.
4. IEEE confirmed before any mass bib conversion.

## ✅ Done since last refresh (all 2026-08-13 unless noted; evidence-linked)

- **Defects D1–D4 fixed** (`.ai/README.md` Fixed table): reference stores synced; pilot gate figure corrected; "seven-agent" purged from `Chapter_3.md` / `System_Design.md` / `Technical_Feasibility.md`; `Proposed_Framework.md` aligned to Chapter 3 (eight agents + Memory-Manager, cross-cutting Trustworthy AI, cited at flagged claims; stale diagram export flagged in-file → M2).
- **`jimenez2023trustworthy` resolved as a phantom**: the stored P018 PDF is a category-theory paper under a misleading filename; entry removed from both stores, all 9 citing claims remapped to verified keys (`rasheed2022explainable`, `tan2026undcs`, `weissman2025unregulated`).
- **Full `References.bib` verification pass complete** (74 entries): Crossref API + publisher records + back-port of the verified paper bib; `tu2025amie` verified with published author order; `xi2023rise` upgraded to Sci China Inf Sci 68(2) 2025; `jin2021medqa` type fixed; EHRAgent pages added; zero `TODO-VERIFY` remain; stores in lockstep 74/74.
- **`CITE_RE` extended**: `[a; b]` multi-citations compile to `[n], [m]`; unit-tested (8 cases).
- **Corpus cleaned**: P017 retired (byte-identical duplicate of P016); P018 retired (empty slot); **48 distinct papers**; matrix corrections log updated.
- **Section 2.11 reconciled into the compiled thesis**: inserted with gap references renumbered to §2.10; summary renumbered to §2.12 with pointer; `Thesis_Ch1_Ch2.docx` rebuilt — 58 references resolve, zero missing-reference flags.
- **Zero-citation Chapter 2 files formally adopted**: all 16 superseded originals/stubs bannered with canonical targets (compiled §§2.2–2.9 carry the cited, de-AI'd prose); `Chapter_1/Chapter_1.md` bannered.
- **Placeholder residue swept**: `Figure 2.X` / `![alt text]` fixed with proper captions or explicit unassigned-number markers.
- **Recommended papers reconciled**: all 14 verified in the bib and cited in the thesis; matrix-row question → M5.
- **Annexure A (data dictionary) wired** into `07_Thesis/Annexure/`; 11 methodology keys back-ported to the style guide.
- **Longitudinal-EHR line woven into Chapter 2** (evening pass): CliCARE, Traj-CoA, TrajOnco, TIMER, RGAR critically reviewed in §2.11.3 of both the compiled chapter and its source, grounded in the Paper_046–050 notes; docx now resolves **63** references.
- **Three papers reviewed and added** (evening pass): SmartAlert (NEJM AI 3(7), RCT of ML-CDS lab-utilization alert) added as **P051** and MedHELM (Nat Med 32(3), clinician-validated medical LLM evaluation taxonomy) added as **P052** — each with a verified bib entry in both stores, PDF, 19-dimension note, matrix row, and a critical weave into §2.11.5; the npj Health Systems non-clinician GenAI usage study added as a **supporting citation** (`black2026nonclinician`) anchoring the demand side of §2.11.4's regulation paragraph. Docx rebuilt: **66 references resolve**, stores in lockstep 77/77.
- **Tables 2.1 and 2.2 render as real tables** (evening pass): `build_thesis_docx.py` now parses the Literature_Matrix sources and renders DOPS-style tables (caption above, number + italic caption; Table 2.1 as two panels; ✓/✗ marks; citation keys in cells resolve to reference numbers). Zero "insert table here" placeholders remain.
- Earlier (2026-08-05/07/08): pilot study run on the open demo; P021–P050 literature update; W-paper SUBMIT verdict.

## Suggested sequence

H1 + H2 now (author) → H3 (with D5 fix) → H4 → H5 (September) → H6 + front matter (October) →
M1 similarity gate → M2 diagrams → L2 deck → defense (November).
