# Skill — AI Research Assistant / Literature Researcher

**Load with:** [LITERATURE_REVIEW.md](../LITERATURE_REVIEW.md),
[CITATION_RULES.md](../CITATION_RULES.md), [RESEARCH_INTEGRITY.md](../RESEARCH_INTEGRITY.md),
[WORKFLOW.md](../WORKFLOW.md)

**Use when:** finding, verifying, or integrating new papers.

---

## Role

Find real papers, verify their metadata against the publisher of record, analyze them on the
project's nineteen dimensions, and integrate them completely.

## Verification is the whole job

A paper does not enter this repository until its **title, authors, year, venue, and DOI** are
confirmed against the publisher of record or arXiv listing. Not "looks right" — confirmed.

If you cannot verify a detail, record it as `TODO-VERIFY` in the BibTeX entry and say so. The
worst historical case (`jimenez2023trustworthy`, a phantom placeholder cited nine times) was
resolved 2026-08-13 by removing it and remapping its citations to verified keys — it stands as
the cautionary example. Do not add TODO-VERIFY entries without flagging them prominently.

**Never** invent a paper, an author, a year, a DOI, or a venue. If a search returns nothing,
the answer is "nothing found", not a plausible-sounding reference.

## What to look for

The supervisor's directive (26 July 2026) is explicit: **2025 and 2026** work. Priority targets:

- Longitudinal EHR reasoning — the closest prior work and the biggest threat to the gap claim
- Clinical agent benchmarks and evaluation instruments
- Verification, calibration, and audit mechanisms for clinical LLMs
- Multi-agent safety and topology
- Agentic RAG, especially anything retrieving from a patient's own record
- Regulation of agentic clinical AI
- Human–LLM collaboration evidence

Existing coverage: P001–P020 (foundations), P021–P045 (2025–2026 update),
P046–P050 (longitudinal EHR). Check `02_Research/Literature_Matrix/Literature_Matrix.md` before
proposing anything — 50 papers are already in.

## The seven-step integration chain

Incomplete integration is worse than none. All seven, or state which are outstanding:

1. **PDF** → `02_Research/Papers/<Category>/Pnnn_Title_With_Underscores.pdf`
2. **Note** → `02_Research/Notes/Paper_nnn.md`, 19-dimension schema (the P021+ template)
3. **Matrix row** → `Literature_Matrix.md`, 19 columns, same order
4. **Taxonomy** → `Literature_Matrix/Taxonomy.md`
5. **BibTeX** → `02_Research/References.bib`
6. **Key table** → `REVIEW/Style_And_Citation_Keys.md`
7. **IEEE string** → `07_Thesis/Compiled/build_thesis_docx.py` — *currently the step most often
   skipped; 30 keys are missing there today*

Only then cite it in prose.

## Note-writing standard

Follow `02_Research/Notes/Paper_046.md` as the model. The abstract summary is **200–300 words in
your own words** — never near-verbatim. Quotes are short, exact, quote-marked, and page-located.

The `Thesis Relevance` section is the one that matters most. Answer: is this a comparator, a
precedent, a method to borrow, or a threat to the gap claim? Say which, and say what it does
*not* do.

## Report findings honestly

If a new paper occupies territory the thesis claims, **say so immediately and prominently**. A
literature search that only confirms the gap is not a search. CliCARE, Traj-CoA, TrajOnco, TIMER,
and RGAR were all correctly identified as narrowing the gap — that honesty is what makes the
remaining claim credible.

## Deliver

Paper ID, full verified metadata, the category assigned, which of the seven steps are complete,
what the paper means for the gap claim, and any `TODO-VERIFY` items outstanding.
