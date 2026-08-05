# Paper 031

## Basic Information
- **Title:** Agentic Retrieval-Augmented Generation: A Survey on Agentic RAG
- **Authors:** Aditi Singh, Abul Ehtesham, Saket Kumar, Tala Talaei Khoei, Athanasios V. Vasilakos
- **Year:** 2025
- **DOI:** 10.48550/arXiv.2501.09136
- **Venue:** arXiv preprint (arXiv:2501.09136)
- **Publisher:** arXiv (Cleveland State University / Kent State / Northeastern / University of Agder)
- **Link:** https://arxiv.org/abs/2501.09136

## Abstract Summary (200–300 words)
This survey structures the emerging field of **Agentic Retrieval-Augmented Generation (Agentic RAG)** — systems that embed autonomous LLM agents directly into the RAG pipeline so that retrieval, query reformulation, evidence validation, and response refinement become agentic decisions rather than static workflow steps. The paper first traces the **evolution of RAG paradigms** — Naïve RAG (keyword retrieval, TF-IDF/BM25), Advanced RAG (dense retrieval, re-ranking, multi-hop), Modular RAG (hybrid retrieval, tool integration, composable pipelines), Graph RAG (graph-structured multi-hop reasoning), and finally Agentic RAG — and analyzes the limitations of traditional RAG in contextual integration, multi-step reasoning, and scalability/latency. It then reviews the four **agentic design patterns** (reflection, planning, tool use, multi-agent collaboration) and five **agentic workflow patterns** (prompt chaining, routing, parallelization, orchestrator–workers, evaluator–optimizer). Its central contribution is a **principled taxonomy of Agentic RAG architectures** based on agent cardinality, control structure, autonomy, and knowledge representation, spanning single-agent routers, multi-agent RAG, hierarchical/corrective/adaptive RAG, graph-based frameworks (Agent-G, GeAR), and Agentic Document Workflows. The survey examines applications in **healthcare**, finance, education, and enterprise document processing, distills practitioner lessons (retrieval quality is the primary bottleneck; agent autonomy requires explicit constraints; evaluation must be process-aware; domain knowledge amplifies agentic gains; auditability must be a first-class design goal), catalogs benchmarks (BEIR, MS MARCO, HotpotQA, MuSiQue, RAGBench, BERGEN, FlashRAG), and identifies open challenges in agent coordination, process-level evaluation, long-term memory management, computational cost, safety/governance, and cross-domain generalization.

## Research Problem
- Traditional RAG pipelines are **static and linear**, limiting multi-step reasoning, iterative refinement, and adaptation to dynamic real-world queries.
- The Agentic RAG field is **fragmented**: diverse architectures, inconsistent terminology, and no unified taxonomy organizing systems along principled design dimensions.
- Output-level metrics (answer correctness, retrieval accuracy) are insufficient because intermediate agentic decisions shape performance.

## Proposed Solution
- An **analytical survey with a principled taxonomy** of Agentic RAG along four dimensions: **agent cardinality, control structure, autonomy, and knowledge representation**, plus a comparative analysis of design trade-offs (Table 3 compares single-agent, multi-agent, hierarchical/corrective, and graph-based/document-centric RAG).
- Positions Agentic RAG as an **explicit control layer** that coordinates retrieval, validates information, invokes tools, and refines responses over external evidence.

## Architecture
- **Single-Agent Router:** one coordinating agent evaluates the query and selects among knowledge sources (structured databases via Text-to-SQL, semantic search, web search).
- **Multi-Agent RAG:** specialized retrieval agents operate in parallel over distinct sources with flat control.
- **Hierarchical / Corrective / Adaptive RAG:** tiered evaluator-based control that grades retrieved evidence and triggers corrective retrieval or adapts strategy to query complexity.
- **Graph-based RAG (Agent-G, GeAR):** combines graph knowledge bases (e.g., disease-to-symptom mappings) with document retrievers and a critic module that evaluates retrieved data quality.
- **Agentic Document Workflows (ADW):** end-to-end document-centric orchestration maintaining state across parsing, retrieval, reasoning, and structured output generation.

## Memory
- Agents integrate **short-term memory** (immediate conversation state) and **long-term memory** (accumulated knowledge and experiences) as core components; Section 12.3 flags long-term memory design as an open challenge — persistent memory risks **knowledge drift and bias reinforcement**, and key questions include selective retention and reconciling external knowledge with stored agent experience.

## Planning
- **Planning** is one of the four foundational agentic patterns: agents autonomously decompose complex tasks into subtasks for multi-hop reasoning; the survey notes planning yields less predictable outcomes than deterministic workflows and recommends **bounded planning horizons and explicit stopping criteria**.

## Reasoning
- Iterative, reflection-driven reasoning: **evaluator–optimizer loops** and self-critique (Self-Refine, Reflexion, CRITIC) refine retrieval and generation; corrective RAG grades evidence sufficiency before generation; graph-based variants add relational/symbolic reasoning on top of LLM reasoning.

## Tool Use
- **Tool use** is a core agentic pattern: vector search, web search, APIs, Text-to-SQL engines, and computational tools; the survey highlights tool-selection optimization as a challenge and recommends predefined tool-access policies for constrained autonomy.

## Multi-Agent
- **Multi-agent collaboration** enables task specialization and parallel retrieval across heterogeneous sources; hierarchical variants add supervisory control; the survey warns of coordination complexity, emergent behavior, and difficult error attribution in multi-agent settings.

## RAG
- The paper's core subject: a complete treatment of RAG paradigm evolution, agentic integration, taxonomy, comparative framework analysis, tooling (LangGraph, LlamaIndex, CrewAI, AutoGen, Semantic Kernel), and benchmarks/datasets for RAG evaluation.

## Healthcare Contribution
- Healthcare is presented as a flagship application domain: a **healthcare diagnostics use case** (Agent-G combining a medical knowledge graph with document retrieval for a diabetes–heart-disease query) and a **patient case summary workflow** (LlamaCloud ADW example).
- Section 10.6 finds Agentic RAG achieves its **strongest gains in domains with structured knowledge and explicit constraints**, naming healthcare explicitly.

## Trustworthy AI
- Section 10.7 argues responsible deployment requires governance mechanisms, **human oversight**, clear operational boundaries, and that explainability, traceability, and **auditability** be first-class design goals for high-stakes applications; Section 12.5 calls for transparent decision-tracing and human-in-the-loop oversight.

## Evaluation
- Surveys benchmarks: **BEIR, MS MARCO, TREC-DL, MuSiQue, 2WikiMultihopQA, HotpotQA, Agent-G, RAGBench (TRACe framework), BERGEN, FlashRAG, GNN-RAG**, plus a task/dataset table adapted from Gao et al.
- Argues existing benchmarks focus on output quality with limited visibility into intermediate decisions; calls for **process-level metrics** capturing reasoning efficiency, tool-usage patterns, and adaptation.

## Research Gap
- No standardized process-aware evaluation of reasoning trajectories, robustness under noisy retrieval, or cost efficiency.
- Long-term memory management (persistence vs. adaptability) unresolved.
- Multi-agent coordination under partial observability lacks convergence guarantees; safety, trust, and governance for autonomous RAG remain open.
- Generalization beyond domain-specific curated benchmarks is unproven.

## Key Contributions
- First principled **taxonomy of Agentic RAG** (cardinality, control, autonomy, knowledge representation) with comparative design trade-off analysis.
- Unified treatment of RAG paradigm evolution and agentic/workflow patterns.
- Application survey (healthcare, finance, education, enterprise documents) with practitioner lessons learned.
- Consolidated benchmark/dataset catalog and an open-challenges research agenda.

## Limitations
- Survey-level treatment: no new system, no empirical experiments, and no quantitative comparison of the surveyed frameworks.
- Healthcare examples are illustrative use cases (single-query diagnostics, document workflows), not validated clinical systems or longitudinal patient-record applications.
- Acknowledges Agentic RAG itself is at an early maturity stage; several taxonomy cells rest on preprints and vendor tutorials.

## Important Quotes
- "Agentic reasoning cannot compensate for consistently poor retrieval." (Section 10.3)
- "Explainability, traceability, and auditability must be first-class design goals" (Section 10.7)

## Thesis Relevance
- Provides the **architectural vocabulary and taxonomy** for positioning the thesis's retrieval layer: the framework's patient-timeline RAG maps to a hierarchical/corrective Agentic RAG with an explicit verification gate.
- Directly supports thesis gap (2): the survey's medical RAG examples ground retrieval in **knowledge graphs and literature**, not the patient's own longitudinal record — confirming the novelty of patient-timeline-grounded RAG over MIMIC-IV.
- Its call for **process-aware evaluation** and auditability as first-class design goals validates thesis gap (3): evaluating verification and audit-trail faithfulness as first-class components.
- Lessons on **constrained autonomy** (bounded planning, tool-access policies, stopping criteria) inform the thesis's layered control and human-in-the-loop design.
- The open challenge on **long-term memory drift** motivates the thesis's design choices for persistent longitudinal patient memory.
- Benchmark catalog shows current RAG evaluation is QA-dataset-centric, reinforcing thesis gap (1) on real ICU-record evaluation.

## References
- Gao, Y., Xiong, Y., Gao, X., et al. "Retrieval-augmented generation for large language models: A survey." (2024). [RAG paradigm evolution basis]
- Lee, M.-C., Zhu, Q., Mavromatis, C., et al. "Agent-G: An agentic framework for graph retrieval augmented generation." (2024).
- Yan, S.-Q., Gu, J.-C., Zhu, Y., Ling, Z.-H. "Corrective retrieval augmented generation." (2024).
- Shinn, N., Cassano, F., Berman, E., et al. "Reflexion: Language agents with verbal reinforcement learning." (2023).
- Zhang, Z., Bo, X., Ma, C., et al. "A survey on the memory mechanism of large language model based agents." (2024).
