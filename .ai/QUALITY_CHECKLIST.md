# QUALITY CHECKLIST

Run before declaring **any** thesis task complete. Do not report done with unchecked boxes —
report the unchecked ones instead.

---

## The eighteen-point gate

```
[ ] Academic quality checked
[ ] Research claims verified
[ ] Citations checked
[ ] No fabricated references
[ ] No unsupported claims
[ ] Terminology consistent
[ ] Research gap consistent
[ ] Objectives consistent
[ ] Research questions consistent
[ ] Methodology consistent
[ ] Architecture consistent
[ ] Dataset claims verified
[ ] Implementation claims verified
[ ] Experimental claims verified
[ ] Limitations documented
[ ] Future work separated from completed work
[ ] Markdown formatting checked
[ ] File placed in correct directory
```

---

## What each check actually means

### Academic quality
- Sentence length varies; no uniform paragraph geometry.
- Bullets under ~20% of the section.
- At least one critical sentence per subsection describing prior work.
- No banned openers (see [ACADEMIC_WRITING.md](ACADEMIC_WRITING.md) §2).
- Active voice; the actor is named.
- US spelling.

### Research claims verified
- Every empirical claim traces to a source, a pilot result, or a marker.
- No claim exceeds what its evidence supports.
- Verbs match the evidence tier (measured / reports / is designed to / expect).

### Citations
- Every key exists in `02_Research/References.bib`.
- Every key is in `REVIEW/Style_And_Citation_Keys.md`.
- Every key is in `07_Thesis/Compiled/build_thesis_docx.py`'s IEEE dict **if** the text feeds
  the compiled build.
- Bracket format matches the destination pipeline (`[a][b]`, not `[a; b]`, for the docx build).
- Each source actually supports the claim attached to it — checked against the paper note.

### No fabricated references
- No invented author, year, venue, DOI, or page range.
- `TODO-VERIFY` entries are not treated as verified.
- `jimenez2023trustworthy` was resolved 2026-08-13: a phantom reference, removed; its citations
  now rest on `rasheed2022explainable`, `tan2026undcs`, `weissman2025unregulated`. No claim may
  cite it again.

### No unsupported claims
- No "proves", "guarantees", "ensures safety", "eliminates hallucination".
- No "significantly" without a test.
- No prospective clinical-benefit claim anywhere.

### Terminology consistent
- "the proposed framework" · "agent" (LLM-driven role) · "module" (non-agent) · "layer" (one of
  six tiers).
- Acronyms defined once on first use; not abbreviated if used three or fewer times.

### Research gap consistent
- Matches `02_Research/Research_Gap.md` and Chapter 2 §2.9.
- Presented as solved / partially solved / open.
- Survives a check against P021–P050, especially CliCARE, Traj-CoA, TrajOnco, TIMER, RGAR.
- Never restates the weak "no unified framework integrates everything" claim.

### Objectives / RQs consistent
- Five canonical RQs; the three gap questions presented as **derived sub-questions**.
- One primary + seven specific objectives.
- Chapter 4 uses H1–H10 as handles, not re-defined RQ labels.

### Methodology consistent
- Design-science framing preserved, including the post-hoc-rationalization caveat.
- Tense discipline: "will be evaluated" for the full evaluation; "was measured" only for the pilot.
- Reproducibility elements present: seeds, pinned versions, config-driven runs, fixed manifest.

### Architecture consistent
- Six layers + cross-cutting Trustworthy AI layer + HITL.
- **Eight specialized agents + Coordinator + Memory-Manager module.** No "seven-agent".
- Framework figure is **Figure 3.1** (Chapter 3), never 4.1 or 2.X.
- Every component passes the six-question justification test.

### Dataset claims verified
- MIMIC-IV module structure correct; notes are a **separate** credentialed release.
- No `NOTEEVENTS` reference.
- Relative time only.
- Demo (100 patients / 140 stays, open licence) never conflated with full credentialed MIMIC-IV.
- **No patient data staged for commit** — verified with `git status`.

### Implementation claims verified
- Each capability assigned to the right bucket: pilot-validated / implemented-not-evaluated /
  scaffold / designed-only.
- No claim that code runs without having run it this session.
- The "Research prototype — NOT a medical device" disclaimer present where needed.

### Experimental claims verified
- Nothing described as executed that has not been.
- Pilot numbers cross-checked against `06_Experiments/results/pilot/pilot_metrics.json`.
- AUROC 0.641 carries CI 0.478–0.792.
- Resolvability 1.00 explained as expected-by-construction.
- The gate's sensitivity floor stated wherever the gate is called effective.

### Limitations documented
- Present in the section itself, not deferred entirely to Chapter 5.
- Threats to validity grouped internal / external / construct.
- Each metric's construct caveat travels with the metric.

### Future work separated
- Nothing in a contributions or results section that is actually future work.
- Future-work items anchored to a named limitation.

### Markdown formatting
- Headings nest correctly; no skipped levels.
- Tables render; pipes escaped where needed.
- Links resolve (relative paths from the file's own location).
- No placeholder residue: `![alt text]`, `2.X`, `*See X.md*`, "Figure 2.X".

### File placement
- Correct directory per [FILE_ORGANIZATION.md](FILE_ORGANIZATION.md).
- Conventional filename.
- Not a superseded draft being extended.
- Generated files regenerated, not hand-edited.

---

## Numerical-consistency sweep

Any number appearing in more than one file must be identical everywhere. Currently repeated:

| Figure | Appears in |
|---|---|
| 140 ICU stays / 100 patients / 20 deaths | pilot README, `pilot_metrics.json`, `paper/05_Pilot_Study.md`, `Progress_Tracker.md`, README |
| AUROC 0.641, CI 0.478–0.792 | pilot README, paper, checklist |
| 11.7 ms / 17.9 ms retrieval | pilot README, paper, README |
| Gate at m = 4 (pass rates 0.43 / 0.14) | pilot README table, pilot README prose, `paper/04_Discussion.md` §4.5, `Progress_Tracker.md` |
| 183 references / resolvability 1.00 | pilot README, paper |
| Reference counts (75 master / 59 paper / 45 build-script dict) | `Progress_Tracker.md`, `paper/README.md`, checklist |

⚠️ Two of these are currently inconsistent — see `.ai/README.md` D1 and D2.

---

## Before committing

- [ ] **The author explicitly asked for a commit in this request** (R16). If not, stop here:
      report what changed and leave the working tree ready.
- [ ] `git status` shows no data file, `.env`, or scratch artifact staged
- [ ] Generated artifacts regenerated from source, not hand-edited
- [ ] Trackers updated (`01_Admin/TODO.md`, `Progress_Tracker.md`, or a `REVIEW/TODO_*.md`)
- [ ] The change is described accurately in the commit message — no overstatement of what was
      completed
- [ ] **No AI attribution** — no `Co-Authored-By:` naming Claude/Anthropic, no "Generated with"
      badge, no AI-assistance note in the body (R16). The author's name only.
