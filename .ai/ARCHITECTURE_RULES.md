# ARCHITECTURE RULES

Governs `04_Architecture/`, Chapter 3 §3.2–3.6, `05_Source_Code/docs/architecture.md`, and every
diagram.

---

## 1. The canonical architecture

**Six horizontal layers**, bottom-up:

1. **Data Layer** — MIMIC-IV contract; exposes a normalized patient timeline, not raw tables.
2. **Memory Layer** — four stores + Memory-Manager module.
3. **Reasoning & Knowledge Layer** — ReAct engine + RAG pipeline + curated clinical knowledge.
4. **Agent Orchestration Layer** — Coordinator + eight specialized agents.
5. **Clinical Decision Layer** — fuses agent outputs into one decision object; arbitrates.
6. **Clinician Dashboard** — review, not automation.

**Cross-cutting: Trustworthy AI Layer** — explanation capture, audit logging, bias monitoring,
confidence calibration. It is *not* a seventh stage in the pipeline; it is a set of controls every
layer writes into. Chapter 3 §3.3.7 states this framing; `04_Architecture/Proposed_Framework.md`
§12 was aligned to it 2026-08-13.

**HITL gating** sits between the Clinical Decision Layer and the dashboard.

Data flows upward during a case; control flows downward; clinician feedback flows back down into
memory.

## 2. The agents — eight specialized + Coordinator

| Agent | Role |
|---|---|
| Coordinator | Builds a condition-triggered DAG; routes; enforces hub-and-spoke topology |
| Monitoring | Detects abnormal vitals and significant change from the incremental event stream |
| Planner | Decomposes the clinical task; selects agents; sequences work |
| **Data/Retrieval** | Owns *all* reads from the Data Layer and RAG pipeline — centralizes provenance |
| Diagnosis | Infers differentials from symptoms, labs, notes |
| Risk Prediction | Mortality, ICU transfer, sepsis, readmission |
| Treatment Recommendation | Evidence-based interventions + interaction checks |
| Explanation | Faithful explanation of why a recommendation was made |
| Verification | Checks recommendations against retrieved patient evidence; guideline compliance; confidence thresholds |

Plus the **Memory-Manager**: a **module**, not an agent, because it applies deterministic policy
rather than LLM reasoning.

**"Seven-agent" is wrong.** It survived in `Chapter_3.md`, `System_Design.md`, and
`Technical_Feasibility.md` as a stale undercount predating the Data/Retrieval Agent; all
occurrences were fixed 2026-08-13 (D3). Fix any reappearance on sight; the worked trace in
Chapter 3 runs eight.

`04_Architecture/Proposed_Framework.md` was the stale 7-agent original; its prose was aligned
to Chapter 3 on 2026-08-13 (D4) — eight agents, Memory-Manager, cross-cutting §12, citations at
the audit-flagged claims. **The framework figure was regenerated 2026-08-14** to the canonical
scheme (`Diagrams/framework_figure_3_1.svg/.png`, 300 dpi, spec 1) and deployed to
`07_Thesis/Images/proposed_framework.png`; the old seven-agent `image.png` is drafting history
only. Chapter 3 remains canonical — do not cite from this file.

## 3. The component justification test

Before any component is added, retained, or drawn, it must answer all six:

1. **Why does it exist?** — which failure mode or requirement does it address?
2. **What input does it receive?** — from which component, in what schema?
3. **What output does it produce?** — in what schema?
4. **Which component consumes that output?** — if nothing does, delete it.
5. **How does it contribute to the research objectives?** — name the objective or RQ.
6. **How will it be evaluated?** — name the metric or state `[NEEDS EXPERIMENT]`.

A component that cannot answer 4 or 6 is decoration. Never add a box because it is common in AI
architecture diagrams.

## 4. Required elements in architecture documentation

Every architecture document must make these explicit, by name:

INPUT · PROCESSING · MEMORY · REASONING · ORCHESTRATION · AGENTS · DECISION · OUTPUT ·
FEEDBACK · SAFETY · HUMAN OVERSIGHT

If a section is missing, the reader cannot trace a case end-to-end.

## 5. Memory layer specifics

Four stores:

| Store | Holds | Notes |
|---|---|---|
| Short-term | Current session: recent vitals, active meds, current labs | Bounded |
| Long-term patient | Prior admissions, chronic conditions, past diagnoses, treatment history | Keyed to the index encounter |
| Vector database | Embeddings of notes, discharge summaries, literature, retrieved evidence | pgvector (prototype) → Qdrant (scale-out) |
| Clinical context | Prior agent outputs, historical recommendations, reasoning traces | The episodic store |

The memory survey's vocabulary is adopted [wu2025memory]: writes are explicit **construction**
events linked to source evidence; **management** includes decay and conflict-resolution rules for
revised lab values; **retrieval is always timestamp-aware**.

Timestamp-awareness is not optional — it is the mechanism that prevents future data leaking into
a decision. The pilot verified this property (`retrieval never returns future data`), and it is
the technical core of the thesis's novelty claim.

## 6. RAG: dual grounding

Every retrieval spans **both** the patient-specific record **and** the external evidence corpus.
The merge preserves a minimum quota from each source so dual grounding cannot collapse to
single-source.

This is the differentiating property. Systems that retrieve only from guidelines cannot
personalize; systems that read only the record cannot bring evidence to bear. Do not describe
the RAG pipeline in a way that loses this.

## 7. Orchestration and safety topology

- The Coordinator builds a **directed acyclic** graph — structurally preventing circular waits.
- **Hub-and-spoke** message topology; no direct agent-to-agent side channels
  [chen2025medsentry]. MedSentry showed open shared channels are the most vulnerable design.
- Input screening on retrieved external content.
- An agent whose outputs repeatedly fail verification can be quarantined.
- **Arbitration protocol** (deterministic, ordered): safety vetoes → evidence weighting →
  escalation.
- One shared message envelope on every hop, carrying provenance (`evidence_refs`), causality
  (`depends_on`, `trace_id`), and audit fields (`model_version`, `audit`) — so a full case is
  replayable from the message log alone.

## 8. The Clinical Decision Layer performs no clinical reasoning

It arbitrates and fuses. Duplicating agent reasoning there would obscure provenance. It **refuses
to emit** a recommendation that has not passed Verification — the refusal path is a design
commitment, because a decision layer that always answers, framing low and high confidence
identically, actively misleads clinicians.

## 9. Trustworthy AI must be wired in, not bolted on

Enforced where each concern arises:

- explanations captured at the reasoning step that produced them;
- audit records written by every agent as it acts;
- bias measured on the data as it is partitioned;
- calibration applied to confidence at the point of emission.

Bolting these on at the end produces plausible but unfaithful post-hoc rationalization — the
exact failure mode the healthcare trustworthy-AI literature warns against.

## 10. Diagrams

Specifications live in `04_Architecture/Diagrams/Diagram_Specs.md`. Eight are specified:

1. System Architecture (Figure 3.1) · 2. Agent Collaboration Sequence · 3. RAG Pipeline ·
4. Memory Architecture · 5. Patient Journey Timeline · 6. HITL / Verification Flowchart ·
7. Deployment Diagram · 8. Methodology Flowchart

Rules:

- Figure numbering follows the chapter it appears in. The framework figure is **Figure 3.1**.
- Design standard (`Thesis_Formatting_Guide.md` §13): white background, IEEE/Springer style,
  blue-and-gray academic palette, rounded rectangles, body-matching typography, vector source
  exported to PNG ≥ 300 dpi, minimal icons.
- Captions **below** figures, `Figure 3.2` italic + caption non-italic, TNR 11 pt, centered.
- Every diagram must be consistent with the canonical agent count and layer set.
- Replace ASCII diagrams and `![alt text]` placeholders — both are flagged defects.

## 11. Architecture claims must match the code

`04_Architecture/System_Design.md` and `05_Source_Code/` must agree, and both must state
implementation status honestly. Currently: the architecture is `[DESIGNED]`, `acdss.pilot` and
the clinician platform are `[IMPLEMENTED]`, and the LLM agent loop is a `[PROPOSED]` scaffold.
An architecture document that reads as if the whole system runs is a research-integrity problem,
not a documentation nicety.
