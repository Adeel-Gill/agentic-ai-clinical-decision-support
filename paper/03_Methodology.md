# 3. Methodology

## 3.1 Design Overview

The framework follows a design-science approach [hevner2004design]: an artifact (the layered
agentic framework) is constructed to close identified gaps and evaluated against explicit
metrics. Six layers organize the system — data, memory, reasoning and knowledge, agent
orchestration, clinical decision, and trustworthy AI — with a clinician dashboard and
human-in-the-loop validation closing the loop. The full architecture is specified in the thesis
(Chapter 3); this section states the components that carry the paper's claims.

## 3.2 Patient-Timeline Retrieval

The memory layer treats the patient's longitudinal EHR trajectory as a first-class retrieval
corpus, alongside — not instead of — external medical knowledge. Four stores are maintained:
short-term working context; long-term patient memory (admissions, diagnoses, medications,
procedures); a vector database over clinical notes and events; and clinical context memory for
the active monitoring episode. Memory operations follow the construction / management /
retrieval decomposition of the agent-memory literature [wu2025memory]: writes are explicit
events linked to source records, management handles decay and revision (a corrected lab value
supersedes but does not erase its predecessor), and retrieval is timestamp-aware so that
evidence reflects what was knowable at decision time. Retrieval-augmented generation then draws
on both corpora — the patient timeline and guideline/literature knowledge
[lewis2020rag; singh2025agenticrag] — so that every recommendation can cite patient-specific
evidence, not only population-level knowledge [zhao2025medrag; ke2025ragfitness].

## 3.3 Agent Orchestration

A coordinator agent delegates to specialized agents — monitoring, planner, diagnosis, risk
prediction, treatment recommendation, explanation, and verification — using ReAct-style
reasoning within each agent [yao2023react]. Coordination follows a hub-and-spoke topology: all
inter-agent messages pass through the coordinator, a choice motivated by evidence that
decentralized medical multi-agent topologies propagate adversarial or erroneous influence
further [chen2025medsentry]. Tool access uses MCP-style standardized interfaces and inter-agent
exchange follows A2A-style conventions [ehtesham2025protocols], keeping the prototype
composable with hospital tooling. External tools follow the validated-tool principle of
RiskAgent and TxAgent — calculations and lookups are delegated to auditable components rather
than generated [liu2025riskagent; gao2025txagent].

## 3.4 Verification Gate and Audit Trail

The verification agent is the framework's distinguishing safety component. Every candidate
recommendation is checked for (a) evidential grounding — is the claim entailed by the retrieved
patient evidence and guidelines, screened against known classes of medical hallucination
[kim2025hallucinations]; (b) guideline compliance and conflict with active orders; and (c) a
calibrated confidence estimate that accompanies the recommendation to the clinician
[atf2025uncertainty; guo2017calibration]. Recommendations failing any check are blocked and
returned with the failure reason. Every check writes to an evidence-linked audit trail; the
trail's faithfulness — whether it accurately reflects the evidence the system actually used —
is treated as a measured property, not an assumed one, using entailment-based spot audits
[es2024ragas]. This combination is designed to satisfy, and to demonstrate compliance with,
emerging expectations for unconfined non-deterministic clinical software: guardrails,
moderation, retrieval grounding, and inspectability [tan2026undcs; weissman2025unregulated].

## 3.5 Human-in-the-Loop Protocol

Clinicians receive only verified recommendations, each with linked evidence, confidence, and
explanation. Review is structured — approve, modify, or reject, with reasons captured into
memory — rather than free-form, reflecting meta-analytic evidence that unstructured
clinician–LLM collaboration produces fragile gains [wang2026collaboration]. Rejections and
modifications feed the monitoring loop as supervision signals.

## 3.6 Evaluation Design

Evaluation uses MIMIC-IV [johnson2023mimic] cohorts (sepsis and deterioration use cases;
Sepsis-3 labels [singer2016sepsis3; vincent1996sofa]) and scores the system on longitudinal
tracking, not one-shot prediction. Primary axes: (1) decision quality against clinical ground
truth and revisited MIMIC-IV baselines [lovon2025mimic]; (2) grounding rate — the fraction of
recommendation claims entailed by retrieved patient evidence, following RAG-evaluation practice
[es2024ragas]; (3) verification-gate effectiveness — ungrounded-recommendation catch rate at
fixed review budget; (4) audit-trail faithfulness under spot audit; and (5) rubric-graded
recommendation quality in the style of physician-rubric benchmarks
[arora2025healthbench; jiang2025medagentbench]. Ablations remove patient-timeline retrieval,
the verification gate, and longitudinal memory in turn, isolating each claimed contribution.
Statistical comparisons follow standard practice for correlated classifiers
[delong1988comparing; dietterich1998approximate] with false-discovery control
[benjamini1995controlling].
