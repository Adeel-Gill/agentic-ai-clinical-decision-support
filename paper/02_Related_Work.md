# 2. Related Work

## 2.1 LLM Agents and Their Infrastructure

The agent paradigm grew from reasoning-and-acting loops [yao2023react] and self-taught tool use
[schick2023toolformer] into general architectures with memory, planning, and reflection
[wang2024survey; shinn2023reflexion]. Multi-agent frameworks — AutoGen's conversational
orchestration [wu2024autogen], CAMEL's role-play [li2023camel], MetaGPT's SOP-driven pipelines
[hong2024metagpt] — established coordination patterns that recent surveys have formalized into
taxonomies of collaboration types and structures [tran2025collaboration] and, at the systems
level, into brain-inspired modular blueprints [liu2025foundationagents]. Agent memory has its
own literature organizing construction, management, and retrieval operations [wu2025memory], and
interoperability is standardizing around MCP for tool access and A2A-style protocols for
inter-agent exchange [ehtesham2025protocols]. Sapkota et al. distinguish single tool-using
agents from orchestrated agentic ecosystems and identify healthcare as a primary beneficiary of
the latter [sapkota2025agents]. This infrastructure maturity is what makes our framework
buildable; none of it, however, addresses what a clinical agent should be grounded in or how its
outputs should be verified.

## 2.2 Medical LLMs and Medical Agents

Medical LLMs progressed from encoding clinical knowledge [singhal2023clinical] through
expert-level question answering [singhal2025medpalm2] to multimodal generalists [tu2024generalist]
and open alternatives [toma2023clinicalcamel]. The agentic turn followed: MedAgents assembles
expert-role panels for zero-shot reasoning [tang2024medagents]; Agent Hospital evolves doctor
agents in a simulated hospital [li2024agenthospital]; AgentClinic embeds them in simulated
dialogue [schmidgall2024agentclinic]; EHRAgent executes code over structured records
[shi2024ehragent]. The 2025 generation is more capable: TxAgent reasons over 211 therapeutic
tools [gao2025txagent], RiskAgent routes to validated risk calculators [liu2025riskagent],
MedRAX orchestrates chest X-ray tools in a training-free loop [fallahpour2025medrax],
DoctorAgent-RL learns proactive consultation policies [feng2025doctoragent], and the AMIE line
extends conversational diagnosis to longitudinal management and multimodal evidence
[palepu2025disease; saab2025multimodal]. Surveying this landscape, Wang et al. conclude that
clinical decision-making attracts the most research and the least deployment evidence
[wang2025baymax]. Across all of these systems, patient state is reconstructed from the prompt or
scenario at each step; none maintains a persistent, evidence-linked model of one real patient
across an admission.

## 2.3 Retrieval-Augmented Generation in Medicine

RAG is the standard mitigation for hallucination [lewis2020rag; gao2023rag], refined by
self-critical variants [asai2024selfrag] and, recently, folded into the agent loop as agentic
RAG — retrieval that is planned, executed iteratively, and reflected upon [singh2025agenticrag].
In medicine, MedRAG couples retrieval with a diagnostic knowledge graph [zhao2025medrag], and a
ten-model npj Digital Medicine study shows guideline-grounded RAG can exceed human accuracy in a
bounded preoperative task [ke2025ragfitness]. The corpus, in every case, is external knowledge.
Retrieval anchored to the patient's own longitudinal record — the grounding a monitoring system
actually needs — remains unexplored, which is the specific opening this work occupies.

## 2.4 Evaluation, Safety, and Regulation

Evaluation practice is catching up with agent capabilities. MedAgentBench places agents in a
FHIR-compliant virtual EHR with physician-authored tasks [jiang2025medagentbench]; HealthBench
grades open-ended health conversations against physician rubrics [arora2025healthbench]; general
surveys catalog agent-evaluation methodology and flag safety as under-measured
[yehudai2025evaluation]. On real records, revisited MIMIC-IV baselines show text-based models
competitive with tabular classifiers for one-shot prediction [lovon2025mimic], and COMPOSER-LLM
demonstrates prospective sepsis alerting with an LLM adjudicating high-uncertainty cases
[shashikumar2025sepsis]. The safety literature supplies taxonomies of medical hallucination
[kim2025hallucinations], arguments for calibrated uncertainty [atf2025uncertainty], threat
models for trustworthy agents [yu2025trustagent], and adversarial stress tests showing that
multi-agent topology shapes harm propagation [chen2025medsentry]. Regulatory analyses find that
unconstrained LLMs already produce medical-device-like output [weissman2025unregulated] and
propose governance for unconfined non-deterministic clinical software [tan2026undcs], while the
only meta-analysis of clinician–LLM collaboration reports fragile gains and clinically
significant error rates [wang2026collaboration]. What this literature demands — grounded
recommendations, calibrated confidence, inspectable trails, structured oversight — is precisely
what no current system measures end-to-end; our framework is designed so that these properties
are evaluated rather than claimed.
