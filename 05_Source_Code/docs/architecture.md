# ACDSS Architecture

How the source modules realize the thesis architecture. See the top-level
[`README.md`](../README.md) for setup and the six-layer overview.

> ⚠️ Research prototype, not a medical device. Decision support only.

---

## Module diagram

```mermaid
flowchart TB
    subgraph L6["Layer 6 · API / UI  (acdss.api)"]
        API["FastAPI app<br/>POST /assess/{id}<br/>GET /health<br/>HITL approve/modify/reject"]
    end

    subgraph L4["Layer 4 · Orchestration  (acdss.orchestration)"]
        GRAPH["LangGraph StateGraph<br/>router → agents →<br/>conflict-resolution → verification gate"]
    end

    subgraph AG["Agents  (acdss.agents)"]
        COORD["Coordinator"]
        PLAN["Planner"]
        DR["DataRetrieval"]
        MON["Monitoring"]
        DX["Diagnosis"]
        RISK["RiskPrediction"]
        TX["Treatment"]
        EXP["Explanation"]
        VER["Verification"]
    end

    subgraph L5["Layer 5 · Decision  (acdss.decision)"]
        ENG["DecisionEngine<br/>Dx / Risk / Tx / Explanation / Confidence"]
    end

    subgraph L3["Layer 3 · Reasoning / RAG  (acdss.rag)"]
        RAG["ingest → retriever → reranker → pipeline"]
    end

    subgraph L2["Layer 2 · Memory  (acdss.memory)"]
        MM["MemoryManager"]
        STM["ShortTerm"]
        LTM["LongTerm"]
        VS["VectorStore (pgvector)"]
        CTX["ClinicalContext"]
    end

    subgraph L1["Layer 1 · Data  (acdss.data)"]
        MIMIC["MimicLoader<br/>MIMIC-IV / Postgres"]
    end

    subgraph X["Cross-cutting"]
        LLM["LLM abstraction<br/>(acdss.llm · Claude default)"]
        MCP["MCP server<br/>query_ehr · search_guidelines · drug_interactions"]
        TRUST["Trust<br/>audit · safety · bias · calibration"]
    end

    API --> GRAPH
    GRAPH --> COORD --> PLAN
    GRAPH --> DR & MON & DX & RISK & TX & EXP & VER
    GRAPH -->|verified| ENG --> API

    DR --> MCP
    DX --> RAG
    TX --> MCP
    RAG --> VS
    MM --> STM & LTM & VS
    MM --> CTX
    CTX --> AG
    DR --> MIMIC
    MCP --> MIMIC
    AG --> LLM
    VER --> TRUST
    ENG --> TRUST
    API --> TRUST
```

---

## Request flow (`POST /assess/{patient_id}`)

```mermaid
sequenceDiagram
    participant C as Clinician (UI)
    participant API as FastAPI
    participant M as MemoryManager
    participant G as LangGraph
    participant A as Agents
    participant V as Verification gate
    participant D as DecisionEngine

    C->>API: POST /assess/{patient_id}
    API->>M: build ClinicalContext (MIMIC-IV + memory + RAG)
    API->>G: invoke(state)
    G->>A: coordinator routes → specialists
    A-->>G: typed AgentOutputs
    G->>G: conflict-resolution
    G->>V: verification gate
    alt gate passes
        V-->>D: verified outputs
        D-->>API: Decision (+ confidence, citations)
        API-->>C: recommendation + disclaimer (awaits HITL)
    else gate blocks / low confidence
        V-->>API: abstain / requires human review
        API-->>C: flagged for clinician review
    end
    C->>API: POST /hitl/{id}/approve|modify|reject
    API->>M: persist feedback (long-term memory + audit)
```

---

## Layer → package map

| Layer | Package | Key symbols |
| ----- | ------- | ----------- |
| 1 Data | `acdss.data` | `MimicLoader`, `PatientRecord`, `VitalSign` |
| 2 Memory | `acdss.memory` | `MemoryManager`, `ShortTermMemory`, `LongTermMemory`, `VectorStore`, `ClinicalContext` |
| 3 Reasoning/RAG | `acdss.rag` | `Ingestor`, `Retriever`, `Reranker`, `RagPipeline` |
| 4 Orchestration | `acdss.orchestration` | `build_graph`, `AssessmentState`, `conflict_resolution_node`, `verification_node` |
| 5 Decision | `acdss.decision` | `DecisionEngine`, `Decision` |
| 6 API/UI | `acdss.api` | `app`, `/assess`, `/health`, HITL routes |
| — Agents | `acdss.agents` | `Agent` ABC + 9 agents |
| — LLM | `acdss.llm` | `LLMClient`, `AnthropicClient` |
| — Tools | `acdss.mcp` | `query_ehr`, `search_guidelines`, `drug_interactions` |
| — Trust | `acdss.trust` | `AuditLog`, `SafetyGuard`, `BiasMonitor`, `Calibrator` |

---

## Design notes

- **LLM is swappable.** All agents depend on the `LLMClient` interface, not the
  concrete Anthropic client, so the provider/model can change via config.
- **Typed agent contracts.** `Agent[I, O]` is generic over Pydantic
  `AgentInput`/`AgentOutput` subclasses, giving each agent a validated I/O shape.
- **Verification gate before decision.** The graph cannot reach the
  `DecisionEngine` unless the verification node sets `verified=True`; the engine
  additionally abstains below `MIN_CONFIDENCE`.
- **Human-in-the-loop by default.** `REQUIRE_HITL` forces every recommendation
  through clinician approve/modify/reject before it is considered final.
- **Trust is cross-cutting.** Audit logging, safety rules, bias monitoring, and
  calibration wrap the pipeline rather than living in any single layer.
