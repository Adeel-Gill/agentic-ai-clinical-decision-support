# Defense Presentation — Full Slide Deck

<p align="center">
  <img src="../07_Thesis/Images/superior_logo.svg" alt="Superior University" width="280" />
</p>

MS Thesis Proposal Defense
**An Agentic AI Framework for Intelligent Patient Monitoring and Clinical Decision Support**
Adeel Gill — MS Artificial Intelligence, The Superior University, Lahore

Target: 17 slides, ~20 minutes plus Q&A. Formal IEEE/Springer style. Content is drawn
strictly from the drafted Chapter 1 and Chapter 2. Speaker notes live in the companion file
[Defense_Speaker_Notes.md](Defense_Speaker_Notes.md); the anticipated examiner Q&A is in
[Defense_Examiner_QA.md](Defense_Examiner_QA.md).

---

## Slide 1: Title Slide

**Visual:** Clean, formal IEEE-style layout. Superior University logo (≈5 cm × 7.43 cm) at
top center — vector source at [07_Thesis/Images/superior_logo.svg](../07_Thesis/Images/superior_logo.svg)
(brand color #701A73). Dark-blue or academic-gray background with white/high-contrast text.

<p align="center">
  <img src="../07_Thesis/Images/superior_logo.svg" alt="Superior University" width="320" />
</p>

- **Title:** An Agentic AI Framework for Intelligent Patient Monitoring and Clinical Decision Support
- **Author:** Adeel Gill
- **Degree:** Master of Science in Artificial Intelligence
- **Supervisor:** Dr. Fawad Nasim
- **Institution:** Faculty of Computer Science and Information Technology, The Superior University, Lahore

---

## Slide 2: Background — Clinical Data Overload

**Visual:** Flowchart of ICU data streams (vital signs, labs, clinical notes, medications)
funneling through a narrow bottleneck into a single clinician icon.

- **Unprecedented data generation:** continuous streams of vitals, labs, notes, and imaging.
- **Cognitive bottleneck:** data production outpaces manual interpretation under time pressure.
- **The role of AI:** reduce the cognitive load of synthesis, not replace clinician judgment.

---

## Slide 3: Background — The Shift to Agentic AI

**Visual:** Side-by-side comparison. Left: "Passive LLM" (Prompt → Black Box → Response).
Right: "Agentic AI Loop" (Perceive ↔ Memory ↔ Reason ↔ Act, with Tool Use).

- **Passive LLMs:** high fluency, but lack persistence, planning, and patient memory.
- **Agentic AI:** shifts models from passive responders to goal-directed systems.
- **Core mechanisms:** autonomous reasoning, tool use, memory management, environmental feedback.

---

## Slide 4: Problem Statement

**Visual:** Three crumbling pillars labeled "Lack of Context," "Opaque Reasoning,"
"Fragmented Systems."

- **Volume & heterogeneity:** reconciling diverse EHR data is slow and error-prone.
- **LLM limitations:** current systems are isolated tools lacking cross-step planning and durable patient models.
- **CDSS deficits:** high predictive accuracy often lacks explainability, current-evidence retrieval, and long-term context.

---

## Slide 5: Literature Review — Agentic Frameworks

**Visual:** Comparison matrix of frameworks (ReAct, AutoGen, CAMEL, MetaGPT) against
clinical needs (Memory, SOPs, Oversight). Checkmarks and crosses.

- **ReAct:** interleaves reasoning and acting, but lacks long-term memory.
- **AutoGen & CAMEL:** enable multi-agent coordination and role-play, but struggle with communication loops.
- **MetaGPT:** enforces Standard Operating Procedures (SOPs), mirroring clinical protocols.
- **Limitation:** general-purpose designs lacking integrated clinical safety.

---

## Slide 6: Literature Review — RAG & Healthcare AI

**Visual:** A "Generator" LLM receiving inputs from a "Retriever" that searches "External
Medical Knowledge" and "EHR Databases."

- **Medical LLMs (e.g., Med-PaLM):** strong QA performance but lack external retrieval and memory.
- **Retrieval-Augmented Generation (RAG):** anchors reasoning to verifiable evidence, reducing hallucinations.
- **Current state (e.g., MedRAG):** improves specificity but focuses on isolated diagnostic snapshots.

---

## Slide 7: Research Gap — The Limits of Current Systems

**Visual:** Venn diagram of three circles — "Longitudinal ICU Evaluation,"
"Patient-Timeline RAG," "Faithful Auditability" — intersecting at "The Missing Framework."

- **Static evaluation:** tested on isolated exams (e.g., MedQA) rather than real longitudinal trajectories.
- **Generic retrieval:** RAG grounds in general guidelines, missing the patient's specific evolving timeline.
- **Omitted trustworthiness:** verification and faithful audit trails are not engineered as first-class components.

---

## Slide 8: Research Objectives

**Visual:** Target icon — one bold central objective, three supporting nodes.

- **Primary:** design an Agentic AI framework for intelligent patient monitoring and CDSS using MIMIC-IV.
- **Secondary 1:** integrate memory, RAG, and ReAct reasoning natively.
- **Secondary 2:** develop specialized clinical agents for monitoring, diagnosis, and treatment.
- **Secondary 3:** embed trustworthy-AI safeguards and human-in-the-loop validation architecturally.

---

## Slide 9: Research Questions

**Visual:** Five sequential chevrons leading to a blueprint icon.

- **RQ1:** What are the architectural limits of current LLM healthcare systems?
- **RQ2:** How can Agentic AI improve reasoning/memory while preserving physician control?
- **RQ3:** How can specialized agents collaborate while preserving explainability?
- **RQ4:** How does RAG improve reliability, and where does retrieval fail?
- **RQ5:** How can this framework be instantiated on the MIMIC-IV dataset?

---

## Slide 10: Proposed Methodology

**Visual:** Four-step process graphic (Phase 1 → Phase 4) with icons for literature,
taxonomy, architecture, evaluation.

- **Phase 1:** critical literature review of LLMs, Agentic AI, and RAG.
- **Phase 2:** taxonomy formulation and research-gap analysis.
- **Phase 3:** design of the layered agentic framework architecture.
- **Phase 4:** bounded prototype specification & experimental evaluation plan.

---

## Slide 11: Proposed Framework — Architecture Overview

**Visual:** Stacked-layer block diagram: Perception (bottom) → Memory → Reasoning/Orchestration
→ Action (top), intersected by a vertical "Verification/Trust" pillar.

- **Perception layer:** ingests EHR records, demographics, labs, notes.
- **Memory layer:** maintains short/long-term context and vector-based semantic stores.
- **Reasoning & orchestration:** sequences tasks via ReAct and routes among agents.
- **Action & verification:** generates recommendations under human review.

---

## Slide 12: Proposed Framework — Specialized Agent Roles

**Visual:** Hub-and-spoke. Central "Coordinator Agent" routing to Monitoring, Diagnosis,
Risk Prediction, Treatment, and Explanation/Verification agents.

- **Coordinator agent:** routes tasks and resolves conflicting recommendations.
- **Monitoring agent:** tracks physiological state over time.
- **Diagnosis & treatment agents:** weigh candidate conditions and propose interventions.
- **Explanation & verification agents:** summarize reasoning and check against guidelines.

---

## Slide 13: Grounding the Framework — RAG & MIMIC-IV

**Visual:** Database schematic — "MIMIC-IV" feeding a "Vector Database" that supplies
patient-specific timeline context to the LLM agents.

- **MIMIC-IV dataset:** rich, retrospective critical-care records for longitudinal design.
- **Patient-timeline RAG:** shifts retrieval from generic guidelines to the patient's own evolving EHR.
- **Context-aware decisions:** fuses medical literature with patient-specific data for continuous monitoring.

---

## Slide 14: Trustworthy AI & Human-in-the-Loop

**Visual:** Workflow ending in a Human-in-the-Loop decision node (Approve / Modify / Reject),
with icons for Audit Log, Explainability, Safety.

- **Explainable AI:** surfaces exact evidence and reasoning for clinical review.
- **Safety verification:** algorithmic checks for contradictions and guideline compliance.
- **Auditability:** tamper-evident logging of retrieved data and agent interactions.
- **Human-in-the-loop (HITL):** clinicians retain final authority to approve, modify, or reject.

---

## Slide 15: Expected Contributions

**Visual:** Three pillars with checkmark icons.

- **Architectural contribution:** a coherent, verifiable multi-agent framework for longitudinal CDSS.
- **Methodological novelty:** patient-timeline retrieval paired with a dedicated verification agent to mitigate hallucinations.
- **Foundation for future work:** a reproducible design and concrete evaluation protocol ready for empirical testing.

---

## Slide 16: Timeline & Scope Boundaries

**Visual:** Simple Gantt of thesis phases plus a distinct "In Scope / Out of Scope" box.

- **In scope:** conceptual architecture design, bounded prototype, evaluation plan, MIMIC-IV integration.
- **Out of scope:** production hospital software, live EHR integration, prospective clinical trials.
- **Timeline:** Literature & Taxonomy → Framework Design → Prototype & Evaluation Planning.

---

## Slide 17: Conclusion & Q&A

**Visual:** "Agentic AI + MIMIC-IV + Trustworthy AI" → "Intelligent Clinical Decision Support."
Bold "Thank You / Q&A" at the bottom.

- **Summary:** transitioning from passive LLMs to verifiable, agent-based clinical workflows.
- **Integration:** fusing memory, RAG, and HITL enables safe, longitudinal monitoring.
- **Final thought:** the framework provides transparent, evidence-based recommendations that assist — not replace — clinical judgment.
