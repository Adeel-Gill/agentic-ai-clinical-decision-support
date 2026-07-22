# Defense Presentation — Outline

MS thesis defense: "An Agentic AI Framework for Intelligent Patient Monitoring and Clinical
Decision Support." Target 15–18 slides, ~20 minutes plus Q&A. Each slide lists its purpose and one
line of speaker notes. Keep visuals sparse; talk to the architecture, not to bullet walls.

---

**Slide 1 — Title**
Title, candidate (Adeel Gill), supervisor, institution, date.
*Notes:* "Good [morning]. I'll present a framework that helps clinicians monitor patients and decide, without taking the decision away from them."

**Slide 2 — The problem in one picture**
A crowded ICU data stream vs. a clinician under time pressure.
*Notes:* "Hospitals produce data faster than anyone can read it; the bottleneck is synthesis, not storage."

**Slide 3 — Motivation**
Why LLMs helped but did not solve it: fluent, but passive and memoryless.
*Notes:* "A chat model answers once and forgets; monitoring needs memory, planning, and evidence."

**Slide 4 — The gap (this is the crux)**
Capable components exist in isolation — MedAgents, MedRAG, Agent Hospital, Clinical Camel — but no integrated, supervised architecture for longitudinal monitoring.
*Notes:* "Each of these does one thing well and stops there. The gap is integration under oversight."

**Slide 5 — Research questions**
RQ1–RQ5 on one slide, phrased tightly.
*Notes:* "Five questions: the limits of current systems, what agentic AI adds, multi-agent oversight, RAG's reliability, and monitoring on MIMIC-IV."

**Slide 6 — Objectives + scope**
Design study: conceptual framework + bounded prototype + evaluation plan; not a clinical trial.
*Notes:* "I'm honest up front about scope — this is a validated design, not deployed hospital software."

**Slide 7 — Approach overview**
Design-oriented methodology in four phases (review → gap → framework → evaluation).
*Notes:* "The method is a design pipeline; each phase feeds the next."

**Slide 8 — Framework architecture (the centerpiece)**
The layered diagram: perception, memory, reasoning, planning/orchestration, action, trustworthy-AI layer.
*Notes:* "This is the heart of the thesis — six layers, each with a clear job and clear seams."

**Slide 9 — The agents**
Monitoring, diagnosis, risk, treatment, explanation, verification, under a coordinator.
*Notes:* "Work divides the way a clinical team divides it; the coordinator routes and verifies."

**Slide 10 — RAG + memory**
How evidence is retrieved and how patient context persists across time.
*Notes:* "RAG grounds recommendations in evidence; memory lets the system reason over an admission, not an instant."

**Slide 11 — Trustworthy-AI layer**
Explainability, safety checks, bias monitoring, audit logging, human-in-the-loop.
*Notes:* "Trust is a first-class layer, not an add-on — every recommendation is explained, logged, and reviewed."

**Slide 12 — Human-in-the-loop workflow**
The approve/modify/reject flow diagram.
*Notes:* "The clinician has final authority, and the interface is built so that authority is real, not nominal."

**Slide 13 — Data: MIMIC-IV**
What the dataset provides and the cohort used.
*Notes:* "Real critical-care records give the framework longitudinal detail — with the caveat that it's single-source and retrospective."

**Slide 14 — Evaluation plan**
Baselines, ablations, metrics (accuracy, retrieval quality, faithfulness, latency). Mark pending.
*Notes:* "Here's how the bounded prototype is tested; results feed the final chapter."

**Slide 15 — Contributions**
C1–C6 tied to objectives, one line each.
*Notes:* "The contribution is integrative: composing known parts into a supervised whole, plus the trustworthy layer and MIMIC-IV grounding."

**Slide 16 — Limitations (say them before they're asked)**
Conceptual scope, retrospective single-source data, latency/cost, no prospective trial, explanation faithfulness.
*Notes:* "I'll name the limits directly — it's a foundation, and I'm clear about what it doesn't yet prove."

**Slide 17 — Future work**
Full implementation, prospective multi-site validation, latency optimization, usability studies.
*Notes:* "The natural next project is implementation and prospective validation."

**Slide 18 — Closing + Q&A**
One-sentence thesis restatement; thanks; questions.
*Notes:* "Integration under supervision, not raw capability, is the bottleneck — and this framework is a tractable way to attack it. Happy to take questions."

---

## Q&A preparation (anticipated questions)

- **Why not just fine-tune a medical LLM?** — Fine-tuning improves the answer; it doesn't add memory,
  planning, retrieval, or oversight across a workflow. The gap is architectural.
- **Isn't MIMIC-IV too narrow?** — Yes, and I say so: it's for design and demonstration, not
  generalizability. Prospective multi-site validation is future work.
- **How do you prevent error propagation between agents?** — Verification agent + human-in-the-loop +
  audit logging; I treat inter-agent interfaces as the main risk surface.
- **Are the explanations faithful?** — Not guaranteed; a fluent explanation can be unfaithful, which is
  exactly why review is mandatory and evidence is surfaced, not just prose.
- **What about latency in real-time monitoring?** — A known limitation; characterized in the thesis,
  with optimization (smaller specialist models, caching, selective retrieval) as future work.
- **What's genuinely novel?** — The integration and the structural trustworthy-AI layer, not any single
  component in isolation.
