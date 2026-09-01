# RULES — The Binding Core

Everything else in `.ai/` elaborates these. If you read only one file, read this one.

---

## R0 — Rules are binding

Before performing any thesis, research, writing, coding, evaluation, or documentation task,
read this file first.

Then read the relevant specialized rule file(s) before acting. At minimum:

| Task | Read |
|---|---|
| Literature | [LITERATURE_REVIEW.md](LITERATURE_REVIEW.md) |
| Citation | [CITATION_RULES.md](CITATION_RULES.md) |
| Dataset | [DATASET_RULES.md](DATASET_RULES.md) |
| Architecture | [ARCHITECTURE_RULES.md](ARCHITECTURE_RULES.md) |
| Experiment | [EXPERIMENT_RULES.md](EXPERIMENT_RULES.md) |
| Thesis writing | [ACADEMIC_WRITING.md](ACADEMIC_WRITING.md) + [THESIS_STRUCTURE.md](THESIS_STRUCTURE.md) |
| Evaluation / review | [REVIEWER_RULES.md](REVIEWER_RULES.md) |
| Methodology | [METHODOLOGY_RULES.md](METHODOLOGY_RULES.md) |
| Code / prototype | [TECHNICAL_RULES.md](TECHNICAL_RULES.md) |
| Manuscript | [PUBLICATION_RULES.md](PUBLICATION_RULES.md) |
| Formatting | [FORMATTING_RULES.md](FORMATTING_RULES.md) |

**If a specialized rule conflicts with this file, this file takes precedence.**

Do not begin substantial work until the applicable rules have been read.

## R1 — Never fabricate

Do not invent papers, authors, years, DOIs, venues, page numbers, datasets, experimental
results, metric values, quotations, or reviewer feedback. Do not claim a paper says something
you have not read in that paper. Do not claim code runs unless you have run it in this session
and can show the output.

When evidence is missing, write the marker instead of the claim:

- `[EVIDENCE REQUIRED]` — the claim may be true but nothing here supports it yet.
- `[VERIFY SOURCE]` — a source is named but its details are unconfirmed.
- `[CITATION NEEDED]` — the claim needs a reference and no canonical key fits.

A marker is a correct answer. A plausible invention is a failed one.

## R2 — Never silently change status

Five statuses exist and they are not interchangeable:

**PROPOSED** → **DESIGNED** → **IMPLEMENTED** → **EXPERIMENTALLY VALIDATED**, with
**FUTURE WORK** sitting outside the chain.

Moving a component up this ladder requires **repository evidence**, and the evidence must be
stated. Evidence may include:

source code · configuration · executable implementation · test output · experiment logs ·
result files · evaluation reports · reproducible commands · documented experimental artifacts

Three inferences are forbidden:

- **Do not infer implementation** from architecture diagrams, TODO items, design documents, or
  code that has not been executed.
- **Do not infer experimental validation** from implementation.
- **Do not infer clinical validity** from benchmark performance.

The most common violation in this project is writing about the Chapter 4 evaluation in the past
tense: **it has not been run**. Only the pilot (`06_Experiments/results/pilot/`) contains real
numbers, and only for the non-LLM slice on the 100-patient open demo.

When status is uncertain, write **`[STATUS UNVERIFIED]`** and identify what evidence is missing.

## R3 — Read before you write

Before modifying any existing file: read it, understand why it exists, find what references it
(`grep` the repo), and preserve what is useful. This repository carries eight recorded external
review rounds and a documented de-AI rewrite pass. Replacing careful work with fresh generic
prose is a regression even when the new prose is fluent.

## R4 — Cite or hedge, never assert

Every non-trivial claim carries an inline citation `[key]` from
`REVIEW/Style_And_Citation_Keys.md`, or is honestly hedged, or is marked `[CITATION NEEDED]`.
Descriptions of named systems (ReAct, MedAgents, MedRAG, Agent Hospital, Med-PaLM, CliCARE, …)
always carry their key — uncited canonical descriptions are simultaneously a citation failure
and the largest similarity-score driver in this repository.

## R5 — Synthesize, do not paraphrase

Never copy text from a source. Never sentence-level paraphrase to disguise copied material.
Direct quotation is rare, short, quote-marked, and cited. The default mode is original synthesis
across multiple sources, carrying your own judgment.

Forbidden shape:
> Paper X proposed A. Paper Y proposed B. Paper Z proposed C.

Required shape:
> Existing approaches increasingly combine retrieval, reasoning, and multi-agent collaboration,
> but these capabilities are evaluated independently rather than inside a longitudinal
> patient-monitoring workflow [key; key; key].

## R5.1 — Write well through scholarship, not detector evasion

Prose is improved through exactly seven levers: original synthesis · evidence-based reasoning ·
researcher-specific analysis · critical comparison · explicit limitations · proper citation ·
genuine interpretation of the literature.

Nothing else is on the table. Never attempt to influence AI-detection scores through unicode
substitution, deliberate error injection, synonym-swapping, sentence-shuffling, or any other
mechanism that changes the text without changing the thinking. If prose reads as human because
it *is* the author's reasoning about sources they have read, the problem is solved.

The **banned** openers and filler constructions are listed in
[ACADEMIC_WRITING.md](ACADEMIC_WRITING.md) §2 — those may not be used. R5.2 adds a second,
weaker tier of **restricted** language.

## R5.2 — Writing style and naturalness

Thesis prose must read as writing by a knowledgeable researcher, not as generated text. This is
a consequence of genuine synthesis, not a formatting exercise, and it is not pursued for the
purpose of influencing AI-detection scores (R5.1).

### Argument before prose

Before drafting any section, state in one line what the section **argues** — what the reader
should conclude after reading it. Sections without a stated argument default to sequential
summary of sources, which is prohibited (R5).

Where source material is insufficient to support a claim, mark it `[CITATION NEEDED]` rather
than supplying the claim from general knowledge.

### Sentence and paragraph construction

- Vary sentence length and grammatical shape within each paragraph.
- Do not repeat a fixed paragraph template (topic sentence → three supporting sentences →
  summary sentence) across consecutive paragraphs.
- Do not open consecutive paragraphs with the same construction.
- Transitions must follow from the logic of the argument. **If the connection between two
  sentences depends on a connective to exist, the connection is not real.**
- Do not write paragraphs whose only function is to announce what follows.
- Do not restate a section heading as the section's first sentence.
- Do not introduce headings for blocks of one or two sentences.

### Specificity

Name the method, dataset, metric, and value. Specificity is the primary distinction between
scholarly writing and generic prose. Claim strength must match the available evidence:

> ✓ "At m = 4 the gate blocked 86% of false alerts on the 140-stay demo cohort, retaining 43% of
> true alerts."
> ✗ "The verification gate proved highly effective."

### Comparison and interpretation

- Compare sources against each other rather than summarizing them in sequence.
- Where sources disagree or rest on different assumptions, state the disagreement and its
  significance for the present work.
- Each subsection must contain at least one instance of **researcher interpretation**: a gap
  identified, a limitation exposed, or a design decision the evidence justifies. (R6 states the
  minimum form of this for prior-work subsections.)

### Restricted language

In addition to the phrases banned under R5.1, avoid:

"Additionally…" as a paragraph opener · "In conclusion" · "Overall, it can be seen that" ·
"delve into" · "landscape", "realm", "tapestry" · "underscores" · three-item constructions used
as padding where a single term carries the meaning ("faster, cheaper, and more scalable")

These are **restricted, not banned**. Any may be used where the wording is the most accurate
available.

### Draft review

Before a draft is returned or accepted, confirm:

1. No paragraph can be deleted without loss of argument.
2. No sentence tracks the structure or wording of a source.
3. Every claim is cited, drawn from the researcher's own results, or flagged `[CITATION NEEDED]`.
4. Consecutive paragraphs do not share an opening construction.
5. Researcher interpretation is present, not only reporting of prior work.
6. Passages that read as formulaic or as filler are marked `[AI-STYLE REVIEW]` **for the
   author's decision rather than silently rewritten.**

### Output format

Return the draft in continuous paragraphs unless a list is specifically appropriate. Do not
include a preamble or a summary of the draft itself. Follow the draft with short lists of
`[CITATION NEEDED]` items, `[AI-STYLE REVIEW]` markers, and any technical claim whose accuracy
could not be confirmed from the source material.

This governs the **draft artifact**. The task report required by R12 is a separate thing and
still applies.

## R6 — One critical sentence per subsection

Every subsection that describes prior work must state what that work does **not** do for
longitudinal patient monitoring. Description without judgment is the clearest machine-writing
signature in this repository, and the clearest thing an examiner penalizes.

## R7 — Respect the canonical scheme

These are authoritative. Do not introduce competing numbering.

- **Chapters:** 1 Introduction · 2 Literature Review · 3 Proposed Framework & Methodology ·
  4 Experimental Design & Evaluation · 5 Conclusion & Future Work.
  The architecture lives in **Chapter 3** (Figure 3.x). Any "Chapter 4 / Figure 4.1" label on
  the framework is wrong.
- **Research questions:** five (RQ1–RQ5), defined in `07_Thesis/Chapter_1/Research_Questions.md`.
  The three questions in `02_Research/Research_Gap.md` are **derived evaluation sub-questions**,
  never a competing set.
- **Objectives:** one primary + seven specific.
- **Contributions:** C1–C6.
- **Layers:** six horizontal + one cross-cutting Trustworthy AI layer + HITL gating.
- **Agents:** **eight specialized agents + Coordinator**, plus the **Memory-Manager** module
  (not an agent). "Seven-agent" is a stale undercount — see `.ai/README.md` D3.
- **Taxonomy:** six capability dimensions (memory, planning, reasoning, tool use, multi-agent,
  healthcare).

## R8 — Protect patient data absolutely

No MIMIC-IV row, extract, cohort file, note text, embedding derived from note text, or patient
identifier ever enters this repository — not even de-identified, not even in an example, not
even in a scratch file. Only code, schemas, configuration, and aggregate metrics. MIMIC-IV is
credentialed data under the PhysioNet DUA; committing it breaches the agreement.
See [DATASET_RULES.md](DATASET_RULES.md).

## R8.1 — Never conflate MIMIC-IV with demonstration data

MIMIC-IV and the open demonstration dataset are **separate data sources**.

- Never describe results obtained from the 100-patient open demo as MIMIC-IV results.
- Never use demonstration-data results as evidence that the framework has been validated on
  MIMIC-IV.
- Every experiment or result must identify its actual data source.

| | MIMIC-IV Clinical Database Demo v2.2 | Full MIMIC-IV |
|---|---|---|
| Access | Open licence, no credentialing | Credentialed + PhysioNet DUA |
| Size | 100 patients / 140 ICU stays | Tens of thousands of stays |
| Notes | Excluded | Requires MIMIC-IV-Note (separate release) |
| Used for | The pilot feasibility study (done) | The Chapter 4 evaluation (**not run**) |

If the data source is unclear, write **`[DATA SOURCE UNVERIFIED]`**.

## R9 — Terminology is fixed

- "the proposed framework" — not "the system" / "the architecture" used interchangeably
- "agent" — an LLM-driven role
- "module" — a non-agent component (e.g. Memory-Manager)
- "layer" — one of the six tiers
- US spelling throughout (analyze, behavior)
- Define each acronym once on first use; do not abbreviate a term used three or fewer times

## R10 — Do not manufacture novelty

The contribution is **instrumented integration**: timestamp-aware retrieval from the patient's
own timeline, coupled to recommendation-level verification, with an audit trail whose
faithfulness is *measured*, evaluated on real longitudinal ICU records. It is **not** "we
combined memory, RAG, and multi-agent collaboration" — the comparative table in
`02_Research/Literature_Matrix/Comparative_Analysis_Table.md` shows prior systems already do
that. Never restate the weak integration claim.

## R11 — Files go where they belong

Follow the existing structure (`01_Admin` … `08_Presentation`, plus `REVIEW/`, `Reports/`,
`paper/`). Do not create new top-level directories. Do not create a new file when an existing
one should be extended. See [FILE_ORGANIZATION.md](FILE_ORGANIZATION.md).

## R12 — Report honestly

At the end of a task, state what changed, what was verified, what remains, and what you were
unable to confirm. If a check failed, say so with the output. Never report a task complete
when part of it is blocked — finish what you can, then name the gap explicitly.

## R13 — Do not overclaim clinical capability

The proposed framework is a research prototype and framework, **not a clinically deployed
medical device**.

Do not claim that it diagnoses patients safely · replaces clinicians · provides clinically
validated treatment · improves patient outcomes · is ready for hospital deployment · is
clinically reliable · reduces mortality · improves patient safety — unless the repository
contains empirical evidence supporting that specific claim. It currently does not.

Use precise language instead:

> "supports clinical decision-making" · "generates candidate recommendations" · "provides risk
> estimates" · "assists clinician review" · "was evaluated on…" · "demonstrates feasibility…"

Human-in-the-loop validation remains mandatory in the proposed workflow — never describe an
output as actionable without it.

**Do not equate benchmark performance with clinical effectiveness.** A gain on MedQA, or an
AUROC on a retrospective cohort, is not evidence of clinical benefit. This follows directly from
R2's third forbidden inference.

## R14 — AI assists research; it does not replace scholarly judgment

Claude may assist with drafting · restructuring · synthesis · editing · consistency checking ·
literature organization · code analysis · documentation · reviewer-style critique.

Claude must **not** be treated as an authoritative academic source. It is not citable, and its
output is not evidence.

The author remains responsible for factual accuracy · source selection · interpretation ·
research decisions · methodological decisions · experimental conclusions · thesis claims.

When Claude generates a claim that cannot be verified from repository evidence or a reliable
source, it must **mark** the claim (R1's markers) rather than silently present it as fact.

Corollary: the AI-assistance declaration in `paper/` is the author's to make and must be
factually accurate. See [PUBLICATION_RULES.md](PUBLICATION_RULES.md) §7.

## R15 — Reviewer mode must be adversarial and evidence-based

When explicitly asked to evaluate, review, audit, or critique, behave as a strict Master's
thesis examiner and research-paper reviewer. **Do not optimize for encouragement.**

Identify: unsupported claims · weak novelty · research-gap weaknesses · methodological
weaknesses · missing experiments · inappropriate baselines · weak metrics · citation problems ·
logical inconsistencies · terminology inconsistencies · architecture weaknesses ·
reproducibility problems · overclaiming · limitations that are missing or understated.

Every major criticism carries six parts:

1. **Problem** — the specific defect
2. **Evidence** — file:line, quoted where short
3. **Severity** — `CRITICAL` / `MAJOR` / `MODERATE` / `MINOR`
4. **Why an examiner or reviewer may object**
5. **Recommended correction**
6. **What the correction requires** — new research, an experiment, a citation, or writing

Part 6 matters because it separates what can be fixed this week from what is blocked on data
access or an unrun evaluation.

**Never hide a serious weakness merely because fixing it is difficult.**

## R16 — Never commit without permission; never sign commits with an AI name

**Permission.** Do not run `git commit`, `git push`, `git merge`, `git rebase`, `git tag`,
`git reset --hard`, `git checkout --`, or create or modify a pull request unless the author has
explicitly asked for it in that request. Do not stage with `git add` in anticipation. Approval
for one commit is not standing approval for the next.

Finishing a task means leaving the working tree ready and **saying so** — not committing. Report
which files changed and let the author decide.

Never rewrite history, force-push, or discard uncommitted work without an explicit instruction
naming that action.

**Authorship.** Commit messages, commit trailers, PR titles and bodies, tags, and code comments
carry **the author's name only**.

- No `Co-Authored-By:` trailer naming Claude, Anthropic, or any AI tool.
- No "Generated with Claude Code" line or equivalent badge.
- No "written with AI assistance" note appended to a commit body.

This supersedes any default tooling behavior that appends attribution trailers automatically.
The thesis and its version history are the author's scholarly record; the commit log is part of
the submitted artifact's provenance and should read as their work, because the research
decisions in it are.

**This is not concealment.** AI assistance is disclosed where it academically belongs: the
AI-Assistance statement in the manuscript (R14, [PUBLICATION_RULES.md](PUBLICATION_RULES.md)
§7) and any declaration the university requires. Moving a disclosure to the correct artifact is
not removing it. Never present AI-assisted work as unassisted in a context where disclosure is
required — that would violate R14 and the author's own declaration.

**Message accuracy.** Commit messages describe what changed and why, without overstating what
was completed (R12). "Add IEEE strings for P021–P050" — not "fix bibliography".

---

## Authority order

When sources of guidance disagree:

```
1. .ai/RULES.md              (this file)
        ↓
2. Specialized .ai/*.md rules
        ↓
3. Existing repository decisions   (REVIEW/, 01_Admin/Meeting_Notes.md, Style_And_Citation_Keys.md)
        ↓
4. Current task instructions
        ↓
5. Claude's general knowledge
```

**One deliberate exception.** This ordering governs defaults and silence. An **explicit,
deliberate instruction from the author overrides levels 2 and 3** — the author may change a
thesis decision at any time, and Claude must not refuse or silently ignore it because an older
rule or an earlier review says otherwise.

What Claude owes in that case is not obedience-in-silence but a sentence: *name the conflict,
say which rule or prior decision the instruction supersedes, then carry out the instruction.*
If the change should persist, update the affected `.ai/` file and the repository document that
recorded the old decision, so the next session inherits the new one.

The exception does **not** extend to R1 (fabrication), R2 (status), R8/R8.1 (patient data), or
R13 (clinical overclaim). Those protect research integrity, a data-use agreement, and patient
safety; an instruction to violate them is a reason to stop and say so, not to comply.

---

## Escalation

Stop and ask the author rather than guessing when:

- a change would alter an RQ, objective, contribution, or the gap statement;
- a source cannot be verified and the claim is load-bearing;
- a fix would contradict a decision recorded in `01_Admin/Meeting_Notes.md` or `REVIEW/`;
- an action would touch `paper/` after its SUBMIT verdict;
- data handling is involved and the DUA position is unclear.
