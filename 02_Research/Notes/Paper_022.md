# Paper 022

## Basic Information
- **Title:** MedAgentBench: A Realistic Virtual EHR Environment to Benchmark Medical LLM Agents
- **Authors:** Yixing Jiang, Kameron C. Black, Gloria Geng, Danny Park, James Zou, Andrew Y. Ng, Jonathan H. Chen
- **Year:** 2025
- **DOI:** 10.48550/arXiv.2501.14654
- **Venue:** arXiv preprint (also NEJM AI); under review
- **Publisher:** Stanford University (arXiv:2501.14654v2)
- **Link:** https://arxiv.org/abs/2501.14654

## Abstract Summary (200–300 words)
MedAgentBench is a broad evaluation suite designed to assess the **agent capabilities of LLMs within a realistic virtual EHR environment**. The authors argue that while LLMs increasingly act as agents — planning, using tools, and executing high-level tasks — no standardized benchmark exists for medical agent capabilities, a critical barrier to adoption in the highly regulated healthcare industry. MedAgentBench contributes three artifacts: (1) **300 patient-specific, clinically derived tasks across 10 categories** written by licensed internal-medicine physicians; (2) a **FHIR-compliant interactive environment** with realistic profiles of 100 patients comprising over 700,000 (785,207) data elements drawn from Stanford's STARR de-identified data warehouse; and (3) benchmark results for 12 state-of-the-art LLMs. The environment uses standard EMR APIs (HAPI FHIR JPA, Dockerized) so it can migrate into live systems. Tasks span patient information and lab retrieval, data aggregation, recording patient data, test ordering, referral ordering, and medication ordering, with codes such as LOINC, NDC, and SNOMED. Evaluation uses **task success rate at pass@1** to reflect the low tolerance for error in clinical settings, split into query SR (GET-only retrieval) and action SR (POST modifications). The best model, **Claude 3.5 Sonnet v2, achieves 69.67% overall success** (85.33% query, 54.00% action), with substantial variation across categories and difficulty. Most models perform better on query than action tasks, and a gap remains between closed- and open-weight models. Common failures include not following output-format instructions and producing full-sentence answers instead of structured values. The authors conclude that current LLMs show promising but not yet reliable agent capabilities, positioning MedAgentBench as a benchmark to track progress toward clinically integrated agentic AI.

## Research Problem
- There is **no standardized benchmark** for evaluating LLM agent capabilities in interactive medical/EHR contexts.
- Traditional medical QA benchmarks (MedQA, MedMCQA) are saturated and oversimplify real clinician–patient interaction.
- Lack of trust, safety, and regulatory validation blocks agent adoption in healthcare.

## Proposed Solution
- A **benchmark** of 300 physician-authored tasks plus a FHIR-compliant interactive EHR environment and an evaluation codebase (built on AgentBench), enabling systematic, migratable assessment of medical LLM agents.

## Architecture
- **Agent orchestrator** mediates between the clinician's high-level task, the LLM provider, and the FHIR server; the agent plans function calls, sends GET/POST requests, and returns a summary.
- Nine FHIR functions exposed (condition/lab/vital/medicationrequest/procedure search and create, patient.search) as JSON schemas; interactions capped at 8 rounds.

## Memory
- No persistent longitudinal memory module is built in; the paper notes developers *could* implement memory-augmented decision-making, but the baseline orchestrator is stateless within the 8-round cap.

## Planning
- The agent interprets a high-level instruction and **plans a sequence of function calls**; difficulty is stratified by number of steps (easy = 1, medium = 2, hard = 3+), directly probing planning depth.

## Reasoning
- Reasoning is implicit in multi-round function selection; the paper notes advanced systems could add hierarchical reasoning or retrieval-augmented reasoning, but the baseline uses a simple single-agent orchestrator.

## Tool Use
- Core focus: the agent must select and correctly format **FHIR API tool calls** (GET for retrieval, POST for record modification) using medical coding systems (LOINC, NDC, SNOMED, CPT, ICD-10).

## Multi-Agent
- Not a focus; the baseline is a single-agent orchestrator. The authors note compound/multi-sub-agent systems could be built on the benchmark but do not evaluate them.

## RAG
- Not implemented in the baseline; the paper mentions retrieval-augmented reasoning as a possible extension. Grounding is via live FHIR data retrieval rather than a retrieval corpus.

## Healthcare Contribution
- First benchmark requiring **autonomous interaction with a medical records environment**; provides a realistic, deployable FHIR sandbox and physician-written tasks that mirror real inpatient/outpatient administrative and clinical workflows.

## Trustworthy AI
- Adopts **pass@1** to mirror clinical low error tolerance; grades action tasks with rule-based sanity checks on POST payloads; explicitly frames trust, safety, and regulatory hurdles as adoption barriers. Notes reliability/reproducibility of repeated actions as future work.

## Evaluation
- 12 LLMs evaluated by success rate (overall/query/action) at pass@1. Claude 3.5 Sonnet v2 leads at 69.67%; GPT-4o 64.00%; DeepSeek-V3 62.67%. Hard tasks collapse for most models (e.g., 23.33% for Claude on hard). 150 tasks retrieval-only, 150 require modification.

## Research Gap
- No current LLM is a highly reliable medical agent; action-based (record-modifying) tasks lag retrieval; the environment omits team coordination/communication and is Stanford-specific (potential cohort bias); coverage excludes surgical/nursing domains.

## Key Contributions
- A 300-task, physician-authored, verifiable medical agent benchmark.
- A migratable FHIR-compliant interactive environment with 100 realistic patients (>700k records).
- Baseline results and error analysis across 12 state-of-the-art LLMs.

## Limitations
- Patient profiles come only from Stanford Hospital, risking non-representative bias.
- Does not capture full real-world complexity requiring multi-team coordination; focuses on medical-record contexts only.
- Uses a simple baseline orchestrator; advanced agent designs and repeated-action reliability untested.

## Important Quotes
- "the first benchmark requiring autonomous interactions with medical records environments" (Contributions, Sec. 1).
- "we exclusively adopt pass@1 in our benchmark" (Sec. 2.4.1).

## Thesis Relevance
- Directly supplies a **FHIR-based interactive evaluation harness** and task taxonomy the thesis can adopt or adapt for its verification/action layer.
- Reinforces **thesis gap (1)**: even this realistic EHR benchmark uses jittered snapshots and administrative tasks — the thesis differentiates by longitudinal MIMIC-IV ICU timelines and monitoring, not one-shot record ops.
- Motivates the thesis's **verification gate**: MedAgentBench's rule-based payload sanity checks and pass@1 stance echo the need for first-class output validation before actions are committed.
- Highlights an opening for **persistent memory and multi-agent orchestration**, which MedAgentBench leaves to future work — the thesis can fill these.
- Provides concrete **tool-use interfaces (FHIR GET/POST, LOINC/SNOMED/NDC)** to model the thesis's action module realistically.

## References
- Liu et al., 2023 — AgentBench: Evaluating LLMs as Agents (arXiv:2308.03688).
- Yao et al., 2024 — tau-bench: Tool-Agent-User Interaction Benchmark (arXiv:2406.12045).
- Schmidgall et al., 2024 — AgentClinic: A Multimodal Agent Benchmark for Simulated Clinical Environments (arXiv:2405.07960).
- Patil et al., 2023 — Gorilla: LLM Connected with Massive APIs / BFCL (arXiv:2305.15334).
- Zou & Topol, 2025 — The Rise of Agentic AI Teammates in Medicine (The Lancet).
