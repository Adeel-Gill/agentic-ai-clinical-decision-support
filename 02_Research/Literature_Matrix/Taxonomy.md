# Taxonomy

This file organizes the collected literature (P001–P045) by theme. A paper may appear under
several categories. IDs refer to `Literature_Matrix.md`; citation keys refer to
`../References.bib`.

## Memory
- P002 Generative Agents (`park2023generative`) — memory stream, reflection, retrieval scoring.
- P005 Voyager (`wang2023voyager`) — skill library as procedural memory.
- P009 Survey of LLM Autonomous Agents (`wang2024survey`) — memory as a core module.
- P011 Agent Hospital (`li2024agenthospital`) — experience accumulation in simulated practice.
- P020 AI Agents vs Agentic AI (`sapkota2025agents`) — shared episodic/semantic/vector memory.
- **P029 Memory Mechanisms Survey (`wu2025memory`) — taxonomy of memory construction, management, retrieval.**
- **P033 Foundation Agents (`liu2025foundationagents`) — brain-inspired memory and world-model modules.**
- **P025 AMIE Disease Management (`palepu2025disease`) — multi-visit patient-context tracking.**

## Planning
- P001 ReAct (`yao2023react`) — interleaved reasoning and acting.
- P008 MetaGPT (`hong2024metagpt`) — SOP-driven task decomposition.
- P009 Survey of LLM Autonomous Agents (`wang2024survey`) — planning module taxonomy.
- P020 AI Agents vs Agentic AI (`sapkota2025agents`) — hierarchical goal decomposition.
- **P023 TxAgent (`gao2025txagent`) — multi-step therapeutic plan construction.**
- **P031 Agentic RAG Survey (`singh2025agenticrag`) — retrieval planning inside the agent loop.**
- **P033 Foundation Agents (`liu2025foundationagents`) — planning as a core cognitive module.**
- **P024 DoctorAgent-RL (`feng2025doctoragent`) — learned consultation strategy as sequential decision-making.**

## Reasoning
- P001 ReAct (`yao2023react`); Chain-of-Thought (`wei2022chain`); Tree of Thoughts (`yao2023tree`); Self-Consistency (`wang2023selfconsistency`); Reflexion (`shinn2023reflexion`).
- P010 MedAgents (`tang2024medagents`) — multi-disciplinary expert-panel reasoning.
- P013/P015 Med-PaLM and Med-PaLM 2 (`singhal2023clinical`; `singhal2025medpalm2`) — clinical CoT and ensemble refinement.
- **P026 AMIE Multimodal (`saab2025multimodal`) — state-aware diagnostic dialogue reasoning.**
- **P027 RiskAgent (`liu2025riskagent`) — tool-verified evidence-based risk reasoning.**
- **P036 MedRAX (`fallahpour2025medrax`) — training-free ReAct-style radiology reasoning.**
- **P039 MIMIC-IV Benchmark Revisit (`lovon2025mimic`) — LLM reasoning over structured EHR features.**

## Tool Use
- P004 Toolformer (`schick2023toolformer`) — self-taught API calls.
- P005 Voyager (`wang2023voyager`) — iterative skill acquisition.
- P012 MedRAG (`zhao2025medrag`) — knowledge-graph-assisted retrieval tooling.
- P020 AI Agents vs Agentic AI (`sapkota2025agents`) — coordinated multi-agent tool access.
- **P023 TxAgent (`gao2025txagent`) — 211-tool biomedical toolbox (ToolUniverse).**
- **P027 RiskAgent (`liu2025riskagent`) — validated clinical calculators as tools.**
- **P036 MedRAX (`fallahpour2025medrax`) — orchestration of specialized CXR tools.**
- **P030 Interoperability Protocols (`ehtesham2025protocols`) — MCP as standardized tool access.**

## Multi-Agent Systems
- P006 AutoGen (`wu2024autogen`); P007 CAMEL (`li2023camel`); P008 MetaGPT (`hong2024metagpt`).
- P010 MedAgents (`tang2024medagents`) — collaborative zero-shot medical reasoning.
- P011 Agent Hospital (`li2024agenthospital`) — evolvable hospital simulacrum.
- **P024 DoctorAgent-RL (`feng2025doctoragent`) — doctor/patient/evaluator agent triad trained with RL.**
- **P032 Collaboration Mechanisms Survey (`tran2025collaboration`) — cooperation/competition/coopetition taxonomy.**
- **P030 Interoperability Protocols (`ehtesham2025protocols`) — A2A, ACP, ANP communication standards.**
- **P042 MedSentry (`chen2025medsentry`) — safety of medical multi-agent topologies.**
- **P033 Foundation Agents (`liu2025foundationagents`) — collective intelligence across agent societies.**

## Retrieval-Augmented Generation
- RAG original (`lewis2020rag`); RAG survey (`gao2023rag`); Self-RAG (`asai2024selfrag`).
- P012 MedRAG (`zhao2025medrag`) — KG-elicited diagnostic retrieval.
- **P031 Agentic RAG Survey (`singh2025agenticrag`) — agent-driven iterative retrieval.**
- **P041 Guideline RAG across 10 LLMs (`ke2025ragfitness`) — clinical-guideline grounding, prospectively framed.**
- **P023 TxAgent (`gao2025txagent`) — real-time biomedical knowledge retrieval during reasoning.**

## Large Language Models in Healthcare
- P013 Med-PaLM (`singhal2023clinical`); P015 Med-PaLM 2 (`singhal2025medpalm2`); P016 Med-PaLM M (`tu2024generalist`); P017 MultiMedQA (`singhal2023clinical`); P019 Clinical Camel (`toma2023clinicalcamel`); P014 LLMs in Medicine survey (`zhou2024survey`).
- **P021 Medical Agents Survey (`wang2025baymax`) — landscape of LLM agents in medicine.**
- **P025/P026 AMIE extensions (`palepu2025disease`; `saab2025multimodal`) — management and multimodal dialogue.**
- **P040 COMPOSER-LLM (`shashikumar2025sepsis`) — prospective bedside sepsis prediction.**
- **P039 MIMIC-IV Benchmark Revisit (`lovon2025mimic`) — LLMs vs tabular baselines on real EHR data.**

## Clinical Decision Support
- P010 MedAgents (`tang2024medagents`); P011 Agent Hospital (`li2024agenthospital`); AgentClinic (`schmidgall2024agentclinic`); EHRAgent (`shi2024ehragent`).
- **P022 MedAgentBench (`jiang2025medagentbench`) — agent tasks inside a FHIR virtual EHR.**
- **P023 TxAgent (`gao2025txagent`) — therapeutic decision support.**
- **P027 RiskAgent (`liu2025riskagent`) — risk-score-backed decisions.**
- **P040 COMPOSER-LLM (`shashikumar2025sepsis`) — deployed early-warning decision support.**

## Trustworthy AI
- P018 Toward Trustworthy AI in Healthcare (`jimenez2023trustworthy`); explainable ML (`rasheed2022explainable`); fairness (`mehrabi2021survey`; `hardt2016equality`); calibration (`guo2017calibration`).
- **P035 TrustAgent Survey (`yu2025trustagent`) — intrinsic/extrinsic trust threat taxonomy.**
- **P037 Medical Hallucinations (`kim2025hallucinations`) — hallucination taxonomy and clinician survey.**
- **P038 Uncertainty Quantification (`atf2025uncertainty`) — calibrated confidence for medical LLMs.**
- **P042 MedSentry (`chen2025medsentry`) — adversarial stress-testing of medical MAS.**
- **P043 Unregulated Device-Like Output (`weissman2025unregulated`) — regulatory exposure of raw LLMs.**
- **P044 UNDCS Regulation (`tan2026undcs`) — governance framework for agentic clinical software.**

## Human-in-the-Loop
- P010 MedAgents (`tang2024medagents`) — expert-consensus stand-in for oversight.
- P018 Trustworthy AI (`jimenez2023trustworthy`) — human oversight as a trust mechanism.
- **P045 Human–LLM Collaboration Meta-Analysis (`wang2026collaboration`) — empirical evidence on clinician–AI teaming.**
- **P044 UNDCS Regulation (`tan2026undcs`) — agent moderation and human accountability requirements.**
- **P028 HealthBench (`arora2025healthbench`) — physician-rubric grading as structured human judgment.**

## Evaluation and Safety Benchmarks
- MedQA (`jin2021medqa`); MultiMedQA (`singhal2023clinical`); RAGAS (`es2024ragas`).
- **P022 MedAgentBench (`jiang2025medagentbench`) — virtual-EHR agent benchmark.**
- **P028 HealthBench (`arora2025healthbench`) — rubric-graded health conversations.**
- **P034 Agent Evaluation Survey (`yehudai2025evaluation`) — evaluation methodology landscape.**
- **P039 MIMIC-IV Benchmark Revisit (`lovon2025mimic`) — real-record prediction baselines.**
- **P042 MedSentry (`chen2025medsentry`) — adversarial safety benchmark.**

## Longitudinal EHR Reasoning (added 2026-08-08)
- **P046 CliCARE (`li2026clicare`) — patient EHR as temporal knowledge graph aligned with guideline KG (AAAI-26; MIMIC-IV).**
- **P047 Traj-CoA (`zeng2025trajcoa`) — chain-of-agents summarization of multi-year records with EHRMem timeline memory.**
- **P048 TrajOnco (`zeng2026trajonco`) — multi-agent temporal reasoning for multi-cancer early detection (Truveta EHR).**
- **P049 TIMER (`cui2025timer`) — temporal instruction benchmark + tuning over longitudinal records (npj Digit Med).**
- **P050 RGAR (`liang2025rgar`) — dual-corpus (EHR context + external knowledge) iterative retrieval for medical QA.**
- Differentiation claimed by the thesis: these compress, align, or benchmark the longitudinal record; none couples timestamp-addressable retrieval to recommendation-level verification with a measured audit trail.

Bold entries are the 2025–2026 additions (P021–P050).
