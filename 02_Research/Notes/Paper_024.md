# Paper 024

## Basic Information
- **Title:** DoctorAgent-RL: Real-World Doctor Agent with Proactive Consultation through Multi-Agent Reinforcement Learning
- **Authors:** Yichun Feng, Jiawei Wang, Lu Zhou, Yikai Zheng, Zhen Lei, Yixue Li
- **Year:** 2025
- **DOI:** 10.48550/arXiv.2505.19630
- **Venue:** arXiv preprint (accepted ICASSP 2026)
- **Publisher:** University of Chinese Academy of Sciences / Guangzhou National Laboratory (arXiv:2505.19630v4)
- **Link:** https://arxiv.org/abs/2505.19630

## Abstract Summary (200–300 words)
DoctorAgent-RL is a **multi-agent reinforcement learning framework** that reformulates clinical consultation as a dynamic decision-making process under uncertainty, modeled as a **Markov Decision Process (MDP)**. The authors argue that single-turn QA systems force patients to state all symptoms at once (yielding vague diagnoses) and that supervised multi-turn dialogue models merely imitate transcripts without genuine clinical reasoning. Their framework comprises three components: (1) a **Patient Agent** that generates pathologically consistent, realistic responses from a hidden medical profile, revealing symptoms turn-by-turn; (2) a **Doctor Agent** initialized by cloning real consultation records and refined via RL to master a strategic *questioning methodology*; and (3) a **Consultation Evaluator** providing multi-dimensional rewards for diagnostic accuracy, information-gathering efficiency, and question standardization. The doctor agent (built on Qwen2.5-7B-Instruct) is trained in two stages: supervised fine-tuning on 1,000 reasoning-augmented dialogues followed by reinforcement learning via Group Relative Policy Optimization (GRPO), with a dynamic turn-budget mechanism. To enable interactive training, the authors built **MTMedDialog**, the first English multi-turn medical consultation dataset supporting dynamic patient simulation (8,086 training / 2,082 test samples across eight disease categories). DoctorAgent-RL achieves a comprehensive average score of 53.9%, outperforming frontier (GPT-4o, DeepSeek-V3), open-source, and domain-specific models, and generalizes to unseen diseases and the HealthBench benchmark (22.3%, first among small open-source models). In prospective trials with 20 real patients across 15 disease types plus blinded human assessment, it reached a **70% exact diagnostic match rate** while preserving general-purpose conversational ability, supporting its use for initial screening and triage.

## Research Problem
- Single-turn systems require complete symptom descriptions up front, causing vague or risky diagnoses.
- Supervised multi-turn models superficially imitate dialogue and cannot **adapt questioning strategies** to real-time conversation state.
- Existing dynamic/multi-agent methods rely on prompt-level optimization and lack real-clinical validation.

## Proposed Solution
- A multi-agent RL framework where a doctor agent learns **proactive, strategic questioning** through interaction with a patient agent and a consultation evaluator, optimizing a questioning methodology rather than memorizing answers.

## Architecture
- Three interacting agents (Doctor, Patient, Consultation Evaluator) in a simulated consultation environment; MDP formulation; two-stage training (SFT then GRPO reinforcement learning) with a dynamic turn budget and a reference LLM for KL regularization.

## Memory
- No explicit persistent longitudinal memory module; state is the evolving multi-turn dialogue context. The patient agent holds a hidden comprehensive profile that it reveals progressively.

## Planning
- The doctor agent plans an information-gathering path across turns, dynamically adjusting which questions to ask based on rewards — effectively learned sequential planning of the consultation.

## Reasoning
- Uses reasoning distillation (structured `<think>` traces) during SFT; RL then teaches strategic, layered questioning. Diagnostic reasoning emerges as a transferable framework (validated on unseen diseases and HealthBench).

## Tool Use
- Not a focus; DoctorAgent-RL does not rely on external tool/API calls or calculators — its intelligence is in dialogue policy, not tool invocation.

## Multi-Agent
- Core focus: doctor agent, patient agent, and consultation evaluator collaborate in a reinforcement-learning loop; the patient agent (Qwen2.5-7B) simulates dynamic symptom disclosure.

## RAG
- Not used. The paper explicitly contrasts its approach with knowledge-graph/predefined-path systems; no retrieval corpus is integrated.

## Healthcare Contribution
- Demonstrates AI capable of **proactive, multi-turn clinical inquiry** validated with real patients (70% exact match), plus MTMedDialog, the first English dataset for dynamic, stateful patient simulation.

## Trustworthy AI
- Rigor via blinded human assessment, real-patient prospective trials, cross-dataset (HealthBench) generalization, ablations, and patient-agent fidelity analysis (information control, response completeness). Preserves general-purpose ability, avoiding over-tuning (contrasted with HuatuoGPT-o1). No formal audit/verification gate.

## Evaluation
- MTMedDialog scoring (LLM-judged 0–5 → 100-scale) plus average turns; DoctorAgent-RL scores 53.9% avg, best across all eight disease categories. Ablations: w/o RL −6.5%, w/o SFT −5.5%, w/o dynamic turn −1.2%. HealthBench 22.3%. Real-patient exact diagnostic match 70%.

## Research Gap
- Prior systems cannot optimize proactive inquiry under patient-led uncertainty or validate in real clinical settings. Remaining gaps: no external knowledge grounding/RAG, no persistent cross-visit memory, and focus on consultation dialogue rather than ICU monitoring or record actions.

## Key Contributions
- DoctorAgent-RL multi-agent RL framework modeling consultation as an MDP with strategic questioning.
- MTMedDialog, the first English dataset for dynamic multi-turn patient simulation.
- Two-stage SFT+GRPO training with dynamic turn budget; real-patient and blinded validation showing 70% exact match and preserved general capability.

## Limitations
- No external knowledge retrieval — diagnostic accuracy bounded by internal medical knowledge.
- Real-patient trial is small (20 patients); consultation-only scope, no medication/order actions or longitudinal record integration.
- Reward design and LLM-judge scoring introduce evaluation dependence on other models.

## Important Quotes
- "the core intelligence of the doctor agent no longer lies in knowing the answer, but rather in learning ... a questioning methodology" (Sec. 1).
- "achieved a 70% exact diagnostic match rate" with real patients (Abstract / Sec. 2.6).

## Thesis Relevance
- Provides a **proactive, uncertainty-aware questioning** paradigm the thesis can adopt for human-in-the-loop information gathering and triage.
- The **Consultation Evaluator** is a reward/critic pattern analogous to the thesis's verification gate — reusable idea for scoring agent outputs before action.
- Real-patient + blinded validation methodology strengthens the thesis's evaluation design beyond exam QA (supports gap 1).
- Differentiate on **gap (2)**: DoctorAgent-RL has no patient-timeline RAG or persistent memory — the thesis adds longitudinal grounding on MIMIC-IV.
- RL/GRPO with a dynamic turn budget offers an optimization lever if the thesis trains policies for monitoring cadence or escalation timing.
- Its preservation of general capability warns against over-tuning specialized clinical agents.

## References
- Shao et al., 2024 — DeepSeekMath / Group Relative Policy Optimization (GRPO) framework.
- Tu et al. (AMIE), 2024 — Diagnostic dialogue via self-play simulation.
- Li et al., 2024 — Agent Hospital: A Simulacrum of Hospital with Evolvable Medical Agents (arXiv:2405.02957).
- Chen et al., 2024 — HuatuoGPT-o1: Medical complex reasoning via verifiable question generation.
- HealthBench, 2025 — Standardized benchmark for medical AI systems.

