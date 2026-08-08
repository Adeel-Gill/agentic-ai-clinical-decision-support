# 3. Methodology

## 3.1 Design Overview

The framework follows a design-science approach [hevner2004design]: an artifact (the layered
agentic framework) is constructed to close identified gaps and evaluated against explicit
metrics. Six layers organize the system: data, memory, reasoning and knowledge, agent
orchestration, clinical decision, and trustworthy AI. A clinician dashboard and
human-in-the-loop validation close the loop, and a cross-cutting trustworthy-AI panel
(explainability, audit logs, safety checks, bias monitoring, human oversight) governs every
layer. Figure 1 shows the full architecture over MIMIC-IV; this section states only the
components that carry the paper's claims. Table 1 summarizes, per component, what is
designed, what is implemented, and what has been evaluated, so that the boundary between the
completed pilot (Section 5) and the planned full evaluation (Section 3.6) is explicit.

Table: Component status: designed, implemented, and evaluated.
| Component | Designed | Implemented | Evaluated |
| Patient-timeline memory (construction, management, retrieval) | Yes | Yes (non-LLM) | Pilot (Section 5) |
| Timestamp-aware retrieval | Yes | Yes | Pilot: latency, no future data |
| Early-warning baseline | Yes | Yes | Pilot: AUROC with proxy labels |
| Verification gate (rule-based form) | Yes | Yes | Pilot: operating curve |
| Audit trail with measured resolvability | Yes | Yes | Pilot: 183/183 references |
| Seven LLM agents and coordinator | Yes | Scaffold only | Planned (Section 3.6) |
| Guideline and literature RAG | Yes | No | Planned (Section 3.6) |
| Calibrated confidence estimation | Yes | No | Planned (Section 3.6) |
| Human-in-the-loop review protocol | Yes | UI prototype | Planned (Section 3.6) |
| Longitudinal evaluation on full MIMIC-IV | Yes | No | Planned (Section 3.6) |

## 3.2 Patient-Timeline Retrieval

The memory layer treats the patient's longitudinal EHR trajectory as a first-class retrieval
corpus alongside (not instead of) external medical knowledge. Four stores are maintained:
short-term working context; long-term patient memory (admissions, diagnoses, medications,
procedures); a vector database over clinical notes and events; and clinical context memory for
the active monitoring episode. Memory operations follow the construction, management, and
retrieval decomposition of the agent-memory literature [wu2025memory]. Writes are explicit
events linked to source records. Management handles decay and revision, so a corrected lab
value supersedes but does not erase its predecessor. Retrieval is timestamp-aware, which keeps
the evidence set limited to what was knowable at decision time. Retrieval-augmented generation
then draws on both corpora, the patient timeline and guideline or literature knowledge
[lewis2020rag; singh2025agenticrag], and every recommendation can therefore cite
patient-specific evidence rather than population-level knowledge alone
[zhao2025medrag; ke2025ragfitness].

## 3.3 Agent Orchestration

This subsection describes the designed orchestration; as Table 1 records, the seven agents
exist as an implementation scaffold, no LLM-based reasoning ran in the pilot of Section 5,
and every present-tense statement here specifies intended behavior rather than demonstrated
behavior. In the design, a coordinator agent delegates to seven specialized agents
(monitoring, planner, diagnosis, risk prediction, treatment recommendation, explanation, and
verification), each of which uses ReAct-style reasoning internally [yao2023react]. Coordination follows a hub-and-spoke
topology. All inter-agent messages pass through the coordinator, a choice motivated by
adversarial evidence that multi-agent topology governs how far a compromised agent's
influence spreads, with open shared-communication designs proving most vulnerable to
contamination [chen2025medsentry]; routing every message through one auditable point also
serves the audit-trail requirement of Section 3.4. Tool access uses MCP-style standardized
interfaces and inter-agent exchange follows A2A-style conventions [ehtesham2025protocols],
which keeps the prototype composable with hospital tooling. External tools follow the
validated-tool principle of RiskAgent and TxAgent: calculations and lookups are delegated to
auditable components rather than generated [liu2025riskagent; gao2025txagent].

## 3.4 Verification Gate and Audit Trail

The verification agent is the framework's distinguishing safety component. Every candidate
recommendation is checked on three axes: (a) evidential grounding, i.e. whether the claim is
entailed by the retrieved patient evidence and guidelines, screened against known classes of
medical hallucination [kim2025hallucinations]; (b) guideline compliance and conflict with
active orders; and (c) a calibrated confidence estimate that accompanies the recommendation to
the clinician [atf2025uncertainty; guo2017calibration]. Recommendations failing any check are
blocked and returned with the failure reason. Every check writes to an evidence-linked audit
trail. Whether that trail accurately reflects the evidence the system actually used is treated
as a measured property rather than an assumed one, using entailment-based spot audits
[es2024ragas]. The confidence value attached to each recommendation is calibrated post hoc on
a held-out calibration split (temperature scaling, with isotonic regression as a fallback for
non-monotone miscalibration) and its quality is evaluated by expected calibration error and
reliability diagrams [guo2017calibration]. This combination is designed to align with
emerging regulatory expectations for unconfined non-deterministic clinical software:
guardrails, moderation, retrieval grounding, and inspectability
[tan2026undcs; weissman2025unregulated].

## 3.5 Human-in-the-Loop Protocol

Clinicians receive only verified recommendations, each with linked evidence, a calibrated
confidence estimate, and an explanation. Review is structured rather than free-form: approve, modify, or reject, with
reasons captured into memory. The choice reflects meta-analytic evidence that unstructured
clinician–LLM collaboration produces gains too uncertain to build on
[wang2026collaboration]. Rejections and modifications feed the monitoring loop as supervision
signals.

## 3.6 Planned Evaluation Design

This subsection specifies the full evaluation of the LLM-based framework; it is designed but
has not yet been executed. The only completed empirical work in this paper is the non-LLM
pilot reported in Section 5, and no result below should be read as obtained. The planned
full evaluation uses MIMIC-IV [johnson2023mimic] cohorts (sepsis and deterioration use cases;
Sepsis-3 labels [singer2016sepsis3; vincent1996sofa]) and scores the system on longitudinal
tracking, not one-shot prediction. Clinical ground truth is defined concretely per use case:
in-hospital mortality from discharge disposition, sepsis onset time under the Sepsis-3
criteria applied to the recorded observations [singer2016sepsis3], and, for treatment
recommendations, concordance with the interventions documented in the record, adjudicated by
clinician review where the record is ambiguous. The primary metrics are defined as follows.
(1) Decision quality: discrimination (AUROC) and calibration of predicted risk against these
labels, compared with revisited MIMIC-IV baselines [lovon2025mimic]. (2) Grounding rate: of
the atomic claims extracted from a recommendation, the fraction entailed by at least one
retrieved patient-evidence item, following RAG-evaluation practice [es2024ragas]. (3)
Verification-gate effectiveness: among recommendations independently judged ungrounded, the
fraction the gate blocks (catch rate) at a fixed clinician-review budget. (4) Audit-trail
faithfulness: the fraction of logged evidence references that both re-resolve to the source
record and match the value the system actually used, under human spot audit. (5)
Recommendation quality: rubric-graded scores in the style of physician-rubric benchmarks
[arora2025healthbench; jiang2025medagentbench]. Ablations remove patient-timeline retrieval,
the verification gate, and longitudinal memory in turn, isolating each claimed contribution.
Statistical comparisons follow standard practice for correlated classifiers
[delong1988comparing; dietterich1998approximate] with false-discovery control
[benjamini1995controlling].
