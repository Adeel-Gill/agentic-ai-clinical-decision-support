# Paper 036

## Basic Information
- **Title:** MedRAX: Medical Reasoning Agent for Chest X-ray
- **Authors:** Adibvafa Fallahpour, Jun Ma, Alif Munim, Hongwei Lyu, Bo Wang
- **Year:** 2025
- **DOI:** 10.48550/arXiv.2502.02673
- **Venue:** Proceedings of the 42nd International Conference on Machine Learning (ICML 2025), Vancouver, Canada; arXiv:2502.02673
- **Publisher:** PMLR (Volume 267)
- **Link:** https://arxiv.org/abs/2502.02673

## Abstract Summary (200–300 words)
MedRAX is presented as the **first versatile AI agent framework specialized for chest X-ray (CXR) interpretation**, integrating state-of-the-art CXR analysis tools with a multimodal large language model in a unified, training-free framework. The motivation is that task-specific CXR models (classification, segmentation, report generation) operate in isolation, fragmenting clinical workflows, while end-to-end multimodal foundation models hallucinate, struggle with multi-step diagnostic reasoning, and lack transparency. MedRAX addresses this by using an LLM (GPT-4o in the reference implementation) as the core of a **ReAct (Reasoning and Acting) loop** that decomposes complex medical queries into sequential analytical steps, dynamically selecting and orchestrating specialized tools: visual QA (CheXagent, LLaVA-Med), segmentation (MedSAM, ChestX-Det/PSPNet), grounding (Maira-2), report generation (a SwinV2+BERT model trained on CheXpert Plus), disease classification (TorchXRayVision DenseNet-121), and CXR image generation (RoentGen). The system maintains a **short-term memory** (LangChain/LangGraph) of user interactions, tool outputs, and images, supports parallel tool execution, and requires no retraining to add new tools. To evaluate multi-step reasoning, the authors introduce **ChestAgentBench**, a benchmark of 2,500 six-choice questions built from 675 expert-curated Eurorad clinical cases across 7 competencies (detection, classification, localization, comparison, relationship, diagnosis, characterization). MedRAX achieves state-of-the-art results: 63.1% overall on ChestAgentBench versus 56.4% for GPT-4o and 39.5% for CheXagent; best overall accuracy on CheXbench VQA; the highest micro-averaged F1 (mF1-14 of 79.1%) on MIMIC-CXR report generation; and 90.35% accuracy on SLAKE VQA. Case studies show MedRAX resolving conflicting tool outputs through systematic reasoning, supporting a hybrid generalist-reasoning-plus-specialist-tools paradigm for medical AI.

## Research Problem
- **Fragmented CXR AI landscape:** task-specific models (classification, segmentation, report generation) operate in isolation, hindering adoption in real clinical workflows.
- **Limits of end-to-end foundation models:** multimodal LLMs hallucinate, reason inconsistently, fail at systematic multi-step diagnostic evaluation of anatomical structures, and lack the transparency of purpose-built medical tools.
- **Evaluation gap:** existing medical VQA benchmarks focus on simple single-step reasoning, so complex agentic multi-step CXR reasoning could not be rigorously assessed.

## Proposed Solution
- **MedRAX:** an open-source, training-free agent framework where an LLM drives a ReAct loop that observes, thinks, and acts by calling specialized CXR tools, integrating their outputs into subsequent reasoning until a final answer is produced.
- **ChestAgentBench:** 2,500 six-choice questions generated with GPT-4o from 675 Eurorad cases, with automated quality verification, to benchmark complex multi-step CXR reasoning across 7 categories.
- **Deployment focus:** a Gradio interface with DICOM support, quantizable tools distributed across CPU/GPU, and local or cloud LLM options to address healthcare privacy requirements.

## Architecture
- **Four interconnected components** (Appendix A): (1) a core multimodal LLM reasoning engine (GPT-4o reference), (2) a specialized toolbox of pre-trained CXR models wrapped with name/description/input_schema/execution_logic interfaces, (3) a workflow orchestrator built on LangChain/LangGraph implementing nodes and conditional edges of a state machine, and (4) an agent memory storing the full structured message history.
- **ReAct loop (Algorithm 1):** Observe(Q, I, M) initializes state; iterative Reason → SelectTools → ExecuteParallel → memory update cycles run until a response can be generated, user input is required, or a timeout t_max triggers a timeout response.
- **Modularity:** tools are decoupled from agent instantiation; new tools require only a class definition, with the LLM learning usage from the tool description without any training.

## Memory
- **Short-term interaction memory:** LangChain-based buffer storing user inputs, LLM thoughts, tool calls, and tool results as structured messages, providing context for each reasoning cycle and multi-turn conversations.
- **Tool-output caching:** memory caches tool outputs to prevent redundant computation in multi-step analyses referencing the same intermediate results.
- **No long-term or longitudinal patient memory:** memory is session-scoped conversation state, not a persistent patient record across encounters.

## Planning
- **Implicit planning via ReAct:** the LLM decomposes complex queries into sequential analytical steps, deciding at each cycle whether to answer directly, ask the user for clarification, or invoke tools (single, sequential, or parallel).
- **Loop control:** conditional decision-making (RequiresUserInput / CanGenerateResponse) plus timeout management governs when the plan terminates.
- No explicit hierarchical planner or task-decomposition module beyond the iterative reasoning loop.

## Reasoning
- **ReAct-style iterative reasoning:** observation → thought → action cycles with explicit thought traces, producing transparent decision traces.
- **Critical tool evaluation:** the system prompt instructs the agent to "critically think about and criticize the tool outputs"; case studies show it resolving conflicting tool outputs (e.g., correctly identifying a chest tube despite LLaVA-Med suggesting a nasogastric tube).
- **Key finding:** explicit stepwise decomposition provides accuracy advantages that model scale alone cannot achieve; general-purpose VLMs (GPT-4o, Llama-3.2-90B) outperform specialized medical VLMs on complex reasoning.

## Tool Use
- **Core contribution:** structured JSON tool-calling over 7 tool categories — visual QA (CheXagent, LLaVA-Med), segmentation (MedSAM, ChestX-Det PSPNet), grounding (Maira-2), report generation (CheXpert Plus-trained SwinV2+BERT), classification (TorchXRayVision DenseNet-121, 18 pathologies), CXR generation (RoentGen), and utilities (DICOM processing, plotting).
- **Robustness:** argument validation against input schemas, tool-failure recovery via error messages fed back into the reasoning loop, parallel execution of independent tools.

## Multi-Agent
- Not a multi-agent system; MedRAX is deliberately a **single-agent tool-orchestration framework**, contrasted with MDAgents whose multi-agent coordination introduces significant computational overhead. The framework does allow multiple agents to share the same toolbox.

## RAG
- Not a core focus; MedRAX retrieves information via specialized vision tools rather than document/knowledge retrieval, and no retrieval-augmented generation over guidelines or literature is implemented.

## Healthcare Contribution
- First specialized agentic framework unifying fragmented CXR AI tools into a clinically deployable workflow with DICOM support and a production-ready interface.
- State-of-the-art CXR interpretation across four benchmarks (ChestAgentBench, CheXbench, MIMIC-CXR report generation, SLAKE VQA).
- ChestAgentBench contributes a large expert-case-derived benchmark (675 Eurorad cases; ER 19.7%, ICU 4.9% of cases) for complex clinical reasoning evaluation.
- Privacy-conscious deployment: local LLM support and Azure OpenAI with data-logging opt-out for MIMIC-CXR handling per PhysioNet recommendations.

## Trustworthy AI
- **Transparency:** ReAct thought/action/observation traces and interface display of intermediate tool outputs give clear decision traces.
- **Positioning:** explicitly framed as an AI co-pilot to augment, not replace, clinical expertise; the impact statement acknowledges bias, hallucination, and privacy risks and calls for robust validation before deployment.
- **Acknowledged gap:** the framework "lacks robust uncertainty quantification mechanisms" and can struggle to resolve contradictory tool outputs.

## Evaluation
- **ChestAgentBench (2,500 questions):** MedRAX 63.1% overall vs GPT-4o 56.4%, Llama-3.2-90B 57.9%, CheXagent 39.5%, LLaVA-Med 28.7%; best in all 7 categories.
- **CheXbench:** best overall (68.1%); Rad-Restruct 68.7%, SLAKE 82.9%; fine-grained image-text reasoning remains near random for all models.
- **MIMIC-CXR report generation (3,858 test images):** highest micro-averaged F1 (mF1-14 79.1%, mF1-5 64.9%) though lower macro-averaged F1 than M4CXR, indicating strength on prevalent conditions.
- **SLAKE VQA (114 CXR samples):** 90.35% accuracy, 91.23% recall, surpassing M4CXR and CheXagent.
- **Case studies:** two Eurorad cases demonstrate conflict resolution across tools and multi-step diagnosis (chest tube identification; left pneumothorax).

## Research Gap
- No uncertainty quantification or confidence calibration in the agent's outputs.
- Evaluation is retrospective benchmark/VQA-style on curated case reports, not prospective or longitudinal real patient monitoring.
- Optimal balance of tool reliance vs. LLM internal reasoning is unresolved; error propagation and spurious correlations from pretrained tools are unstudied.
- Comprehensive clinical validation for real-world utility remains outstanding.

## Key Contributions
- MedRAX, a training-free specialized agent framework dynamically orchestrating heterogeneous CXR tools within a ReAct loop.
- ChestAgentBench, a 2,500-question multi-step reasoning benchmark from 675 expert-curated Eurorad clinical cases.
- Empirical demonstration that structured tool orchestration outperforms both general-purpose and specialist end-to-end models, with transparent workflows.
- A production-ready, privacy-flexible interface enabling local or cloud deployment.

## Limitations
- Struggles to resolve contradictory tool outputs in fine-grained visual tasks (classification vs. segmentation conflicts).
- Computational overhead of running multiple specialized tools increases response time versus end-to-end models.
- Lacks robust uncertainty quantification mechanisms.
- Single-modality scope (chest X-rays); benchmark questions are GPT-4o-generated with automated (not fully manual) verification.

## Important Quotes
- "the first versatile AI agent that seamlessly integrates state-of-the-art CXR analysis tools" (Abstract)
- "The framework also lacks robust uncertainty quantification mechanisms." (Section 6, Limitations)

## Thesis Relevance
- Validates the thesis's core architectural bet: an **LLM-driven ReAct loop orchestrating specialized clinical tools** outperforms monolithic end-to-end models on complex medical reasoning — direct support for the thesis's reasoning layer design.
- Its **tool-wrapper pattern** (name/description/schema/execution) and LangGraph state-machine orchestration are directly reusable for the thesis's monitoring and decision-support agents over MIMIC-IV data.
- Confirms thesis gap (1): MedRAX is evaluated on curated case-report VQA (Eurorad, only 4.9% ICU cases), not longitudinal real ICU records — the thesis extends agentic evaluation to MIMIC-IV patient timelines.
- Its session-scoped short-term memory contrasts with the thesis's **persistent longitudinal patient memory**; MedRAX shows what tool-output caching achieves and where cross-encounter memory is missing.
- The explicitly acknowledged absence of uncertainty quantification and conflict-resolution guarantees motivates the thesis's **verification gate and audit trail** as first-class evaluated components.
- Its transparent thought/action/observation traces are a precursor to the thesis's audit-trail faithfulness evaluation, which MedRAX does not itself quantify.

## References
- Yao, S. et al. (2023). ReAct: Synergizing reasoning and acting in language models. (foundational reasoning-acting loop)
- Kim, Y. et al. (2024). MDAgents: An adaptive collaboration of LLMs for medical decision-making. NeurIPS 2024. (multi-agent medical reasoning baseline)
- Li, B. et al. (2024). MMedAgent: Learning to use medical tools with multi-modal agent. (tool-using medical agent requiring retraining)
- Jiang, Y. et al. (2025). MedAgentBench: Dataset for benchmarking LLMs as agents in medical applications. (interactive EHR agent benchmark)
- Chen, Z. et al. (2024). CheXagent: Towards a foundation model for chest X-ray interpretation. (specialist CXR foundation model and CheXbench)
