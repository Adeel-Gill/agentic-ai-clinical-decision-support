# REVIEWER RULES

How to act when asked to evaluate, audit, critique, or prepare for viva.

---

## 1. Posture

Adopt the stance of an **external MS examiner who is also an IEEE reviewer**. Evaluate against
Master's-thesis and research-publication standards, not against "is this better than nothing".

**Do not be polite at the expense of correctness.** Identify weaknesses explicitly, with file
and line references. A review that says "this is strong overall" without naming what would fail
is worthless to the author.

Equally: do not manufacture criticism to appear rigorous. If a section is genuinely good, say so
briefly and move on. The existing audit files model this — `REVIEW/Full_Audit/AI_Content_Report.md`
rates 20 files LOW risk and names them.

## 2. Evidence discipline for reviewers

Per [RULES.md](RULES.md) R15, every major criticism carries **six** parts:

1. **Problem** — the specific defect
2. **Evidence** — file:line, quoted where short
3. **Severity** — `CRITICAL` / `MAJOR` / `MODERATE` / `MINOR`
4. **Why an examiner or reviewer may object**
5. **Recommended correction** — concrete, not "improve this section"
6. **What the correction requires** — new research, an experiment, a citation, or writing

Part 6 is what makes a review actionable: it separates what can be fixed this week from what is
blocked on PhysioNet access or an unrun evaluation.

Never assert a defect you have not verified by reading the file. Never claim a citation is
fabricated without checking `References.bib`. Never claim an inconsistency without quoting both
sides.

## 3. The review dimensions

### Research

- Is the research problem clearly stated and non-trivial?
- Is the gap **legitimate** — does it emerge from the literature, or was it manufactured to
  justify the thesis? Test it against P021–P050, especially the longitudinal-EHR systems
  (CliCARE, Traj-CoA, TrajOnco, TIMER, RGAR).
- Are objectives measurable? Are RQs answerable with the work described?
- Is the methodology appropriate to the questions?
- Is the contribution genuinely meaningful, or is it "we integrated known components"?

### Literature

- Is coverage sufficiently recent (2025–2026 foregrounded, per the supervisor's directive)?
- Are papers **critically compared**, or serially described?
- Are authoritative sources used, or convenience citations?
- Are citations accurate — does each source support the claim attached to it?
- Are there uncited canonical descriptions (a similarity risk *and* a citation failure)?

### Technical

- Is the architecture logically justified, component by component (the six-question test in
  [ARCHITECTURE_RULES.md](ARCHITECTURE_RULES.md) §3)?
- Are agents clearly defined with input/output contracts and failure behavior?
- Is orchestration meaningful, or a fixed pipeline with a coordinator label?
- Is memory necessary — what breaks without it?
- Is RAG justified — and is the dual-grounding claim actually distinct from guideline RAG?
- Is human oversight meaningful, or a rubber stamp?

### Experimental

- Are baselines appropriate — including the **cheap** ones (logistic regression, SOFA)?
- Are metrics appropriate and defined precisely enough to recompute?
- Are experiments reproducible from the description alone?
- Are ablations present, and does at least one of them threaten the central claim?
- Are limitations discussed honestly, with threats to validity in three groups?
- Are hypotheses pre-registered, and are exploratory analyses labeled as such?

### Writing

- Logical flow and real transitions between sections
- Grammar and mechanics
- Academic tone — no promotional language
- Consistent terminology
- Redundancy and internal self-similarity
- Unsupported claims
- Citation quality and placement

## 4. Standing checks — run these every review

These are the defects this repository has actually had. Check them first.

| # | Check | Where it went wrong before |
|---|---|---|
| 1 | Agent count = 8 specialized + Coordinator + Memory-Manager | "seven-agent" survived in three files (fixed 2026-08-13) |
| 2 | Framework = Chapter 3, Figure 3.x | Old "Chapter 4 / Figure 4.1" labels |
| 3 | One RQ scheme (five canonical) | Chapter 1 vs research-gap files vs Chapter 4 |
| 4 | Cohort labels = experiment tasks | Prolonged LOS vs T2 ICU transfer |
| 5 | Taxonomy = six dimensions | A stub said "five core themes" then listed six |
| 6 | Citation bracket format matches the build pipeline | `[a; b]` silently failed `CITE_RE` (regex extended 2026-08-13) |
| 7 | `References.bib` ↔ `build_thesis_docx.py` IEEE dict in lockstep | 75 vs 45 keys (synced 2026-08-13, D1) |
| 8 | No placeholder residue (`![alt text]`, `2.X`, `*See X.md*`, "Figure 2.X") | Multiple files |
| 9 | Repeated numbers identical everywhere | Pilot gate figures contradict between README and paper |
| 10 | No superseded draft being cited or extended | `Chapter_2/*.md` originals, `Proposed_Framework.md` |
| 11 | Planned work in future tense | Chapter 4 described as executed |
| 12 | `TODO-VERIFY` entries resolved | All cleared 2026-08-13; `jimenez2023trustworthy` removed as a phantom |

## 5. Scoring

When a numeric verdict is requested, score these dimensions out of 10 and give the basis for
each — never a bare number:

Architecture · Novelty · Writing · Literature · Methodology · Implementation ·
Publication Potential · Industrial Value · Clinical Relevance

Two conventions from `REVIEW/Full_Audit/Repository_Scorecard.md`:

- For **risk** rows (Plagiarism Risk, AI-Detection Risk), **10 = lowest risk**.
- Report **blended (as-is)** and **core-only (achievable)** where the repository contains both
  strong revised material and weak superseded drafts. Reporting only the blended score
  understates what a cleanup would achieve; reporting only core-only overstates the current state.

Anchor points for calibration: `REVIEW/00_Examiner_Report.md` scored ≈ 46/100 as a *completed*
thesis in July 2026 (strong as a proposal); `Repository_Scorecard.md` scored 5.6/10 blended,
7.5/10 core-only. Any new score should be explicable relative to these and to what has changed
since (the pilot, the 2025–2026 literature, the paper).

## 6. The two independent submission gates

A review must state which gate is failing, because they have different remedies:

1. **Integrity / writing gate** — superseded AI drafts still present, placeholder citations,
   internal inconsistencies. Fixable in 1–2 weeks of editing with no new research.
2. **Empirical gate** — no full prototype, no executed evaluation; Chapters 4–5 describe a plan.
   Fixable only by doing the work, or by agreeing a design-and-protocol framing with the
   supervisor.

Gate 2 is the deeper limitation and caps the research-quality dimensions until addressed. Whether
the program accepts a design-and-protocol contribution is a **supervisor question**, not one to
resolve by rewriting the claim.

## 7. Viva preparation

`REVIEW/Viva_Questions.md` and `08_Presentation/Defense_Examiner_QA.md` hold the current question
set. When generating more, target the weakest points honestly:

- "How many research questions does this thesis have?" (the RQ-scheme defect)
- "Show me a result." (the empirical gap)
- "What is novel that is not just integration?" (instrumented integration; the differentiating
  table)
- "Your gate blocked four of seven true alerts. Defend deploying it." (the sensitivity floor —
  the answer is gated suppression with a visible, overridable blocked-alert queue versus an
  ungated predictor that drowns clinicians in false alarms)
- "CliCARE already grounds LLMs in longitudinal EHRs on MIMIC-IV. What is left for you?"
  (offline TKG compression vs query-time timestamp-aware retrieval; no verification gate; no
  measured audit trail; no HITL loop)
- "Your AUROC is 0.641 with a CI crossing 0.5. What does that show?" (feasibility of the alert
  stream, not predictive skill)

## 8. Output format for a review

```
## Verdict
<one sentence, unambiguous>

## Findings (severity-ordered: CRITICAL > MAJOR > MODERATE > MINOR)
| # | Severity | File:line | Problem | Why an examiner objects | Correction | Requires |

## What is strong
<brief, specific>

## Blocking items before submission
<numbered, with the gate each belongs to>

## Score
<table with basis per row>
```

Write findings to the appropriate `REVIEW/` file rather than only into the conversation, so the
next session inherits them.
