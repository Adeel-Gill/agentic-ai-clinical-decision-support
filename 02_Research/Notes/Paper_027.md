# Paper 027

## Basic Information
- **Title:** RiskAgent: Synergizing Language Models with Validated Tools for Evidence-Based Risk Prediction
- **Authors:** Fenglin Liu, Jinge Wu, Hongjian Zhou, Xiao Gu, Jiayuan Zhu, Jiazhen Pan, et al.
- **Year:** 2025 (arXiv v2 revised Feb 2026)
- **DOI:** 10.48550/arXiv.2503.03802
- **Venue:** arXiv preprint (arXiv:2503.03802); formatted for ICML 2026 submission
- **Publisher:** arXiv (University of Oxford, University College London, TU Munich, University of Glasgow)
- **Link:** https://arxiv.org/abs/2503.03802

## Abstract Summary (200–300 words)
**RiskAgent** is a multi-agent framework that couples a lightweight LLM (an 8B LLaMA-3 backbone) with **hundreds of validated clinical decision tools** (evidence-based calculators from MDCalc) to produce **generalizable, faithful, evidence-based clinical risk predictions**. The authors argue that current medical LLMs excel at exam-style QA but fail on real clinical decision-making, that fine-tuning to embed all knowledge in weights is data- and compute-intensive, that commercial API use raises privacy concerns, and that LLMs still hallucinate and cannot cite evidence sources. RiskAgent instead offloads precise calculation and guideline adherence to external validated tools. The system uses three LLM agents inspired by actor-critic RL — a **Decider** (analyzes the problem, selects tools, interprets tool outputs, drafts answers), an **Executor** (parses parameters, invokes tools, formats outputs), and a **Reviewer** (reflects on the process, catches wrong tool selection or parameter-parsing errors, and triggers retries) — plus an **Environment** component with five sub-environments (tool retrieval-ranking, required parameters, tool outputs, formatting prompts, and historical analysis). A single 8B model, instruction-fine-tuned with LoRA, serves all three agent roles. To evaluate generalist risk prediction, the authors build **MedRisk**, a benchmark of 12,352 questions spanning 154 diseases, 86 symptoms, 50 specialties, and 24 organ systems (split into qualitative and quantitative halves). RiskAgent-8B reaches 78.34% (qualitative) and 76.33% (quantitative) accuracy, roughly doubling GPT-4o and outperforming o1, o3-mini, and Meditron-70B by >20% with 10x fewer parameters. It also generalizes on external MedCalc-Bench tool learning and on MedQA/MedMCQA/MMLU. The authors stress that RiskAgent is a decision-support tool requiring clinician oversight.

## Research Problem
- LLMs are strong on medical exams but perform poorly (15.83%–58.77% accuracy) on tasks requiring **precise calculation and adherence to evidence-based clinical guidelines**.
- Four cited barriers: clinical inefficacy, resource-intensive fine-tuning, privacy concerns with commercial LLMs, and **unfaithful/hallucinated outputs that cannot cite evidence sources**.
- Goal: a resource-efficient, transparent, trustworthy way to make generalist clinical risk predictions.

## Proposed Solution
- Instead of embedding all knowledge in model weights, **enable a lightweight LLM to collaborate with hundreds of validated evidence-based tools** (clinical calculators), so predictions are grounded, traceable, and cheaper to run.
- A three-agent (Decider/Executor/Reviewer) framework over a five-part Environment, with a single LoRA-fine-tuned 8B model playing all roles.

## Architecture
- **Decider**: analyzes the medical problem, selects appropriate tools from retrieved candidates, analyzes tool outputs, and produces initial answers.
- **Executor**: parses required parameters for the selected tool, invokes it, and converts outputs into risk scores/choices.
- **Reviewer**: reviews the full history, reflects (Reflect[right]/Reflect[wrong]); on error, sends feedback so the Decider re-selects tools or the Executor re-parses.
- **Environment (5)**: (1) retrieval-ranking to extract top-N relevant tools from a library of M; (2) required-parameter schemas; (3) tool output store; (4) formatting/system prompts; (5) historical analysis store.
- Backbone: LLaMA-3-8B, parameter-efficient fine-tuning (LoRA); one shared model for all three agents keeps total size at 8B.

## Memory
- No persistent longitudinal patient memory. Working memory is the **Environment 5 historical-analysis store** that accumulates the Decider/Executor trace within a case for the Reviewer to reflect over.

## Planning
- Planning is **tool-selection and execution planning**: the Decider plans which validated tool(s) to invoke; the Reviewer enables replanning (re-select tools / re-parse parameters) when a step fails.

## Reasoning
- **Tool-grounded, evidence-based reasoning** rather than pure parametric reasoning; an actor-critic-inspired reflection loop (Reviewer as critic) verifies each decision. Baseline comparisons include ReAct-style reasoning; the paper's advance is grounding reasoning in validated calculators.

## Tool Use
- Core contribution. Hundreds (387 retained, predicting 154 diseases) of validated clinical calculators from **MDCalc** are wrapped as callable tools; a retrieval-ranking algorithm surfaces the top-N per query; the Executor handles parameter parsing and invocation. Evaluated for tool-learning generalization on external MedCalc-Bench.

## Multi-Agent
- Yes — a three-agent Decider/Executor/Reviewer collaboration modeled on actor-critic RL, with division of labor to reduce each component's learning burden and improve accuracy.

## RAG
- Uses a **retrieval-ranking step over a tool library** (retrieve top-N tools) rather than retrieval over a document/text corpus; it is retrieval of tools, not classic passage RAG.

## Healthcare Contribution
- **MedRisk** benchmark: 12,352 generalist risk-prediction questions across 154 diseases, 86 symptoms, 50 specialties, 24 organ systems (qualitative + quantitative).
- Demonstrates that an 8B model + validated tools beats far larger general and medical LLMs on clinical risk prediction, viable for **resource-limited institutions** and privacy-sensitive settings.
- Evidence-traceable predictions (sources cited via the invoked tool) improve transparency for clinical decision support.

## Trustworthy AI
- **Faithfulness/hallucination mitigation** via grounding in validated tools and tracing the evidence source behind each decision.
- Reviewer agent adds a **verification/reflection gate** with retries; answers verified by clinicians in examples.
- Impact statement: retrospective HIPAA-de-identified data; explicit that RiskAgent is decision-support and **clinician oversight remains essential**.

## Evaluation
- **Risk prediction (MedRisk)**: RiskAgent-8B 78.34% (qual.) / 76.33% (quant.), ~2x GPT-4o's 38.39% (quant.); beats o1, o3-mini, GPT-4.5, Meditron-70B; improvement significant (p < 0.01), five runs with mean/STD.
- **Tool learning (MedCalc-Bench)**: RiskAgent-GPT-4o 67.71% overall; strong on physical (97.08%) and dosage (95.00%) calculations.
- **QA (MedQA/MedMCQA/MMLU)**: RiskAgent-GPT-4o competitive/best (e.g., MedQA 87.8, MedMCQA 80.8).
- **Ablations**: each of Tool Library, Decider, Executor, Reviewer contributes; adding the tool library alone boosts the basic LLM >14%.

## Research Gap
- Prior tool-augmented medical agents (MedAgents, MDAgents) rely on parametric knowledge without validated calculators; AgentMD pioneered calculator integration but with limited coverage and heavy prompting of proprietary models.
- RiskAgent targets **broad validated-tool coverage with a lightweight trainable model**, but is still evaluated on curated benchmark questions rather than longitudinal real-patient records/ICU streams.

## Key Contributions
- RiskAgent: a clinically efficient multi-agent framework synergizing a lightweight LLM with hundreds of validated tools for faithful, evidence-based recommendations.
- MedRisk benchmark for generalist medical risk prediction (12,352 cases).
- Extensive experiments showing state-of-the-art risk prediction, tool-learning, and QA generalization with an 8B model.

## Limitations
- Designed specifically for **risk prediction**; broader clinical tasks are out of scope.
- Depends on the coverage/quality of the external tool library (MDCalc); tools not covering a scenario limit applicability.
- Evaluated on retrospective, de-identified, benchmark-style data — not prospective or longitudinal deployment; clinician oversight required; privacy regulations must be met in real deployment.

## Important Quotes
- "clinician oversight remains essential to ensure patient safety and validate tool applicability" (Impact Statement)
- "traces the information source (i.e., evidence) behind our system's decisions" (Section 4.1)

## Thesis Relevance
- Direct model for the thesis's **tool-verification and audit-trail** layer: grounding LLM outputs in validated tools and tracing evidence per decision is exactly the kind of first-class verification the thesis targets (gap 3).
- Decider/Executor/Reviewer maps cleanly onto the thesis's **multi-agent + verification-gate + human-in-the-loop** design, with the Reviewer as a reflective verification component.
- Demonstrates a **lightweight (8B) deployable agent** — relevant for privacy-sensitive ICU settings where commercial APIs may be disallowed.
- Reinforces thesis gap (1): even RiskAgent evaluates on constructed benchmark questions (MedRisk), not real longitudinal ICU records like MIMIC-IV.
- Its retrieval-ranking over a tool library informs how the thesis might route between clinical calculators and patient-timeline RAG.
- Emphasis on faithfulness and evidence-tracing supports the thesis's audit-trail-faithfulness evaluation.

## References
- Jin, Q., et al. "AgentMD: Empowering Language Agents for Risk Prediction with Large-Scale Clinical Tool Learning." (calculator integration precedent).
- Tang, X., et al. "MedAgents: Large Language Models as Collaborators for Zero-shot Medical Reasoning." (2024).
- Kim, Y., et al. "MDAgents: An Adaptive Collaboration of LLMs for Medical Decision-Making." (2024).
- Khandekar, N., et al. "MedCalc-Bench: Evaluating Large Language Models for Medical Calculations." (2025).
- Yao, S., et al. "ReAct: Synergizing Reasoning and Acting in Language Models." (2023).
