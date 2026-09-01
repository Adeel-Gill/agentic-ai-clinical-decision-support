# PUBLICATION RULES

Governs `paper/` — the W-category manuscript — and any future journal or conference submission.

---

## 1. Current state: handle with care

`paper/SUBMISSION_CHECKLIST.md` records a **100/100 SUBMIT verdict after eight external review
rounds**. The manuscript, its bibliography (59 verified entries), its numerical consistency, and
its disclosure sections have all been closed out.

**Do not casually edit this manuscript.** Before changing anything in `paper/`:

1. Read `SUBMISSION_CHECKLIST.md` and `REVISION_REPORT.md` to learn what a change would undo.
2. Confirm the change is requested, not inferred.
3. Check whether the same number or claim appears elsewhere (the numerical-consistency sweep
   verified 12/12 repeated figures identical).
4. Regenerate derived artifacts: `python paper/tools/md2tex.py` rebuilds `_body_generated.tex`
   and `references.bib`. Never hand-edit either.

Outstanding items are **author-only** and must not be filled in by an assistant: author block
fields, the declaration sign-off (Funding / Competing Interests / Author Contributions /
AI-Assistance — these are declarations in the author's name), the Turnitin run, and venue
confirmation.

## 2. What counts as novelty here

**Not** "we combined memory, RAG, and multi-agent collaboration." The comparative table shows
prior systems already integrate those.

The claim is **instrumented integration**, stated narrowly in `paper/04_Discussion.md` §4.1:

> timestamp-aware retrieval from the patient's own timeline coupled to recommendation-level
> verification, an audit trail whose faithfulness is *measured* rather than assumed, and
> evaluation that scores longitudinal tracking on de-identified real-world ICU records.

Three properties make this a defensible novelty claim:

1. It **concedes** what is not novel — tool-using medical agents, multi-agent coordination,
   clinical RAG, and emerging longitudinal grounding are all explicitly disclaimed.
2. It is **falsifiable** — "If the ablations show these components do not improve grounded
   decision quality, the framework's thesis fails honestly; the components are separable and
   testable by design."
3. It is **bounded** — "Within the literature reviewed for this study."

Any novelty claim in a future submission must have all three properties. Permitted novelty types:
architectural integration, workflow, coordination mechanism, evaluation methodology,
trustworthy-AI mechanism, dataset application. Combination alone is never sufficient.

## 3. Priorities for a W-category venue

| Priority | What it means here |
|---|---|
| Novelty | Instrumented integration, narrowly and falsifiably stated |
| Methodological rigor | Design science + pre-registered hypotheses + fair baseline ladder |
| Recent literature | 2025–2026 foregrounded; the longitudinal-EHR paragraph is mandatory |
| Reproducibility | Config-driven runs, fixed manifest, pinned versions, seeds |
| Clear research gap | Solved / partially solved / open, checked against P021–P050 |
| Measurable contribution | Every claim maps to a metric or is marked as designed |
| Strong evaluation | Pilot real numbers + designed full evaluation, clearly separated |
| Appropriate citations | Verified against publisher of record |
| Transparent limitations | Four named, plus the dedicated sensitivity-floor section |

## 4. Honesty guardrails — never remove in revision

Verbatim from `paper/SUBMISSION_CHECKLIST.md`:

- The pilot is labeled **feasibility-only** everywhere (abstract, §4 rationale, §5.4,
  limitations).
- **AUROC 0.641 is always reported with its CI (0.478–0.792)** and never as predictive skill.
- **No claim of prospective clinical benefit anywhere.**
- **Trail resolvability 1.00 is explained as expected-by-construction** in the deterministic
  pilot.

Add to these, from the manuscript's own commitments:

- Future tense for unbuilt components (§III-C/D/E).
- "A stream of alerts, not validated predictions" scoping for the baseline.
- Table I distinguishes designed / implemented / evaluated.
- §4.5 treats the gate's sensitivity floor as a first-class safety issue, not a footnote.

A reviewer who finds one of these softened will reasonably distrust everything else.

## 5. Manuscript structure

| File | Section |
|---|---|
| `00_Abstract.md` | Abstract (~250 words) + keywords |
| `01_Introduction.md` | Introduction |
| `02_Related_Work.md` | Related work, incl. the longitudinal-EHR paragraph |
| `03_Methodology.md` | Framework and evaluation design |
| `05_Pilot_Study.md` | Pilot feasibility study (real numbers) |
| `04_Discussion.md` | Claims, evaluation practice, safety/regulation, limitations, sensitivity floor, future work |
| `06_Conclusion.md` | Conclusion |
| `main.tex` + `_body_generated.tex` | IEEEtran manuscript |
| `references.bib` | 59 cited keys, regenerated from the master |

Section 5 (pilot) appearing before Section 4 (discussion) in file numbering is intentional — the
`.tex` ordering is what matters.

## 6. Build and format

- IEEEtran (generic IEEE journal). If the venue turns out to be Springer, swap the documentclass
  to `llncs` or `svjour3` and the bibliography style to `splncs04`; body and bib carry over.
- No LaTeX toolchain is installed locally. Overleaf is the fastest path; MiKTeX is the local
  option.
- Regenerate the body and trimmed bib with `python paper/tools/md2tex.py` from the repository
  root after editing any section `.md`.
- The architecture figure (`04_Architecture/` Figure 3.1 exported to PDF/EPS) still needs
  embedding in Methodology §3.1.

## 7. Ethics and disclosure sections

Required and present: Ethics, Data Availability, Funding, Competing Interests, Author
Contributions, AI-Assistance statement.

The AI-assistance declaration is the author's to make and must be **factually accurate** about
how AI tools were used in preparing the manuscript. An assistant may draft the structure; the
author confirms the content. Never write a declaration that overstates or understates AI
involvement.

Data availability must state that MIMIC-IV requires credentialed PhysioNet access and that the
pilot used the openly licensed demo — those are different access regimes.

## 8. Similarity checking

- Run Turnitin on the **compiled submission artifact**, not the repository scaffold.
- Exclude bibliography and quotations.
- Do not store the draft in the repository as part of the check.
- Targets: < 15% overall, < 2% single source.
- The dominant risks are internal self-similarity and uncited canonical descriptions — both are
  deletion/citation problems, not rewriting problems.

## 9. Never do these

- Never inflate a result to strengthen a claim.
- Never remove a limitation to make a paper more attractive.
- Never claim a venue, acceptance, or review outcome that has not occurred.
- Never fabricate reviewer comments or a response-to-reviewers entry.
- Never submit anywhere on the author's behalf, or draft correspondence implying you have.
- Never fill in author identity fields, affiliations, ORCIDs, or declarations.
- Never claim novelty that the differentiating-capabilities table does not support.
