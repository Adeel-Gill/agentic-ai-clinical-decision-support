# Paper 047

## Basic Information
- **Title:** Traj-CoA: Patient Trajectory Modeling via Chain-of-Agents for Lung Cancer Risk Prediction
- **Authors:** Sihang Zeng, Yujuan Fu, Sitong Zhou, Zixuan Yu, Lucas Jing Liu, Jun Wen, et al.
- **Year:** 2025
- **DOI:** 10.48550/arXiv.2510.10454
- **Venue:** NeurIPS 2025 Workshop — The Second Workshop on GenAI for Health: Potential, Trust, and Policy Compliance; arXiv:2510.10454
- **Publisher:** arXiv / NeurIPS Workshop
- **Link:** https://arxiv.org/abs/2510.10454

## Abstract Summary (200–300 words)
Traj-CoA tackles **patient trajectory modeling** over longitudinal EHRs that are both extremely long (75th-percentile inputs reach 120k tokens) and noisy (inconsistent formats, copy-forwarded content, irregular sampling), conditions under which single LLMs suffer the **lost-in-the-middle** failure and RAG offers only an incomplete solution. The framework converts a patient's multimodal five-year history (notes, diagnoses, labs, medications, vitals) into a unified, chronologically nested **XML representation**, then applies **time-aware chunking** that splits the record by timestamp into temporally coherent chunks of at most 8k tokens. A **chain of worker agents** processes chunks sequentially: each worker receives the current chunk, the previous worker's evolving summary, and recent memory entries, extracts salient task-related events, and passes an updated summary down the chain. Because sequential summarization progressively abstracts away early but critical events, Traj-CoA adds **EHRMem**, a shared long-term memory module in which workers deposit deduplicated, timestamped clinical events, building a distilled timeline of the record. A final **manager agent** synthesizes the last worker summary together with the full EHRMem timeline to output a 1-10 lung cancer risk score with reasoning. In a zero-shot one-year lung cancer risk prediction task on a proprietary case-control dataset (300-instance test set, 28 cases), Traj-CoA with MedGemma-27B achieves AUROC 0.766 and F1 0.380, beating machine learning (XGBoost 0.763), deep learning (RETAIN, PatientTM), fine-tuned Clinical ModernBERT, vanilla long-context prompting, and RAG baselines; ablating EHRMem drops AUROC by 1.8%. Analyses show performance scales positively with context up to 160k tokens, salient events span all seven clinical categories and the full time horizon, and identified themes (COPD, smoking, nodules, anemia) align with established clinical risk knowledge.

## Research Problem
- LLMs fail at **temporal reasoning over very long (32k-128k+ token), noisy longitudinal EHRs**; longer context windows alone degrade performance (vanilla 64k worse than 32k).
- Existing remedies (temporal instruction tuning, e.g., TIMER) were confined to short or ICU records (<16k tokens); RAG risks losing informative events scattered through the history.
- Agent-based long-context methods had been applied to medical QA but not to **predictive patient trajectory modeling**.

## Proposed Solution
- **Traj-CoA**: unified XML input + time-aware chunking + chain-of-agents sequential processing + **EHRMem** long-term memory + manager-agent synthesis, all zero-shot (no task-specific training or feature engineering).
- Worker agents extract salient signals per chunk while removing localized noise; EHRMem preserves a deduplicated, timestamped global event timeline; the manager conditions its risk prediction on both the final summary and the entire memory.

## Architecture
- Two-stage chain-of-agents (adapted from Zhang et al.'s CoA): stage one, workers W_i sequentially compute S_i = W_i(I_W, S_{i-1}, c_i, M[-k:]) and append events E_i to memory M; stage two, manager O = M(I_M, S_C, M).
- Default configuration: MedGemma-27B base model, 8k-token chunks, up to 15 chunks (120k-token context); chunking preserves timestamp completeness by splitting on timestamps rather than fixed sizes.

## Memory
- Core focus: **EHRMem** is a structured, append-only long-term memory of timestamped task-relevant clinical events with prompt-based **deduplication** against copy-forwarding; it counteracts catastrophic forgetting in the summary chain and gives the manager a distilled global clinical timeline — the ablation shows it contributes 1.8% AUROC and 8.1% F1.

## Planning
- Not a core focus; the agent chain follows a fixed sequential workflow with task-specific instructions rather than dynamic planning.

## Reasoning
- Sequential **temporal reasoning**: each worker analyzes temporal patterns of the current chunk relative to the aggregated summary; the manager performs global synthesis, weighing recent events more heavily without discarding early history (verified by the temporal distribution of salient events in memory and output).

## Tool Use
- Not a core focus; no external tools are called — the authors list access to external knowledge/tools as future work.

## Multi-Agent
- Core focus: a **chain of worker agents plus a manager agent** communicating through summaries and shared memory; positioned explicitly as a multi-agent system for temporal reasoning, in contrast to prior biomedical MAS used for QA, diagnostics, or trial optimization.

## RAG
- Used as a baseline (bge-m3 retriever over time-aware chunks, top-32): RAG reaches AUROC 0.753 but with poor precision (0.221), and the paper argues retrieval risks information loss versus full-context sequential processing — a latency/completeness trade-off.

## Healthcare Contribution
- Zero-shot **one-year lung cancer risk prediction** from five years of real multimodal EHR data, outperforming supervised ML/DL/BERT baselines without any training data.
- Clinically aligned interpretability: identified salient events cluster into themes recognized by screening guidelines (smoking, COPD, nodules, anemia, inflammatory markers, weight loss).
- Framework is task-agnostic in design, promising a general approach for longitudinal EHR prediction.

## Trustworthy AI
- Partially addressed: interpretability analyses (t-SNE, TopicGPT-style categorization, temporal distributions) validate that reasoning is clinically meaningful, and the discussion concedes further design and validation are needed to make Traj-CoA "more trustworthy" — but there is no output verification, no faithfulness measurement of the extracted events, and no human-in-the-loop mechanism.

## Evaluation
- Proprietary case-control dataset anchored to chest-related radiology exams, cases registry-cross-validated, 1:10 matched; test set 300 instances (28 cases / 272 controls); XML token IQR 28k-121k for cases.
- Traj-CoA: AUROC 0.766 ± 0.019, F1 0.380 ± 0.018 over 5 seeds — best AUROC among all models including supervised baselines; ablation w/o EHRMem: 0.748/0.299.
- Sensitivity: performance peaks at 8k chunk size (small chunks cause catastrophic forgetting, large chunks lost-in-the-middle); AUROC improves monotonically as context extends 40k → 160k, unlike vanilla prompting which degrades at 64k.
- Behavior analyses (Q3-Q5): events span all seven categories, cover the full horizon with clinically sensible recency concentration, and form clinically valid themes.

## Research Gap
- Open question addressed: robust temporal reasoning on 32k-128k+ token EHRs **without further training**; prior MAS work had not tackled temporal reasoning for longitudinal prediction.
- Remaining gaps the paper flags: no external knowledge access, single-institution single-task validation, prompt dependence, and unexplained mechanism of event synthesis across subpopulations.

## Key Contributions
- First chain-of-agents framework for **temporal reasoning over long and noisy EHRs** in a predictive (not QA) setting.
- **EHRMem** long-term memory design with inclusive extraction heuristic and deduplication, empirically shown to prevent forgetting of early events.
- Zero-shot performance exceeding supervised ML/DL/BERT and vanilla/RAG LLM baselines; positive context scaling to 160k tokens.
- Clinically aligned interpretability analysis of what the system attends to across time.

## Limitations
- Small, single-institution test set (28 positive cases) and a single prediction task; broader validation pending.
- Higher encoding complexity than RAG (O(L·L_C)); sequential chain adds latency.
- Requires carefully crafted task-specific prompts; no external knowledge grounding.
- Explains what events are salient but not how they are synthesized into predictions; no fairness/subpopulation analysis.

## Important Quotes
- "distilling critical events into a shared long-term memory module, EHRMem" (Abstract, p. 1)
- "further design and validation are needed to make it more trustworthy" (Sec. 6, p. 9)

## Thesis Relevance
- Its **EHRMem** — a persistent, timestamped, deduplicated event timeline — is the closest architectural cousin of the thesis's longitudinal patient memory; the thesis borrows the principle that an explicit timeline must survive summarization.
- Validates the thesis's premise that temporal structure (time-aware chunking, timestamp preservation) is what makes long-record reasoning work, and that naive long-context or vanilla RAG both fail.
- Key difference: Traj-CoA **compresses the record sequentially** into summaries + memory for a single risk score; the thesis instead performs **timestamp-aware retrieval** from the stored timeline on demand for each recommendation.
- Traj-CoA performs **no recommendation-level verification** — extracted events and risk scores are never checked against source EHR evidence — whereas the thesis gates every recommendation through evidence verification.
- It produces **no audit trail**; interpretability is post-hoc population-level analysis, not per-decision measured evidence chains as in the thesis.
- Task scope differs: binary risk prediction versus the thesis's clinical decision-support recommendations with human-in-the-loop validation on MIMIC-IV ICU data.

## References
- Zhang, Y., Sun, R., Chen, Y., Pfister, T., Zhang, R., Arik, S. Ö. "Chain of agents: Large language models collaborating on long-context tasks." NeurIPS 37 (2024).
- Cui, H. et al. "TIMER: Temporal instruction modeling and evaluation for longitudinal clinical records." arXiv:2503.04176 (2025).
- Liu, N. F. et al. "Lost in the middle: How language models use long contexts." arXiv:2307.03172 (2023).
- Li, R. et al. "CARE-AD: a multi-agent large language model framework for Alzheimer's disease prediction using longitudinal clinical notes." npj Digital Medicine 8:541 (2025).
- Wornow, M. et al. "Context clues: Evaluating long context models for clinical prediction tasks on EHRs." (2025).
