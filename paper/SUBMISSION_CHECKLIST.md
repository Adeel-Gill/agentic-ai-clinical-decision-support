# Submission Checklist — W-Category Paper

**Deadline:** 2026-08-10 · **Format:** generic IEEE journal (IEEEtran); adjust when venue is fixed.

## FINAL STATUS (2026-08-08): 100/100 — SUBMIT
Eight external review rounds (72→72→72 stale-file loop →92→96→98→97→100). Closing gate
passed: numerical consistency sweep clean (12/12 repeated figures identical everywhere);
all metadata declarations present. Remaining actions are the author's alone:
1. Fill [Department]/[University]/[email] in `main.tex` \author block and `tools/md2docx.py`
   AUTHOR line; rebuild (md2tex.py → tectonic → md2docx.py).
2. Personally confirm the Funding / Competing Interests / Author Contributions /
   AI-Assistance statements are factually accurate (they are declarations in your name).
3. University Turnitin run (exclude bibliography/quotes; don't store draft in repository).
4. Venue confirmation with supervisor; adapt template if Springer/Elsevier.
Viva prep: defend the sensitivity floor (why gated suppression with visible blocked-alert
queue beats an ungated predictor that drowns clinicians in false alarms) — see
REVIEW/Viva_Questions.md.

## Revision history (compressed)
- 2026-08-07: pilot study added; humanization + plagiarism pass; verified refs.
- 2026-08-08 (three review rounds): novelty repositioned to *instrumented integration*;
  Related Work gained the longitudinal-EHR paragraph (CliCARE, Traj-CoA, TrajOnco, TIMER,
  RGAR — all verified; refs 54→59); Table I (designed/implemented/evaluated); formal metric
  + ground-truth + true/false-alert + leakage definitions; calibration methodology;
  future-tense for unbuilt components (III-C/D/E); "stream of alerts, not validated
  predictions" scoping; dedicated §4.5 sensitivity-floor safety subsection; abstract says
  "measures in combination". Examiner-style score at last external check: 72/100 MINOR
  REVISIONS (both MUST-FIX rounds addressed).

## Manuscript state (2026-08-08)

| Item | Status |
|---|---|
| Abstract (≈250 words) + keywords | ✅ `00_Abstract.md` / in `main.tex` |
| Introduction, Related Work, Methodology, Pilot Study, Discussion, Conclusion | ✅ all drafted |
| LaTeX manuscript | ✅ `main.tex` + `_body_generated.tex` (generated from the .md sections) |
| Bibliography | ✅ `references.bib` — 59 entries, all cited, trimmed from `../02_Research/References.bib` |
| Reference verification | ✅ 5 flagged entries verified against publisher records (NEJM AI, PMLR 267, KDD '25, Findings of ACL 2026, Nature 642) |
| Pilot results | ✅ real numbers from `../06_Experiments/results/pilot/` |
| Architecture figure | ⬜ export `../04_Architecture/` Figure 3.1 as PDF/EPS and add `\includegraphics` in Methodology §3.1 |
| Author block | ⬜ placeholder — fill real affiliation, email, co-authors/supervisor |
| Word/page count vs venue limit | ⬜ check after first compile |

## How to compile

No LaTeX toolchain is installed on this machine. Two options:

**Overleaf (fastest):** create a blank project, upload `main.tex`, `_body_generated.tex`,
`references.bib` (IEEEtran is preinstalled), compile with pdfLaTeX.

**Local (MiKTeX):** install MiKTeX (https://miktex.org/download), then:
```bash
cd paper
pdflatex main && bibtex main && pdflatex main && pdflatex main
```

To regenerate `_body_generated.tex` and `references.bib` after editing any section .md
(run from the repository root):
```bash
python paper/tools/md2tex.py
```

## Remaining before submission (in order)

1. **Confirm venue with Dr. Nasim** — and that "framework + pilot feasibility" framing is
   acceptable there. If Springer instead of IEEE: swap documentclass to `llncs` or `svjour3`
   and `\bibliographystyle{splncs04}`; body and bib carry over unchanged.
2. Fill author block; add ORCID if required.
3. Export and embed the architecture figure; reference it in §3.1.
4. Compile; check length; trim Discussion first if over limit.
5. Proofread pass against `REVIEW/Style_And_Citation_Keys.md` rules (US spelling, no filler
   openers) — the LaTeX body inherited the compliant prose but the abstract is new.
6. Supervisor review → apply → submit.

## Honesty guardrails (do not remove in revision)

- The pilot is labeled feasibility-only everywhere (abstract, §4 rationale, §5.4, limitations).
- AUROC 0.641 is always reported with its CI (0.478–0.792) and never as predictive skill.
- No claim of prospective clinical benefit anywhere.
- Trail resolvability 1.00 is explained as expected-by-construction in the deterministic pilot.
