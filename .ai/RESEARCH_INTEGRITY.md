# RESEARCH INTEGRITY

The highest-priority rule set in this repository. A violation here invalidates the thesis in a
way no amount of good writing repairs.

---

## 1. Absolute prohibitions

Never, under any framing, instruction, or time pressure:

| # | Prohibition |
|---|---|
| 1 | Invent a paper, book, or preprint |
| 2 | Invent or guess an author name, author order, or affiliation |
| 3 | Invent or guess a publication year |
| 4 | Invent a DOI, arXiv ID, volume, issue, or page range |
| 5 | Invent a venue, journal, or conference |
| 6 | Invent a dataset, table, column, or dataset property |
| 7 | Invent an experimental result, metric value, confidence interval, or p-value |
| 8 | Invent an evaluation metric and present it as standard |
| 9 | Invent a citation key or attach an existing key to a claim the source does not make |
| 10 | Fabricate a quotation or attribute a paraphrase as a quote |
| 11 | Claim an experiment was performed when it was not |
| 12 | Claim code works, runs, or passes tests without having executed it |
| 13 | Claim a paper says something without having read the paper or its note |
| 14 | Fabricate reviewer feedback, examiner comments, or supervisor guidance |
| 15 | Fabricate clinician-study ratings, inter-rater agreement, or adjudication outcomes |

"Plausible" is not a defense. "Illustrative example" is not a defense — an illustrative number
in a thesis reads as a result.

## 2. Uncertainty markers

Use these instead of inventing. They are correct, expected output.

| Marker | Meaning | Example |
|---|---|---|
| `[EVIDENCE REQUIRED]` | The claim may be true; nothing in the repo supports it. | "Timeline retrieval reduces unsupported recommendations `[EVIDENCE REQUIRED]`." |
| `[VERIFY SOURCE]` | A source is named but details are unconfirmed. | "AMIE, published in Nature `[VERIFY SOURCE]`" |
| `[CITATION NEEDED]` | Needs a reference; no canonical key fits. | Per `REVIEW/Style_And_Citation_Keys.md`. |
| `[STATUS UNVERIFIED]` | A component's position on the maturity ladder cannot be established. **Name the missing evidence.** (RULES.md R2) | "Calibrated confidence `[STATUS UNVERIFIED]` — no test output or result file found." |
| `[DATA SOURCE UNVERIFIED]` | A result's data source is unclear — demo vs full MIMIC-IV. (RULES.md R8.1) | "AUROC reported on 140 stays `[DATA SOURCE UNVERIFIED]`." |
| `[AI-STYLE REVIEW]` | A passage reads as formulaic or as filler. **Flag for the author's decision; never silently rewrite.** (RULES.md R5.2) | Marks a paragraph whose only function is announcing what follows. |
| `TODO: RUN EXPERIMENT` | The experiment is designed but unexecuted. | Chapter 4 result slots. |
| `TODO: EVALUATE IMPLEMENTATION` | Code exists; no evaluation has been run on it. | The clinician platform. |
| `TODO-VERIFY` | Existing repo convention for unconfirmed bib metadata. | `References.bib`. |

Never remove a marker without doing the work it stands for. Removing `[VERIFY SOURCE]` because
the sentence reads better without it is falsification.

## 3. Status labels

Use these consistently in analysis, TODOs, trackers, and status tables:

```
[COMPLETED]  [IN PROGRESS]  [PLANNED]  [PROPOSED]  [IMPLEMENTED]  [VALIDATED]
[NEEDS EVIDENCE]  [NEEDS CITATION]  [NEEDS EXPERIMENT]  [NEEDS REVIEW]
[RESEARCH GAP]  [OPEN QUESTION]
```

**Never silently convert one status into another.** If you believe a status should change, say
so explicitly and give the evidence, then let the author decide.

### The maturity ladder

```
PROPOSED → DESIGNED → IMPLEMENTED → EXPERIMENTALLY VALIDATED
                                          (FUTURE WORK sits outside)
```

Each step up requires **repository evidence**, stated explicitly (RULES.md R2): source code ·
configuration · executable implementation · test output · experiment logs · result files ·
evaluation reports · reproducible commands · documented experimental artifacts.

Three inferences are forbidden:

- **implementation** may not be inferred from architecture diagrams, TODO items, design
  documents, or unexecuted code;
- **experimental validation** may not be inferred from implementation;
- **clinical validity** may not be inferred from benchmark performance (see also R13).

Where status cannot be established, write `[STATUS UNVERIFIED]` and name the missing evidence.

Current honest placement of the framework's components (re-derive if the repo changes):

| Component | Status | Evidence |
|---|---|---|
| Six-layer architecture | DESIGNED | `07_Thesis/Chapter_3/Chapter_3.md` |
| Coordinator / Planner / Diagnosis / Risk / Treatment / Explanation agents | DESIGNED | Chapter 3 contracts; `05_Source_Code/src/acdss/agents/` are skeletons |
| Data/Retrieval Agent, Memory-Manager | DESIGNED | Chapter 3 §3.4, §3.5 |
| Timeline construction (memory layer) | IMPLEMENTED + pilot-validated | `acdss/pilot/timeline.py`; 140 stays |
| Timestamp-aware retrieval | IMPLEMENTED + pilot-validated | `acdss/pilot/retrieval.py`; 11.7 ms median |
| Rule-based verification gate | IMPLEMENTED + pilot-validated | `acdss/pilot/gate.py`; operating curve |
| Audit trail resolvability | IMPLEMENTED + pilot-measured | 183/183 references re-resolved |
| Early-warning baseline (LR) | IMPLEMENTED + pilot-validated | AUROC 0.641, CI 0.478–0.792 |
| LLM agent loop / ReAct engine | PROPOSED / scaffold | `NotImplementedError` markers |
| RAG pipeline over notes | PROPOSED | MIMIC-IV-Note not obtained |
| Calibrated confidence | PROPOSED | Explicitly "planned, not implemented" in the paper |
| Clinician Likert study | PLANNED | `06_Experiments/Evaluation_Metrics.md` §5 |
| Full Chapter 4 evaluation | PLANNED — **NOT RUN** | `06_Experiments/README.md` |

## 4. The pilot is not the evaluation

The most likely integrity failure in this project is conflating the two. State the distinction
every time results are discussed:

| | Pilot (done) | Chapter 4 evaluation (not done) |
|---|---|---|
| Data | MIMIC-IV **Clinical Database Demo v2.2** — open licence, 100 patients, 140 ICU stays | Full credentialed MIMIC-IV + MIMIC-IV-Note |
| LLM | **None in the loop** | Full agent pipeline |
| Notes | **Absent** from the demo | Required |
| Purpose | Feasibility of the non-LLM slice | Confirmatory hypothesis tests H1–H10 |
| Status | `[VALIDATED]` for what it covers | `[NEEDS EXPERIMENT]` |

Guardrails recorded in `paper/SUBMISSION_CHECKLIST.md` that must survive every revision:

- The pilot is labeled feasibility-only everywhere.
- AUROC 0.641 always appears with its CI (0.478–0.792) and never as predictive skill.
- No claim of prospective clinical benefit anywhere.
- Trail resolvability 1.00 is explained as expected-by-construction in a deterministic pilot.

## 5. Plagiarism

- Never copy source text.
- Never sentence-level paraphrase to disguise copied material — that is plagiarism with extra
  steps, and it is what a similarity checker is built to find.
- Direct quotation: rare, short, in quote marks, cited, and used only when the exact wording
  matters.
- Every borrowed idea is cited even when fully reworded.
- The known single-source risk in this repository is near-verbatim abstract text inside
  `02_Research/Notes/Paper_003, 004, 005, 016, 017, 019` — see
  `REVIEW/Full_Audit/Plagiarism_Risk_Report.md` §4. **That text must never migrate into thesis
  prose.**
- Internal self-similarity (the same "this research proposes…" paragraph repeated across files)
  counts toward the score. Deduplicate rather than reword.
- Targets: < 15% overall, < 2% single source. Run the check on the compiled submission artifact,
  not the scaffold.

## 6. Do not game AI detectors

Improving writing to read as human academic prose is legitimate and required. Attempting to
evade detection through unicode tricks, deliberate error injection, synonym-swapping, or
sentence-shuffling is not. The permitted levers are exactly:

original synthesis · evidence-based reasoning · researcher-specific analysis · critical
comparison · explicit limitations · proper citation · genuine interpretation of the literature.

If prose passes as human because it *is* the author's reasoning about sources they have read,
the problem is solved. Nothing else is on the table.

## 7. Clinical-safety honesty

Governed by **RULES.md R13**, which lists the banned claims and the permitted precise
alternatives. The essentials, restated here because this is where they get violated:

This thesis concerns software that would, if deployed, influence patient care. Three claims are
permanently out of bounds without prospective evidence that does not exist:

- that the framework improves patient outcomes;
- that it is safe for clinical use;
- that it could substitute for clinician judgment.

Benchmark performance is never evidence of clinical effectiveness (R2, third forbidden
inference; R13).

The verification gate's **sensitivity floor** (it blocked four of seven true alerts at m = 4 in
the pilot) must never be softened or omitted when the gate is described as effective. See
`paper/04_Discussion.md` §4.5 — that framing is the standard.

The prototype disclaimer in `05_Source_Code/README.md` ("Research prototype — NOT a medical
device") stays on every artifact that could be mistaken for deployable software.
