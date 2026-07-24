# Citation Audit (Phase 6)

Covers: missing citations, duplicate citations, weak support, claims without references, matrix papers never cited, and keys cited but absent from `References.bib`.

**Rules honored:** no citation was fabricated; no reference was invented. Findings are drawn only from files actually present.

---

## 1. How citations work in this repo (read first)

Citations are **Markdown placeholders** `[key]`, not LaTeX `\cite`. They are resolved to IEEE numbered references at build time by `07_Thesis/Compiled/build_thesis_docx.py`, which contains its **own** IEEE‑string dictionary (`IEEE = {…}`, 45 entries) keyed by BibTeX key. So there are **two reference stores that must stay in sync**:

1. `02_Research/References.bib` (45 entries)
2. the `IEEE` dict in `build_thesis_docx.py` (45 entries)

The build regex is `\[([A-Za-z]+\d{4}[a-z0-9]*)\]` — it matches **single‑key** brackets only. It leaves unknown keys visibly untouched and prints `[MISSING REFERENCE: key]` in the reference list for any cited key it cannot find. Two consequences:

- The `[a; b]` multi‑key format used in the source section files **will not be split** — only `[a][b]` (as in `Compiled/`) resolves correctly. **Standardize the format.**
- Any key used in prose but absent from the `IEEE` dict silently becomes a missing reference.

---

## 2. Reference inventory — all 45 keys are used somewhere (no orphans)

Every key in `References.bib` is cited at least once across the thesis body, `Compiled/`, or `06_Experiments/`. Verified individually. Notable placements:

- `singhal2025medpalm2` — used only in `Compiled/Chapter_2.md` (and Recommended_Additional_Papers). Not in the working section files.
- `hayes2007krippendorff` — used only in `06_Experiments/Evaluation_Metrics.md:71`.
- `singer2016sepsis3` — `Chapter_4.md`, `Experimental_Design.md`, `Cohort_Definition.md`.
- `hardt2016equality`, `mehrabi2021survey`, `guo2017calibration`, `delong1988comparing`, `dietterich1998approximate`, `benjamini1995controlling`, `es2024ragas`, `vincent1996sofa`, `goldberger2000physiobank`, `hevner2004design` — used in Ch3/Ch4/Experiments.

→ **No dead references to delete.** (Contrast: `rasheed2022explainable` is unused in the *literature notes/matrix* but **is** used in the thesis body — Ch3, Ch4, Trustworthy_Revised — so it is fine.)

---

## 3. CRITICAL — unverified / placeholder reference cited many times

| Key | Problem | Cited in | Severity |
|---|---|---|---|
| `jimenez2023trustworthy` | `References.bib` entry is a **placeholder**: author `"Jimenez-Luna, Jose and others"`, `journal = {arXiv preprint (TODO-VERIFY exact citation matched to P018 placeholder slot)}`, plus a `TODO-VERIFY` note. The build‑script IEEE string is literally `'Author(s), "Toward trustworthy AI in healthcare," 2023. [full citation to verify]'`. **And the backing note `Paper_018.md` is the wrong paper entirely (a category‑theory maths paper).** | Ch3 (L53, L177, L181), Ch4 (L57), Trustworthy_Revised (L3, L70, L78), Evaluation_Metrics (L85), Research_Gap_Analysis (L15) — **~9 uses** | **CRITICAL** |
| `tu2025amie` | Venue unverified — `note = {arXiv:2401.05654; TODO-VERIFY final venue}`; IEEE string says "[venue to verify]". | Ch3 (L7), Ch4 (L81), Ch5 (L112), Experimental_Design (L96) | HIGH |

**Action:** locate the real "Toward Trustworthy AI in Healthcare" paper (the intended P018), fill the full bibliographic record in **both** stores, and confirm it actually supports the ~9 claims that cite it. Until then this is the audit's single worst integrity exposure — it reads as a fabricated citation.

**Whole‑`.bib` caveat:** the file header states every entry "reflects best‑available metadata … verify each entry against the publisher of record … Do not submit without this pass." Treat all 45 as verify‑pending; prioritize the two above and any arXiv‑only entries that have since been formally published.

---

## 4. Files with ZERO inline citations (missing‑citation hotspots)

These make substantive, citable claims with **no references at all**:

| File | Note |
|---|---|
| `07_Thesis/Chapter_1/Chapter_1.md` | Superseded stub; `Chapter_1_Revised.md` is fully cited. |
| `07_Thesis/Chapter_2/AI_in_Healthcare.md` | Needs `thirunavukarasu2023llms`, `zhou2024survey`, `singhal2023clinical`, `tu2024generalist`. |
| `07_Thesis/Chapter_2/Large_Language_Models_in_Healthcare.md` | Needs `singhal2023clinical`, `singhal2025medpalm2`, `tu2024generalist`, `toma2023clinicalcamel`, `jin2021medqa`. |
| `07_Thesis/Chapter_2/LLM_Based_Agents.md` | Needs `yao2023react`, `park2023generative`, `wu2024autogen`, `li2023camel`, `hong2024metagpt`, `schick2023toolformer`, `wang2023voyager`, `lewis2020rag`. |
| `07_Thesis/Chapter_2/Agentic_AI_Frameworks.md` | Needs `wu2024autogen`, `li2023camel`, `hong2024metagpt`, `yao2023react`, `li2024agenthospital`. |
| `07_Thesis/Chapter_2/Taxonomy_of_LLM_Based_Agents.md` | Needs `xi2023rise`, `wang2024survey`, `sapkota2025agents` + per‑system keys. |
| `07_Thesis/Chapter_2/Trustworthy_AI_in_Healthcare.md` | Needs `rasheed2022explainable`, `jimenez2023trustworthy`, `lewis2020rag`. |
| `07_Thesis/Chapter_2/Chapter_Summary.md` | Recap; cite sparingly or not at all — but currently names ~10 systems with no keys. |
| `04_Architecture/Proposed_Framework.md` | Names ~12 systems, zero keys; unhedged claims. |
| `04_Architecture/Taxonomy.md` | Zero keys. |
| `03_Dataset/Preprocessing_Pipeline.md` | Zero keys (may be acceptable — procedural — but the MIMIC‑IV claims should cite `johnson2023mimic`). |

The **`_Revised` siblings and `Compiled/` versions already carry the right citations** — so for the Chapter‑2 items the fix is "finish the revision / adopt Compiled," not "invent references."

---

## 5. Claims that need a reference (representative, not exhaustive)

| Claim | File:line | Suggested existing key |
|---|---|---|
| "RAG reduces hallucinations and improves factual accuracy" (stated as fact) | `04_Architecture/Proposed_Framework.md:153` | `lewis2020rag`, `gao2023rag` |
| Med‑PaLM contributions / MultiMedQA evaluation | `Large_Language_Models_in_Healthcare.md:13‑24` | `singhal2023clinical` |
| Med‑PaLM 2 "expert‑level" benchmark performance | `…:30‑41` | `singhal2025medpalm2` |
| "ReAct combines reasoning traces with actions" | `LLM_Based_Agents.md:11` | `yao2023react` |
| "Toolformer … learn when and how to call external tools" | `Taxonomy_of_LLM_Based_Agents.md:160` | `schick2023toolformer` |
| MIMIC‑IV preprocessing / de‑identification claims | `03_Dataset/Preprocessing_Pipeline.md` | `johnson2023mimic` |

---

## 6. Duplicate / colliding citation keys

- **P017 key collision:** the Literature Matrix reassigns Paper_017 to `singhal2023clinical`, which is **already Paper_013's key**. Paper_016 and Paper_017 are the same Med‑PaLM M paper (`tu2024generalist`). Either the intended distinct P017 paper is missing a key, or the row is a duplicate. Resolve before building the numbered reference list.
- No duplicate `@article`/`@inproceedings` keys exist in `References.bib` itself.

---

## 7. Matrix papers never cited in the thesis body

All 20 matrix papers map to existing keys, and all are cited **somewhere** (mostly via the `Compiled/` chapters and Research‑Gap files). Watch‑items:
- `wang2023voyager`, `wang2023selfconsistency`, `yao2023tree`, `schick2023toolformer` — currently cited **only** inside `Compiled/Chapter_2.md`. If a section file (not Compiled) becomes the submission source, these citations vanish. Another reason to fix the canonical‑file decision (Consistency Report §10).

---

## 8. Style‑guide drift

`REVIEW/Style_And_Citation_Keys.md` instructs authors to "cite using ONLY the BibTeX keys below," but its table lists **34** keys while `References.bib` has **45**. Missing from the table: `hevner2004design`, `vincent1996sofa`, `es2024ragas`, `guo2017calibration`, `hardt2016equality`, `mehrabi2021survey`, `delong1988comparing`, `dietterich1998approximate`, `benjamini1995controlling`, `hayes2007krippendorff`, `singer2016sepsis3`. All 11 are legitimate and used. **Back‑port them into the style guide** so it stops under‑listing valid keys.

---

## 9. Action list (feeds `TODO_Citations.md`)

1. **CRITICAL:** verify/replace `jimenez2023trustworthy` in both `References.bib` and `build_thesis_docx.py`; confirm it supports its ~9 citing claims.
2. **CRITICAL:** verify `tu2025amie` venue.
3. Run the full 45‑entry `.bib` verification pass (publisher of record, DOIs, arXiv→published upgrades).
4. Standardize citation format to single‑key `[key]` brackets (build‑script compatible) — or fix `CITE_RE` to split `[a; b]`.
5. Add inline citations to the zero‑citation files (or adopt the `_Revised`/`Compiled` versions).
6. Keep `References.bib` ↔ `build_thesis_docx.py` IEEE dict in lockstep.
7. Resolve the P017/P013 key collision.
8. Update the style‑guide key table to 45.
