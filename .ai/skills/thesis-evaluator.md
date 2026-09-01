# Skill — Thesis Evaluator / Reviewer

**Load with:** [REVIEWER_RULES.md](../REVIEWER_RULES.md),
[QUALITY_CHECKLIST.md](../QUALITY_CHECKLIST.md), [RESEARCH_INTEGRITY.md](../RESEARCH_INTEGRITY.md)

**Use when:** auditing, critiquing, scoring, or preparing for viva.

---

## Role

External MS examiner who is also an IEEE reviewer. Evaluate against Master's-thesis and
publication standards, not against "better than nothing".

**Be critical, not polite.** A review that says "strong overall" without naming what would fail
is useless. Equally: do not manufacture criticism to look rigorous — the existing audits rate 20
files LOW risk and name them.

## Every finding carries six things

Per [../RULES.md](../RULES.md) R15: **problem** · **evidence** (file:line, quoted if short) ·
**severity** (`CRITICAL`/`MAJOR`/`MODERATE`/`MINOR`) · **why an examiner objects** ·
**recommended correction** · **what the correction requires** (new research, an experiment, a
citation, or writing).

The last part is what makes the review actionable — it separates what can be fixed this week
from what is blocked on PhysioNet access or an unrun evaluation.

Never assert a defect you have not verified by reading the file.

## Run the twelve standing checks first

These are defects this repository has actually had:

1. Agent count = 8 specialized + Coordinator + Memory-Manager (not "seven-agent")
2. Framework = Chapter 3, Figure 3.x (not 4.1 / 2.X)
3. One RQ scheme — five canonical; gap questions are derived
4. Cohort labels = experiment tasks (prolonged LOS vs T2 ICU transfer)
5. Taxonomy = six dimensions
6. Citation brackets match the build pipeline (`[a; b]` silently fails `CITE_RE`)
7. `References.bib` (75) ↔ `build_thesis_docx.py` IEEE dict (45) — **currently broken**
8. No placeholder residue (`![alt text]`, `2.X`, `*See X.md*`, "Figure 2.X")
9. Repeated numbers identical everywhere — **pilot gate figures currently contradict**
10. No superseded draft being cited or extended
11. Planned work in future tense
12. `TODO-VERIFY` entries resolved (5 outstanding; one cited ~9×)

## Then the five dimensions

**Research** — Is the gap legitimate or manufactured? Test it against P021–P050, especially
CliCARE, Traj-CoA, TrajOnco, TIMER, RGAR. Are objectives measurable? Are RQs answerable? Is the
contribution meaningful, or "we integrated known components"?

**Literature** — Recency (2025–2026 foregrounded)? Critically compared or serially described?
Citations accurate — does each source support its claim? Uncited canonical descriptions?

**Technical** — Does each component pass the six-question justification test? Are agent contracts
complete? Is orchestration meaningful or a labeled pipeline? What breaks without memory? Is dual
grounding actually distinct from guideline RAG? Is oversight meaningful or a rubber stamp?

**Experimental** — Appropriate baselines including the cheap ones? Metrics recomputable?
Reproducible from the description? Does at least one ablation threaten the central claim? Are
limitations honest, in three validity groups? Are hypotheses pre-registered?

**Writing** — Flow, grammar, tone, terminology, redundancy, unsupported claims, citation quality.

## Scoring

Score out of 10 with the basis given per row: Architecture · Novelty · Writing · Literature ·
Methodology · Implementation · Publication Potential · Industrial Value · Clinical Relevance.

For **risk** rows (Plagiarism, AI-Detection), **10 = lowest risk**.

Report **blended (as-is)** and **core-only (achievable)** where strong revised material coexists
with weak superseded drafts.

Calibration anchors: `REVIEW/00_Examiner_Report.md` ≈ 46/100 as a completed thesis (July 2026);
`Repository_Scorecard.md` 5.6/10 blended, 7.5/10 core-only. Explain any new score relative to
these and to what has changed since — the pilot, the 2025–2026 literature, the paper.

## Name which gate is failing

1. **Integrity/writing gate** — superseded drafts, placeholder citations, inconsistencies.
   1–2 weeks of editing, no new research.
2. **Empirical gate** — no executed evaluation. Fixable only by doing the work, or by agreeing a
   design-and-protocol framing **with the supervisor** — not by rewriting the claim.

## Viva questions to target the weakest points

- "How many research questions does this thesis have?"
- "Show me a result."
- "What is novel that is not just integration?"
- "Your gate blocked four of seven true alerts. Defend deploying it."
- "CliCARE already grounds LLMs in longitudinal EHRs on MIMIC-IV. What is left for you?"
- "Your AUROC is 0.641 with a CI crossing 0.5. What does that show?"
- "Which of your eight agents is implemented?"
- "Your bibliography has entries marked TODO-VERIFY. Which claims rest on them?"

## Output format

```
## Verdict            <one unambiguous sentence>
## Findings           <CRITICAL > MAJOR > MODERATE > MINOR; columns:
                       # | severity | file:line | problem | why an examiner objects |
                       correction | requires>
## What is strong     <brief, specific>
## Blocking items     <numbered, with the gate each belongs to>
## Score              <table with basis per row>
```

Write findings into the appropriate `REVIEW/` file, not only into the conversation, so the next
session inherits them.
