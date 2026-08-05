# Paper 035

## Basic Information
- **Title:** A Survey on Trustworthy LLM Agents: Threats and Countermeasures
- **Authors:** Miao Yu, Fanci Meng, Xinyun Zhou, Shilong Wang, Junyuan Mao, Linsey Pang, et al.
- **Year:** 2025
- **DOI:** 10.48550/arXiv.2503.09648
- **Venue:** arXiv:2503.09648 (KDD 2025)
- **Publisher:** arXiv / ACM
- **Link:** https://arxiv.org/abs/2503.09648

## Abstract Summary (200–300 words)
This survey proposes **TrustAgent**, a comprehensive framework for studying the trustworthiness of LLM-based agents and multi-agent systems (MAS), arguing that adding modules — memory, tools, environment, and other agents — to an LLM expands the attack surface in ways prior "trustworthy LLM" research cannot cover. TrustAgent is characterized by three features. It is **modular**: trustworthiness is split into **intrinsic** aspects — the LLM **brain**, **memory in retrieval** (long-term RAG-style vector stores plus short-term dialogue memory), and **tools for action** — and **extrinsic** aspects — agent-to-agent, agent-to-environment, and agent-to-user interactions. It is **technical**: for each module the survey systematizes **attacks, defenses, and evaluation** paradigms. It is **multi-dimensional**: trustworthiness spans safety, privacy, truthfulness, fairness, and robustness. For the brain, attacks include jailbreak (including agent-driven and infectious variants), prompt injection, and backdoors; defenses include alignment, single-model filters (e.g., GuardAgent guardrails), and multi-agent shields (debate, reviewer agents, AutoDefense); evaluation ranges from focused assessments (InjecAgent, AgentDojo) to general benchmarks (Agent-SafetyBench, AgentHarm, R-Judge). Memory threats comprise **memory poisoning** (PoisonedRAG, AgentPoison), **privacy leakage** (RAG-Thief, embedding inversion), and **memory misuse** (multi-turn jailbreaks); defenses include detection (TrustRAG clustering), prompt modification, and output intervention (RobustRAG). Tool threats include manipulation and abuse, with defenses "notably scarce." Extrinsic sections cover cooperative and infectious agent-to-agent attacks, topological/collaborative defenses, environment-specific risks (including healthcare, e.g., Polaris and privacy-preserving medical agents), and user-trust calibration. The authors identify open gaps — tool-invocation defenses, systematic memory and inter-agent evaluation — and outline future directions toward trustworthy agent ecosystems.

## Research Problem
- Prior trustworthiness research targets **standalone LLMs**; agents add memory, tools, environment interaction, and inter-agent communication, each introducing **new attack surfaces and failure modes** that existing taxonomies, defenses, and benchmarks do not cover.
- Existing agent-security surveys address only sub-aspects (mostly attacks on the LLM brain), lack a modular view, a defense/evaluation treatment, and MAS coverage.

## Proposed Solution
- The **TrustAgent framework**: a modular (intrinsic: brain, memory, tool; extrinsic: agent, environment, user), technical (attack / defense / evaluation), and multi-dimensional (safety, privacy, truthfulness, fairness, robustness) taxonomy of agent trustworthiness.
- For every module it distills **named technical paradigms** (e.g., memory poisoning vs. privacy leakage vs. memory misuse; alignment vs. single-model filter vs. multi-agent shield) and maps existing systems onto them, with a maintained GitHub catalog.

## Architecture
- Not proposing a system, but its reference agent decomposition is architectural: an LLM **brain** (reasoning structures IO/CoT/ToT/GoT; agent structures SayCan, ReAct, Reflexion), **memory in retrieval** (working/short-term and long-term/knowledge, vector database + embeddings), and **tools for action** (APIs, code interpreters, search, sensors, robots), embedded in MAS frameworks such as CAMEL, ChatDev, AutoGen, MetaGPT.

## Memory
- One of the deepest treatments of **memory trustworthiness** available: long-term memory is explicitly equated with RAG vector stores; attacks include **memory poisoning** (PoisonedRAG, GARAG genetic attacks, AgentPoison backdoor triggers — dangerous because injected data persists and continuously misleads until removed), **privacy leakage** (RAG-Thief, RAG-MIA membership inference, embedding inversion), and **memory misuse** (multi-turn jailbreaks exploiting short-term dialogue storage, e.g., Crescendo).
- Defenses: **detection** (TrustRAG K-means clustering, Mahalanobis-distance filtering, perplexity/LLM-based checks), **prompt modification** (templates, query rewriting), and **output intervention** (RobustRAG isolate-then-aggregate, safety filters); the authors stress there is **no systematic memory-trustworthiness evaluation** yet.

## Planning
- Not a core focus; planning appears only as a phase of tool invocation (planning, selection, execution) whose steps expose attack interfaces, and in guardrail systems that check task plans.

## Reasoning
- Not a core focus as a capability; reasoning structures (CoT, ToT, GoT, CoT-SC) are catalogued as brain mechanisms, and attacks such as second-type backdoors show malicious triggers can corrupt **intermediate reasoning without altering final outputs** — a direct argument for reasoning-trace verification.

## Tool Use
- Analyzed as a threat surface: **tool manipulation** (jailbreak-driven extraction, prompt injection causing malfunction, ToolCommander tool injection, AUTOCMD command forgery, third-party API output manipulation) and **tool abuse** (agents autonomously hacking websites, exploiting one-day vulnerabilities); defenses are "notably scarce" (GuardAgent, AgentGuard being first steps); evaluation via dataset testing (ToolSword, InjectAgent, AgentHarm) and sandbox simulation (ToolEmu, HAICosystem).

## Multi-Agent
- Extrinsic agent-to-agent section covers **cooperative attacks** (coordinated misinformation spread, Agent-in-the-Middle communication interception, adversarial persuasion) and **infectious attacks** (Prompt Infection, CORBA self-propagation, Agent Smith exponential multimodal jailbreak spread; NetSafe on how hallucinations propagate across MAS topologies), plus **collaborative defenses** (debate voting, BlockAgents Proof-of-Thought, Audit-LLM, AutoDefense, PsySafe) and **topological defenses** (GPTSwarm, G-Safeguard GNN anomaly detection).

## RAG
- RAG is treated as the concrete realization of long-term agent memory, and its trustworthiness (poisoning, membership inference, extraction, robust aggregation) is a central subject — one of the few surveys analyzing RAG through a security rather than accuracy lens.

## Healthcare Contribution
- Healthcare appears in the digital-environment section: knowledge-driven reasoning agents to safeguard sensitive medical data (GuardAgent authors) and **Polaris**, a safety-focused multi-agent LLM constellation for real-time patient interactions; the taxonomy's truthfulness dimension explicitly lists **disease misdiagnosis** as a representative risk.

## Trustworthy AI
- The paper's entire subject: it extends Trustworthy LLM research to **Trustworthy Agents** across five dimensions (safety, privacy, truthfulness, fairness, robustness, plus accountability/transparency/explainability under "others"), systematizing attack–defense–evaluation for each agent module and highlighting guardrail agents, multi-agent shields, and user trust calibration and transparency as key mechanisms.

## Evaluation
- Surveys the evaluation landscape rather than running experiments: brain benchmarks (InjecAgent, AgentDojo, Agent-SafetyBench, AgentHarm with 110 malicious tasks, R-Judge with 27 risk scenarios), memory metrics (ASR, retrieval-ASR, chunk recovery rate), tool evaluation (ToolSword, ToolEmu sandbox, HAICosystem), and agent-interaction safety (SafeAgentBench, JAILJUDGE) — concluding that memory and inter-agent trustworthiness evaluation are still **in their infancy**.

## Research Gap
- **Defense mechanisms for tool invocation are largely missing**; no vetting of third-party tools/APIs exists.
- **No systematic, reliable evaluation** for memory trustworthiness or inter-agent interaction trustworthiness.
- Static-dataset evaluation cannot capture agents' dynamic, context-dependent behavior — dynamic, real-time evaluation frameworks are needed.
- User-side trust calibration, transparency, and explainable agent decisions are underexplored, especially in multi-agent settings.

## Key Contributions
- **TrustAgent**: the first modular, technique-oriented, multi-dimensional taxonomy of agent/MAS trustworthiness spanning intrinsic (brain, memory, tool) and extrinsic (agent, environment, user) modules.
- Systematic paradigms for **attack, defense, and evaluation** per module, unifying scattered work (jailbreak/injection/backdoor; alignment/filter/shield; focused/general benchmarks).
- Identification of infectious MAS attacks and topological defenses as a distinctly agentic threat class.
- Actionable gap analysis and future directions, with a public categorized repository.

## Limitations
- Survey only — no new defense, benchmark, or empirical comparison is contributed.
- Rapidly evolving threat landscape means coverage (March 2025) will date quickly.
- Healthcare and other regulated domains are touched only briefly; no treatment of clinical audit, accountability, or human-in-the-loop oversight requirements.
- Fairness and truthfulness dimensions receive thinner technical coverage than safety/privacy.

## Important Quotes
- "once malicious data is injected into memory, it may continuously influence the agent" (Sec. 2.2.1)
- "research on defenses against tool-related attacks is notably scarce" (Sec. 2.3.2)

## Thesis Relevance
- Directly substantiates thesis gap (3): this survey confirms that **verification, oversight, and trustworthiness evaluation of agent modules are immature** — memory and inter-agent evaluation are "in their infancy" — so the thesis's audited verification gate addresses a documented field-wide deficiency.
- Its memory-poisoning analysis shows that a **persistent longitudinal patient memory is also a persistent attack/corruption surface**, motivating the thesis's verification of memory-derived claims against source records (audit-trail faithfulness).
- The **guardrail-agent paradigm** (GuardAgent, AgentGuard) and multi-agent shields (reviewer/debate agents) provide the taxonomic home and citable precedent for the thesis's verifier agent as a "single-model filter / guard agent" over clinical outputs.
- Backdoor attacks that corrupt **intermediate reasoning without changing final outputs** justify the thesis evaluating reasoning-trace/audit-trail faithfulness, not just answer accuracy.
- The healthcare entries (Polaris constellation, medical privacy guardrails) and the "disease misdiagnosis" truthfulness risk position the thesis inside the survey's own map of high-stakes digital-environment agents while showing none are evaluated on longitudinal ICU data.
- The call for **dynamic, real-time evaluation** of context-dependent agent behavior supports the thesis's episode-level evaluation over evolving MIMIC-IV patient timelines rather than static QA items.

## References
- Chen et al., AgentPoison: Red-teaming LLM agents via poisoning memory or knowledge bases, NeurIPS 2024 [15]
- Zou et al. / Zhu et al., PoisonedRAG: Knowledge corruption attacks on RAG [148]
- Xiang et al., GuardAgent: Safeguarding LLM agents via knowledge-enabled reasoning [105]
- Mukherjee et al., Polaris: A safety-focused LLM constellation architecture for healthcare [68]
- Hua et al., TrustAgent: Towards safe and trustworthy LLM-based agents, Findings of EMNLP 2024 [40]
