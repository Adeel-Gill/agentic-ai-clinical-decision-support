# Abstract

Large language model (LLM) agents have moved rapidly from medical question answering into
clinical workflows: they call validated tools, conduct diagnostic dialogue, and in isolated
cases operate prospectively at the bedside. Yet three properties that would make such systems
trustworthy for a specific patient remain unmeasured across the 2025–2026 literature:
retrieval grounded in the patient's own longitudinal record rather than external knowledge
alone, evaluation on real, noisy intensive-care admissions rather than examinations or
synthetic records, and verification whose audit trail is itself checked rather than assumed.
This paper presents an agentic AI framework for intelligent patient monitoring and clinical
decision support designed around these three gaps. Specialized agents for monitoring,
diagnosis, risk prediction, treatment recommendation, explanation, and verification operate
under a coordinator over a memory layer that treats the patient timeline as a first-class
retrieval corpus; every recommendation must pass an evidence-entailment verification gate and
carries calibrated confidence into a structured clinician review step. We specify an
evaluation design on MIMIC-IV that scores longitudinal patient tracking, and we report a
pilot feasibility study on the openly licensed 100-patient MIMIC-IV demo: timelines for 140
ICU stays build in under three seconds; timestamp-aware retrieval answers in about 12 ms
without returning future information; a rule-based verification gate blocks 86% of false
alerts while retaining 43% of true alerts at its strictest informative threshold; and all 183
logged audit-trail references re-resolve exactly against source records. The pilot
establishes implementability, not clinical utility; the framework's contribution is making
trustworthiness properties measurable that current systems only assert.

# Keywords

agentic AI; clinical decision support; patient monitoring; large language models;
retrieval-augmented generation; verification; audit trail; human-in-the-loop; MIMIC-IV
