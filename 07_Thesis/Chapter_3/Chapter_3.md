# Chapter 3 — Proposed Framework and Methodology

## 3.1 Design Methodology

This chapter presents the design of the proposed framework and the methodology that produced it. The work follows a design-science research process, which treats the framework itself as the primary research artifact and organizes the investigation around four activities: identifying a problem, designing an artifact that addresses it, demonstrating the artifact on a realistic case, and evaluating whether the demonstration meets the stated objectives [hevner2004design]. I adopt this stance deliberately. A purely empirical study would ask whether one model outperforms another on a benchmark; a design study instead asks whether a coherent architecture can be assembled from known components to satisfy clinical requirements that no single existing system satisfies at once. That framing matters because the contribution here is integrative rather than a new learning algorithm.

The problem is drawn from the gaps established in Chapter 2. Retrieval-augmented clinical systems such as MedRAG improve factual grounding but operate as isolated question-answering pipelines rather than continuous decision support [zhao2025medrag]. Multi-agent medical reasoners such as MedAgents demonstrate that specialization improves answer quality on examination-style questions, yet they neither maintain longitudinal patient memory nor expose their reasoning to a clinician for approval [tang2024medagents]. Agent Hospital simulates collaborative care but does so in a synthetic environment disconnected from real electronic health records [li2024agenthospital]. AgentClinic and AMIE advance interactive diagnostic dialogue, but their evaluations emphasize conversational competence over auditable, guideline-anchored recommendations that a supervising physician can inspect [schmidgall2024agentclinic; tu2025amie]. The design objective, therefore, is a framework that combines multi-agent specialization, dual-grounded retrieval, persistent patient memory, and mandatory human oversight over one longitudinal record source, MIMIC-IV [johnson2023mimic].

The design activity proceeds top-down. I first fix the layering that separates data, memory, knowledge, orchestration, decision, and presentation concerns, then specify the agents that populate the orchestration layer, and finally define the memory and retrieval machinery that the agents depend on. Each design decision is justified against the literature or, where the literature is silent, against an explicit engineering trade-off. The demonstration activity is a worked patient trajectory carried end-to-end through every agent (Section 3.7); it is a textual trace rather than measured results because the prototype is bounded and its empirical evaluation belongs to Chapter 4. The evaluation activity is likewise deferred to Chapter 4, but this chapter states the mechanisms — bias measurement, calibration, audit logging — that make evaluation possible, so that the artifact is falsifiable rather than merely plausible.

A caveat is worth stating early. Design-science research is vulnerable to post-hoc rationalization, where every choice appears inevitable in hindsight. To guard against that, I flag two components the original design in `Proposed_Framework.md` omitted — a dedicated Data/Retrieval Agent and a Memory-Manager module — and argue for them explicitly rather than folding them silently into the existing agents (Section 3.4). Where a design choice is a genuine bet under uncertainty, such as the vector-store selection, I say so and defer the risk analysis to the companion feasibility document.

## 3.2 Architecture Overview

The proposed framework is organized into six horizontal layers with one cross-cutting layer, illustrated in Figure 3.1. The horizontal layers, from the data substrate upward, are the Data Layer, the Memory Layer, the Reasoning and Knowledge Layer, the Agent Orchestration Layer, the Clinical Decision Layer, and the Clinician Dashboard. Cutting across all six is the Trustworthy AI Layer, which is not a stage in the pipeline but a set of controls — explanation capture, audit logging, bias monitoring, and confidence calibration — that every layer writes into and that governs whether an output is allowed to surface. Human-in-the-loop (HITL) control sits between the Clinical Decision Layer and the dashboard, gating any recommendation before a clinician sees it framed as actionable.

The layering is a separation-of-concerns device. Data acquisition should not know how memory is summarized; reasoning should not know how the dashboard renders; and the orchestration of agents should be describable independently of the specific large language model that backs each agent. This is the same architectural discipline that distinguishes agentic systems from monolithic prompting, where retrieval, memory, and control collapse into a single context window [sapkota2025agents]. Keeping the layers distinct also localizes the two hardest risks — context-window pressure in the Memory Layer and end-to-end latency in the Orchestration Layer — so that mitigations can be applied without redesigning the whole framework.

Data flows upward during a case and control flows downward. A patient event enters at the Data Layer, is contextualized by the Memory Layer, is grounded by the Reasoning and Knowledge Layer through retrieval, is processed by a condition-dependent subset of agents in the Orchestration Layer, is fused and checked in the Clinical Decision Layer, and is presented for approval at the dashboard. The clinician's decision then flows back down as feedback written into memory. The remainder of this chapter walks each layer and then specifies the agents.

**Figure 3.1:** Proposed six-layer Agentic AI framework with a cross-cutting Trustworthy AI layer and human-in-the-loop gating, grounded in the MIMIC-IV critical-care database.

## 3.3 Layer Specifications

### 3.3.1 Data Layer

The Data Layer is the framework's contract with MIMIC-IV [johnson2023mimic]. Its responsibility is to expose the relevant relational tables — patients, admissions, ICU stays, chartevents for vital signs, labevents, prescriptions, procedures, diagnoses coded in ICD, and the free-text notes — as a normalized patient timeline rather than as raw tables. Its input is a patient identifier and a time window; its output is a chronologically ordered event stream in which each event carries a type, a timestamp, a value with units, and a provenance pointer back to the source row. That provenance pointer is not cosmetic: it is what lets a downstream explanation cite the exact laboratory result that drove a recommendation, and it is what the audit log records.

A subtlety the original design glossed over is that MIMIC-IV timestamps are shifted per patient for de-identification, so absolute dates are meaningless while intervals are preserved [johnson2023mimic]. The Data Layer therefore works exclusively in relative time from admission. It also performs unit harmonization and range validation, because a downstream Diagnosis Agent that receives a potassium value in the wrong unit will reason confidently toward a wrong conclusion. Interface-wise, the layer offers two operations to the rest of the framework: a bulk timeline fetch used at case initialization, and an incremental "events since timestamp t" fetch used by the Monitoring Agent to detect change.

### 3.3.2 Memory Layer

The Memory Layer retains what the framework has seen and concluded. Its inputs are the timeline events from the Data Layer, the intermediate outputs of every agent, and clinician feedback; its outputs are context bundles assembled on request for whichever agent is about to run. It comprises four memory types (detailed in Section 3.5) and, critically, a Memory-Manager module that decides what to keep verbatim, what to summarize, and what to evict. The original design listed the four memory stores but left the control policy implicit; making the Memory-Manager an explicit component is one of this chapter's additions, because context-window pressure is a first-order technical risk and cannot be managed by storage alone.

### 3.3.3 Reasoning and Knowledge Layer

This layer supplies grounded reasoning to the agents above it. It houses the ReAct reasoning engine (Section 3.7) and the RAG pipeline (Section 3.6), and it exposes curated knowledge — clinical practice guidelines, a drug-interaction reference, and a medical knowledge base of disease, symptom, and lab-interpretation entries. Its input is a natural-language query plus the current patient context; its output is a ranked set of evidence passages, each with a citation, together with the reasoning trace that consumed them. The layer's defining property in this framework is dual grounding: every retrieval spans both the patient-specific record and the external evidence corpus, so that a recommendation is anchored simultaneously in what is true of this patient and what is true in the literature. Systems that retrieve only from external corpora, as most medical RAG work does, cannot personalize; systems that read only the record cannot bring guidelines to bear [zhao2025medrag; gao2023rag].

### 3.3.4 Agent Orchestration Layer

The Orchestration Layer is where the framework's intelligence is distributed. A Coordinator routes work to specialized agents — Monitoring, Planner, Diagnosis, Risk Prediction, Treatment Recommendation, Explanation, and Verification — plus the newly added Data/Retrieval Agent. Its input is a triggering event and the current patient context; its output is a set of validated agent results handed to the Clinical Decision Layer. The routing is not a fixed sequence. As Section 3.4 details, the Coordinator builds a condition-triggered directed acyclic graph so that, for example, a stable routine check does not invoke the full seven-agent pipeline. This is a direct response to the latency problem: MedAgents reports roughly forty seconds per examination question with a handful of agents, and a naive seven-agent pipeline would multiply that into minutes per case [tang2024medagents].

### 3.3.5 Clinical Decision Layer

This layer fuses agent outputs into a single decision object: a diagnosis with differentials, a risk score, a treatment recommendation, a faithful explanation, and a calibrated confidence value. Its input is the set of verified agent results; its output is one structured recommendation plus a disposition flag that the HITL gate reads. The layer performs no clinical reasoning of its own — that would duplicate the agents and obscure provenance. It arbitrates, using the conflict-resolution protocol of Section 3.4, and it refuses to emit a recommendation that has not passed the Verification Agent. The refusal path matters: a decision layer that always produces an answer, even a low-confidence one framed identically to a high-confidence one, actively misleads clinicians.

### 3.3.6 Clinician Dashboard

The dashboard presents the decision object for human review. Its input is the recommendation and its supporting evidence and confidence; its output is the clinician's action — approve, modify, reject, or request more information — captured as feedback. The design principle is that the dashboard supports review, not automation: nothing it displays is enacted without a clinician's explicit action. It surfaces the explanation and the cited evidence alongside every recommendation, because an explanation the clinician must hunt for is an explanation that will be ignored under time pressure.

### 3.3.7 Trustworthy AI Layer (cross-cutting)

The Trustworthy AI Layer is described with its mechanisms in Section 3.8. Architecturally, it is cross-cutting because trustworthiness cannot be a terminal checkpoint; it must be enforced where each concern arises. Explanations are captured at the reasoning step that produced them, audit records are written by every agent as it acts, bias is measured on the data as it is partitioned, and calibration is applied to confidence at the point of emission. Bolting these onto the end would produce plausible-looking but unfaithful post-hoc rationalizations, which is precisely the failure mode trustworthy-AI work in healthcare warns against [rasheed2022explainable; jimenez2023trustworthy].

## 3.4 Agent Specifications

Each agent is an LLM-driven role with a defined contract: what it consumes, what tools or retrieval it may call, the schema of what it emits, and how it behaves on failure. The contracts below are the interfaces the Coordinator relies on. I present them as compact tables because a contract is inherently tabular; the reasoning around them stays in prose.

Two components are additions to the original design and are marked as such. The **Data/Retrieval Agent** was missing: the original framework assumed agents would somehow acquire their own data, which conflates reasoning with I/O and makes provenance untraceable. Introducing a dedicated agent that owns all reads from the Data Layer and the RAG pipeline centralizes provenance and lets every other agent be a pure reasoner over supplied evidence. The **Memory-Manager** (Section 3.5) is the second addition, a non-agent module rather than an agent because it applies deterministic policy rather than LLM reasoning.

### 3.4.1 Agent contracts

**Monitoring Agent**

| Field | Specification |
|---|---|
| Inputs | Incremental event stream ("events since t") from the Data Layer |
| Tools / Retrieval | Threshold rules; short-term memory read; trend queries |
| Output schema | `{alerts:[{type, severity, evidence_ref, delta}], stable:bool}` |
| Failure / escalation | On missing data, emit `data_gap` alert; never suppress an alert on uncertainty |

**Planner Agent**

| Field | Specification |
|---|---|
| Inputs | Triggering alerts; patient context summary |
| Tools / Retrieval | Task-decomposition prompt; agent registry |
| Output schema | `{plan:[{agent, inputs, depends_on}], rationale}` |
| Failure / escalation | If it cannot decompose, escalate to Coordinator for default full pipeline |

**Data/Retrieval Agent** *(added)*

| Field | Specification |
|---|---|
| Inputs | Structured query from any agent (patient scope and/or external scope) |
| Tools / Retrieval | Data Layer timeline API; RAG pipeline (Section 3.6) |
| Output schema | `{passages:[{text, source, citation, score}], record_slices:[...]}` |
| Failure / escalation | On empty retrieval, return explicit `no_evidence` marker, never fabricate |

**Diagnosis Agent**

| Field | Specification |
|---|---|
| Inputs | Timeline slices, retrieved evidence, patient history summary |
| Tools / Retrieval | ReAct loop; dual-grounded retrieval via Data/Retrieval Agent |
| Output schema | `{differentials:[{dx, likelihood, evidence_refs}], primary_dx}` |
| Failure / escalation | If differentials are undifferentiable, flag `insufficient_evidence` and request more data |

**Risk Prediction Agent**

| Field | Specification |
|---|---|
| Inputs | Timeline slices; diagnosis output; historical outcomes |
| Tools / Retrieval | Risk scoring; trend analysis; guideline retrieval |
| Output schema | `{risks:[{outcome, probability, horizon, evidence_refs}]}` |
| Failure / escalation | Report wide uncertainty bounds rather than a false point estimate |

**Treatment Recommendation Agent**

| Field | Specification |
|---|---|
| Inputs | Diagnosis, risks, current medications, allergies |
| Tools / Retrieval | Guideline retrieval; drug-interaction checker |
| Output schema | `{recommendations:[{action, dose, rationale, evidence_refs}], contraindications:[...]}` |
| Failure / escalation | On detected interaction, withhold the offending action and flag it |

**Explanation Agent**

| Field | Specification |
|---|---|
| Inputs | All upstream outputs and their evidence_refs |
| Tools / Retrieval | Trace assembly; citation resolution |
| Output schema | `{explanation, cited_evidence:[...], reasoning_trace_ref}` |
| Failure / escalation | If a claim lacks an evidence_ref, mark it `unsupported` rather than narrating it |

**Verification Agent**

| Field | Specification |
|---|---|
| Inputs | Fused recommendation and all supporting evidence |
| Tools / Retrieval | Guideline compliance checks; consistency and confidence checks |
| Output schema | `{verdict: pass\|fail\|review, violations:[...], adjusted_confidence}` |
| Failure / escalation | Any hard violation forces `fail`; borderline forces `review` (HITL) |

### 3.4.2 Coordinator routing logic

The Coordinator does not run every agent for every event. It maintains an agent registry and constructs, per triggering event, a directed acyclic graph whose nodes are agents and whose edges are data dependencies. Routing is condition-triggered. A Monitoring alert of low severity with no new abnormal labs routes to a short path — Monitoring then Verification then dashboard — because invoking Diagnosis, Risk, and Treatment on a stable patient wastes latency budget and inflates cost with no clinical gain. An alert that crosses a deterioration threshold routes to the full graph: Planner decomposes the task, the Data/Retrieval Agent gathers dual-grounded evidence, Diagnosis and Risk run in parallel since neither depends on the other, Treatment consumes both, Explanation consumes all three, and Verification gates the result. The parallelism is deliberate and is the single most effective latency mitigation available, since the dominant cost is LLM inference and independent branches can run concurrently [tang2024medagents].

The Planner and the Coordinator have distinct jobs that are easy to confuse. The Planner proposes a decomposition — which agents, in which order, with which inputs. The Coordinator decides whether to accept that plan, executes it against real dependencies and resource limits, handles agent failures, and enforces the conflict-resolution protocol. Separating proposal from execution keeps the Planner a pure reasoning agent and keeps failure handling in one place.

### 3.4.3 Conflict-resolution and arbitration protocol

Specialized agents will sometimes disagree. The Risk Prediction Agent may flag high sepsis risk while the Diagnosis Agent's primary differential is non-infectious; the Treatment Agent may propose an intervention the Verification Agent finds contraindicated. A framework that silently averages such disagreements produces incoherent recommendations. The proposed arbitration protocol is explicit and ordered. First, **hard safety constraints dominate**: any Verification violation — a drug interaction, a guideline breach, a dosing error — vetoes the conflicting recommendation outright, regardless of other agents' confidence. Second, for non-safety disagreements, arbitration is **evidence-weighted**: the Clinical Decision Layer compares the strength and recency of the cited evidence behind each position, preferring the claim grounded in higher-quality retrieved evidence over the one resting on model priors alone [asai2024selfrag]. Third, when evidence is comparable and the disagreement persists, the protocol **does not force a resolution**; it emits both positions with their evidence and sets the disposition flag to `review`, escalating to the clinician through HITL. The design bias is toward surfacing genuine uncertainty rather than manufacturing false consensus, which is the safer failure mode in a decision-support setting where the human retains authority.

## 3.5 Memory Model

The framework maintains four kinds of memory, mirroring the memory taxonomy that emerges from the agent literature [park2023generative; wang2024survey]. **Short-term working memory** holds the current reasoning session: the active labs, recent vitals, and the running ReAct trace. **Long-term patient memory** holds the longitudinal record — prior admissions, chronic conditions, past diagnoses, and treatment history — persisted across sessions. **Semantic vector memory** holds embeddings of clinical notes, discharge summaries, and external literature for similarity retrieval. **Episodic clinical-context memory** holds prior agent outputs, past recommendations, and clinician feedback, so the framework can recall what it concluded before and how the clinician responded.

The read/write/reflect policy governs how these stores are used. On **read**, the Memory-Manager assembles a context bundle by pulling the working set verbatim, the most relevant long-term facts by recency and clinical salience, and the top semantic matches from vector memory. On **write**, every agent output and every clinician action is appended to episodic memory with provenance, and notable events are promoted from short-term to long-term memory. On **reflect** — a periodic consolidation borrowed from reflective agent designs [park2023generative; shinn2023reflexion] — the Memory-Manager compresses stale working memory into summaries, extracts durable facts into long-term memory, and discards transient detail. Reflection is where the framework turns a growing transcript into a stable patient model instead of an ever-lengthening log.

The hardest problem this layer confronts is the context window, and I treat it as a first-order risk rather than an implementation detail. A full MIMIC-IV ICU stay contains thousands of chart events and long free-text notes; concatenating them exceeds any practical context length, and even where it fits, models attend poorly to the middle of very long contexts. The mitigation is twofold. **Summarization** collapses older and lower-salience content into compact structured summaries during reflection, so the working context carries a faithful digest rather than raw history. **Retrieval windowing** ensures that instead of loading the whole record, each agent receives only the timeline slices and evidence passages its current query retrieved, bounded to a fixed token budget. The Memory-Manager enforces that budget, evicting the least relevant material first and always preserving provenance pointers so that a summarized fact can be expanded back to its source on demand. This is where the Memory-Manager earns its place as an explicit module: the policy is deterministic, safety-relevant, and too important to leave scattered across agent prompts.

## 3.6 Retrieval-Augmented Generation Pipeline

Retrieval is the mechanism by which the framework grounds its outputs in evidence rather than in the language model's parametric memory, following the original retrieval-augmented generation formulation [lewis2020rag] and the design patterns consolidated in the RAG survey literature [gao2023rag]. The pipeline has six stages: ingest, chunk, embed, retrieve, rerank, and generate.

**Ingest** brings two corpora into the system. The first is patient-specific: MIMIC-IV clinical notes and structured events for the patient under care [johnson2023mimic]. The second is external: clinical practice guidelines and a curated slice of medical literature. **Chunk** splits documents into passages sized to balance retrieval precision against context cost — clinical notes are segmented on section boundaries rather than fixed windows, because splitting a lab-interpretation paragraph mid-sentence destroys its meaning. **Embed** maps each chunk to a dense vector; the framework uses a biomedical sentence-embedding model rather than a general-purpose one, because domain-tuned embeddings materially improve retrieval of clinical text where general models conflate distinct medical concepts [zhao2025medrag]. **Retrieve** performs approximate nearest-neighbor search over the vector store. **Rerank** applies a cross-encoder to the top candidates, which is more expensive per pair but far more precise than embedding similarity alone and is the stage most responsible for keeping irrelevant passages out of the prompt [gao2023rag]. **Generate** composes the reranked evidence with the query and the patient context into the answering agent's prompt.

The differentiating property is **dual grounding**. Every retrieval issued by the Data/Retrieval Agent runs against both the patient timeline and the external corpus, and the two result sets are merged before reranking. A treatment recommendation is thus anchored simultaneously in this patient's renal function and creatinine trend and in the guideline that conditions dosing on renal function. Retrieving from only one source is the common failure of prior work: external-only RAG cannot personalize, and record-only retrieval cannot bring current evidence to bear [zhao2025medrag; gao2023rag]. The framework also adopts a self-reflective retrieval check in the spirit of Self-RAG, where the answering agent assesses whether retrieved passages actually support the intended claim and re-queries or abstains if they do not, rather than generating over weak evidence [asai2024selfrag].

For concrete choices, the vector store is **pgvector** for the bounded prototype and **Qdrant** as the scale-out option. The justification is honest rather than aspirational: pgvector keeps embeddings in the same PostgreSQL instance that already holds the MIMIC-IV relational data, which eliminates a separate service, simplifies provenance joins between an embedding and its source row, and is entirely adequate at prototype scale. Qdrant is named as the migration target because a full-corpus deployment with many concurrent cases will outgrow pgvector's filtered-search performance, and Qdrant offers payload filtering and horizontal scaling designed for that regime. The embedding model is a biomedical bi-encoder and the reranker a cross-encoder, chosen for the precision reasons above. These choices carry risk, and that risk — index size, reranker latency, retrieval quality — is analyzed in the companion feasibility document rather than asserted away here.

## 3.7 ReAct Reasoning Loop

The agents reason using the ReAct paradigm, which interleaves reasoning traces with actions so that a model can think, act on the environment, observe the result, and think again [yao2023react]. This matters clinically because diagnosis is not a single forward pass; it is a loop of hypothesis, evidence-gathering, and revision. A pure chain-of-thought prompt reasons without acting and cannot pull the specific lab value it needs mid-inference [wei2022chain]; ReAct closes that gap by letting each reasoning step issue a retrieval or tool call and fold the observation back in. The framework also permits self-correction in the manner of Reflexion, where an agent that reaches a dead end revises its approach using a record of what failed [shinn2023reflexion].

The following worked trace demonstrates the loop end-to-end for one patient scenario. Consider an ICU patient, on relative day two of admission, whose recent chart events show rising heart rate, a rising temperature, and a new lactate elevation.

The Monitoring Agent, reading the incremental event stream, emits a high-severity alert: temperature and heart rate crossing thresholds with an abnormal lactate, evidence-referenced to the specific chartevents rows. The Coordinator sees a threshold-crossing alert and constructs the full DAG. The Planner decomposes the task: establish a diagnosis, quantify deterioration risk, and propose an intervention, in that dependency order. The Data/Retrieval Agent runs dual-grounded retrieval — pulling the patient's recent vitals, white-cell count, and culture status from the timeline, and pulling sepsis-recognition guidance from the external corpus.

The Diagnosis Agent now enters its ReAct loop. *Thought*: the triad of fever, tachycardia, and lactate elevation suggests an infectious process; sepsis is a leading differential but requires a suspected source. *Action*: retrieve recent culture and imaging results. *Observation*: cultures pending, no imaging; white-cell count elevated. *Thought*: evidence is consistent with sepsis but the source is unconfirmed, so the differential must remain open. *Action*: none further; emit differentials with sepsis primary and evidence references. Running in parallel, the Risk Prediction Agent quantifies short-horizon deterioration and ICU-mortality risk, citing the lactate trend and vitals. The Treatment Recommendation Agent consumes both, retrieves the sepsis bundle guidance, checks the patient's current medications and renal function through the drug-interaction tool, and proposes early evidence-based steps with dosing conditioned on renal function, withholding any action that the interaction check flags.

The Explanation Agent assembles a faithful narrative in which every clause carries an evidence reference back to a chartevent, a lab, or a cited guideline passage; any claim it cannot ground it marks as unsupported rather than narrating smoothly over the gap. The Verification Agent checks guideline compliance, cross-agent consistency, and confidence. Here it finds no hard violation but notes that the diagnostic source is unconfirmed, so it returns a `review` verdict with adjusted confidence. The Clinical Decision Layer fuses the outputs into one recommendation and, because the verdict is `review`, sets the disposition to escalate. The dashboard presents the sepsis-leaning recommendation, the risk figures, the cited evidence, and the calibrated confidence, explicitly flagged for clinician confirmation of the source. The clinician's decision is written back to episodic memory. The trace shows the design working as intended: specialization, dual grounding, faithful explanation, and — crucially — an honest escalation rather than a manufactured certainty.

## 3.8 Trustworthy AI Layer

Trustworthiness in this framework is a set of mechanisms, not a checklist, and each mechanism is wired into the layer where its concern originates [rasheed2022explainable; jimenez2023trustworthy].

**Faithful explainability.** The Explanation Agent does not paraphrase a conclusion after the fact; it assembles the explanation from the evidence references that the reasoning agents actually consumed. Every clause resolves to a provenance pointer — a specific chart event, lab result, or cited guideline passage. A claim without a supporting reference is labeled unsupported and shown as such, which prevents the fluent-but-fabricated rationalizations that undermine post-hoc explanation methods. Faithfulness here means the explanation is constructed from the same evidence the decision was, not reconstructed to fit it.

**Structured audit logs.** Every agent writes an append-only audit record as it acts: a timestamp in relative time, the agent identity, the inputs it received, the tool or retrieval calls it made, the evidence references it used, its output, and the model version. Records are immutable and chained so that a full case can be replayed exactly. This structure is what makes the framework accountable — a clinician or auditor can reconstruct why any recommendation was produced, which is a precondition for clinical governance [jimenez2023trustworthy].

**Bias measurement on MIMIC-IV subgroups.** Rather than asserting fairness, the framework measures it. MIMIC-IV carries demographic attributes — age, sex, and coded ethnicity — that permit subgroup analysis [johnson2023mimic]. The Trustworthy AI Layer partitions evaluation cases by these attributes and computes performance-parity metrics across subgroups, so that a Risk Prediction Agent that systematically under-estimates risk for one group is detected rather than deployed. The specific parity metrics and the statistical treatment are specified in Chapter 4; the mechanism the framework provides is the partitioning and the per-subgroup measurement hook [hardt2016equality; mehrabi2021survey].

**Confidence calibration.** Raw language-model confidence is poorly calibrated, so the framework post-processes it. The Verification Agent's `adjusted_confidence` is a calibrated value produced by a post-hoc calibration step fit on held-out cases, so that a reported confidence of 0.8 corresponds to roughly 80 percent empirical correctness rather than an arbitrary self-report [guo2017calibration]. Calibrated confidence is load-bearing: it drives the HITL disposition, since low or borderline confidence forces escalation, and it lets the dashboard distinguish a confident recommendation from a tentative one instead of presenting both identically.

## 3.9 Human-in-the-Loop Workflow

The framework never enacts a clinical decision autonomously. Human-in-the-loop control sits between the Clinical Decision Layer and any action, and it is mandatory rather than optional. The disposition flag set during arbitration determines how a recommendation reaches the clinician: a clean pass surfaces as an actionable recommendation with its evidence and calibrated confidence, while a `review` or `fail` disposition surfaces with the specific reason for escalation — an unconfirmed diagnostic source, a detected contraindication, an unresolved inter-agent conflict — foregrounded.

The clinician has four responses: approve, modify, reject, or request more information. Each is captured as structured feedback and written to episodic memory with full provenance. Approval confirms the recommendation and records the concurrence. Modification records both the original and the edited recommendation, which is the most informative signal the framework can receive because it localizes exactly where the machine and the clinician diverged. Rejection records the recommendation as declined with an optional reason. A request for more information re-triggers the Coordinator with the clinician's question as an additional constraint. This feedback loop is not merely logged; it feeds the reflect stage of the Memory Layer and, over time, the calibration and bias-monitoring datasets of the Trustworthy AI Layer, so that clinician oversight compounds into measurable improvement rather than evaporating after each case.

## 3.10 Summary

This chapter specified the proposed framework as a design-science artifact: six horizontal layers, a cross-cutting Trustworthy AI layer, and mandatory human oversight, all grounded in MIMIC-IV. Beyond restating the layered structure, it supplied the rigor an examiner expects — per-agent contracts with explicit inputs, tools, output schemas, and failure behavior; a condition-triggered DAG for Coordinator routing that also serves as the primary latency mitigation; and an ordered conflict-resolution protocol that lets safety constraints veto, weighs evidence for other disagreements, and escalates genuine uncertainty rather than forging consensus. It made two components explicit that the original design omitted, the Data/Retrieval Agent and the Memory-Manager, and justified each. It treated the context window as a first-order risk answered by summarization and retrieval windowing, specified a dual-grounded RAG pipeline with concrete and honestly-hedged technology choices, and walked a full patient scenario through the ReAct loop end-to-end. Finally, it framed trustworthiness as wired-in mechanisms — faithful explanation, chained audit logs, subgroup bias measurement, and calibrated confidence — rather than a terminal checklist. The empirical evaluation of these claims, including the bias metrics and calibration procedure flagged above, is the subject of Chapter 4.
