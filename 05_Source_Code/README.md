# ACDSS — Agentic Clinical Decision Support System

Prototype source-code scaffold for the MS thesis **"An Agentic AI Framework for
Intelligent Patient Monitoring and Clinical Decision Support."**

> ⚠️ **Research prototype — NOT a medical device.**
> This code is an academic proof-of-concept. It is **not** validated, cleared, or
> approved for clinical use by any regulatory body (FDA, EMA, MHRA, etc.). It must
> **never** be used to make, inform, or substitute real diagnostic, monitoring, or
> treatment decisions for actual patients. All outputs require review by a qualified
> licensed clinician. Data used must be de-identified and handled under the
> applicable data-use agreement (e.g. PhysioNet credentialed access for MIMIC-IV).

---

## 1. What this is

A clean, modular Python scaffold (skeletons + docstrings + `TODO`s, **not** a full
implementation) that an examiner can read as a credible engineering plan and that
the student can flesh out incrementally.

Technology choices:

| Concern              | Choice                                            |
| -------------------- | ------------------------------------------------- |
| Language             | Python 3.11                                       |
| API / UI backend     | FastAPI + Uvicorn                                 |
| Agent orchestration  | LangGraph (state graph over LangChain-core)       |
| LLM                  | Provider-agnostic `LLMClient`; default Anthropic Claude |
| Vector store         | pgvector on PostgreSQL                             |
| Tool exposure        | MCP server (`query_ehr`, `search_guidelines`, `drug_interactions`) |
| Config               | `pydantic-settings`, all secrets via environment  |
| Evaluation           | ragas (RAG faithfulness / relevancy)              |

---

## 2. The six-layer architecture

The framework decomposes into six layers. Each maps to a package under
`src/acdss/`:

| # | Layer                     | Package                | Responsibility                                              |
| - | ------------------------- | ---------------------- | ----------------------------------------------------------- |
| 1 | **Data**                  | `acdss.data`           | Load a patient cohort / observations from MIMIC-IV (Postgres). |
| 2 | **Memory**                | `acdss.memory`         | Short-term (session), long-term (persistent), vector store, clinical context, and the `MemoryManager` that coordinates them. |
| 3 | **Reasoning / RAG**       | `acdss.rag`            | Ingest → retrieve → rerank → compose grounded context over guidelines. |
| 4 | **Orchestration**         | `acdss.orchestration`  | LangGraph state graph wiring the agents, a conflict-resolution node, and a verification gate. |
| 5 | **Decision**              | `acdss.decision`       | Aggregate verified agent outputs into Dx / Risk / Tx / Explanation + confidence. |
| 6 | **API / UI**              | `acdss.api`            | FastAPI app: assessment endpoint, health, and human-in-the-loop (HITL) approve / modify / reject. |

Cross-cutting **trustworthy-AI** concerns (`acdss.trust`) — audit logging, safety
guardrails, bias monitoring, calibration — and the **LLM abstraction**
(`acdss.llm`) and **MCP server** (`acdss.mcp`) support all six layers.

The agents themselves live in `acdss.agents`:
Coordinator, Monitoring, Planner, Diagnosis, RiskPrediction,
TreatmentRecommendation, Explanation, Verification, plus DataRetrieval.
(The MemoryManager lives in `acdss.memory.manager`.)

See [`docs/architecture.md`](docs/architecture.md) for a module diagram.

---

## 3. Repository layout

```
05_Source_Code/
├── README.md
├── pyproject.toml
├── .env.example
├── .gitignore
├── docker/
│   ├── Dockerfile
│   └── docker-compose.yml
├── docs/
│   └── architecture.md
├── src/acdss/
│   ├── config.py
│   ├── llm/            # LLMClient interface + Anthropic impl
│   ├── data/           # MIMIC-IV cohort loader
│   ├── memory/         # short/long-term, vector store, context, manager
│   ├── rag/            # ingest, retriever, reranker, pipeline
│   ├── agents/         # base ABC + 9 concrete agents
│   ├── orchestration/  # LangGraph state graph
│   ├── decision/       # aggregation engine
│   ├── trust/          # audit, safety, bias, calibration
│   ├── mcp/            # MCP tool server
│   └── api/            # FastAPI app
└── tests/
    ├── test_smoke.py
    └── test_agents.py
```

---

## 4. Setup

Requires Python 3.11 and (for the vector store) a PostgreSQL instance with the
`pgvector` extension.

```bash
cd 05_Source_Code

# 1. Create a virtual environment
python3.11 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

# 2. Install (editable, with dev extras)
pip install -e ".[dev]"

# 3. Configure — copy the template and fill in placeholders
cp .env.example .env
#   edit .env: LLM_API_KEY, DB_URL, MODEL_NAME, ...
```

Bring up Postgres/pgvector (and, optionally, the app) with Docker:

```bash
cd docker
docker compose up -d db          # just the database
# docker compose up --build      # database + app
```

---

## 5. Run

```bash
# From 05_Source_Code/ with the venv active and .env populated:
uvicorn acdss.api.main:app --reload --port 8000

# Health check
curl http://localhost:8000/health

# Trigger an assessment for a (de-identified) patient id
curl -X POST http://localhost:8000/assess/10001217
```

Run the MCP tool server (stdio transport) separately:

```bash
python -m acdss.mcp.server
```

Run the test suite:

```bash
pytest
```

---

## 6. Status

Every module is a **skeleton**: classes, function signatures, typed Pydantic
models, docstrings, and `TODO` / `raise NotImplementedError` markers. Nothing here
performs real inference or database work yet — it defines the shape the student
implements against.
