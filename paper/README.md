# W-Category Paper — Working Draft

**Working title:** An Agentic AI Framework for Intelligent Patient Monitoring and Clinical
Decision Support with Patient-Timeline Retrieval and Verified Recommendations

**Status:** first assembled draft, created 2026-08-05 from the thesis materials and the
2025–2026 literature update (P021–P045). No earlier paper draft existed in the repository;
this skeleton was created to meet the 10 August 2026 submission deadline recorded in
`../01_Admin/TODO.md`. All sections need author review before submission.

**Target:** W-category venue (per supervisor meeting of 26 July 2026 — confirm the specific
venue and its formatting requirements).

## Files
- [01_Introduction.md](01_Introduction.md)
- [02_Related_Work.md](02_Related_Work.md)
- [03_Methodology.md](03_Methodology.md)
- [05_Pilot_Study.md](05_Pilot_Study.md) — pilot feasibility study on the open MIMIC-IV demo (real numbers; added 2026-08-07)
- [04_Discussion.md](04_Discussion.md)
- References: cite keys resolve against [../02_Research/References.bib](../02_Research/References.bib)

## Assembly notes
- Citation keys follow `REVIEW/Style_And_Citation_Keys.md`; entries marked TODO-VERIFY in the
  .bib must be checked before camera-ready.
- Empirical status (updated 2026-08-07): the full credentialed MIMIC-IV evaluation has not
  been executed, but the paper now includes a **pilot feasibility study** on the openly
  licensed MIMIC-IV demo (Section 5): timeline construction, timestamp-aware retrieval, an
  early-warning baseline (AUROC 0.641, wide CI, honestly framed), a verification-gate
  operating curve, and a measured audit trail. Framing is therefore
  "framework + pilot feasibility," which is materially stronger than design-only —
  confirm with the supervisor that this suffices for the chosen venue.
- Pilot code: `../05_Source_Code/src/acdss/pilot/`; aggregate results:
  `../06_Experiments/results/pilot/`.
