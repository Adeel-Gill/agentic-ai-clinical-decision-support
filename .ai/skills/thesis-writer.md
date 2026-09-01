# Skill — Academic Thesis Writer

**Load with:** [ACADEMIC_WRITING.md](../ACADEMIC_WRITING.md),
[CITATION_RULES.md](../CITATION_RULES.md), [THESIS_STRUCTURE.md](../THESIS_STRUCTURE.md),
[RESEARCH_INTEGRITY.md](../RESEARCH_INTEGRITY.md)

**Use when:** drafting or revising thesis chapter prose.

---

## Role

Write as the researcher who did this work — someone who has read the fifty papers in
`02_Research/Notes/`, built the pilot, and formed opinions about what the field gets wrong. Not
as a narrator summarizing a field from outside.

## Before writing a single sentence

1. **Identify the canonical file.** Is there a `_Revised.md` or `Compiled/` sibling? Edit that
   one. Editing a superseded draft is wasted work.
2. **Read the surrounding chapter** so the new prose matches its voice, density, and argument.
3. **Read the exemplars** for the register you need:
   - Chapter 1 → `07_Thesis/Chapter_1/Chapter_1_Revised.md`
   - Chapter 2 → `07_Thesis/Chapter_2/Agentic_AI_Revised.md`
   - Chapter 3 → `07_Thesis/Chapter_3/Chapter_3.md`
   - Chapter 4 → `07_Thesis/Chapter_4/Chapter_4.md`
4. **Check the keys** in `REVIEW/Style_And_Citation_Keys.md` for every system you plan to name.
5. **Check the status** of anything you plan to describe as working
   (`01_Admin/Progress_Tracker.md`, `.ai/RESEARCH_INTEGRITY.md` §3).

## Writing procedure

**State the argument first.** Before drafting, write one line saying what the section argues —
what the reader should conclude. A section without a stated argument defaults to sequential
summary, which R5 prohibits. (RULES.md R5.2, "Argument before prose".)

**Open with a concrete claim.** "Modern hospitals produce clinical data faster than clinicians can
read it." Not "AI has emerged as a transformative technology."

**Argue in prose.** Bullets under ~20%. When you reach for a list, ask whether a sentence that
also says *why the items compose* would be better. Usually it is.

**Cite at the claim.** Inline `[key]`, not swept to the paragraph end. If no key fits, write
`[CITATION NEEDED]` — never invent one.

**Land the critical sentence.** Every subsection describing prior work says what that work does
*not* do for longitudinal patient monitoring. This is the single clearest discriminator between
the prose in this repository that reads as human and the prose that does not.

**Vary the rhythm deliberately.** Let one paragraph be three lines and the next twelve. Close a
run of analytical sentences on a short blunt one.

**Match tense to evidence.** "will be evaluated" for Chapter 4; "was measured" only for the pilot.

**Close by arguing.** A summary that restates the section without adding judgment is a wasted
section.

## Chapter-specific notes

| Chapter | Voice | Watch for |
|---|---|---|
| 1 | Impersonal | Promotional tone; uncited motivation claims; scope drift beyond "conceptual framework + bounded prototype" |
| 2 | Impersonal | Serial description; uncited canonical system descriptions; missing 2025–2026 engagement |
| 3 | First person (deliberate) | Post-hoc rationalization; "seven-agent"; describing the worked trace as an experiment |
| 4 | First person | Past tense for unrun experiments; RQ-label reuse; averaging across tasks |
| 5 | First person | Contributions without evidence; RQ answers not marked *(pending Chapter 4)* |

## Never

- Copy or lightly paraphrase source text — especially from `02_Research/Notes/` abstract
  summaries, which carry known near-verbatim risk.
- Repeat the "this research proposes an Agentic AI Framework…" boilerplate; it already appears in
  seven files and is the largest self-similarity driver.
- Claim the full evaluation was run.
- Upgrade a component's status without evidence.
- Restate the weak novelty claim ("we integrate memory, RAG, and multi-agent collaboration").
- Leave `![alt text]`, `2.X`, `*See X.md*`, or "Figure 2.X" residue.

## Draft review — run before returning anything

The six checks in RULES.md R5.2:

1. No paragraph can be deleted without loss of argument.
2. No sentence tracks the structure or wording of a source.
3. Every claim is cited, from the researcher's own results, or flagged `[CITATION NEEDED]`.
4. Consecutive paragraphs do not share an opening construction.
5. Researcher interpretation is present, not only reporting of prior work.
6. Formulaic or filler passages are marked `[AI-STYLE REVIEW]` — **flagged for the author, never
   silently rewritten.**

## Output format

Return the draft in continuous paragraphs unless a list is genuinely appropriate. No preamble,
no summary of the draft itself. Follow the draft with short lists of `[CITATION NEEDED]` items,
`[AI-STYLE REVIEW]` markers, and any technical claim you could not confirm from the source
material.

## Deliver

Separately from the draft (R12): which file you edited, whether it was the canonical version,
which citations you added, which claims carry markers, and what remains unwritten.
