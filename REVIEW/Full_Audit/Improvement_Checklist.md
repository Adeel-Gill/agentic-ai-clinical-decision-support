# Originality Improvement Checklist (Phase 7)

Concrete moves to raise originality and scholarly value, prioritized **High / Medium / Low impact**. Originality here means *your synthesis, judgment, and structure* — the parts a similarity checker cannot match and an examiner most rewards. The good news: your defensible contribution already exists in `Research_Gap_Analysis.md` and `02_Research/Research_Gap.md` (patient‑timeline RAG + dedicated verification gate + faithful audit, evaluated on real MIMIC‑IV rather than exam QA). The work below **surfaces and hardens** that contribution.

---

## HIGH IMPACT

### H‑1. Consolidate to one canonical Chapter 2, delete the drafts
Combine → split correctly: adopt `Compiled/Chapter_2.md`'s structure, fold the four `_Revised` sections in, **delete** the originals and stubs. This single act removes most self‑similarity *and* most AI‑pattern text. (Cross‑ref: Review Report §2; AI Report §4.)

### H‑2. Add a "prior systems vs. this framework" capability matrix (your own table)
`Research_Gap_Analysis.md` already describes it in prose ("when scored on the five differentiating columns … no prior system carries more than a single check"). **Turn it into an actual table** with rows = ReAct, AutoGen, MetaGPT, MedAgents, Agent Hospital, MedRAG, EHRAgent, AgentClinic, AMIE, Med‑PaLM and columns = {patient‑timeline RAG, verification gate, longitudinal memory, real‑ICU evaluation, faithful audit trail}. This is high‑originality, zero‑similarity, and it visually proves the gap.

### H‑3. Write your own critical analysis into the review, not just descriptions
For each named system, add one sentence of *your* judgment about what it does **not** do for longitudinal monitoring (the `_Revised` files model this: "MedAgents … its evaluation centers on QA rather than monitoring a patient over time [tang2024medagents]"). Do this for every system still described neutrally in the un‑revised files.

### H‑4. Elevate the framework discussion: justify each design choice against a named alternative
Chapter 3 is strong but can be more clearly *yours* by contrasting each decision with the option you rejected (e.g., condition‑triggered DAG vs fixed pipeline; pgvector vs Qdrant — already hedged; dual‑grounded vs external‑only RAG). Frame these as defended bets, not descriptions.

### H‑5. Finish Chapter 5 as argued prose
Convert the outline to full conclusions once Chapter 4 has numbers. Tie each contribution (C1–C6) to its objective and to the RQ it answers. An examiner reads the conclusion first — an outline signals "unfinished."

---

## MEDIUM IMPACT

### M‑1. Add a layer‑to‑RQ / objective traceability table
One table mapping the six framework layers + trustworthy layer → objectives (1–7) → RQs (1–5) → Chapter‑4 metrics. Demonstrates end‑to‑end coherence and fixes the RQ‑scheme confusion (Consistency Report §3–4) in one artifact.

### M‑2. Add a dedicated Limitations subsection to Chapter 2/3 (not only Chapter 5)
You already write honest limitations in Ch4 §4.8 and Ch5 §5.4. Pull a short, explicit "limits of the design as specified" note into Chapter 3's summary so the design chapter itself is self‑critical.

### M‑3. Expand Future Work with specifics tied to your gaps
Chapter 5 §5.5 is good but generic. Anchor each item to one of the three research‑gap questions (e.g., "prospective multi‑site validation" → external‑validity limitation from §4.8).

### M‑4. Add a comparison table of memory / reasoning / RAG design choices
A small table contrasting the four memory types and the RAG stages against how prior agent systems handle them — turns Chapter 3's prose into a reusable reference and shows synthesis.

### M‑5. Reconcile and cite the taxonomy once, as your own contribution
The taxonomy (six dimensions) is potentially an original synthesis. Present it once, cite `xi2023rise`/`wang2024survey`/`sapkota2025agents`, and explicitly state what your taxonomy adds beyond those surveys (the healthcare dimension + the mapping to your layers).

---

## LOW IMPACT (polish)

- **L‑1.** Replace ASCII diagrams (`Agentic_AI_Frameworks.md`, `RAG` files) with proper captioned figures per `04_Architecture/Diagrams/Diagram_Specs.md`.
- **L‑2.** Add a glossary/notation note (many acronyms already in the build script's abbreviations list — surface it).
- **L‑3.** Standardize terminology: "Data/Retrieval Agent" vs "Data Agent"; "Trustworthy AI Layer" vs "trust layer".
- **L‑4.** Add a one‑paragraph positioning statement in Chapter 1 distinguishing "AI agents" from "Agentic AI" per `sapkota2025agents` (you cite it; make the distinction explicit as an original framing).

---

## Originality scorecard logic

| Move | Similarity impact | Examiner impact |
|---|---|---|
| H‑1 delete drafts | ↓↓↓ overall % | ↑ (clean submission) |
| H‑2 capability matrix | ↓ (tables don't match) | ↑↑ (proves the gap) |
| H‑3 critical sentences | ↓ (reworded) | ↑↑ (shows judgment) |
| H‑4 defended choices | neutral | ↑↑ (shows depth) |
| M‑1 traceability table | neutral | ↑ (coherence) |

**Sequence:** H‑1 first (it subsumes much of the AI/plagiarism cleanup), then H‑2/H‑3 (originality + similarity), then H‑4/H‑5, then the M and L items.
