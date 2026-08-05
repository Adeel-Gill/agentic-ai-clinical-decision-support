# Literature Update Report — 2025–2026 Papers (P021–P045)

**Date:** 2026-08-05
**Scope:** Tasks 1–13 of the August 2026 literature-update request.

## Summary

- **25 new papers added** (P021–P045), all published or first released in 2025–2026, all with
  verified metadata (landing page fetched per paper) and legally free PDFs (arXiv or open-access
  npj Digital Medicine).
- Every paper has: a PDF in its category folder, a note (`Paper_0NN.md`), a row in the
  Literature Matrix (md **and** xlsx), and a BibTeX entry. Relevant papers also appear in the
  research gap, taxonomy, Chapter 2 (new Section 2.11), the proposed framework, and the
  W-category paper draft.

## Papers Added

| Range | Cluster | Papers |
|---|---|---|
| P021–P028 | Medical LLM agents & CDS | Baymax survey, MedAgentBench, TxAgent, DoctorAgent-RL, AMIE disease management, AMIE multimodal, RiskAgent, HealthBench |
| P029–P035 | Agentic AI foundations | Memory mechanisms survey, interoperability protocols (MCP/A2A/ACP/ANP), Agentic RAG survey, collaboration mechanisms survey, foundation agents survey, agent evaluation survey, TrustAgent survey |
| P036–P041 | Medical reasoning, RAG & monitoring | MedRAX, medical hallucinations, uncertainty quantification, MIMIC-IV benchmark revisit, COMPOSER-LLM sepsis (prospective), guideline RAG across 10 LLMs |
| P042–P045 | Safety, regulation, HITL | MedSentry, unregulated device-like output, UNDCS regulation (Matters Arising), human–LLM collaboration meta-analysis |

Two candidates found during search were deliberately dropped to stay within the 20–25 target:
the MCP security-threats paper (overlaps the interoperability survey) and GEM (ECG grounding,
most peripheral to the framework).

## Files Created

- `02_Research/Papers/<category>/P021_… P045_….pdf` — 25 PDFs (six category folders)
- `02_Research/Notes/Paper_021.md … Paper_045.md` — 25 notes (existing template)
- `07_Thesis/Chapter_2/Recent_Advances_2025_2026.md` — new Section 2.11
- `paper/README.md`, `paper/01_Introduction.md`, `paper/02_Related_Work.md`,
  `paper/03_Methodology.md`, `paper/04_Discussion.md` — W-category paper draft
  (no prior draft existed; created against the 2026-08-10 deadline)
- `Reports/Literature_Update_Report.md` — this report

## Files Modified

- `02_Research/References.bib` — +25 entries (45 → 70); no duplicate keys or DOIs
- `02_Research/Literature_Matrix/Literature_Matrix.md` — rows P021–P045 appended, header note added
- `02_Research/Literature_Matrix/Literature_Matrix.xlsx` — same 25 rows (rows 24–48), schema unchanged
- `02_Research/Literature_Matrix/Literature_2025_2026.md` — populated with the 25-paper table + trends
- `02_Research/Literature_Matrix/Taxonomy.md` — full P001–P045 category mapping
- `02_Research/Research_Gap.md` — solved / partially solved / open status appended
- `07_Thesis/Chapter_2/Research_Gap_Analysis.md` — closing 2025–2026 paragraph
- `04_Architecture/Taxonomy.md` — new Section 7 mapping recent advances to the taxonomy
- `04_Architecture/Proposed_Framework.md` — new Section 16 (five refinements)
- `REVIEW/Style_And_Citation_Keys.md` — 25 canonical keys added
- `01_Admin/TODO.md`, `Progress_Tracker.md`, `Timeline.md`, `Meeting_Notes.md` — statuses updated
- `README.md` — layout table (paper/, Reports/) and status block

## Literature Trends (2025–2026)

1. **Agents displaced chatbots** — tool selection, validated calculators, and training-free
   orchestration are now baseline (TxAgent, RiskAgent, MedRAX).
2. **Benchmarks moved toward realism** — virtual FHIR EHRs (MedAgentBench), physician rubrics
   (HealthBench); best agents still only ~70% task success.
3. **RAG became agentic** — retrieval planned and iterated inside the agent loop; strong clinical
   results for guideline grounding.
4. **Memory formalized** — construction/management/retrieval taxonomy, but no patient-anchored
   longitudinal memory in any published system.
5. **Infrastructure standardized** — MCP/A2A/ACP/ANP protocols.
6. **Safety became measurable** — hallucination taxonomies, uncertainty quantification,
   multi-agent adversarial stress tests (topology matters).
7. **Regulation arrived** — LLM output already meets medical-device criteria; UNDCS governance
   proposals prescribe guardrails, moderation, retrieval grounding, inspectability.
8. **One prospective deployment** — COMPOSER-LLM sepsis alerting; evidence bar is rising.

## Research Gaps After the Update

Confirmed still open (and claimed by the thesis): patient-timeline retrieval as a first-class
corpus; longitudinal evaluation on real ICU records rather than exams or synthetic EHRs; a
verification gate with *measured* audit-trail faithfulness. Full argument in
`02_Research/Research_Gap.md` and Section 2.11.

## Framework Improvements Adopted

Five bounded refinements (Proposed_Framework.md §16): MCP/A2A standardized interfaces; memory
operation taxonomy (construction/management/retrieval, timestamp-aware); verification agent
gains hallucination-taxonomy grounding checks + calibrated confidence; hub-and-spoke topology
hardening per MedSentry; evaluation/regulatory alignment (MedAgentBench- and HealthBench-style
comparators, UNDCS safeguard mapping). Core idea unchanged.

## Potential Thesis Improvements

- Promote Section 2.11 into the compiled thesis (`Thesis_Ch1_Ch2.docx`) and regenerate the TOC;
  decide whether 2.10 (Chapter Summary) should follow 2.11.
- Chapter 4: add grounding-rate, verification catch-rate, and audit-trail-faithfulness metrics
  with the new benchmark comparators.
- Chapter 5: cite the regulatory trajectory (UNDCS) in future work.
- Six older Chapter 2 sections still need the de-AI/citation pass (see `_Rewrite_Notes.md`).

## Potential Journal Paper Improvements

- `paper/` draft is complete for Introduction / Related Work / Methodology / Discussion; needs:
  abstract + keywords, conclusion, venue selection and formatting (LaTeX), trimmed .bib, and a
  decision on whether a bounded experiment can run before submission (framework-only framing
  otherwise). Deadline 2026-08-10.

## Quality Verification (Task 12)

- ✓ No duplicate papers (25 unique arXiv IDs/DOIs, checked against P001–P020)
- ✓ No duplicate citations (70 unique bib keys, no duplicate DOIs)
- ✓ Internal links checked in modified files — none broken
- ✓ Consistent `P0NN_Title.pdf` filenames; numbering continues after P020
- ✓ All 54 citation keys used in new prose resolve in References.bib
- ✓ Matrix: 45 unique rows, 19 columns each, previous entries untouched
- ✓ P044 metadata corrected to version of record (Matters Arising; exact title)

## Remaining TODOs

1. Verify TODO-VERIFY bib entries (MedAgentBench NEJM AI details, MedRAX ICML pages,
   TrustAgent KDD pages, agent-evaluation survey venue) before submission.
2. Merge Section 2.11 into the compiled Word/PDF thesis documents.
3. W-paper: venue confirmation, abstract/conclusion, LaTeX build, supervisor review before
   2026-08-10.
4. Pre-existing reconciliation items (P016/P017 duplicate check; P018 authors) remain flagged
   in the matrix corrections log.
5. `Comparative_Analysis_Table` and `Research_Gap_Matrix` (xlsx/md) were not extended in this
   pass; extend if the supervisor wants the new papers scored on the differentiating columns.
