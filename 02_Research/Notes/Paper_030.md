# Paper 030

## Basic Information
- **Title:** A Survey of Agent Interoperability Protocols: Model Context Protocol (MCP), Agent Communication Protocol (ACP), Agent-to-Agent Protocol (A2A), and Agent Network Protocol (ANP)
- **Authors:** Abul Ehtesham, Aditi Singh, Gaurav Kumar Gupta, Saket Kumar
- **Year:** 2025
- **DOI:** 10.48550/arXiv.2505.02279
- **Venue:** arXiv preprint (arXiv:2505.02279)
- **Publisher:** arXiv (Kent State, Cleveland State, Youngstown State, Northeastern)
- **Link:** https://arxiv.org/abs/2505.02279

## Abstract Summary (200–300 words)
This survey examines four emerging **agent interoperability protocols** that standardize how LLM-powered autonomous agents integrate tools, share context, and coordinate tasks across heterogeneous systems, arguing that ad-hoc integrations do not scale, secure, or generalize. **Model Context Protocol (MCP)** (Anthropic, Nov 2024) provides a JSON-RPC client-server interface for secure tool invocation and typed context ingestion, exposing four core primitives — Tools, Resources, Prompts, and Sampling. **Agent Communication Protocol (ACP)** (IBM, Mar 2025) is a general-purpose RESTful-HTTP protocol supporting MIME-typed multipart messages, synchronous and asynchronous interactions, structured session management, message routing, and role-based/decentralized-identity authentication, with runtime, offline, and manifest-based discovery. **Agent-to-Agent Protocol (A2A)** (Google, Apr 2025) enables peer-to-peer task delegation via capability-based **Agent Cards** using HTTP and Server-Sent Events, aimed at enterprise agent collaboration within trust boundaries. **Agent Network Protocol (ANP)** targets open-internet, decentralized agent discovery and collaboration using W3C **decentralized identifiers (DIDs)** and JSON-LD graphs in a peer-to-peer model. The paper traces the historical evolution of agent communication (KQML, FIPA-ACL, SOA/ESB, RAG, function calling, Toolformer, ReAct) across three phases, then compares the four protocols along architecture, discovery, messaging format, session support, security, and use case (Table 7). It analyzes lifecycle security challenges and mitigations per protocol. Finally it proposes a **phased adoption roadmap**: MCP for tool access, then ACP for structured multimodal messaging, then A2A for enterprise collaboration, then ANP for decentralized agent marketplaces — concluding that no single protocol suffices and complementary adoption is the practical path.

## Research Problem
- LLM agents suffer from **fragmented, ad-hoc interoperability**: no unified way to discover capabilities, exchange context, authenticate peers, and coordinate actions across different frameworks and vendors.
- Function-calling ecosystems use static tool definitions, framework-specific security, and inconsistent metadata, preventing dynamic discovery and cross-framework reuse.

## Proposed Solution
- A comparative survey of MCP, ACP, A2A, and ANP, each addressing a distinct interoperability tier, plus a **phased, complementary adoption roadmap** and per-protocol lifecycle security analysis.

## Architecture
- **MCP**: Host (client) ↔ MCP Server over JSON-RPC 2.0; transport via Stdio or HTTP+SSE; message types Requests/Results/Errors/Notifications; capabilities Tools (model-controlled), Resources (app-controlled), Prompts (user-controlled), Sampling (server-controlled).
- **ACP**: brokered client-server (registry + task routing), REST/HTTP, MIME-typed multipart messages, session/run-state tracking, RBAC/DID auth.
- **A2A**: peer-like client/remote-agent, Agent Cards for capability discovery, Task + Artifact messaging over JSON, HTTP+SSE + push notifications.
- **ANP**: decentralized P2P, DID (did:wba) identity, JSON-LD with Schema.org and meta-protocol negotiation.

## Memory
- Not a core focus; notes that some frameworks (e.g., Semantic Kernel) unify **memory stores** with planning/plugins, and ACP supports stateful, long-running services vs. stateless utilities. No memory taxonomy.

## Planning
- Not a focus; mentions LLM agents plan multi-step workflows and that frameworks provide planning modules, but the survey is about the communication substrate beneath planning, not planning itself.

## Reasoning
- Contextualizes ReAct (interleaving chain-of-thought reasoning with action calls) and Reflexion as single-agent reasoning/action techniques that the protocols are meant to complement at the coordination layer.

## Tool Use
- Central. MCP is framed as "USB-C for AI" for standardized tool/context access; discusses OpenAI function calling, LangChain, LlamaIndex, plugin stores, and their limitations (static tool registries, ad-hoc security) that protocol standards resolve.

## Multi-Agent
- Yes — the survey's core concern is **multi-agent interoperability**: peer discovery, capability negotiation, task delegation, and cross-vendor collaboration (A2A, ANP), plus lightweight orchestration frameworks (CrewAI, AutoGen/AG2, Swarm, Semantic Kernel, SmolAgents).

## RAG
- Discussed historically: RAG (2020) coupled dense vector retrieval with LLM decoding to ground outputs and reduce hallucinations, but treats retrieval/generation as separate batch processes and does not prescribe how to translate grounded content into actions — motivating protocol-level standards.

## Healthcare Contribution
- Not a healthcare paper; no clinical application or evaluation. Contribution is domain-agnostic infrastructure that a clinical multi-agent system could adopt.

## Trustworthy AI
- Substantial **security focus**: per-protocol lifecycle security-challenge/mitigation tables; MCP prompt-injection and centralized-server risks; DID-based trustless identity, mutual TLS, JWS, bearer tokens; access control and authentication as first-class concerns.

## Evaluation
- No empirical benchmark; the "evaluation" is a **qualitative comparative analysis** (Table 7) across architecture, discovery, message format, session support, security, strengths, and limitations, plus a timeline (Table 2) and a phased roadmap.

## Research Gap
- No single protocol covers all deployment contexts; interoperability **bridges between protocols**, shared **trust frameworks** for agent collaboration, and **standardized evaluation benchmarks** are missing and flagged as future work.

## Key Contributions
- Structured comparison of MCP, ACP, A2A, ANP across multiple dimensions (Table 7).
- Historical timeline of agent communication standards (KQML → FIPA-ACL → SOA → RAG → function calling → MCP/ACP/A2A/ANP).
- Per-protocol lifecycle security-challenge and mitigation analysis.
- A four-stage phased adoption roadmap.

## Limitations
- Descriptive survey with no implementation, quantitative evaluation, or benchmark; protocols are young and evolving, so comparisons may date quickly.
- Coverage is architecture/spec-level; lacks real deployment case studies (including healthcare).

## Important Quotes
- "MCP addresses this by standardizing how applications deliver tools, datasets, and sampling instructions to LLMs, akin to a USB-C for AI" (Section 2)
- "no single protocol suffices across all contexts" (Section 10, Conclusion)

## Thesis Relevance
- Directly informs the thesis's **multi-agent orchestration and integration layer**: MCP for secure tool invocation (e.g., clinical calculators, EHR/FHIR access) and A2A/ACP for coordinating specialist agents (monitoring, retrieval, verification).
- MCP's typed Tools/Resources/Prompts model provides a concrete, auditable interface for the thesis's **verification gate and audit trail** — every tool call is structured and loggable (gap 3).
- Lifecycle security analyses (prompt injection, DID-based identity, RBAC) are essential for a safety-critical ICU deployment handling PHI.
- The phased roadmap (start with MCP) offers a pragmatic build order for the thesis prototype.
- Distinguishes protocol-level standardization from single-agent reasoning (ReAct) and RAG, clarifying where the thesis's components sit in the stack.
- Highlights the absence of standardized multi-agent evaluation benchmarks — reinforcing the thesis's contribution of rigorous evaluation on real ICU data.

## References
- Anthropic. "Model Context Protocol (MCP)." (2024) — JSON-RPC context/tool standard.
- Google. "Agent-to-Agent (A2A) Protocol." (2025) — Agent Cards, peer task delegation.
- IBM. "Agent Communication Protocol (ACP)." (2025) — RESTful multipart messaging.
- Lewis, P., et al. "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks." (2020).
- Yao, S., et al. "ReAct: Synergizing Reasoning and Acting in Language Models." (2023).
