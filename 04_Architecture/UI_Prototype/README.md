# ACDSS Platform — UI Prototype

`acdss_ui_prototype.html` is a self-contained, clickable design prototype of the clinician
platform for the proposed framework. Open it directly in any browser — no build, no server,
no external assets. **All data shown is synthetic** (shaped like the MIMIC-IV demo); the
prototype is a design artifact, not a clinical tool.

## Screens

| Screen | What it demonstrates |
|---|---|
| Unit Overview | Bed grid with 24 h sparklines, risk scores **with confidence intervals**, verification-state chips; review queue shows only gate-verified alerts |
| Patient Timeline | Multi-lane longitudinal timeline (vitals, labs, meds, prior admissions) with a **"replay what was knowable"** cursor — events after the cursor disappear, mirroring timestamp-aware retrieval |
| Recommendation Review | The human-in-the-loop core: claim-level evidence linking (click a claim, its evidence highlights), calibrated-confidence bar, verification banner with gate detail, Approve/Modify/Reject with mandatory reason |
| Alerts & Gate | Verified vs **blocked** alerts (blocked are auditable, never hidden), plus the gate operating curve from the pilot study (true vs false alert pass rates) |
| Audit Trail | Append-only log; every entry expands to evidence references with source table + row, re-resolution check marks, and the clinician decision + reason |
| Agent Monitor | Hub-and-spoke orchestration diagram (Coordinator-mediated, no side channels), agent status incl. quarantine state, system health strip with pilot metrics |

## Design principles encoded

1. **Evidence first, recommendation second** — every AI output is visually subordinate to
   the evidence and verification state that produced it (the thesis differentiator).
2. **Nothing auto-executes** — the clinician is unmistakably the decision-maker; blocked
   alerts stay visible and overridable.
3. **Uncertainty is always shown** — risk scores never appear without their interval.
4. Status colors (green/amber/red) are reserved for clinical state and always paired with
   an icon + label; data series use a validated two-color palette (`#0d9488`, `#b45309`,
   CVD-checked).

## Relation to the implementation

The screens map 1:1 onto the framework layers (04_Architecture/Proposed_Framework.md) and
onto the `acdss` package scaffold: FastAPI routes in `05_Source_Code/src/acdss/api/` would
serve these views; the pilot package (`acdss.pilot`) already computes the metrics shown on
the Alerts and Agent Monitor screens.
