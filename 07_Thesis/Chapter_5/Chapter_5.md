# CHAPTER 5

# CONCLUSION AND FUTURE WORK

> Status: structured outline with prose stubs. To be completed after Chapter 4 results are in.
> RQ answers are marked *(pending)* until the evaluation in Chapter 4 is finalized.

---

## 5.1 Overview

Short framing paragraph. Restate, in one or two sentences, what the thesis set out to do: design
an Agentic AI framework for intelligent patient monitoring and clinical decision support, built
around MIMIC-IV and supervised by a clinician at every recommendation [johnson2023mimic]. State
that this chapter summarizes the contributions, revisits the five research questions, states the
limitations candidly, and sets a direction for future work.

*Stub:* "This thesis argued that the obstacle to clinically useful AI is integration, not raw model
capability, and it responded with a layered, human-supervised agentic framework. This chapter draws
the argument to a close..."

---

## 5.2 Summary of Contributions (tied to objectives)

Prose, not a bare list. Tie each contribution back to the specific objective it satisfies
(objectives are in Chapter 1). Keep bullets under ~20% of the section.

- **C1 — Critical synthesis and gap (Obj. 1, 2).** A critical review of Agentic AI, LLMs, RAG, and
  healthcare AI that locates a specific, defensible gap: capable components exist in isolation, few
  integrated and supervised architectures exist [tang2024medagents; zhao2025medrag; li2024agenthospital].
- **C2 — Taxonomy of LLM-based agents (Obj. 1).** A classification of architectural components and
  research trends used to position the framework [xi2023rise; wang2024survey].
- **C3 — Layered agentic framework (Obj. 3).** An architecture composing memory, reasoning, planning,
  RAG, and multi-agent orchestration as interacting layers rather than bolted-on features
  (Chapter 3) [yao2023react; lewis2020rag].
- **C4 — Specialized clinical agents (Obj. 4).** Distinct agents for monitoring, diagnostic support,
  risk prediction, treatment recommendation, and explanation, under a coordinator.
- **C5 — Trustworthy-AI layer (Obj. 5).** Explainability, safety verification, bias monitoring, audit
  logging, and human-in-the-loop validation embedded structurally, not appended
  [rasheed2022explainable; jimenez2023trustworthy].
- **C6 — MIMIC-IV grounding + bounded prototype and evaluation plan (Obj. 6, 7).** The design is
  instantiated on real critical-care data and paired with a concrete evaluation plan for future
  implementation [johnson2023mimic].

*Critical stub sentence:* note that these contributions are architectural and conceptual; the thesis
delivers a validated design and a bounded prototype, not a deployed clinical system.

---

## 5.3 Answers to the Research Questions

One subsection per RQ. Each opens with a one-line restatement, then a short answer grounded in the
review (Ch. 2), the framework (Ch. 3), and the evaluation (Ch. 4). Mark empirical claims *(pending
Chapter 4)* until results are final.

### RQ1 — Limitations of current LLM-based healthcare systems
*(answer largely from Ch. 2; complete.)* Passive, memoryless responders; task-narrow; weak evidence
integration; opaque. Distinguish architectural limits from incidental engineering ones
[thirunavukarasu2023llms; zhou2024survey]. *(pending: quantitative baseline comparison from Ch. 4.)*

### RQ2 — How Agentic AI improves reasoning, planning, memory, collaboration
*(answer from Ch. 2 + Ch. 3.)* Map each capability to a framework layer; state the oversight
constraint that bounds autonomy [xi2023rise; yao2023react]. *(pending evaluation evidence.)*

### RQ3 — Multi-agent collaboration with explainability and oversight
*(answer from Ch. 3.)* Coordinator + specialized agents + Explanation Agent + HITL. Critical note on
error propagation across agent interfaces. *(pending ablation on agent configuration, Ch. 4.)*

### RQ4 — RAG and external knowledge for reliability and transparency
*(answer from Ch. 2 + Ch. 3.)* Grounding reduces hallucination and enables citation; retrieval
quality is the binding constraint and does not reach zero error [lewis2020rag; zhao2025medrag].
*(pending: retrieval-quality and faithfulness metrics, Ch. 4.)*

### RQ5 — Supporting patient monitoring on MIMIC-IV
*(answer from Ch. 3 + Ch. 4.)* Longitudinal context from MIMIC-IV; vector retrieval; monitoring
agent over admission timeline [johnson2023mimic]. *(pending: prototype results on the defined
cohort, Ch. 4.)*

---

## 5.4 Limitations

Be honest and specific — this section protects the thesis's credibility. Prose paragraphs.

- **Conceptual scope.** The primary deliverable is a framework and bounded prototype, not production
  software or an EHR-integrated system; some claims rest on design analysis rather than deployment.
- **Retrospective, single-source data.** MIMIC-IV is retrospective ICU data from one institution, so
  results reflect one setting's practice patterns and do not establish generalizability
  [johnson2023mimic].
- **Latency and cost.** Memory, retrieval, reasoning, and multiple coordinated agents impose
  compute and latency overhead that a real-time monitoring loop may struggle to absorb; the thesis
  characterizes this rather than fully solving it.
- **No prospective clinical trial.** The framework is not validated on live patients; safety and
  clinical benefit claims are therefore bounded and await prospective study.
- **Explanation faithfulness / automation bias.** LLM explanations may be plausible without being
  faithful, and human reviewers are prone to deferring to confident suggestions; the HITL step
  mitigates but does not remove these risks.

---

## 5.5 Future Work

Prose with a few anchored bullets. Move from nearest-term to most ambitious.

- Implement the full prototype and run the Chapter 4 evaluation at scale on the MIMIC-IV cohort.
- Add prospective and multi-site validation to test generalizability beyond a single ICU source.
- Optimize latency/cost (smaller specialist models, caching, selective retrieval) for real-time use.
- Strengthen retrieval quality and explanation-faithfulness measurement.
- Expand the trustworthy-AI layer with formal bias audits and regulatory-alignment analysis.
- Explore live EHR integration and clinician usability studies to test the HITL interface against
  automation bias in practice [tu2025amie; schmidgall2024agentclinic].

---

## 5.6 Closing Remarks

Two or three sentences. Restate the central claim (integration under supervision, not raw
capability, is the bottleneck), acknowledge that the contribution is a foundation rather than a
finished clinical product, and close on what a follow-on project should build first.

*Stub:* "The framework does not replace the clinician; it is arranged so that the clinician's
authority is easy to exercise. Whether that promise holds in practice is the question the next
project must answer, and this thesis has tried to make that question a tractable one."
