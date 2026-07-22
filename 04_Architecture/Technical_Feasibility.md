# Technical Feasibility Analysis

This document assesses whether the framework of Chapter 3 can be built and run as a bounded prototype, and where it will strain. The tone is deliberately skeptical: a feasibility study that only lists strengths is not a feasibility study. Each subsection names a bottleneck, explains why it bites, and states a concrete mitigation. The consolidated risk table in Section 10 summarizes likelihood, impact, and mitigation for each.

## 1. Context Window

The framework's most pervasive constraint is the context window. A single MIMIC-IV ICU stay can contain thousands of chart events and multi-page free-text notes [johnson2023mimic]. Concatenating a patient's history into one prompt is infeasible, and even where it technically fits, models attend unevenly across very long contexts, so relevant middle content is effectively lost. Because seven agents each need context, naive context assembly multiplies the problem.

*Mitigation.* The Memory-Manager (Chapter 3, Section 3.5) enforces retrieval windowing and summarization: each agent receives only the retrieved slices its query needs, bounded to a fixed token budget, while older history is compressed into structured summaries during the reflect stage. Provenance pointers let any summary be expanded back to source on demand, so compression does not lose auditability. This converts an unbounded history problem into a bounded retrieval problem.

## 2. Seven-Agent Latency

Latency is the risk most likely to undermine clinical usefulness. MedAgents reports on the order of forty seconds per examination question using a small number of collaborating agents [tang2024medagents]. A seven-agent pipeline run sequentially would plausibly reach several minutes per case, which is unacceptable for anything approaching real-time monitoring. The problem compounds because ReAct loops issue multiple LLM calls per agent [yao2023react].

*Mitigation.* Three levers, all committed in the design. First, the Coordinator short-circuits stable cases to a two-call path rather than the full DAG (Section 3.4). Second, independent branches — Diagnosis and Risk — run in parallel, so their latencies overlap rather than add. Third, non-reasoning steps (Monitoring, interaction checks) are rule-based and cheap. The residual risk is that full-DAG deteriorating cases still exceed the 30-second target; this is flagged honestly rather than assumed away, and the Chapter 4 evaluation measures it.

## 3. Scalability

Per-case work is independent, which makes the application tier embarrassingly parallel and horizontally scalable behind the gateway. The real ceiling is the model-serving tier: concurrent cases contend for inference throughput, and self-hosting introduces GPU capacity limits.

*Mitigation.* Request batching at the serving tier, a hosted endpoint for the prototype to defer GPU operations, and horizontal replication of the stateless application container. At scale, self-hosted open-weight serving trades operational cost for throughput control. Cases queue gracefully because monitoring is not hard-real-time in the prototype.

## 4. Memory Management

Beyond the context window, memory carries a correctness risk: stale or wrongly-promoted facts. If the reflect stage promotes a transient observation into long-term memory, later reasoning inherits a false premise. Conversely, over-aggressive eviction can drop a clinically relevant prior.

*Mitigation.* The Memory-Manager applies deterministic, salience-based promotion rules rather than letting agents write long-term memory freely, and every promoted fact retains a provenance pointer so it can be audited and, if wrong, traced and corrected. Keeping this policy in one module (not scattered across agent prompts) is what makes it reviewable.

## 5. Vector Database Choice

The prototype uses pgvector; a full deployment likely outgrows it. pgvector's filtered approximate search degrades under high concurrency and large indexes, and it lacks the payload-filtering ergonomics of purpose-built stores.

*Mitigation.* pgvector is justified for the prototype because co-locating embeddings with MIMIC-IV relational data in one PostgreSQL instance simplifies provenance joins and removes a second service. Qdrant is the named migration target for the scale-out regime, chosen for payload filtering and horizontal scaling. The abstraction is kept behind the Data/Retrieval Agent, so the store can be swapped without touching agent logic.

## 6. RAG Pipeline Risks

Retrieval quality bounds output quality: irrelevant or misleading passages produce confidently wrong recommendations [gao2023rag]. Clinical text is especially unforgiving because general-purpose embeddings conflate distinct medical concepts, and chunking that splits a clinical section destroys meaning. Dual grounding adds a merge step where patient and external results can crowd each other out.

*Mitigation.* Domain-tuned biomedical embeddings, section-aware chunking, and a cross-encoder rerank stage that removes weak passages before generation [zhao2025medrag; gao2023rag]. A self-reflective retrieval check in the spirit of Self-RAG lets the answering agent detect unsupportive evidence and re-query or abstain rather than generate over it [asai2024selfrag]. The merge preserves a minimum quota from each source so dual grounding cannot collapse to single-source.

## 7. MCP Integration

Exposing tools through the Model Context Protocol is promising but not free: an immature tool schema, versioning drift, or a slow tool call stalls the whole ReAct loop, and a mis-specified tool invites the model to call it incorrectly.

*Mitigation.* Tools are exposed with typed, versioned MCP schemas and per-call timeouts, so a slow or failing tool returns a structured error the agent can handle rather than hanging. The Data/Retrieval Agent centralizes tool access, which localizes MCP integration to one place and keeps other agents insulated from tool churn.

## 8. Multi-Agent Communication

A shared message envelope (System Design, Section 3) reduces integration risk, but multi-agent systems can still deadlock on circular dependencies or flood the audit log. Disagreements, if unmanaged, yield incoherent output.

*Mitigation.* The Coordinator builds a directed *acyclic* graph, structurally preventing circular waits, and the arbitration protocol (Chapter 3, Section 3.4) resolves disagreement deterministically: safety vetoes, then evidence weighting, then escalation. The single envelope makes every hop auditable and debuggable.

## 9. Workflow Engine

The design commits to LangGraph. The risk is framework lock-in and the maturity of a fast-moving library: breaking API changes or missing features could force rework.

*Mitigation.* The orchestration logic — the condition-triggered DAG and arbitration — is specified independently of LangGraph in Chapter 3, so the engine is an implementation detail rather than the design. LangGraph is chosen because the workflow genuinely needs stateful graphs with conditional edges, parallel branches, and cycles, which linear chain frameworks model awkwardly. If it proves unsuitable, the graph specification ports to another stateful orchestrator without redesigning the framework.

## 10. Consolidated Risk Table

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Context window overflow across 7 agents | High | High | Retrieval windowing + summarization via Memory-Manager; fixed per-call token budget |
| Full-DAG latency exceeds clinical tolerance | High | High | Short-circuit routing for stable cases; parallel Diagnosis/Risk; rule-based non-reasoning steps [tang2024medagents] |
| Model-serving throughput bottleneck at scale | Medium | Medium | Batching; horizontal app-tier scaling; self-hosted serving option |
| Wrong fact promoted to long-term memory | Medium | High | Deterministic salience-based promotion; provenance-preserving, auditable writes |
| pgvector degrades under scale | Medium | Medium | Justified for prototype; Qdrant migration target; store abstracted behind Data/Retrieval Agent |
| Poor retrieval quality → confident wrong output | Medium | High | Biomedical embeddings; section-aware chunking; cross-encoder rerank; Self-RAG abstention [asai2024selfrag; gao2023rag] |
| MCP tool failure stalls ReAct loop | Low | Medium | Typed versioned schemas; per-call timeouts; centralized tool access |
| Inter-agent deadlock / incoherent output | Low | High | Acyclic graph by construction; deterministic arbitration protocol |
| LangGraph lock-in / API churn | Low | Medium | Engine-independent graph spec; portable to another stateful orchestrator |
| Subgroup performance disparity undetected | Medium | High | Built-in MIMIC-IV subgroup partitioning and parity measurement (Chapter 3, Section 3.8) [johnson2023mimic] |

## 11. Verdict

The framework is feasible as a bounded prototype, with two risks — context-window pressure and full-DAG latency — rated high on both likelihood and impact. Neither is fatal: both have concrete, already-designed mitigations, and both are measurable in Chapter 4 rather than assumed. The honest position is that the framework will demonstrably run and produce grounded, auditable recommendations on MIMIC-IV cases, while meeting the aggressive 30-second full-DAG latency target remains the open empirical question the evaluation must answer.
