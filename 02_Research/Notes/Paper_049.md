# Paper 049

## Basic Information
- **Title:** TIMER: Temporal Instruction Modeling and Evaluation for Longitudinal Clinical Records
- **Authors:** Hejie Cui, Alyssa Unell, Bowen Chen, Jason Alan Fries, Emily Alsentzer, Sanmi Koyejo, Nigam H. Shah
- **Year:** 2025
- **DOI:** 10.1038/s41746-025-01965-9
- **Venue:** npj Digital Medicine (2025) 8:577, Article
- **Publisher:** Nature Portfolio (Springer Nature)
- **Link:** https://www.nature.com/articles/s41746-025-01965-9

## Abstract Summary (200–300 words)
TIMER addresses the finding that even long-context LLMs struggle to **reason across patient timelines** in multi-visit EHRs. The method improves temporal reasoning via **time-aware instruction tuning**: instruction-response pairs are generated (Gemini-1.5-Pro) directly from de-identified longitudinal records in the Stanford STARR repository (OMOP-CDM, 1990-2023), with each pair **linked to specific timestamps** so responses must justify claims with dated evidence (e.g., chemotherapy started 01/2020, EGFR mutation found 05/2020). The authors first expose **temporal biases in existing resources**: MedAlign, though spanning a median 3,895 days, places 55.3% of its clinician-written questions in the final 25% of timelines (recency bias), while model-generated instructions cluster at timeline edges (25.9% early, 52.1% late) — a lost-in-the-middle pattern. TIMER therefore introduces a **normalized temporal position metric** and controlled sampling to build tuning sets with Recent-Events, Timeline-Extremes, or Full-Timeline distributions, plus **TIMER-Eval**, a model-generated benchmark filtered to require synthesis across at least two timestamped evidence snippets and validated by three clinicians (mean 95/100 relevance, 98/100 accuracy). Instruction-tuning Llama-3.1-8B-Instruct and Qwen-2.5-7B-Instruct with 5,000 TIMER pairs improves MedAlign correctness (30.69% → 34.32% for Llama) and TIMER-Eval correctness (45.02% → 48.51%), outperforms conventional medical QA tuning (MedInstruct) by 6.3-8.45% in head-to-head wins, and beats all seven medical baselines including MedLM-Medium. **Distribution-matched training** yields up to +6.5% advantages, largest for uniformly distributed evaluation. An LLM-judge (GPT-4o-mini) is validated against clinician rankings (Spearman |rho| up to 0.97). Case studies show tuned models gain temporal boundary adherence, trend detection, and chronological precision. The paper concludes that mere medical content exposure is insufficient — models must learn to integrate information across time.

## Research Problem
- LLMs process very long contexts but fail at **temporal reasoning over longitudinal, multi-visit EHRs** — integrating temporally dispersed evidence and maintaining chronological consistency.
- Existing clinical instruction datasets are temporally deficient: exam-style QA is idealized; MIMIC-Instr covers single visits (median 7.2 days); MedAlign is >70% simple retrieval and heavily **recency-biased** (55.3% of questions in the final 25% of timelines).
- Evaluation sets inherit these biases, so models' longitudinal-synthesis capability was never properly measured.

## Proposed Solution
- **TIMER**: generate **timestamp-linked instruction-response pairs** from real longitudinal EHRs, requiring responses to cite specific dates, and instruction-tune base LLMs on them (LoRA, 6 epochs, 5,000 pairs, 16k context).
- Controlled **temporal distribution sampling** (Recent-Events / Timeline-Extremes / Full-Timeline) to study and correct distributional bias in both tuning and evaluation.
- **TIMER-Eval**: a clinician-validated, model-generated evaluation schema with explicit time-evidence attribution, filtered to demand multi-timepoint synthesis.

## Architecture
- Not an agent architecture: a data-generation + fine-tuning + evaluation pipeline (EHR chunking into 16k-token segments, Gemini-1.5-Pro pair generation, two-stage automatic/manual quality filtering, LoRA instruction tuning of Llama-3.1-8B / Qwen-2.5-7B).

## Memory
- Not a core focus; temporal grounding is baked into model weights via tuning rather than an external longitudinal memory — the record itself is provided in-context at inference.

## Planning
- Not a core focus; no planning components — the contribution is training-data methodology.

## Reasoning
- Central: defines and improves three measurable facets of **longitudinal temporal reasoning** — temporal boundary adherence (limiting analysis to a specified window), trend detection over serial measurements, and chronological precision (correct dating/ordering of events).

## Tool Use
- Not a core focus; no tool calling — models answer directly over the provided record.

## Multi-Agent
- Not a core focus; single-model instruction tuning and single-judge evaluation.

## RAG
- Not a core focus; no retrieval component (records are truncated to fit context for baselines) — though the temporal-bias findings directly motivate timestamp-aware retrieval designs.

## Healthcare Contribution
- First systematic method for **temporally grounded clinical instruction tuning** on real longitudinal EHRs (STARR, OMOP-CDM), released open-source so any institution with EHR access can regenerate tuning/eval data.
- Quantifies previously unrecognized **temporal biases** in flagship clinical benchmarks (MedAlign recency bias; edge-focus of model-generated questions).
- Demonstrates that conventional medical instruction tuning can even degrade base-model performance, while temporal grounding consistently helps — relevant to disease trajectory modeling, treatment-response monitoring, and chart review.

## Trustworthy AI
- Validation discipline: three clinicians rate TIMER-Eval samples (relevance 95/100, accuracy 98/100, complexity 80/100, strong inter-rater agreement); the LLM-judge is validated against human rankings (Spearman |rho| = 0.97 average).
- Explicitly flags unassessed **fairness across demographic subgroups**, calibration, and the risk that model-generated data encodes training biases — but offers no output verification or audit mechanism.

## Evaluation
- Benchmarks: MedAlign (clinician-curated) and TIMER-Eval; metrics: LLM-judge correctness/completeness (bootstrap n=10,000) plus BERTScore/ROUGE-L/CHRF/METEOR.
- TIMER-tuned Llama-3.1-8B: MedAlign correctness 34.32% (vs. 30.69% base, 29.70% MedInstruct); TIMER-Eval correctness 48.51%; completeness +6.27 points over base; consistent gains replicated on Qwen-2.5-7B.
- Head-to-head: +23.8% win margin over base on MedAlign; +39.5% over MedLM-Medium; +6.3%/+8.45% over MedInstruct.
- Distribution-matching experiments: matched training beats mismatched by +1.2% to +6.5%, largest for uniformly distributed questions (Full-Timeline vs. Recent-Events training).

## Research Gap
- Fills: absence of temporally grounded instruction data and temporally controlled evaluation for longitudinal EHRs.
- Leaves open: fairness/calibration analysis, multimodal expansion (labs, imaging), scalable verification of model-generated data, frontier-model coverage, and deployment-task integration.

## Key Contributions
- **Timestamp-linked instruction tuning** method yielding consistent temporal-reasoning gains (up to 6.6% completeness) across two base architectures.
- Discovery and quantification of **recency/edge biases** in existing clinical instruction datasets via a normalized temporal position metric.
- **TIMER-Eval** with controlled temporal distributions and clinician validation; evidence that train/eval **distribution matching** matters (up to +6.5%).
- Validated LLM-judge protocol and open-source release.

## Limitations
- Instruction and evaluation data are model-generated (Gemini-1.5-Pro); may not capture physician reasoning, and only a subset was clinician-screened.
- Single-institution data source (Stanford STARR); frontier and larger medical models (Me-LLaMA, Meditron-70B) not tuned/evaluated.
- No fairness, subgroup, or calibration analysis; text-only modality.
- Tuning improves in-context reasoning but does not verify outputs — hallucinated temporal claims are penalized only statistically by the judge.

## Important Quotes
- "LLMs struggle to reason across patient timelines" (Abstract, p. 1)
- "55.3% of its instructions reference only the final 25% of patient timelines" (Results, p. 3)

## Thesis Relevance
- Provides the strongest published evidence for the thesis's core design choice: temporal grounding must be **explicit and timestamp-linked** — the thesis borrows TIMER's normalized temporal position analysis to show its retrieval covers the whole timeline, not just recent events.
- TIMER's recency-bias findings directly justify the thesis's **timestamp-aware retrieval** from the patient's own timeline: evaluation and generation that ignore temporal distribution silently overweight recent data.
- The thesis borrows its evaluation apparatus: clinician-validated LLM-judge (Spearman-validated), correctness/completeness dimensions, and controlled temporal sampling for building MIMIC-IV test questions.
- Key difference: TIMER bakes temporal skill into **model weights** (record compressed/truncated into context, knowledge parametric), whereas the thesis keeps the record external and retrieves dated evidence per recommendation — updatable and inspectable.
- TIMER has **no recommendation verification and no audit trail**: temporal fidelity is encouraged by training and measured in aggregate, never enforced or traced per output — the thesis's verification gate and measured audit-trail faithfulness address exactly this.
- Task scope differs: instruction-following QA over records versus the thesis's monitoring + decision-support recommendations with human-in-the-loop validation.

## References
- Fleming, S. L. et al. "MedAlign: A clinician-generated dataset for instruction following with electronic medical records." AAAI 2024, 22021-22030.
- Wu, Z. et al. "Instruction tuning large language models to understand electronic health records." NeurIPS Datasets and Benchmarks Track (2024).
- Wornow, M. et al. "Context Clues: Evaluating long context models for clinical prediction tasks on EHR data." ICLR 2025.
- Hager, P. et al. "Evaluating and mitigating limitations of large language models in clinical decision making." Nature Medicine 30:2613-2622 (2024).
- Singhal, K. et al. "Large language models encode clinical knowledge." Nature 620:172-180 (2023).
