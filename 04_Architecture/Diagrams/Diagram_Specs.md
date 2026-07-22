# Diagram Specifications

Renderable Mermaid source for the figures referenced in Chapter 3 and the system-design documents. Each block is self-contained; a one-line caption follows each.

## 1. System Architecture (Figure 3.1)

```mermaid
flowchart TB
    subgraph L6[Clinician Dashboard]
        D1[Patient summary, alerts, risks, recommendations, explanation, confidence]
    end
    subgraph L5[Clinical Decision Layer]
        C1[Clinical Decision Engine: fuse + arbitrate + disposition flag]
    end
    subgraph L4[Agent Orchestration Layer]
        O1[Coordinator: condition-triggered DAG]
        O2[Monitoring / Planner / Data-Retrieval]
        O3[Diagnosis / Risk / Treatment]
        O4[Explanation / Verification]
    end
    subgraph L3[Reasoning and Knowledge Layer]
        K1[ReAct engine]
        K2[RAG pipeline]
        K3[Guidelines + knowledge base]
    end
    subgraph L2[Memory Layer]
        M1[Memory-Manager]
        M2[Short-term / Long-term / Vector / Episodic]
    end
    subgraph L1[Data Layer]
        DT1[Timeline service over MIMIC-IV]
    end
    T[Trustworthy AI Layer: explainability, audit, bias, calibration]

    L1 --> L2 --> L3 --> L4 --> L5 --> L6
    T -.cross-cutting.- L1
    T -.cross-cutting.- L2
    T -.cross-cutting.- L3
    T -.cross-cutting.- L4
    T -.cross-cutting.- L5
    T -.cross-cutting.- L6
```
*Figure 3.1: The six horizontal layers with the cross-cutting Trustworthy AI layer, grounded in MIMIC-IV.*

## 2. Agent Collaboration Sequence (one patient case)

```mermaid
sequenceDiagram
    participant Mon as Monitoring
    participant Coord as Coordinator
    participant Plan as Planner
    participant DRA as Data/Retrieval
    participant Dx as Diagnosis
    participant Risk as Risk
    participant Tx as Treatment
    participant Exp as Explanation
    participant Ver as Verification
    participant HITL as Clinician

    Mon->>Coord: high-severity alert (fever, tachy, lactate)
    Coord->>Plan: decompose task
    Plan-->>Coord: plan (Dx, Risk, Tx)
    Coord->>DRA: dual-grounded retrieval
    DRA-->>Coord: patient slices + guideline passages
    par parallel branches
        Coord->>Dx: diagnose
        Coord->>Risk: predict risk
    end
    Dx-->>Coord: sepsis (source unconfirmed)
    Risk-->>Coord: high deterioration risk
    Coord->>Tx: recommend (uses Dx + Risk)
    Tx-->>Coord: sepsis bundle, renal-adjusted
    Coord->>Exp: assemble faithful explanation
    Exp-->>Coord: cited narrative
    Coord->>Ver: verify
    Ver-->>Coord: review (source unconfirmed)
    Coord->>HITL: escalate for confirmation
    HITL-->>Coord: approve / modify / reject
```
*Agent collaboration for a deteriorating ICU case: parallel Diagnosis and Risk, treatment fusion, faithful explanation, and Verification-driven escalation to the clinician.*

## 3. RAG Pipeline

```mermaid
flowchart LR
    subgraph Sources
        P[Patient EHR timeline\nMIMIC-IV]
        E[External guidelines + literature]
    end
    P --> ING[Ingest]
    E --> ING
    ING --> CH[Chunk: section-aware]
    CH --> EM[Embed: biomedical bi-encoder]
    EM --> VDB[(Vector store\npgvector / Qdrant)]
    Q[Agent query + patient context] --> RET[Retrieve: ANN over both sources]
    VDB --> RET
    RET --> MRG[Merge patient + external\nwith per-source quota]
    MRG --> RR[Rerank: cross-encoder]
    RR --> SRAG{Evidence supports claim?}
    SRAG -- no --> RET
    SRAG -- yes --> GEN[Generate grounded output]
```
*RAG pipeline with dual grounding over patient record and external evidence, a rerank stage, and a Self-RAG-style support check that re-queries or abstains on weak evidence.*

## 4. Memory Architecture

```mermaid
flowchart TB
    IN[Timeline events + agent outputs + clinician feedback] --> MM[Memory-Manager]
    MM -->|read: assemble bounded context| CTX[Context bundle to agent]
    MM -->|write: append with provenance| EPI[(Episodic clinical-context)]
    MM -->|write: promote durable facts| LTM[(Long-term patient)]
    MM -->|hold session working set| STM[(Short-term working)]
    MM -->|embed notes + literature| VEC[(Semantic vector)]
    MM -->|reflect: summarize + evict\npreserve provenance| STM
    LTM --> MM
    VEC --> MM
    EPI --> MM
```
*Four memory stores governed by a Memory-Manager applying read, write, and reflect policies under a fixed token budget.*

## 5. Patient Journey Timeline (MIMIC-IV tables)

```mermaid
flowchart LR
    A[patients\ndemographics] --> B[admissions]
    B --> C[icustays]
    C --> D[chartevents\nvital signs]
    C --> E[labevents\nlab results]
    C --> F[prescriptions\nmedications]
    C --> G[procedures]
    B --> H[diagnoses_icd]
    C --> I[noteevents\nclinical notes]
    D --> TL[Normalized patient timeline\nrelative time from admission]
    E --> TL
    F --> TL
    G --> TL
    H --> TL
    I --> TL
```
*Patient journey assembled from core MIMIC-IV tables into a single relative-time timeline consumed by the Data Layer.*

## 6. HITL / Verification Flowchart

```mermaid
flowchart TB
    REC[Fused recommendation] --> VER{Verification checks}
    VER -->|hard violation| FAIL[Disposition: fail]
    VER -->|borderline / conflict| REVIEW[Disposition: review]
    VER -->|clean pass| PASS[Disposition: pass]
    FAIL --> HITL[Clinician review]
    REVIEW --> HITL
    PASS --> DASH[Dashboard: actionable + evidence + confidence]
    DASH --> HITL
    HITL --> A{Clinician action}
    A -->|approve| FB[Record concurrence]
    A -->|modify| FBM[Record original + edit]
    A -->|reject| FBR[Record decline + reason]
    A -->|more info| RETRIG[Re-trigger Coordinator]
    FB --> MEM[(Episodic memory + calibration/bias datasets)]
    FBM --> MEM
    FBR --> MEM
```
*Verification sets a disposition that gates presentation; every clinician action is captured as provenance-tagged feedback feeding memory and the trustworthy-AI datasets.*

## 7. Deployment Diagram

```mermaid
flowchart LR
    BR[Clinician browser] -->|HTTPS| API[FastAPI gateway]
    subgraph App[Application container]
        API --> LG[LangGraph orchestrator]
        LG --> MCP[MCP tool host]
    end
    LG -->|inference| LLM[LLM endpoint]
    MCP --> EMB[Embedding + reranker service]
    MCP --> PG[(PostgreSQL + pgvector\nMIMIC-IV + embeddings)]
    LG --> LOG[(Append-only audit store)]
    EMB --> PG
```
*Server-side deployment: one application container hosts orchestration and MCP tools over a model-serving tier and a PostgreSQL/pgvector data tier with an append-only audit store.*

## 8. Methodology Flowchart (design-science)

```mermaid
flowchart LR
    P[Problem\ngaps from Chapter 2] --> D[Design\n6-layer framework + agents]
    D --> DEMO[Demonstrate\nworked MIMIC-IV trace]
    DEMO --> EVAL[Evaluate\nChapter 4 metrics]
    EVAL -->|refine| D
    EVAL --> CONT[Contribution\nintegrated agentic CDSS]
```
*Design-science research cycle: problem to design to demonstration to evaluation, with refinement feeding back into design.*
