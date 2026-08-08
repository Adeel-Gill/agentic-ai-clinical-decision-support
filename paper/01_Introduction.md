# 1. Introduction

An intensive-care clinician deciding whether to escalate treatment reasons over a patient's
trajectory: what the lactate did overnight, which medications were started and stopped, how
this admission compares with the last one. The language-model systems now entering clinical
workflows do not reason this way. They can select and invoke validated clinical tools
[gao2025txagent; liu2025riskagent], sustain multi-turn diagnostic dialogue
[palepu2025disease; saab2025multimodal], and in one documented case run prospectively, in
silent mode, inside a live emergency-department deployment [shashikumar2025sepsis]; their underlying machinery, from reasoning-and-acting
loops [yao2023react] and retrieval-augmented generation [lewis2020rag] to multi-agent
coordination [wu2024autogen] and structured memory [wu2025memory], is individually mature.
Each of these systems, however, rebuilds its picture of the patient from the current prompt
and retains nothing once the interaction ends.

This research is motivated by three shortfalls that follow from that mismatch between
clinical reasoning and system design. The
first concerns evaluation substrate. The strongest medical agents are still graded on
curated examinations or synthetic records [tang2024medagents; li2024agenthospital;
jiang2025medagentbench], whereas a real intensive-care admission is noisy, longitudinal, and
internally revised as results are corrected and orders change [johnson2023mimic]; competence
on the former substrate does not establish competence on the latter. The second concerns
grounding direction. Clinical retrieval-augmented systems, including those with strong
results, treat external knowledge as the corpus and the patient as the query
[zhao2025medrag; ke2025ragfitness]. Emerging work grounds models in the longitudinal record
for prediction and summarization, but there the record is input to be compressed, not
timestamp-addressable evidence coupled to each recommendation the system makes. The third
concerns verifiability. The field can now characterize hallucination
and uncertainty in clinical language models [kim2025hallucinations; atf2025uncertainty], and
regulators have begun demanding inspectable safeguards for agentic clinical software
[tan2026undcs; weissman2025unregulated], but published systems rarely check an individual
recommendation against the patient evidence that was retrieved for it, and within the
literature reviewed for this study we found none that measures whether its own audit trail
faithfully records what the system used.

This paper presents an agentic AI framework for intelligent patient monitoring and clinical
decision support in which each of those three properties is a designed, measurable component
rather than an aspiration. Specialized LLM agents for monitoring, diagnosis, risk
prediction, treatment recommendation, explanation, and verification operate under a
coordinator. Beneath them, a memory layer makes the patient's longitudinal EHR timeline a
first-class retrieval corpus. Above them, a verification gate blocks recommendations that
the retrieved evidence does not support, writing every decision to an audit trail whose
faithfulness is itself an evaluation target. Clinician oversight is structured rather than
advisory; recommendations arrive only after verification, carrying linked evidence and a
calibrated confidence estimate, because the meta-analytic record suggests unstructured human–LLM
collaboration yields gains too uncertain to rely on [wang2026collaboration].

The contributions are: (1) a layered framework that grounds retrieval in the patient
timeline rather than only in external knowledge; (2) a verification gate and evidence-linked
audit trail specified as measurable components, with metrics for recommendation grounding
and trail faithfulness; (3) an evaluation design on MIMIC-IV that scores longitudinal
patient tracking rather than one-shot question answering, positioned against the exam-based
and synthetic-EHR benchmarks that dominate current practice [jiang2025medagentbench;
arora2025healthbench; lovon2025mimic]; (4) an analysis of how the framework's safeguards map
onto emerging regulatory requirements for unconfined non-deterministic clinical software
[tan2026undcs]; and (5) a pilot feasibility study on the openly licensed MIMIC-IV demo that
grounds the framework's distinguishing mechanisms in de-identified real-world ICU data: timelines for 140 stays
build in under three seconds, timestamp-aware retrieval answers in roughly 12 ms without
returning future information, the verification gate's evidence requirement suppresses false
alerts faster than true ones (86% versus 57% blocked at four required signals), and every
logged audit-trail reference re-resolves against the source record. These are feasibility
results on a 100-patient cohort, and the paper reports them with that caveat throughout.

The remainder of the paper reviews related work (Section 2), details the framework and its
evaluation design (Section 3), discusses implications and limitations (Section 4), and
reports the pilot study (Section 5).
