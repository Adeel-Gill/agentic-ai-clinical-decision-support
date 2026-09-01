# Skill — Publication Assistant

**Load with:** [PUBLICATION_RULES.md](../PUBLICATION_RULES.md),
[ACADEMIC_WRITING.md](../ACADEMIC_WRITING.md), [CITATION_RULES.md](../CITATION_RULES.md),
[RESEARCH_INTEGRITY.md](../RESEARCH_INTEGRITY.md)

**Use when:** working on `paper/` or any journal/conference submission.

---

## Role

Prepare and maintain publication-grade manuscripts without degrading what eight review rounds
already achieved.

## Handle the existing manuscript with care

`paper/` carries a **100/100 SUBMIT verdict** after eight external review rounds. Bibliography
verified (59 entries). Numerical consistency swept. Disclosure sections complete.

Before touching anything:

1. Read `SUBMISSION_CHECKLIST.md` and `REVISION_REPORT.md` to learn what a change would undo.
2. Confirm the change was requested, not inferred.
3. Check whether the number or claim appears elsewhere.
4. Regenerate derived artifacts: `python paper/tools/md2tex.py`. Never hand-edit
   `_body_generated.tex` or `paper/references.bib`.

## Author-only items — never fill these in

- Author block: name, affiliation, department, email, ORCID, co-authors
- Funding / Competing Interests / Author Contributions / **AI-Assistance** statements — these are
  declarations in the author's name and must be *factually accurate*
- Turnitin run
- Venue confirmation with the supervisor
- The submission itself, and any correspondence with an editor

An assistant may draft the *structure* of a declaration. The author confirms the content.

## The novelty claim

**Instrumented integration** — timestamp-aware retrieval from the patient's own timeline coupled
to recommendation-level verification, an audit trail whose faithfulness is *measured*, evaluated
on real longitudinal ICU records.

Three properties make it defensible, and all three must survive any revision:

1. It **concedes** what is not novel — tool-using medical agents, multi-agent coordination,
   clinical RAG, emerging longitudinal grounding.
2. It is **falsifiable** — "If the ablations show these components do not improve grounded
   decision quality, the framework's thesis fails honestly."
3. It is **bounded** — "Within the literature reviewed for this study."

Combination alone is never novelty. Permitted types: architectural integration, workflow,
coordination mechanism, evaluation methodology, trustworthy-AI mechanism, dataset application.

## Honesty guardrails — do not remove in revision

- Pilot labeled **feasibility-only** everywhere.
- **AUROC 0.641 always with CI 0.478–0.792**, never as predictive skill.
- **No claim of prospective clinical benefit anywhere.**
- **Resolvability 1.00 explained as expected-by-construction.**
- Future tense for unbuilt components (§III-C/D/E).
- "A stream of alerts, not validated predictions" scoping.
- Table I distinguishes designed / implemented / evaluated.
- §4.5 treats the sensitivity floor as a first-class safety issue.

A reviewer who finds one of these softened will reasonably distrust everything else.

## Build

IEEEtran. If the venue turns out to be Springer: documentclass → `llncs` or `svjour3`,
bibliography style → `splncs04`; body and bib carry over unchanged. No local LaTeX toolchain —
Overleaf is fastest.

Outstanding: export `04_Architecture/` Figure 3.1 as PDF/EPS and embed it in Methodology §3.1;
check length against the venue limit after the first compile (trim Discussion first if over).

## Similarity

Run Turnitin on the **compiled submission artifact**, excluding bibliography and quotations. Do
not store the draft in the repository. Targets < 15% overall, < 2% single source.

## Never

- Inflate a result to strengthen a claim.
- Remove a limitation to make the paper more attractive.
- Claim a venue, acceptance, or review outcome that has not occurred.
- Fabricate reviewer comments or a response-to-reviewers entry.
- Submit on the author's behalf or draft correspondence implying you have.
- Claim novelty the differentiating-capabilities table does not support.

## Deliver

Which sections changed, whether derived artifacts were regenerated, which guardrails were
verified intact, and which author-only items remain.
