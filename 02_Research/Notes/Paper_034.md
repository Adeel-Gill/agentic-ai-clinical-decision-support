# Paper 034

## Basic Information
- **Title:** Survey on Evaluation of LLM-based Agents
- **Authors:** Asaf Yehudai, Lilach Eden, Alan Li, Guy Uziel, Yilun Zhao, Roy Bar-Haim, et al.
- **Year:** 2025
- **DOI:** 10.48550/arXiv.2503.16416
- **Venue:** arXiv:2503.16416 (Findings of ACL)
- **Publisher:** arXiv / Association for Computational Linguistics
- **Link:** https://arxiv.org/abs/2503.16416

## Abstract Summary (200–300 words)
This paper, from IBM Research, the Hebrew University, and Yale, presents the **first comprehensive survey of evaluation methods for LLM-based agents** — systems that plan, reason, and use tools while interacting with dynamic environments. The authors organize the field along five perspectives. First, **core agent capabilities**: planning and multi-step reasoning (PlanBench, FlowBench, Natural Plan — showing even SOTA models struggle with long-horizon planning), function calling and tool use (ToolBench, BFCL and its multi-turn successors, ComplexFuncBench, MCP-server-based frontier benchmarks), **self-reflection** (LLM-Evolve, LLF-Bench — with no standardized methodology yet), and **memory** (episodic, semantic, and procedural; StreamBench, MemBench, MemoryAgentBench — revealing weak long-range consistency and dynamic-memory handling). Second, **application-specific evaluation** for web agents (WebShop, Mind2Web, WebArena), software engineering agents (SWE-bench family, SWE-Lancer), scientific agents (ScienceAgentBench, CORE-Bench, PaperBench), and conversational agents (tau-Bench, tau2-Bench, IntellAgent). Third, **generalist agent evaluation** (GAIA/Gaia2, OSWorld, AppWorld, AgentBench, HAL). Fourth, an analysis of **core benchmark dimensions** — data curation (hybrid human/synthetic), environment (static vs. dynamic), interaction interface (code/tools/GUI), metrics (unit tests, state match, answer match), and safety — showing that almost no major benchmark incorporates safety constraints. Fifth, **developer-facing evaluation frameworks** (LangSmith, Langfuse, Vertex AI, Galileo, Patronus) supporting final-response, stepwise, and trajectory-based assessment. The survey identifies two trends — increasingly realistic evaluations and continuously updated "live" benchmarks — and five gaps: fine-grained/granular evaluation, cost-efficiency metrics, scalable automated evaluation, safety and policy compliance, and decoupling backbone-LLM from agent-harness contributions.

## Research Problem
- The shift from static LLMs to interactive agents demands a **new evaluation paradigm**: assessing sequential decision-making, environment interaction, and long-horizon task completion rather than single text outputs.
- Existing evaluations are fragmented across applications, rely on coarse **end-to-end success metrics**, saturate quickly, and largely ignore safety, robustness, and cost.
- No prior work had mapped the agent-evaluation landscape or defined its shared structural dimensions.

## Proposed Solution
- A **five-perspective taxonomy** of agent evaluation: (1) core capability benchmarks (planning, tool use, self-reflection, memory); (2) application-specific benchmarks (web, SWE, scientific, conversational); (3) generalist-agent benchmarks and leaderboards; (4) an orthogonal **benchmark-dimension analysis** (data curation, environment dynamicity, interface, metric, safety); (5) developer evaluation frameworks and gym-like environments.
- A comparative table characterizing representative benchmarks along these dimensions, plus actionable benchmark recommendations and a continuously updated GitHub repository.

## Architecture
- Not a systems paper; it adopts the standard decomposition of an agent into a **backbone LLM plus an agent harness (scaffold)** and argues evaluation must eventually attribute performance to each component separately — including specific modules such as memory or planning.

## Memory
- A dedicated capability section: memory enables reasoning across extended interactions with **episodic** (past interactions), **semantic** (factual), and **procedural** memory types; evaluated first via long-context benchmarks, now via dedicated agentic-memory benchmarks (StreamBench, MemBench, MemoryAgentBench) for multi-session continual improvement and retrieval effectiveness.
- Key finding: current methods "remain limited in maintaining long-range consistency and handling dynamic memory."

## Planning
- Planning/multi-step reasoning is a first-class evaluated capability: PlanBench adapts classical planning to expose long-term planning gaps; FlowBench tests structured workflow following; Natural Plan tests real-world natural-language planning — with the consistent result that **even SOTA models struggle with long-horizon planning**.

## Reasoning
- Multi-step reasoning is evaluated jointly with planning (HotpotQA-style multi-hop tasks used for ReAct-like agents), and reasoning quality is flagged as an intermediate process obscured by end-to-end metrics — motivating the survey's call for step-level, trajectory-based assessment.

## Tool Use
- Extensive treatment: function calling decomposed into **intent recognition, function selection, and parameter mapping**; benchmark evolution from single-step synthetic (ToolAlpaca, ToolBench, BFCL v1) to multi-turn stateful (BFCL v2/v3), nested dependent calls (NESTFUL), implicit-parameter and constraint-heavy scenarios (ComplexFuncBench), up to real **MCP-server-sourced** frontier benchmarks (MCP Atlas, ToolDecathlon) that still challenge current models.

## Multi-Agent
- Not a core focus; multi-agent collaboration appears only peripherally — as an extended capability in Gaia2, in frameworks supporting multi-agent evaluation (AutoGen, Botpress), and in the safety discussion of emergent multi-agent risks.

## RAG
- Not a core focus; retrieval appears via memory-retrieval benchmarks and a note that Databricks Mosaic AI evaluation targets RAG-like tasks, but RAG evaluation per se is not systematized.

## Healthcare Contribution
- Not a core focus; no medical benchmarks or clinical agents are reviewed — application coverage is web, software engineering, science, and customer-service conversation, underscoring the absence of standardized clinical agent evaluation.

## Trustworthy AI
- Safety is analyzed as a **benchmark dimension and a critical gap**: of the eight representative benchmarks compared, only ST-WebAgentBench-style efforts test policy compliance; robustness is quantified via pass^k; the authors call for "guardrail" metrics penalizing success achieved through non-compliant actions, safety benchmarks for adversarial robustness and policy compliance, and note most developer frameworks lack built-in safety/compliance evaluation.

## Evaluation
- The paper's entire subject: it catalogs metrics (unit tests, end-to-end success, action/state/answer matching), contrasts **reference-based vs. reference-free (LLM-as-judge)** trajectory evaluation, surveys stepwise and goal-progress metrics in developer frameworks, and documents the trend toward dynamic environments and live, continuously refreshed benchmarks (BFCL versions, SWE-bench Verified/Pro).

## Research Gap
- **Granular evaluation**: coarse end-to-end success obscures intermediate failures (tool selection, reasoning quality); standardized fine-grained trajectory metrics are missing.
- **Cost-efficiency** (tokens, API cost, latency) is almost never measured; **safety and policy compliance** are absent from mainstream benchmarks.
- **Scalability**: human-annotated static benchmarks are unsustainable; automated/synthetic evaluation and agent-as-judge methods are immature.
- **Attribution**: benchmarks conflate backbone-LLM capability with harness design, preventing systematic credit assignment to modules like memory or planning.

## Key Contributions
- First comprehensive **survey of LLM-agent evaluation**, spanning capabilities, applications, generalist benchmarks, dimensions, and tooling.
- A reusable **benchmark-dimension framework** (data, environment, interface, metric, safety) exposing structural gaps such as near-universal absence of safety constraints.
- Identification of field trends (realistic, live benchmarks) and a concrete research agenda (granularity, cost, safety, automation, LLM/harness decoupling).
- A maintained GitHub repository tracking the evolving landscape.

## Limitations
- Snapshot of a fast-moving field; very recent benchmarks may be missing (acknowledged by the authors).
- Breadth constrains depth per benchmark; selection is representative rather than exhaustive.
- Offers taxonomy and recommendations but no new benchmark, metric implementation, or empirical comparison of its own.
- Domain coverage omits high-stakes settings (healthcare, law), where evaluation requirements differ most.

## Important Quotes
- "even SOTA models struggle with long-horizon planning" (Sec. 2, Planning)
- "critical gaps... in assessing cost-efficiency, safety, and robustness" (Abstract)

## Thesis Relevance
- Provides the **methodological vocabulary** for the thesis evaluation chapter: environment dynamicity, interface, metric type, reference-based vs. LLM-as-judge — letting the MIMIC-IV evaluation be positioned rigorously against the field's standards.
- Directly documents thesis gap (1): agent evaluation is dominated by web/SWE/science/customer-service benchmarks with **no longitudinal clinical benchmark**, so evaluating agents on real ICU records is a genuine contribution.
- Its finding that memory evaluation shows weak **long-range consistency and dynamic memory handling** motivates the thesis's explicit evaluation of persistent longitudinal patient memory.
- The identified gap in **fine-grained, step-level evaluation** and missing "guardrail"/safety metrics justifies the thesis treating verification-gate performance and audit-trail faithfulness as first-class measured components rather than incidental design features.
- The call to **decouple LLM capability from harness design** supports the thesis's ablation-style analysis of framework components (RAG, memory, verification) independent of the backbone model.
- The pass^k robustness metric and LLM-as-judge trade-offs (flexibility vs. reliability) offer concrete, citable protocol choices for the thesis experiments.

## References
- Yao et al., ReAct: Synergizing reasoning and acting in language models (2022) — agent = LLM + harness framing
- Valmeekam et al., PlanBench: An extensible benchmark for evaluating planning (2023)
- Jimenez et al., SWE-bench: Can language models resolve real-world GitHub issues? (2023)
- Mialon et al., GAIA: A benchmark for general AI assistants (2023)
- Park et al., Generative Agents (2023) — memory mechanisms for extended interaction
