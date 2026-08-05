# Paper 025

## Basic Information
- **Title:** Towards Conversational AI for Disease Management
- **Authors:** Anil Palepu, Valentin Liévin, Wei-Hung Weng, Khaled Saab, David Stutz, Yong Cheng, et al.
- **Year:** 2025
- **DOI:** 10.48550/arXiv.2503.06074
- **Venue:** arXiv preprint
- **Publisher:** Google Research / Google DeepMind (arXiv:2503.06074v1)
- **Link:** https://arxiv.org/abs/2503.06074

## Abstract Summary (200–300 words)
This paper advances the Articulate Medical Intelligence Explorer (**AMIE**) from diagnostic dialogue toward **management reasoning** — disease progression, therapeutic response, and safe medication prescription over multiple patient visits. The authors build an **LLM-based agentic system** with two specialized agents inspired by dual-process ("Thinking, Fast and Slow") cognition: a **Dialogue Agent** ("system 1") for fast, empathetic conversation that maintains persistent state across visits, and a **Management Reasoning (Mx) Agent** ("system 2") that uses Gemini's long-context capabilities to reason over multi-visit patient context and hundreds of pages of clinical guidelines to produce structured, citation-annotated management plans. The Mx Agent uses coarse retrieval (Gecko embeddings over 627 guideline documents totaling ~10.5M tokens), long-context in-context reasoning (256k-token budget, ~6 guidelines), ensemble-style draft-and-refine plan generation, and **decoding constraints** that force output into a predefined JSON schema with valid guideline citations for interpretability and traceability. In a randomized, blinded, virtual multi-visit OSCE study, AMIE was compared to **21 primary care physicians across 100 multi-visit scenarios** (five specialties, grounded in UK NICE and BMJ Best Practice guidelines). AMIE was **non-inferior to PCPs across all 15 evaluation axes and three visits**, and scored significantly better in preciseness of treatments and investigations and in alignment/grounding of plans in guidelines. Specialist physicians and patient actors preferred AMIE more often than PCPs on MXEKF axes. On **RxQA**, a new 600-question medication-reasoning benchmark from US (OpenFDA) and UK (BNF) formularies validated by board-certified pharmacists, both AMIE and PCPs benefited from external drug information, and AMIE outperformed PCPs on higher-difficulty questions. The work marks a significant step toward conversational AI for longitudinal disease management.

## Research Problem
- Diagnostic reasoning is necessary but **not sufficient** for clinical care; **management reasoning** (investigations, care planning over time, prescribing) is under-explored and hard to evaluate due to context specificity.
- Prior LLM management-reasoning studies used static, non-conversational settings.

## Proposed Solution
- A **dual-agent AMIE system** separating fast conversational response (Dialogue Agent) from slow, guideline-grounded management planning (Mx Agent), evaluated via a multi-visit remote OSCE and the RxQA benchmark.

## Architecture
- **Dialogue Agent** (Gemini 1.5 Flash, fine-tuned) handles conversation and orchestrates the system; **Mx Agent** (Gemini long-context) is invoked as a tool to produce management plans. Shared **agent state** (patient summary, differential, management plan) bridges the two.

## Memory
- Strong focus: a modular **persistent agent state** maintained across multiple visits, updated by an asynchronous background reasoning sub-routine — includes current patient summary, current differential diagnosis, current management plan, and visit number for context-specific logic.

## Planning
- The Mx Agent plans care via a structured pipeline: analyze patient → set management goals → fill/plan management plan (in-visit investigations, ordered investigations, recommendations), using draft-and-merge ("ensemble refinement") across four drafts.

## Reasoning
- **Chain-of-reasoning** in the Dialogue Agent (Plan Response → Generate Response → Refine Response); long-context multi-document structured reasoning in the Mx Agent, with reasoning steps (analysis, management_goals) chained to plan construction in a single constrained model call.

## Tool Use
- The Mx Agent is invoked as a **tool** by the Dialogue Agent; a Gecko-embedding retriever tool performs coarse guideline filtering; for RxQA the system ingests OpenFDA/BNF formularies as retrievable resources.

## Multi-Agent
- Yes: a two-agent symbiosis (Dialogue Agent + Mx Agent) mapped to dual-process cognition, communicating through shared agent state.

## RAG
- Yes, hybrid: **coarse embedding retrieval** (Gecko 1B over titles/abstracts) to filter 627 guidelines, then **long-context in-context retrieval/reasoning** over ~256k tokens. Citations are generated as an integral part of reasoning rather than post-hoc attribution.

## Healthcare Contribution
- First rigorous, randomized, blinded evaluation of conversational **longitudinal disease-management reasoning** vs. PCPs, plus RxQA, a pharmacist-validated medication-reasoning benchmark grounded in national formularies.

## Trustworthy AI
- Emphasis on **interpretability and traceability**: every management-plan item is annotated with explicit guideline citations enforced via JSON decoding constraints. Grounding in authoritative NICE/BMJ guidelines and formularies; blinded specialist + patient-actor evaluation; McNemar tests with FDR correction.

## Evaluation
- Multi-visit OSCE: 100 scenarios, 21 PCPs, 21 patient actors, 10 specialist physicians; 15 axes over 3 visits. AMIE non-inferior on all axes; better treatment preciseness (e.g., 94% vs. 67% visit 1) and guideline alignment/grounding. MXEKF: AMIE preferred (median 42% win vs. PCP 8%). RxQA: AMIE beats PCPs on higher-difficulty questions in open-book setting.

## Research Gap
- Management reasoning had little rigorous, conversational, longitudinal evaluation. Remaining gaps: OSCE is a simulated analogue (not real deployment); static between-visit intervals; guideline corpus is a limited sample; real-world translation needs further study.

## Key Contributions
- A dual-agent (Dialogue + Mx) AMIE system for multi-visit, guideline-grounded management reasoning with citation-constrained structured generation.
- A randomized, blinded multi-visit OSCE showing non-inferiority to PCPs and superior preciseness/guideline grounding.
- RxQA, a 600-question medication-reasoning benchmark from OpenFDA and BNF validated by pharmacists.

## Limitations
- OSCE with patient actors is a controlled analogue, not real patient care; no real-world clinical outcomes.
- Between-visit intervals were static and logistically constrained; guideline corpus was a limited sample.
- System relies on proprietary Gemini models and long-context compute; latency capped at ~1 minute per plan.

## Important Quotes
- "AMIE's management plans were non-inferior to those from PCPs" (Sec. 4.1.1).
- "we generate citations as an integral part of the reasoning process" (Sec. 2.2.2).

## Thesis Relevance
- The **dual-process two-agent design** (fast dialogue + slow reasoning) with a **shared persistent agent state across visits** is a strong template for the thesis's longitudinal patient-memory layer.
- **Citation-constrained structured generation** directly informs the thesis's verification gate and audit-trail faithfulness (gap 3): every recommendation is traceable to a source via enforced JSON schema.
- Confirms **gap (2)** partly closed at the guideline level — AMIE grounds in guidelines/formularies; the thesis differentiates by grounding in the patient's *own* longitudinal ICU timeline (MIMIC-IV), not just external guidelines.
- The **multi-visit OSCE + MXEKF rubric** and RxQA offer rigorous, human-blinded evaluation methodology to emulate beyond static QA (gap 1).
- Long-context in-context retrieval vs. chunked pipelines is a design trade-off to weigh for the thesis's RAG component.
- Reinforces **human-in-the-loop** framing: AMIE augments PCP-style reasoning with explicit guideline entailment for clinician review.

## References
- Tu et al., 2024 — Towards Conversational Diagnostic AI (AMIE baseline).
- Kahneman, 2011 — Thinking, Fast and Slow (dual-process cognition inspiration).
- Gemini Team, 2024 — Gemini technical report (long-context base models).
- Lee et al., 2024 — Gecko: text embeddings for coarse retrieval.
- NICE Guidance & BMJ Best Practice — clinical practice guideline corpora.
