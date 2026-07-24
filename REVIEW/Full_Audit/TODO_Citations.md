# TODO — Citations

Priority: **Critical / High / Medium / Low.** Source: `Citation_Audit.md`. Rule: never fabricate a citation or reference.

## Critical
- [ ] **Verify/replace `jimenez2023trustworthy`** — the `References.bib` entry is a `TODO-VERIFY` placeholder ("Jimenez-Luna, Jose and others"), the backing note `Paper_018.md` is the wrong paper (category theory), yet it is cited ~9× (Ch3 L53/177/181, Ch4 L57, Trustworthy_Revised L3/70/78, Evaluation_Metrics L85, Research_Gap_Analysis L15). Find the real "Toward Trustworthy AI in Healthcare" paper, fill full metadata in **both** `References.bib` and `build_thesis_docx.py`, and confirm it supports each citing claim.
- [ ] **Verify `tu2025amie` venue** (`note = TODO-VERIFY final venue`).

## High
- [ ] **Full 45‑entry `.bib` verification pass** against publisher of record (DOIs, venues, arXiv→published upgrades) — the file header mandates it before submission.
- [ ] **Add inline citations to the zero‑citation files** (or adopt their `_Revised`/`Compiled` versions): `AI_in_Healthcare`, `Large_Language_Models_in_Healthcare`, `LLM_Based_Agents`, `Agentic_AI_Frameworks`, `Taxonomy_of_LLM_Based_Agents`, `Trustworthy_AI_in_Healthcare`, `04_Architecture/Proposed_Framework`, `04_Architecture/Taxonomy`. Suggested keys per file are listed in `Citation_Audit.md` §4.
- [ ] **Standardize citation format** to single‑key `[key]` brackets (what `build_thesis_docx.py`'s `CITE_RE` matches). The `[a; b]` form in source files will NOT resolve — either convert to `[a][b]` or extend the regex.

## Medium
- [ ] **Sync the two reference stores** — `References.bib` (45) and the `IEEE` dict in `build_thesis_docx.py` (45) must match key‑for‑key; any drift prints `[MISSING REFERENCE]`.
- [ ] **Resolve the P017/P013 key collision** — matrix reassigns Paper_017 to `singhal2023clinical` (already Paper_013's key); Paper_016=Paper_017=Med‑PaLM M (`tu2024generalist`). Fix the note + matrix row.
- [ ] **Add citations to specific unsupported claims** (Citation_Audit §5), e.g. `Proposed_Framework.md:153` "RAG reduces hallucinations" → `lewis2020rag`, `gao2023rag`.

## Low
- [ ] **Update `REVIEW/Style_And_Citation_Keys.md`** — back‑port the 11 missing methodology/stats keys (`hevner2004design`, `vincent1996sofa`, `es2024ragas`, `guo2017calibration`, `hardt2016equality`, `mehrabi2021survey`, `delong1988comparing`, `dietterich1998approximate`, `benjamini1995controlling`, `hayes2007krippendorff`, `singer2016sepsis3`) so the canonical table matches `References.bib`.
- [ ] Confirm `wang2023voyager`, `wang2023selfconsistency`, `yao2023tree`, `schick2023toolformer` (currently cited only inside `Compiled/Chapter_2.md`) survive into the final submission source.
- [ ] Confirm every `.bib` `TODO-VERIFY` note is cleared before the final build.
