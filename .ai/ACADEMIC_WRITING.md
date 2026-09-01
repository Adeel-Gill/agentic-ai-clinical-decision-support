# ACADEMIC WRITING

The target voice is a Master's-level researcher who has read the sources, formed judgments, and
is willing to say what does not work. It is not a survey narrator and not a press release.

The canonical exemplars in this repository — read one before writing:

- `07_Thesis/Chapter_1/Chapter_1_Revised.md` — cited, varied, honest about scope
- `07_Thesis/Chapter_3/Chapter_3.md` — design-science voice, defended bets, per-agent contracts
- `07_Thesis/Chapter_2/Agentic_AI_Revised.md` — critical caveat in every subsection
- `02_Research/Research_Gap.md` — three concrete testable questions, no hand-waving
- `paper/04_Discussion.md` — narrow claims, named limitations

---

## 1. Non-negotiable style rules

From `REVIEW/Style_And_Citation_Keys.md`, which remains authoritative:

1. **Vary sentence length.** Avoid uniform 3–5 sentence paragraphs. Mix a short blunt sentence
   into a run of long analytical ones.
2. **Bullets under ~20%** of any section. Argue in prose. Tables are fine for genuinely tabular
   content (contracts, metrics, comparisons) — lists standing in for argument are not.
3. **Every non-trivial claim** gets an inline citation `[key]` or an honest hedge.
4. **One critical sentence per subsection** — what the cited work fails to do.
5. **Active voice; name the actor.** "The Coordinator routes…", not "work is routed…".
6. **US spelling** (analyze, behavior, modeling).
7. **Fixed terminology** — see [RULES.md](RULES.md) R9.

## 2. Banned openers

These are explicitly banned by the project style guide. Do not use them, and rewrite them when
found:

- "represents the next evolution"
- "plays a crucial role"
- "In today's world"
- "It is worth noting"
- "Furthermore, current research rarely"
- "One major limitation"
- "Another significant gap"

Extend the ban to their close relatives, which appear in the flagged HIGH-risk files:

- "has emerged as a transformative technology"
- "The rapid development of X has transformed…"
- "provides a comprehensive and systematic…"
- "landmark", "seminal", "state-of-the-art" as unearned praise
- "delve into", "leverage" as a verb of last resort, "robust" without a metric

### Restricted (weaker tier)

[RULES.md](RULES.md) R5.2 maintains a second list — "Additionally…" as a paragraph opener,
"In conclusion", "Overall, it can be seen that", "landscape"/"realm"/"tapestry", "underscores",
and padding triads. Those are **restricted, not banned**: usable where the wording is genuinely
the most accurate available. The list above is banned outright.

## 3. The structural AI signature

`REVIEW/Full_Audit/AI_Content_Report.md` established that the dominant machine-writing tell in
this repository is **structural**, not connective-word abuse. Watch for and eliminate:

| Signature | Fix |
|---|---|
| Uniform paragraph geometry (eight paragraphs of near-identical length) | Vary deliberately; let one paragraph be three lines and the next twelve |
| Bold header → three-sentence block, repeated | Convert to continuous argued prose with real transitions |
| Bullet dump replacing explanation | Fold into a sentence that also says *why* the items compose |
| Per-item templates (intro → bullets → ASCII diagram → "However, challenges remain") | Give each item its own shape driven by what is actually interesting about it |
| Description without judgment | Add the critical sentence |
| Identical closing paragraph across sections | Delete; write a real bridge to the next section |
| Placeholder residue: `*See X.md*`, `2.X`, `![alt text]`, "Figure 2.X" | Strip repo-wide |

## 4. Before / after

The project's own recorded fixes (`07_Thesis/Chapter_2/_Rewrite_Notes.md`) define the target.

**Banned opener → concrete cited claim**

> ✗ "Agentic AI represents the next evolution of intelligent systems by enabling autonomous
> agents to reason, plan, collaborate…"

> ✓ "Large Language Models made text generation cheap and fluent, and in doing so they exposed
> how little fluency alone accomplishes when a task requires acting over time. Out of that gap
> grew Agentic AI: systems that do not merely produce text but analyze a situation, form a plan,
> take actions, and adjust when the environment answers back [xi2023rise; wang2024survey]."

**Uncited name-drop list → cited critical prose**

> ✗ "MedAgents introduced collaborative medical reasoning. MedRAG combined retrieval. Agent
> Hospital explored simulation. Clinical Camel investigated open models."

> ✓ "MedAgents shows that role specialization improves answer quality, though its evaluation
> centers on question answering rather than on monitoring a patient over time
> [tang2024medagents]."

**Overclaim → honest limitation**

> ✗ "By retrieving verified clinical evidence before generating a response, RAG reduces the
> probability of unsupported recommendations."

> ✓ "It does not eliminate it: a model can still misread, over-generalize, or selectively use a
> correctly retrieved passage, so retrieval lowers the hallucination rate without driving it to
> zero, and clinical use has to be designed around the residue."

## 5. Claim calibration

Match the verb to the evidence:

| Evidence | Permitted phrasing |
|---|---|
| Measured in the pilot | "the pilot measured", "in this pilot, X was Y (95% CI …)" |
| Reported by a cited source | "X reports", "X finds", with the key |
| Design intent, unbuilt | "the framework is designed to", "will be evaluated" |
| Hypothesis | "we expect", "H3 predicts", with the falsification condition |
| Unknown | `[EVIDENCE REQUIRED]` |

Never: "proves", "guarantees", "ensures safety", "eliminates hallucination", "significantly
improves" without a test, "state-of-the-art" without a comparison table.

## 6. Voice policy

Recorded, deliberate, and to be applied consistently
(`REVIEW/Full_Audit/Writing_Quality_Report.md` §8):

- **Chapters 1–2:** impersonal, third-person.
- **Chapters 3–5:** first person is permitted and used ("I adopt this stance", "I flag two
  components…") because they are the author's design and methodology.
- **`paper/`:** first-person plural ("we claim", "our evaluation design"), matching the
  submitted manuscript.

Do not mix within a chapter. Confirm the DOPS template permits first person before extending
it — `07_Thesis/Thesis_Formatting_Guide.md` §12 prescribes "objective, third-person tone" for
general academic writing, so first person in Ch3–5 is a house choice that must be defended if
challenged.

## 7. Paragraph discipline

- Split any paragraph carrying three distinct reasons into three paragraphs. Known offenders
  are listed in `REVIEW/Full_Audit/Writing_Quality_Report.md` §5.
- Do not over-fragment in the other direction: bold header + two sentences, repeated, is a
  bullet dump wearing a disguise.
- Every chapter's **first paragraph** must overview the whole chapter — what it covers, its
  contents, its structure. This is a DOPS template requirement, not a stylistic preference.
- Every section needs a real transition from the previous one, not a fresh generic opener.

## 8. Chapter openings and closings

**Openings** state a concrete claim and take a stance. Model:

> "Modern hospitals produce clinical data faster than clinicians can read it."

**Closings** argue what was and was not shown. A summary that restates the section without
adding judgment is a wasted section. `07_Thesis/Chapter_3/Chapter_3.md` §3.9 and
`Chapter_4.md` §4.9 are the models; `07_Thesis/Chapter_2/Chapter_Summary.md` is the
anti-model (pure name-drop recap, uncited).

## 9. Numbers in prose

- Report a metric with its uncertainty every time (CI, IQR, or n).
- Report n alongside any rate.
- State the denominator: "four of seven true alerts", not "many alerts".
- Never round a number differently in two places — the numerical-consistency sweep in
  `paper/SUBMISSION_CHECKLIST.md` exists because this happened.
- When quoting a pilot number, cross-check it against
  `06_Experiments/results/pilot/pilot_metrics.json`, which is the source of record.
