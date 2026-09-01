# WORKFLOW — The Nine Phases

Every substantial thesis task runs these phases in order. Small edits may compress phases 2–4,
but phases 6, 7, and 8 are never skipped.

---

## Phase 1 — Understand the request

Restate the task in one sentence, and classify it:

| Class | Examples | Primary skill |
|---|---|---|
| Write | draft/revise chapter prose | `thesis-writer` |
| Review | audit, critique, viva prep | `thesis-evaluator` |
| Research | find/verify papers, extend the matrix | `literature-researcher` |
| Design | architecture, agents, diagrams | `architecture-reviewer` |
| Data | cohort, preprocessing, MIMIC-IV | `dataset-analyst` |
| Experiment | protocol, results, metrics | `experiment-reviewer` |
| Edit | line editing, consistency, de-AI | `academic-editor` |
| Publish | `paper/` manuscript | `publication-writer` |

If the request is ambiguous in a way that changes the work materially, ask **now** — not after
producing something wrong. If it is ambiguous in a way a careful colleague would resolve
themselves, resolve it and state the assumption.

## Phase 2 — Inspect the repository

Never write from memory of what the repo probably contains. Actually read:

- the target file, in full;
- the files it references and the files that reference it (`grep -rn "<filename>" --include="*.md"`);
- `REVIEW/Style_And_Citation_Keys.md` for keys and voice;
- the relevant `.ai/` rule file;
- `01_Admin/Progress_Tracker.md` for current status of whatever you are about to describe.

For claims about prior work, read the **paper note** in `02_Research/Notes/` — that is the
project's record of what the paper actually says. If no note exists, the claim is unsupported.

## Phase 3 — Identify dependencies

Before editing, list what else must stay consistent:

- Does this touch an RQ, objective, contribution, or the gap statement?
- Does another chapter cross-reference this section or figure number?
- Does the compiled build (`07_Thesis/Compiled/build_thesis_docx.py`) consume it?
- Is the same fact stated elsewhere (numbers repeated across pilot README, paper, tracker)?
- Is there a `_Revised` or `Compiled` sibling that is the canonical version?

Editing a superseded draft instead of its canonical sibling is the most common wasted-work
failure in this repository.

## Phase 4 — Perform the work

Apply the rules for the class of work. Preserve existing structure and voice. Improve rather
than replace. Where you make a judgment call, make it visible in the text (a hedge, a stated
assumption, a `[VERIFY SOURCE]` marker) rather than burying it.

## Phase 5 — Cross-check against thesis objectives

Trace what you wrote back up the chain:

```
Research Question → Objective → Research Gap → Methodology →
Framework → Experiment → Result → Conclusion
```

Ask: which RQ does this serve? Which objective? If the answer is "none", either the work is
out of scope or the chain has a hole worth reporting.

## Phase 6 — Check academic integrity

Non-negotiable gate:

- [ ] Every citation key exists in `02_Research/References.bib`.
- [ ] Every cited claim is one the source actually makes (check the note).
- [ ] No fabricated author, year, venue, DOI, metric, or result.
- [ ] No status upgrade without evidence (`PROPOSED` → `IMPLEMENTED`, planned → completed).
- [ ] No copied or lightly-paraphrased source text.
- [ ] Uncertainty is marked, not smoothed over.

## Phase 7 — Check cross-chapter consistency

- [ ] Chapter/figure/table numbers follow the canonical scheme (framework = Chapter 3).
- [ ] Agent count is eight specialized + Coordinator + Memory-Manager module.
- [ ] RQ references point at the five canonical RQs.
- [ ] Terminology matches R9 ("the proposed framework", agent/module/layer).
- [ ] Any number repeated elsewhere (pilot metrics, cohort size, entry counts) still matches
      every other place it appears.
- [ ] Tense discipline: "will be evaluated" for planned, "was evaluated" only for the pilot.

## Phase 8 — Report what changed

State plainly:

- files created / modified / deleted, with paths;
- what was verified and how;
- what claims carry markers and why;
- anything you deliberately did not touch, and why.

## Phase 9 — Report remaining work

Name what is still open, in priority order, and where it is tracked
(`01_Admin/TODO.md`, `REVIEW/TODO_Prioritized.md`, `REVIEW/Full_Audit/TODO_*.md`). If the task
surfaced a new defect, add it to the appropriate TODO file rather than only mentioning it in
conversation.

---

## Special workflow: "complete the thesis"

Do **not** respond by generating missing chapters. Run an audit first:

1. Inventory what is complete, in progress, planned, and absent.
2. Identify weak work (uncited, list-heavy, superseded drafts still in place).
3. Identify contradictions (see `.ai/README.md` "Known live defects" and
   `REVIEW/Full_Audit/Consistency_Report.md`).
4. Identify missing evidence, missing experiments, missing citations.
5. Produce a **prioritized TODO** distinguishing what can be written now from what is blocked
   on data access, prototype work, or experimental results.
6. Then work the list in order, one item at a time, reporting after each.

Fabricating experimental evidence to "finish" Chapters 4 and 5 is the worst possible outcome
of this request. The honest answer to "finish the thesis" is: *the writing can be finished; the
empirical chapters cannot, until the evaluation is run.*

## Special workflow: adding a new paper

1. Verify the paper exists and its metadata (title, authors, year, venue, DOI) against the
   publisher of record.
2. PDF → `02_Research/Papers/<Category>/Pnnn_Title_With_Underscores.pdf`.
3. Note → `02_Research/Notes/Paper_nnn.md` using the 19-dimension schema
   (see [LITERATURE_REVIEW.md](LITERATURE_REVIEW.md)).
4. Matrix row → `02_Research/Literature_Matrix/Literature_Matrix.md` (19 columns, same order).
5. Taxonomy mapping → `02_Research/Literature_Matrix/Taxonomy.md`.
6. BibTeX entry → `02_Research/References.bib`; add the key to
   `REVIEW/Style_And_Citation_Keys.md`.
7. **Also** add the IEEE string to `07_Thesis/Compiled/build_thesis_docx.py` — the two stores
   must stay in lockstep or the compiled document prints `[MISSING REFERENCE]`.
8. Only then cite it in prose.
