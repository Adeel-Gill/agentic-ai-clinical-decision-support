# Abstract

Clinicians reason over a patient's trajectory; the large language model (LLM) agents now
entering clinical workflows reason over a prompt. Although such agents can invoke validated
tools, sustain diagnostic dialogue, and in one documented case run prospectively in silent
mode in a live clinical setting, we identify three properties needed for trust in a specific patient that, to the
best of our knowledge, no published system measures: retrieval grounded in the patient's own longitudinal record
rather than external knowledge alone, evaluation on real intensive-care admissions rather
than examinations or synthetic records, and verification whose audit trail is itself
checked rather than assumed. We present an agentic AI framework for intelligent patient
monitoring and clinical decision support that makes each of these a designed, measurable
component. Specialized agents for monitoring, diagnosis, risk prediction, treatment
recommendation, explanation, and verification operate under a coordinator, over a memory
layer in which the patient timeline is a first-class retrieval corpus; recommendations must
pass an evidence-entailment verification gate before reaching a structured clinician review
step, accompanied by calibrated confidence. We specify an evaluation design on MIMIC-IV that
scores longitudinal patient tracking, and report a pilot feasibility study on the openly
licensed 100-patient MIMIC-IV demo: timelines for 140 ICU stays build in under three
seconds; timestamp-aware retrieval answers in about 12 ms without returning future
information; a rule-based verification gate blocks 86% of false alerts while retaining 43%
of true alerts at its strictest informative threshold; and all 183 logged audit-trail
references re-resolve exactly against source records. The pilot establishes
implementability, not clinical utility; the framework's contribution is making
trustworthiness properties measurable that current systems only assert.

# Keywords

agentic AI; clinical decision support; patient monitoring; large language models;
retrieval-augmented generation; verification; audit trail; human-in-the-loop; MIMIC-IV
