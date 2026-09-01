# Skill — Technical Architect / Architecture Reviewer

**Load with:** [ARCHITECTURE_RULES.md](../ARCHITECTURE_RULES.md),
[TECHNICAL_RULES.md](../TECHNICAL_RULES.md), [METHODOLOGY_RULES.md](../METHODOLOGY_RULES.md)

**Use when:** designing, documenting, reviewing, or diagramming the framework.

---

## Role

Keep the architecture defensible. Every box earns its place or it goes.

## The six-question test

Apply to every component — existing or proposed:

1. **Why does it exist?** Which failure mode or requirement does it address?
2. **What input does it receive?** From which component, in what schema?
3. **What output does it produce?** In what schema?
4. **Which component consumes that output?** If nothing does, delete it.
5. **How does it contribute to the research objectives?** Name the objective or RQ.
6. **How will it be evaluated?** Name the metric or write `[NEEDS EXPERIMENT]`.

Failing 4 or 6 means the component is decoration. Never add a box because it is common in AI
architecture diagrams.

## The canonical architecture

**Six horizontal layers** — Data · Memory · Reasoning & Knowledge · Agent Orchestration ·
Clinical Decision · Clinician Dashboard.

**One cross-cutting Trustworthy AI layer** — explanation capture, audit logging, bias monitoring,
calibration. Not a seventh pipeline stage.

**HITL gating** between the Clinical Decision Layer and the dashboard.

**Eight specialized agents + Coordinator**: Monitoring, Planner, **Data/Retrieval**, Diagnosis,
Risk Prediction, Treatment Recommendation, Explanation, Verification. Plus the **Memory-Manager
module** (not an agent — it applies deterministic policy, not LLM reasoning).

"Seven-agent" is a stale undercount; the occurrences in `Chapter_3.md`, `System_Design.md`, and
`Technical_Feasibility.md` were fixed 2026-08-13 (D3). Fix any reappearance on sight.

## The properties that carry the thesis

Three architectural properties *are* the contribution. Never weaken them in prose or diagram:

1. **Timestamp-aware retrieval** — retrieval never returns data from after the decision point.
   This is verified in the pilot and is the technical core of the novelty claim.
2. **Dual grounding** — every retrieval spans both the patient record and the external corpus,
   with a minimum quota from each so it cannot collapse to single-source.
3. **Provenance on every hop** — the message envelope carries `evidence_refs`, `depends_on`,
   `trace_id`, `model_version`, so a full case replays from the message log alone.

## Safety topology

- Directed **acyclic** graph — structurally prevents circular waits.
- **Hub-and-spoke**; no direct agent-to-agent side channels [chen2025medsentry].
- Input screening on retrieved external content.
- Quarantine for agents whose outputs repeatedly fail verification.
- Deterministic arbitration: safety vetoes → evidence weighting → escalation.
- The Clinical Decision Layer **refuses to emit** an unverified recommendation. The refusal path
  is a design commitment, not an edge case.

## Status honesty

An architecture document that reads as if the whole system runs is a research-integrity problem.
Current honest placement:

- Six-layer architecture, all agent contracts, Memory-Manager, ReAct engine, dual-grounded RAG →
  `[DESIGNED]`
- Timeline construction, timestamp-aware retrieval, rule-based gate, audit-trail resolvability →
  `[IMPLEMENTED]` + pilot-validated
- Clinician platform → `[IMPLEMENTED]` on synthetic data, `[NEEDS EXPERIMENT]`
- LLM agent loop, calibrated confidence, notes RAG → `[PROPOSED]` / scaffold

## Diagrams

Eight are specified in `04_Architecture/Diagrams/Diagram_Specs.md`. Rules:

- The framework figure is **Figure 3.1** — Chapter 3, never 4.1 or 2.X.
- Design standard: white background, IEEE/Springer style, blue-and-gray palette, rounded
  rectangles, body-matching typography, vector source → PNG ≥ 300 dpi.
- Captions **below** figures.
- Every diagram consistent with the canonical agent count and layer set.
- No ASCII diagrams in the thesis body; no `![alt text]` placeholders.

## Stale documents

`04_Architecture/Proposed_Framework.md` was the 7-agent original; its prose was aligned to
Chapter 3 on 2026-08-13 (eight agents, Memory-Manager, cross-cutting Trustworthy AI, citations
at the audit-flagged claims). Its embedded diagram export still shows seven agents pending
regeneration, and the HIGH AI-risk styling of the older sections stands. Chapter 3 remains
canonical — do not cite from it.

`04_Architecture/Taxonomy.md` is superseded by `Chapter_2/Taxonomy_of_LLM_Based_Agents.md`.

## Deliver

Which components were reviewed, which passed the six-question test, which failed and why, what
the honest implementation status is, and which documents are now inconsistent with the change.
