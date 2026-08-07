# 1. Introduction

Large language models have moved quickly from answering medical examination questions to acting
inside clinical workflows. Systems now select and call validated clinical tools
[gao2025txagent; liu2025riskagent], conduct multi-turn diagnostic conversations
[palepu2025disease; saab2025multimodal], and in at least one case operate prospectively at the
bedside [shashikumar2025sepsis]. The building blocks of such systems — ReAct-style reasoning
[yao2023react], retrieval-augmented generation [lewis2020rag], multi-agent coordination
[wu2024autogen], and structured agent memory [wu2025memory] — are individually mature.

What has not matured is the evidence that these systems can be trusted with a specific patient
over time. Three shortfalls recur across the strongest published work. First, evaluation remains
distant from deployment: medical agents are still graded on curated examinations or synthetic
records [tang2024medagents; li2024agenthospital; jiang2025medagentbench], not on the noisy,
longitudinal, internally revised record of a real intensive-care admission [johnson2023mimic].
Second, retrieval is grounded in guidelines and literature rather than in the patient: even
strong clinical RAG deployments treat external knowledge as the corpus and the patient as the
query [zhao2025medrag; ke2025ragfitness], leaving the patient's own timeline — prior labs, prior
admissions, the trend of a vital sign — outside the evidence base. Third, verification and
auditability are asserted rather than measured: hallucination and uncertainty are now well
characterized [kim2025hallucinations; atf2025uncertainty], and regulators increasingly demand
inspectable safeguards for agentic clinical software [tan2026undcs; weissman2025unregulated],
yet published systems rarely check a recommendation against the retrieved patient evidence, and
none that we are aware of measures the faithfulness of its own audit trail.

This paper presents an agentic AI framework for intelligent patient monitoring and clinical
decision support designed around these three shortfalls. The framework organizes specialized
LLM agents — monitoring, diagnosis, risk prediction, treatment recommendation, explanation, and
verification — under a coordinator, over a memory layer that treats the patient's longitudinal
EHR timeline as a first-class retrieval corpus, with a dedicated verification gate and an audit
trail whose faithfulness is itself an evaluation target. Clinician oversight is structured
rather than advisory: recommendations reach the clinician only after verification, with linked
evidence and calibrated confidence, a design choice supported by meta-analytic evidence that
unstructured human–LLM collaboration yields fragile gains [wang2026collaboration].

The contributions are: (1) a layered framework that grounds retrieval in the patient timeline
rather than only in external knowledge; (2) a verification gate and evidence-linked audit trail
specified as measurable components, with metrics for recommendation grounding and trail
faithfulness; (3) an evaluation design on MIMIC-IV that scores longitudinal patient tracking
rather than one-shot question answering, positioned against the exam-based and synthetic-EHR
benchmarks that dominate current practice [jiang2025medagentbench; arora2025healthbench;
lovon2025mimic]; and (4) an analysis of how the framework's safeguards map onto emerging
regulatory requirements for unconfined non-deterministic clinical software [tan2026undcs];
and (5) a pilot feasibility study on the openly licensed MIMIC-IV demo that grounds the
framework's distinguishing mechanisms in real ICU data — timelines for 140 stays build in
under three seconds, timestamp-aware retrieval answers in roughly 12 ms without returning
future information, the verification gate's evidence requirement suppresses false alerts
faster than true ones (86% versus 57% blocked at four required signals), and every logged
audit-trail reference re-resolves against the source record. These are feasibility results
on a 100-patient cohort, and the paper reports them with that caveat throughout.

The remainder of the paper reviews related work (Section 2), details the framework and its
evaluation design (Section 3), discusses implications and limitations (Section 4), and
reports the pilot study (Section 5).
