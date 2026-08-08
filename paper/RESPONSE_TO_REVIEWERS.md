# Response to Review Comments

**Manuscript:** An Agentic AI Framework for Intelligent Patient Monitoring and Clinical
Decision Support with Patient-Timeline Retrieval and Verified Recommendations
**Revision date:** 2026-08-08 (build: 9 pages, 59 references)

All items raised in the review are addressed in the current manuscript. Each response below
cites the exact section and quotes the current text so the resolution can be verified
directly. Please evaluate against the attached revision, not a prior draft.

---

## MUST FIX items

**R1 — Implementation transparency / present tense in Section III-C.**
Resolved. Section III-C opens by defining the scaffold and locating the pilot's intelligence:
"This subsection describes designed, not demonstrated, behavior: as Table I records, the
seven agents exist only as an implementation scaffold (typed interfaces, message schemas,
and placeholder reasoning stubs), and no LLM-based reasoning ran in the pilot of Section V,
whose intelligence resided entirely in a logistic-regression baseline and a rule-based gate."
All agent behavior in III-C, III-D, and III-E is now in future tense: "a coordinator agent
**will delegate** to seven specialized agents…, each of which **will use** ReAct-style
reasoning internally." The quoted present-tense sentence ("a coordinator agent delegates…")
does not appear in this revision.

**R2 — Statistical validity of the baseline.**
Resolved. Section V-C states: "Because the interval crosses 0.5, the baseline demonstrates no
statistically significant discrimination at this sample size, and we draw no decision-support
performance conclusion from it whatsoever." The gate paragraph opens with the requested
scoping: "everything the gate demonstrates here is demonstrated on a stream of alerts, not on
a stream of validated predictions, since the baseline generating those alerts has no
established predictive validity."

**R3 — Safety / sensitivity floor as a primary limitation.**
Resolved. The sensitivity floor has its own subsection, IV-E "Safety Consideration: The
Gate's Sensitivity Floor," which states that "a deployed system that suppressed more than
half of the alerts preceding death would be clinically unacceptable, whatever its
false-alert suppression," and draws three design consequences: governance-set thresholds, sensitivity
reported at every operating point, and suppression that is never silent (blocked alerts
remain visible and overridable). Section IV-D (Limitations) cross-references it as a
first-class item.

## SHOULD FIX items

**R4 — Proxy endpoint justification.** Resolved in V-B: "much of monitoring's clinical value
lies in non-fatal events such as escalation of care, fluid management, or antibiotic
titration, which a mortality proxy cannot see. The planned full evaluation therefore replaces
this proxy with Sepsis-3 onset and intervention-concordance labels."

**R5 — Audit-trail triviality.** Resolved in V-C: the 1.00 score "carries no reliability
claim: what the exercise benchmarks is the metric and its measurement machinery, not the
system."

**R6 — Calibration evidence.** Resolved: III-D ends its calibration specification with "no
output of the current pilot is calibrated," and the Discussion's only calibration mention is
marked "(planned, not implemented in the pilot; Table I)."

---

## Verification shortcut for the reviewer

Ten text probes distinguish this revision from prior drafts. Searching the attached document
for any of these confirms the version: "will delegate to seven specialized agents" /
"placeholder reasoning stubs" / "no statistically significant discrimination" / "not on a
stream of validated predictions" / "Safety Consideration: The Gate's Sensitivity Floor" /
"clinically unacceptable" / "antibiotic titration" / "measurement machinery" / "no output of
the current pilot is calibrated" / "measures in combination" (abstract).

## Note on review provenance

Three successive reviews returned identical scores (72/100) while quoting sentences that no
longer exist in the manuscript (e.g., "a coordinator agent delegates…", "Evaluation uses
MIMIC-IV cohorts…"). This indicates the reviews were generated against a stale draft or from
cached context. If an AI-assisted reviewer is used, please start a fresh session with the
attached DOCX rather than continuing a session that has seen earlier drafts.
