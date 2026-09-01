# Skill — Scientific Editor

**Load with:** [ACADEMIC_WRITING.md](../ACADEMIC_WRITING.md),
[FORMATTING_RULES.md](../FORMATTING_RULES.md), [CITATION_RULES.md](../CITATION_RULES.md),
[QUALITY_CHECKLIST.md](../QUALITY_CHECKLIST.md)

**Use when:** line editing, de-AI passes, consistency sweeps, or formatting compliance.

---

## Role

Improve prose without changing meaning, and enforce consistency across a repository that has a
recorded history of drifting.

**Editing never changes a claim's strength.** If a sentence overclaims, flag it — do not quietly
soften it into something the author did not assert. If a sentence is unsupported, mark it
`[CITATION NEEDED]` — do not attach a plausible key.

## The de-AI pass

The dominant machine-writing signature here is **structural**, not connective-word abuse. Fix in
this order:

1. **Banned openers** — "represents the next evolution", "plays a crucial role", "In today's
   world", "It is worth noting", "has emerged as a transformative technology", "The rapid
   development of X has transformed", "provides a comprehensive and systematic".
2. **Bullet dumps** — fold into prose that also says *why* the items compose. Bullets < 20%.
3. **Uniform paragraph geometry** — vary deliberately; three lines then twelve.
4. **Per-item templates** — intro → bullets → diagram → "However, challenges remain", repeated.
   Give each item a shape driven by what is interesting about it.
5. **Missing critical sentence** — every subsection on prior work says what it does *not* do.
6. **Identical closing paragraphs** — delete; write a real bridge.
7. **Placeholder residue** — `![alt text]`, `2.X`, `*See X.md*`, "Figure 2.X".
8. **Promotional adjectives** — "landmark", "seminal", "state-of-the-art" without a comparison.

The model of the target style is `07_Thesis/Chapter_2/_Rewrite_Notes.md` §(c), which records five
before/after fixes. Six Chapter 2 sections still need this pass; the work order is §(b) of that
file.

## The consistency sweep

| Check | Canonical value |
|---|---|
| Agent count | 8 specialized + Coordinator + Memory-Manager module |
| Framework location | Chapter 3, Figure 3.1 |
| RQ scheme | Five (RQ1–RQ5); gap questions are derived sub-questions |
| Taxonomy | Six capability dimensions |
| Layers | Six horizontal + one cross-cutting + HITL |
| Terminology | "the proposed framework" · agent · module · layer |
| Spelling | US throughout |
| Voice | Ch1–2 impersonal; Ch3–5 first person; `paper/` first-person plural |
| Citation brackets | `[a][b]` for the docx build; `[a; b]` fails `CITE_RE` |

## The numerical sweep

Any number appearing in more than one file must be identical everywhere. Cross-check against
`06_Experiments/results/pilot/pilot_metrics.json`:

140 stays / 100 patients / 20 deaths · AUROC 0.641 (CI 0.478–0.792) · 11.7 ms / 17.9 ms ·
gate m = 4 pass rates 0.43 / 0.14 · 183 references / resolvability 1.00 · reference counts.

⚠️ Two inconsistencies are currently live — see `.ai/README.md` D1 and D2.

## Paragraph surgery

Split any paragraph carrying three distinct reasons. Known offenders are listed in
`REVIEW/Full_Audit/Writing_Quality_Report.md` §5 — Chapter 4 §4.2 cohort justification,
RAG_Revised §2.6.6, Chapter 3 §3.4.3 arbitration and §3.5 memory, Chapter 4 threats to validity.

Do not over-fragment in the other direction: bold header + two sentences, repeated, is a bullet
dump in disguise.

## Formatting compliance

Per `07_Thesis/Thesis_Formatting_Guide.md`: TNR throughout, body 12 pt, 1.5 spacing, justified,
0.5″ first-line indent, A4, 1″ margins with 1.25″ left. Headings 16/14/12/12-italic. Table
captions **above**, figure captions **below**. Roman front matter, decimal body, via section
breaks and field codes — never typed.

Every chapter's first paragraph overviews the whole chapter. This is a DOPS requirement.

## Grammar nits on record

`Notes/Paper_002.md:534` trailing "Support.s" · `Paper_007.md:72` "agents areAlphabetically" ·
`Paper_012.md:34` "strucutred" · orphaned commas throughout `Paper_019.md` (a copy-paste
forensic signature — those passages need rewriting, not just comma removal).

## Never

- Change a claim's strength while editing.
- Add a citation to fix an unsupported claim — mark it instead.
- Edit a superseded draft when a `_Revised` or `Compiled` sibling exists.
- Hand-edit a generated file (`_body_generated.tex`, `paper/references.bib`, `.docx`, `.pptx`).
- Remove a hedge, a limitation, or an uncertainty marker to improve flow.

## Deliver

Which files were edited, which categories of fix were applied, which claims were flagged rather
than changed, which inconsistencies were found, and which remain.
