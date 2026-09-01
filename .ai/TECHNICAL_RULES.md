# TECHNICAL RULES

Governs `05_Source_Code/`, `04_Architecture/System_Design.md`,
`04_Architecture/Technical_Feasibility.md`, and every claim about what the software does.

---

## 1. Implementation-claim discipline

The most dangerous sentence in this project is one that implies more of the system runs than
does. Before writing any capability claim, check which bucket it falls into:

| Bucket | Contents | Permitted language |
|---|---|---|
| **Implemented + pilot-validated** | `acdss.pilot`: timeline construction, timestamp-aware retrieval, logistic-regression early-warning baseline, rule-based verification gate, measured audit trail | "was measured", "runs in 11.7 ms median" |
| **Implemented, not evaluated** | Clinician platform (React + FastAPI, `app_dashboard.py`, `dashboard.py`, six screens) — **synthetic fixtures** | "is implemented on synthetic data"; add `TODO: EVALUATE IMPLEMENTATION` |
| **Scaffold** | `acdss/agents/`, `acdss/memory/`, `acdss/rag/`, `acdss/orchestration/`, `acdss/decision/`, `acdss/trust/`, `acdss/mcp/`, `acdss/llm/` — typed signatures, docstrings, `TODO` / `NotImplementedError` | "is specified", "will be implemented" |
| **Designed only** | ReAct engine, dual-grounded RAG over notes, calibrated confidence, LangGraph orchestration | "the framework is designed to" |

Never claim code works without running it in the current session and showing the output.
`pytest` passing on smoke tests is not evidence that the agent loop works.

## 2. The prototype disclaimer is mandatory

Every artifact that could be mistaken for deployable software carries it:

> **Research prototype — NOT a medical device.** Not validated, cleared, or approved for clinical
> use by any regulatory body. Must never be used to make, inform, or substitute real diagnostic,
> monitoring, or treatment decisions. All outputs require review by a qualified licensed
> clinician.

This is not boilerplate to trim. `weissman2025unregulated` establishes that unconstrained LLM
output already meets medical-device criteria — the disclaimer is a regulatory position, not a
formality.

## 3. Technology stack (and why)

Each choice is a defended bet, documented in `System_Design.md` §4. Do not change one without
restating its justification.

| Concern | Choice | Justification |
|---|---|---|
| Language | Python 3.11 | — |
| Orchestration | **LangGraph** | The workflow is a stateful DAG with conditional edges, parallel branches, and cycles (ReAct). Linear chain frameworks model this awkwardly. The graph spec is engine-independent, so LangGraph is an implementation detail. |
| Tool exposure | **MCP** | Typed, versioned, auditable tool interface; decouples tool implementation from agent prompts [ehtesham2025protocols]. |
| LLM serving | Hosted endpoint (prototype); self-hosted open-weight as scale-out | Removes GPU ops for a bounded prototype; provider-generic by design. |
| Vector store | **pgvector** → **Qdrant** | pgvector co-locates embeddings with MIMIC-IV relational data in one PostgreSQL instance, simplifying provenance joins. Qdrant is the named migration target. |
| Embeddings | Biomedical bi-encoder + cross-encoder reranker | Domain-tuned retrieval; rerank removes weak passages before the prompt. |
| Relational | **PostgreSQL** | MIMIC-IV ships relational; pgvector lives here too. |
| API | **FastAPI** | Async suits long-running I/O-bound agent calls; server-side only. |
| Audit store | Append-only, hash-chained log | Immutability and replay are governance requirements. |
| Evaluation | ragas | RAG faithfulness / relevancy [es2024ragas]. |

## 4. Non-functional targets

From `System_Design.md` §5. These are **targets**, not measurements.

| Stage | Budget (s) |
|---|---|
| Monitoring (rule-based, no LLM) | ≤ 1 |
| Planner | ≤ 4 |
| Data/Retrieval | ≤ 3 |
| Diagnosis / Risk (parallel) | ≤ 8 |
| Treatment | ≤ 6 |
| Explanation | ≤ 5 |
| Verification | ≤ 4 |
| **End-to-end, parallelized** | **≤ 30** |

The 30-second target is acknowledged as aggressive: MedAgents reports ~40 s per question with
fewer agents [tang2024medagents]. The three levers are short-circuit routing for stable cases,
parallel Diagnosis/Risk branches, and rule-based non-reasoning steps. Whether the target is met
is an **open empirical question** for Chapter 4 — never write it as achieved.

## 5. The ten named risks

`Technical_Feasibility.md` is deliberately skeptical and rates each risk. The two rated High on
both likelihood and impact:

1. **Context-window overflow across the agent pipeline** — mitigated by Memory-Manager retrieval
   windowing, per-call token budgets, and provenance-preserving summarization.
2. **Full-DAG latency exceeding clinical tolerance** — mitigated by short-circuit routing,
   parallel branches, rule-based steps; residual risk flagged honestly.

The other eight: model-serving throughput; wrong fact promoted to long-term memory; pgvector
degradation at scale; poor retrieval quality producing confident wrong output; MCP tool failure
stalling the ReAct loop; inter-agent deadlock; LangGraph lock-in; undetected subgroup
performance disparity.

Any feasibility discussion that lists only strengths is not a feasibility study. Preserve the
skeptical tone.

## 6. Privacy in the software design

- All processing is **server-side**. Patient data reaches the browser only as rendered
  recommendations.
- Embeddings and records stay in one controlled PostgreSQL instance.
- The audit log records every access.
- Timestamps are handled in **relative time only**, consistent with de-identification.
- Secrets via environment (`pydantic-settings`); `.env` is gitignored; `.env.example` carries
  placeholders only.

## 7. Code quality expectations

This is research code, held to research-code standards — reproducibility over polish:

- Typed signatures and Pydantic models at module boundaries.
- Docstrings that state the contract, not what the code obviously does.
- Deterministic seeds wherever randomness enters.
- No network calls in tests.
- No patient data in fixtures — the clinician platform uses `demo_data.py` synthetic fixtures
  precisely for this reason.
- Reproduction commands stay accurate in the README when file paths change.

## 8. Running the prototype

Recorded in `README.md` and `05_Source_Code/README.md`. Verify before citing:

```bash
# Pilot (real demo data, kept outside the repo)
cd 05_Source_Code/src
python -m acdss.pilot.run_pilot --data <demo_root> --out ../../06_Experiments/results/pilot

# Clinician platform — backend then frontend
python -m uvicorn acdss.api.app_dashboard:app --reload --port 8000
cd 05_Source_Code/frontend && npm install && npm run dev   # http://localhost:5173
```

Pilot dependencies are only `pandas`, `numpy`, `scikit-learn`. The gate operating curve and agent
health metrics are served from `06_Experiments/results/pilot/` when present.

## 9. What the code must never do

- Read from a path inside the repository for patient data.
- Write patient-derived artifacts anywhere under version control.
- Log prompt contents containing patient text outside the secured environment.
- Present synthetic fixture output as real results in a screenshot or figure without labeling it.
- Ship a default that sends patient data to a hosted LLM endpoint without an explicit,
  documented configuration step.
