# Paper 029

## Basic Information
- **Title:** From Human Memory to AI Memory: A Survey on Memory Mechanisms in the Era of LLMs
- **Authors:** Yaxiong Wu, Sheng Liang, Chen Zhang, Yichao Wang, Yongyue Zhang, Huifeng Guo, et al. (Huawei Noah's Ark Lab)
- **Year:** 2025
- **DOI:** 10.48550/arXiv.2504.15965
- **Venue:** arXiv preprint (arXiv:2504.15965)
- **Publisher:** arXiv (Huawei Noah's Ark Lab)
- **Link:** https://arxiv.org/abs/2504.15965

## Abstract Summary (200–300 words)
This survey systematically reviews **memory mechanisms in LLM-driven AI systems** and grounds them in **human memory** from neuroscience. Memory is defined as the process of encoding, storing, and retrieving information so a system can retain and reuse knowledge from past interactions. The authors argue that prior reviews classify memory mainly along the **time** dimension (short-term vs. long-term), which is insufficient. They propose a classification along **three dimensions — object, form, and time — yielding eight quadrants**: object (personal vs. system memory), form (non-parametric vs. parametric memory), and time (short-term vs. long-term memory). They first analyze human memory (sensory, working, explicit/episodic and semantic, implicit/procedural) and its processes (encoding, storage, retrieval, plus consolidation, reconsolidation, reflection, forgetting), then draw explicit parallels to AI memory: sensory inputs, KV-cache as parametric short-term memory, non-parametric long-term memory (external stores, RAG) as analogous to episodic memory, parametric long-term memory (model weights) as semantic memory, and reflection/refinement of traces as procedural/implicit memory. The survey organizes existing work into **personal memory** (contextual multi-turn dialogue, long-term cross-session memory with construction/management/retrieval/caching, parametric knowledge editing) and **system memory** (contextual and parametric intermediate reasoning/planning traces such as CoT and ReAct). It catalogs many systems (MemoryBank, MemGPT, mem0, MemoryScope, HippoRAG, A-MEM, Generative Agents) and benchmarks (LOCOMO, LongMemEval-style, BABILong). Finally, it identifies open problems and future directions: unimodal→multimodal memory, static→stream memory, specific→comprehensive memory, exclusive→shared memory, individual→collective privacy, and rule-based→automated self-evolution.

## Research Problem
- No systematic review had connected **human memory** with **LLM-driven AI-system memory**, nor organized memory beyond the single time dimension.
- Existing work under-explores the **object** (personal vs. system) and **form** (parametric vs. non-parametric) dimensions and how human-memory insights can inform better AI memory architectures.

## Proposed Solution
- A **three-dimensional (object, form, time), eight-quadrant taxonomy** of AI memory, tightly mapped onto human-memory categories, used to organize and analyze existing personal-memory and system-memory research and to derive open problems.

## Architecture
- Not a single system; the survey's organizing "architecture" is the taxonomy: personal memory (Quadrants I–IV) and system memory, each split into contextual (non-parametric) and parametric, and short-term vs. long-term. Reference systems include MemGPT, MemoryBank, mem0, MemoryScope, HippoRAG, Generative Agents.

## Memory
- The entire paper. Key AI-memory constructs: **short-term/working memory** (current-session multi-turn context, KV-cache), **long-term memory** (external cross-session stores retrieved on demand), **parametric memory** (knowledge in weights; edited via knowledge editing), **non-parametric memory** (external documents/databases accessed via RAG). Human-inspired operations: encoding, storage, retrieval, consolidation, reconsolidation, reflection, forgetting.

## Planning
- Treated as a consumer/producer of memory: **system memory** stores intermediate planning/reasoning traces (CoT, ReAct) that strengthen an agent's ability to decompose and execute complex tasks; planning itself is not the survey's subject.

## Reasoning
- Reasoning is enhanced by memory: chain-of-thought and ReAct traces are stored as system memory; reflection over accumulated traces (implicit/procedural memory analogue) lets agents learn from successes and failures.

## Tool Use
- Mentioned as an agent capability alongside memory and planning; intermediate tool/search results are stored as system memory. Not a focus of the survey.

## Multi-Agent
- Touched on via "From Exclusive Memory to Shared Memory": future **shared/collaborative memory** across models/domains (e.g., a medical model sharing knowledge with a finance model) and multi-agent systems (ChatDev, MetaAgents, Generative Agents) that use memory.

## RAG
- Central to the **form** dimension: non-parametric memory is dynamically accessed via **retrieval-augmented generation**; the survey catalogs retrieval/management approaches (RET-LLM, HippoRAG/HippoRAG 2, MemoRAG, EMG-RAG, SECOM) and caching for acceleration (Prompt Cache, Contextual Retrieval).

## Healthcare Contribution
- Not a healthcare paper, but explicitly uses medicine as a motivating example for **multimodal memory**: combining text (records), images (imaging), and speech (doctor-patient conversations) to better understand and diagnose conditions.

## Trustworthy AI
- Addresses **privacy** as a future challenge (individual → collective privacy, balancing data utility vs. preservation) and, via reflection/forgetting, the controlled updating and discarding of memory. No dedicated verification/audit framework.

## Evaluation
- Survey (no new experiments). Catalogs memory **benchmarks**: MADial-Bench, LOCOMO, MemDaily, MSC, MMRC, Ego4D, EgoLife, BABILong — for evaluating long-term/personal memory and long-context recall.

## Research Gap
- Memory architectures are narrow/task-specific; the field lacks **comprehensive, collaborative memory systems** integrating multiple memory types with continual updating.
- Gaps: unimodal vs. multimodal memory, static (batch) vs. stream (real-time) memory, exclusive vs. shared memory, and rule-based vs. automated self-evolution.

## Key Contributions
- Systematic definition of LLM-driven AI-system memory and its correspondence to human memory.
- The object/form/time three-dimensional, eight-quadrant classification.
- Structured review of personal-memory and system-memory research.
- Identification of open problems and six future directions.

## Limitations
- A survey: no empirical validation or new benchmark; taxonomy boundaries (e.g., object vs. form) can overlap.
- Coverage is broad rather than deep per method; excludes modality/dynamics as primary axes; no domain-specific (e.g., clinical) memory design guidance beyond illustrative examples.

## Important Quotes
- "memory... the process of acquiring, storing, retaining, and subsequently retrieving information" (Section 1)
- "non-parametric long-term memory... analogous to episodic memory in humans" (Section 2.2.2)

## Thesis Relevance
- Provides the **theoretical scaffolding for the thesis's persistent longitudinal patient memory**: the object/form/time taxonomy maps directly onto storing a patient's timeline (non-parametric long-term/episodic) vs. medical knowledge in weights (parametric/semantic) — addressing thesis gap (2).
- Distinguishes **short-term (session)** from **long-term (cross-encounter)** memory, exactly the split needed to track an ICU patient across shifts/admissions.
- Memory operations (encoding, retrieval, consolidation, reflection, forgetting) offer concrete design primitives for a clinical memory module and for pruning stale/irrelevant records.
- RAG-as-non-parametric-memory framing supports grounding retrieval in the **patient's own record** rather than only external guidelines.
- "System memory" (CoT/ReAct traces) motivates persisting the agent's reasoning trace for the thesis's **audit trail** (gap 3).
- Future directions (multimodal, stream, shared memory) align with real-time ICU vital-sign streams and multi-agent coordination.

## References
- Zhong, W., et al. "MemoryBank: Enhancing Large Language Models with Long-Term Memory." (long-term memory mechanism).
- Packer, C., et al. "MemGPT: Towards LLMs as Operating Systems." (memory management/paging).
- Park, J. S., et al. "Generative Agents: Interactive Simulacra of Human Behavior." (episodic memory + reflection).
- Lewis, P., et al. "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks." (non-parametric memory).
- Yao, S., et al. "ReAct: Synergizing Reasoning and Acting in Language Models." (system-memory reasoning traces).
