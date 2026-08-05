# Paper 039

## Basic Information
- **Title:** Revisiting the MIMIC-IV Benchmark: Experiments Using Language Models for Electronic Health Records
- **Authors:** Jesus Lovon-Melgarejo, Thouria Ben-Haddi, Jules Di Scala, Jose G. Moreno, Lynda Tamine
- **Year:** 2025
- **DOI:** 10.48550/arXiv.2504.20547
- **Venue:** arXiv:2504.20547v1 (cs.CL, 29 Apr 2025); CL4Health Workshop
- **Publisher:** arXiv (University of Toulouse, IRIT)
- **Link:** https://arxiv.org/abs/2504.20547

## Abstract Summary (200–300 words)
This paper addresses the lack of standardized text-based evaluation benchmarks for electronic health records by **revisiting the MIMIC-IV benchmark** and making it usable for modern language models. Two concrete contributions are made. First, the authors integrate the MIMIC-IV ICU cohort (built on the healthylaife MIMIC-IV-Data-Pipeline of Gupta et al., 2022) into the **Hugging Face datasets library**, providing a reproducible object that produces either tabular or textual patient representations while respecting MIMIC access policies. Second, they propose a **template-based data-to-text transformation** that converts six groups of structured ICU features — demographics (DEMO), diagnoses (COND), chart events/labs (CHART/LAB), medications (MEDS), procedures (PROC), and output events (OUTE) — into a natural-language document summarizing a patient's ICU entry. They evaluate on the **patient mortality classification** task using eight models: four tabular classifiers (Gradient Boosting, XGBoost, Random Forest, Logistic Regression) and six fine-tuned Transformers (DistilBERT, BERT, RoBERTa, BioClinicalBERT, BioBERT, BiomedNLP), plus two zero-shot LLMs (Llama-2 13b and its medical variant Meditron 7b). Findings: their standardized tabular pipeline slightly exceeds the original benchmark (Gradient Boosting AU-ROC 0.86 vs 0.85); fine-tuned text-based models are **competitive with strong tabular classifiers** (AU-ROC 0.87–0.88), with domain-specific models winning on AU-PRC; and an ablation shows the diagnosis (COND) feature alone drives most performance. In contrast, **zero-shot LLMs struggle** (Llama-2 AU-ROC ~0.50, Meditron ~0.61), are highly prompt-sensitive (prompt P2 left 69% of Llama-2 questions unanswered), and fail to encode EHR representations for the downstream task. The work underlines the promise of text-based EHR modeling and the current limits of zero-shot LLMs on structured clinical data.

## Research Problem
- No standardized, easily shareable text-input benchmark for EHRs blocks adoption of NLP/LLMs for health prediction tasks.
- Existing EHR Transformers (TransformEHR, BEHRT, Med-BERT) require costly bespoke pre-training on tabular data and don't leverage advances in general LLMs or free benchmarks like MIMIC-IV.
- It is unclear how to effectively convert structured EHR data into linguistic form that LLMs can exploit for non-linguistic downstream tasks.

## Proposed Solution
- A Hugging Face `datasets` object that reproducibly generates MIMIC-IV cohorts in both tabular and template-based text formats.
- A six-feature-group, template-based data-to-text conversion producing per-patient ICU summary documents.
- A comprehensive benchmark on patient mortality classification across tabular classifiers, fine-tuned Transformers, and zero-shot LLMs.

## Architecture
- Not a novel model architecture; it standardizes a data pipeline and evaluates off-the-shelf models. The pipeline (Figure 1) transforms MIMIC-IV raw data into a mortality cohort, then into either a tabular vector or a templated text document, feeding classical ML, fine-tuned encoder Transformers, or zero-shot decoder LLMs.

## Memory
- Not a core focus; no persistent or longitudinal memory. Temporal features (CHART/LAB, MEDS over time intervals) are collapsed via reduction/expansion strategies (sampling vs. averaging across time windows), with two aggregation configurations (Representation 1: 2766 features; Representation 2: 1110 features).

## Planning
- Not a core focus; no agentic planning. The only procedural choices are preprocessing/aggregation strategy and prompt selection.

## Reasoning
- Not a core focus; the zero-shot LLM setup elicits a single binary yes/no mortality/survival judgment (output limited to 2 tokens), with no chain-of-thought or multi-step reasoning. Prompt sensitivity is analyzed but reasoning quality is not.

## Tool Use
- Not a core focus; no tool orchestration. Implementation uses Scikit-learn and Hugging Face libraries as engineering tools only.

## Multi-Agent
- Not a core focus; single-model evaluations throughout.

## RAG
- Not a core focus; no retrieval augmentation. The template-based data-to-text step is the only mechanism for injecting structured patient information into the text models.

## Healthcare Contribution
- A reusable, reproducible MIMIC-IV text benchmark lowering the barrier to text-based EHR modeling for the community.
- Empirical evidence that fine-tuned clinical/general Transformers on templated EHR text match strong tabular baselines on ICU mortality (AU-ROC ~0.88).
- An ablation identifying diagnosis codes (COND) as the dominant predictive signal, with labs/chart events (CHART/LAB) as reliable no-expert features.

## Trustworthy AI
- Not a central focus, though reproducibility and standardized benchmarking are trust-adjacent contributions. The zero-shot **unanswered-question analysis** (Table 5) surfaces reliability concerns: Llama-2 failed to emit a valid answer for up to 69% of cases under prompt P2, an implicit abstention/robustness signal.

## Evaluation
- **Tabular (Table 3):** Gradient Boosting AU-ROC 0.86/AU-PRC 0.53 (Representation 1), exceeding Gupta et al. (0.85/0.48); Representation 2 matches with far fewer features.
- **Fine-tuned text (Table 4):** RoBERTa/BioBERT/BiomedNLP AU-ROC 0.88; medical-domain models lead on AU-PRC (up to 0.47).
- **Zero-shot LLMs (Table 4):** Llama-2 (13b) AU-ROC 0.50; Meditron (7b) 0.61 with prompt P1; strong prompt sensitivity; Meditron more stable across prompts.
- **Ablation (Table 6):** COND alone ≈ top AU-ROC; MEDS/PROC/OUTE add little; best performance reached before using all features.

## Research Gap
- Zero-shot LLMs cannot effectively encode/transfer EHR representations to downstream tasks; better structured-to-text translation is needed.
- Input truncation (512 tokens fine-tuned) drops MEDS/PROC/OUTE information; richer templates are needed to capture time-series features.
- Alternatives such as in-context learning and prompt-tuning are suggested but untested here.

## Key Contributions
- A Hugging Face-integrated, reproducible MIMIC-IV benchmark supporting tabular and text formats.
- A six-group template-based EHR-to-text transformation.
- A comprehensive eight-model comparison on ICU mortality showing text models are competitive but zero-shot LLMs are not.
- An ablation quantifying per-feature-group contributions.

## Limitations
- Single downstream task (in-ICU mortality) and single dataset (MIMIC-IV); generalization untested.
- Token truncation removes relevant features; templates are simple and don't fully encode temporal dynamics.
- Only two zero-shot LLMs and a limited prompt set explored; no in-context learning or fine-tuned generative LLMs.
- Default "No" answer for unanswered LLM questions may bias reported metrics.

## Important Quotes
- "fine-tuned text-based models are competitive against robust tabular classifiers" (Abstract)
- "SOTA LLMs struggle to encode and transfer EHR representations to downstream tasks" (Section 4.3)

## Thesis Relevance
- Directly grounds the thesis's **MIMIC-IV ICU evaluation**: this paper provides a reproducible Hugging Face benchmark and a mortality cohort the thesis can adopt as a baseline harness.
- The template-based **structured-EHR-to-text transformation** (six feature groups) is a concrete, reusable recipe for feeding MIMIC-IV data into the thesis's LLM agents.
- Its key negative result — zero-shot LLMs fail on EHR representation (AU-ROC ~0.50) — motivates the thesis's agentic scaffolding (RAG over the patient timeline, reasoning, memory) rather than naive zero-shot prompting; the thesis differs by adding these layers.
- The prompt-sensitivity and high unanswered-rate findings argue for the thesis's verification gate and robust prompting/abstention handling.
- The ablation (COND dominates; time-series features underused due to truncation) tells the thesis where longitudinal temporal modeling and better feature templating add value over this baseline.
- Establishes strong tabular baselines (AU-ROC ~0.86) the thesis must beat or match while adding interpretability and monitoring.

## References
- Johnson, A. E. W. et al. (2023). MIMIC-IV, a freely accessible electronic health record dataset. Scientific Data. (core dataset)
- Gupta, M. et al. (2022). An extensive data processing pipeline for MIMIC-IV. ML4H / PMLR. (preprocessing pipeline and original benchmark)
- Chen, Z. et al. (2023). Meditron-70b: scaling medical pretraining for large language models. (medical LLM evaluated)
- Alsentzer, E. et al. (2019). Publicly available clinical BERT embeddings (ClinicalBERT). (clinical encoder used)
- Van Veen, D. et al. (2023). Clinical text summarization: adapting LLMs can outperform human experts. (EHR-to-text motivation)
