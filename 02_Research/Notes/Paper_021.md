# Paper 021

## Basic Information
- **Title:** A Survey of LLM-based Agents in Medicine: How far are we from Baymax?
- **Authors:** Wenxuan Wang, Zizhan Ma, Zheng Wang, Chenghan Wu, Jiaming Ji, Wenting Chen, et al.
- **Year:** 2025
- **DOI:** 10.48550/arXiv.2502.11211
- **Venue:** ACL 2025 Findings
- **Publisher:** Association for Computational Linguistics (arXiv preprint arXiv:2502.11211v2)
- **Link:** https://arxiv.org/abs/2502.11211

## Abstract Summary (200–300 words)
This survey provides a comprehensive review of **LLM-based agents in medicine**, analyzing roughly 60 studies (screened from ~300 candidates) published between 2022 and 2024. It organizes the field around four architectural pillars: **system profile, clinical planning, medical reasoning, and external capacity enhancement**. The authors distinguish LLM-based agents from standalone LLMs by their capacity for external knowledge retrieval, task planning, and tool invocation, enabling autonomous, adaptive decision-making rather than isolated text generation. The survey identifies four agent paradigms — **Single Agent, Sequential Task Chain, Collaborative Experts, and Iterative Evolution** — and maps them onto application scenarios: clinical decision support and diagnosis, clinical data analytics and documentation, medical training and simulation, and healthcare service optimization. It reviews evaluation frameworks, classifying benchmarks into static Q&A (MedQA, MedMCQA, PubMedQA, MMLU), workflow-based simulation (MedChain, AI Hospital, AgentClinic, ClinicalLab), and automated evaluation frameworks, alongside exact-match, semantic-similarity, and LLM-based metrics. The authors argue that static exam-style QA benchmarks are saturated and fail to capture interactive, sequential clinical decision-making. The discussion catalogs open challenges: hallucination management, multimodal and multilingual integration, cross-department interoperability, implementation and resource barriers, algorithmic bias, and privacy/security (GDPR, HIPAA). Future directions emphasize reasoning inspired by DeepSeek-R1 and inference-time scaling, integration with physical systems (medical robots), and advances in training simulation. The survey stresses **transparency and traceability**, patient-centered design, and the need for verification and dynamic error-correction systems, especially in multi-agent settings where errors can propagate. It concludes that although LLM-based medical agents show promise across diagnostics, documentation, and workflows, they remain early-stage, requiring real-time error correction, improved multimodal fusion, and hybrid reasoning to achieve reliable clinical integration.

## Research Problem
- The field lacks a **structured overview** of how LLM-based agents are architected, applied, and evaluated in medicine, despite rapid growth.
- Standalone LLMs cannot reliably perform interactive, multi-step clinical tasks; they hallucinate, lack real-time knowledge, and are not auditable.
- Existing evaluations rely on **static QA benchmarks** that do not reflect dynamic, sequential clinical workflows.

## Proposed Solution
- Not a system; this is a **systematic survey** that proposes a unifying conceptual framework and taxonomy for LLM-based medical agents.
- Defines a four-component architecture (profile, clinical planning, medical reasoning, external capacity enhancement) and four agent paradigms.
- Synthesizes challenges and future research directions across technical, evaluation, implementation, and ethical dimensions.

## Architecture
- **Profile:** three prototypes — Functional Modularization (e.g., MEGDA/MAGDA), Role Specialization (clinical roles), and Departmental Organization (discipline-based knowledge boundaries).
- **Clinical Planning:** task decomposition into subtasks; adaptive and iterative self-evolution architectures (e.g., MDAgents).
- **External Capacity Enhancement:** perception (EHR ingestion, OCR, CLIP for images), knowledge integration (knowledge graphs, drug databases, guideline repositories), and an action layer (medical calculators, EHR interfaces).

## Memory
- **Memory-Enhanced Reasoning** is a named module: long-term memory lets agents accumulate knowledge and past clinical experiences, refining decisions over time and maintaining continuity in patient care.
- Iterative Evolution frameworks maintain an **experience base** of past cases (e.g., Agent Hospital).

## Planning
- Clinical planning breaks complex tasks into subtasks (data ingestion, hypothesis generation, treatment planning, risk assessment).
- Adaptive Planning updates strategies from real-time data; Iterative Self-Evolution enables continuous improvement.

## Reasoning
- Reviews Multi-Step Diagnostic Reasoning (Chain-of-Thought, Tree-of-Thought), Reflective Decision-Making (ReAct-inspired reason-act alternation), Collaborative Group Reasoning (consensus across specialist agents), and Memory-Enhanced Reasoning.

## Tool Use
- External capacity via medical calculators, EHR interfaces, image analysis software; knowledge integration with drug interaction databases and guideline repositories; nested tool calling (e.g., MENTI). Table 1 tags many surveyed systems with tool-use capability.

## Multi-Agent
- Central theme: Collaborative Experts and Sequential Task Chain paradigms assign specialized roles (radiology, pathology, lab) that communicate via standardized protocols to aggregate findings (e.g., MedAgents, MDAgents, EHRAgent, ColaCare).

## RAG
- Discusses retrieval-augmented generation for documentation and patient-friendly report generation (iterative self-reflection + RAG) and knowledge integration grounding inferences in trusted external sources.

## Healthcare Contribution
- Provides the field's structured map of medical agent architectures, applications, benchmarks, and challenges — a reference taxonomy for researchers and practitioners entering clinical agent design.

## Trustworthy AI
- Dedicated coverage of hallucination management (MedHallBench, HaluEval), transparency/traceability, algorithmic bias (BiasMedQA — precision falling below 80%), and privacy/security (GDPR, HIPAA, inference/data-extraction attacks, differential privacy).

## Evaluation
- Not an empirical study; it categorizes benchmarks (static Q&A, workflow-based simulation, automated frameworks) and metrics (exact match, semantic similarity via BLEU/ROUGE/BERTScore, LLM-based). Notes that ColaCare demonstrated gains on MIMIC-III and MIMIC-IV.

## Research Gap
- Static benchmarks do not capture dynamic clinical workflows; verification and error-correction systems are underdeveloped; patient-centered feedback is largely absent; multimodal and cross-department integration remain unsolved.

## Key Contributions
- A four-pillar architectural taxonomy and four-paradigm classification of LLM-based medical agents.
- A structured survey of application scenarios with a summary table mapping systems to paradigms and tool use.
- A categorized review of benchmarks and metrics, plus a challenge/opportunity roadmap.

## Limitations
- Coverage focuses on 2022–early 2024 English-language publications in major databases (PubMed, ACM, arXiv, Google Scholar), potentially missing newer or non-English work.
- Being a survey, it offers no new empirical results or system implementation.

## Important Quotes
- "Clinical decisions must be auditable and explainable to align with medical ethics" (Sec. 2.2, Transparency and Traceability).
- "these agents operate autonomously and adapt dynamically to new information" (Sec. 2.1).

## Thesis Relevance
- Provides the **taxonomy backbone** (profile, planning, reasoning, external capacity) to position the thesis's layered multi-agent framework.
- Confirms **thesis gap (1)**: surveyed agents are largely evaluated on exam QA and simulated hospitals, not longitudinal real ICU records like MIMIC-IV — differentiate by evaluating on real timelines.
- Confirms **thesis gap (3)**: explicitly calls for verification systems and dynamic error-correction, motivating the thesis's verification gate and audit trail as first-class components.
- Validates **persistent longitudinal memory** as a recognized but under-realized module (Memory-Enhanced Reasoning) — adopt and strengthen for continuity of care.
- Supports **human-in-the-loop / patient-centered design** as an ethical necessity flagged by the survey.
- Endorses **ReAct-style reflective reasoning** and Collaborative Experts as reusable design patterns.

## References
- Yao et al., 2023 — ReAct: Synergizing Reasoning and Acting in Language Models (arXiv:2210.03629).
- Tang et al., 2024 — MedAgents: LLMs as Collaborators for Zero-Shot Medical Reasoning (arXiv:2311.10537).
- Kim et al., 2024 — MDAgents: An Adaptive Collaboration of LLMs for Medical Decision-Making (NeurIPS 2024).
- Shi et al., 2024 — EHRAgent: Code Empowers LLMs for Few-Shot Tabular Reasoning on EHRs (arXiv:2401.07128).
- Wei et al., 2023 — Chain-of-Thought Prompting Elicits Reasoning in LLMs (arXiv:2201.11903).
