# Skill — Literature Review Assistant

**Load with:** [LITERATURE_REVIEW.md](../LITERATURE_REVIEW.md),
[ACADEMIC_WRITING.md](../ACADEMIC_WRITING.md), [CITATION_RULES.md](../CITATION_RULES.md)

**Use when:** writing or revising Chapter 2 and the comparative tables.

---

## Role

Turn fifty analyzed papers into an argument. Not a catalogue.

## The organizing principle

Organize by **theme, capability, and disagreement** — never by paper. A given system may appear
in several places and need not have its own paragraph anywhere.

The spine that already works (`07_Thesis/Compiled/Chapter_2.md`):

```
2.1 intro → 2.2 LLMs and agents → frameworks → taxonomy → clinical systems →
RAG → trustworthy AI → 2.9 research gap → 2.10 summary → 2.11 recent advances
```

Each transition must carry an argument, not just a topic switch.

## For each system, three moves

1. What it does — one sentence, in your own words, cited.
2. What it establishes — the finding this thesis builds on.
3. **What it does not do** for longitudinal patient monitoring — the critical sentence.

Then compare across systems. Where do they agree? Where do they diverge? What does no one do?

## The comparative table is the gap's proof

`02_Research/Literature_Matrix/Comparative_Analysis_Table.md` carries two blocks:

- **General capabilities** — nearly everything ticks everything. This is *why* the integration
  claim is weak.
- **Differentiating capabilities** — patient-timeline RAG · verification gate · longitudinal
  memory · real ICU data · faithful audit trail. No prior row carries more than one.

Rules: every ❌ must be defensible; keep the paragraph that explains the honest ratings (MetaGPT
and Agent Hospital *do* have some persistent memory; MedRAG *does* retrieve from EHR databases) —
without it the table is a strawman. If a new paper ticks a differentiating column, add the row.

## Recency

2025–2026 work is foregrounded, per the supervisor's directive. Any claim about the current
state of the field must engage P021–P050, not stop at 2023–2024. The five longitudinal-EHR
systems (CliCARE, Traj-CoA, TrajOnco, TIMER, RGAR) are the most dangerous to overlook — they are
the nearest prior work.

## Maintain the three-way sort

`02_Research/Research_Gap.md` sorts the field into **effectively solved / partially solved /
still open**. Conceding what the field has settled makes the remaining claim stronger, not weaker.
Keep that structure whenever the gap is restated.

## Files: canonical vs superseded

| Canonical | Superseded — do not extend |
|---|---|
| `07_Thesis/Compiled/Chapter_2.md` | most `Chapter_2/*.md` originals |
| `Chapter_2/*_Revised.md` | their non-revised siblings |

Six sections still need the de-AI + citation pass. The work order is
`07_Thesis/Chapter_2/_Rewrite_Notes.md` §(b): `AI_in_Healthcare`,
`Large_Language_Models_in_Healthcare`, `LLM_Based_Agents`, `Agentic_AI_Frameworks`,
`Taxonomy_of_LLM_Based_Agents`, `Chapter_Summary`. Suggested keys per file are listed there and
in `REVIEW/Full_Audit/Citation_Audit.md` §4.

`Research_Gap.md` and `Research_Gap_Analysis.md` are owned separately — check before editing.

## Never

- Write "Paper X proposed… Paper Y proposed…"
- Describe a named system without its citation key.
- Repeat the "this research proposes…" closing boilerplate.
- Praise without a limitation ("landmark", "seminal", "state-of-the-art").
- Claim a paper says something not recorded in its note.
- Suppress a competitor that occupies claimed territory.

## Deliver

Which sections were revised, which citations added, which systems gained a critical sentence,
what the change means for the gap claim, and which sections still need the pass.
