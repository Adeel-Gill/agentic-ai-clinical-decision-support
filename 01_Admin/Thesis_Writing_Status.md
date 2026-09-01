# Thesis Writing Status

Maintained per `01_Admin/THESIS_AI_PROMPT.md` (Final Output section). Update after each
substantial working session. Scores are evidence-based — no inflation.

**Last session: 2026-08-13 (full-day sweep)** — defects D3/D4, citation infrastructure
(`CITE_RE`, phantom removal, full bib verification), Section 2.11 reconciliation + docx
rebuild, superseded-file adoption, placeholder sweep, annexure wiring, tracker refresh.

## Completed

- Chapters 1–2: compiled, cited, de-AI'd versions are canonical; §2.11 Recent Advances
  integrated and summary renumbered §2.12; the longitudinal-EHR line (P046–P050) — the
  nearest prior work to the thesis contribution — critically reviewed in §2.11.3; Tables 2.1
  and 2.2 render as real tables from the Literature_Matrix sources; `Thesis_Ch1_Ch2.docx`
  rebuilt — **63 references resolve, zero missing-reference flags, zero table placeholders**.
- **Citation infrastructure is submission-grade**: `References.bib` fully verified against
  publishers of record (74 entries; Crossref API + publisher pages + verified-paper-bib
  back-port); zero `TODO-VERIFY`; both reference stores in lockstep 74/74; `CITE_RE` resolves
  the R5-sanctioned `[a; b]` form; 11 methodology keys back-ported to the style guide.
- **The phantom citation is gone**: `jimenez2023trustworthy` (cited 9×, no real paper behind
  it) removed; all citing claims remapped to verified keys. The single worst integrity
  exposure in the audit is closed.
- **Corpus cleaned**: 48 distinct papers (P017 = byte-identical duplicate, retired; P018 =
  empty slot behind a misleading filename, retired); matrix corrections log documents both.
- Defects D1–D4 fixed and recorded; all 17 superseded originals/stubs bannered with canonical
  targets; placeholder residue swept; Annexure A (data dictionary) wired.
- Pilot feasibility study (2026-08-07, open demo); W-paper at SUBMIT (100/100).
- DOPS template installed; official prompt at `01_Admin/THESIS_AI_PROMPT.md`.

## Partially Completed

- Prototype: `acdss.pilot` implemented and pilot-validated; **LLM agent loop is a scaffold**.
- Diagrams: framework export still shows 7 agents (flagged in-file); five spec'd diagrams
  unproduced; taxonomy figure unplaced/unnumbered in the compiled chapter.
- P046–P050 notes + matrix rows landing (2026-08-08).
- Front matter: Annexure A wired; title page, declarations, TOC, abstract remain.

## Missing

- **The Chapter 4 evaluation — not run.** No cohort, no configs, no results. This is the
  thesis-defining gap; nothing written may imply otherwise (R2/R8.1).
- PhysioNet credentialing / DUA (author action, gates everything).
- Chapter 5 results-dependent content; defense deck; full-thesis compile.

## Template Compliance Issues

- Pagination scheme (Roman → Arabic) and front-matter build still pending.
- Figure captions/numbering: pending diagram production (M2); table/figure conventions
  otherwise encoded in the build script.

## Academic Risks

- Similarity: free-checker 26% on the paper analyzed as bibliography + coined-term matches
  (verified: "unconfined non-deterministic clinical software" is the UNDCS paper's own term,
  used verbatim 2×). Official Turnitin (references excluded) not yet run — that is the number
  that counts. Quote-marking fixes in `paper/` await author's go (SUBMIT status).
- The superseded scaffolds still exist on disk (bannered, not deleted) — deletion is the
  recorded review recommendation and the author's call.

## Technical Risks

- LLM agent loop unbuilt; full-DAG latency target (≤30 s) unproven.
- D5 (cohort labels ↔ T1–T4) open — fold into the cohort manifest work.
- D6 (pilot wall-clock discrepancy) needs a re-run or an author ruling.

## Required Evidence

- PhysioNet credentialing record + signed DUA.
- Cohort manifest + splits; run configs B0–B3 + ablations; results + audit traces.
- Turnitin similarity report on the official pipeline.

## Recommended Changes

- Work `REVIEW/TODO_Prioritized.md` (refreshed end-of-session 2026-08-13) in sequence:
  H1/H2 author actions now, then cohort → LLM loop → evaluation.
- Delete the bannered superseded files once confirmed unreferenced (M6 there).

## Remaining Thesis Work

September: cohort + LLM loop + Chapter 4 runs. October: Ch4/Ch5 write-up, front matter, full
compile, official similarity check. November: proofread, submit, defense.

## Open Questions for Supervisor / DOPS

1. Title-page wording for MS Artificial Intelligence (template says "MASTER OF PHILOSOPHY").
2. Chapter 4 renaming permission; then reconcile template vs `.ai/RULES.md` R7 titles.
3. Abstract word count if Faculty overrides 300–400.
4. Confirm IEEE before any mass bib conversion.
5. **Was the W-paper submitted before 2026-08-10?** Two camera-ready errata noted (shi2024ehragent
   pages; yehudai2025evaluation title).
6. D6 ruling: re-run pilot or declare the authoritative timing run.

## Submission Readiness

Writing and citation infrastructure are near submission-grade for Ch1–3. The thesis remains
blocked on the evidence chain: data access → cohort → LLM loop → evaluation. It cannot be
examined until Chapter 4 has real results.

---

## Scores

| Dimension | /10 | Justification |
|---|---|---|
| Academic Quality | 7 | Claims discipline is now enforced end-to-end (phantom removed, every reference verified); the core empirical chapter still does not exist. |
| Literature Review | 8 | 48 distinct papers, fully verified bib, current §2.11, cleaned matrix; remaining: figure placement and the M5 matrix-scope decision. |
| Methodology | 7 | Chapter 3 examiner-grade and internally consistent post-D3/D4; D5 mapping and final figures outstanding. |
| Technical Contribution | 5 | `acdss.pilot` implemented and pilot-validated; the LLM agent loop — the heart of the claim — is still a scaffold. |
| Evaluation | 2 | Only the feasibility pilot on the 100-patient open demo; the Chapter 4 evaluation has not been run. |
| Writing Quality | 7 | Compiled chapters are cited, varied, critical prose; superseded scaffolds neutralized by banners (deletion pending). |
| Research Novelty | 7 | Instrumented integration is specific, piloted, and now cleanly cited; unproven at evaluation scale. |
| Template Compliance | 5 | Build encodes core styles; annexure wired; docx rebuilds cleanly; front matter and pagination scheme still absent. |
| **Overall Readiness** | **4** | Everything except the evidence chain advanced today — but the evidence chain is the thesis. |
