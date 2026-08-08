# Paper 046

## Basic Information
- **Title:** CliCARE: Grounding Large Language Models in Clinical Guidelines for Decision Support over Longitudinal Cancer Electronic Health Records
- **Authors:** Dongchen Li, Jitao Liang, Wei Li, Xiaoyu Wang, Longbing Cao, Kun Yu
- **Year:** 2026
- **DOI:** 10.1609/aaai.v40i37.40421
- **Venue:** Proceedings of the AAAI Conference on Artificial Intelligence, 40(37):31554-31562 (AAAI 2026); arXiv:2507.22533
- **Publisher:** Association for the Advancement of Artificial Intelligence (AAAI)
- **Link:** https://arxiv.org/abs/2507.22533

## Abstract Summary (200–300 words)
CliCARE targets clinical decision support over **longitudinal cancer EHRs**, where a single patient's record can span decades and exceed 20,000 tokens. The authors identify three barriers to LLM deployment: **long-context failure** in temporal reasoning over fragmented multi-year records, **clinical hallucination** that standard RAG cannot prevent because retrieved text fragments miss process-oriented guideline logic, and **unreliable evaluation** since lexical metrics like ROUGE cannot assess clinical validity. CliCARE addresses these with a three-stage pipeline. First, **EHR-to-TKG transformation** converts raw records into patient-specific **Temporal Knowledge Graphs**: a clinical-text Longformer extractively summarizes historical notes, BERT-based information extraction identifies discrete clinical events (diagnoses, staging, regimens, biomarker trends), and entity linking maps them to a standardized biomedical KG with hierarchical timestamp granularity. Second, **Trajectory-Guideline Alignment** matches the patient's temporal trajectory against normative paths enumerated from a **guideline knowledge graph** built from clinical practice guidelines, using BERT cosine-similarity path matching, zero-shot **LLM-based reranking** for clinical plausibility, and bootstrapping-style **alignment expansion**; the fused, evidence-grounded representation conditions the LLM to generate a clinical summary and an actionable recommendation. Third, an **Expert-Validated LLM-as-a-Judge** protocol scores outputs on Factual Accuracy, Completeness, Clinical Soundness, and Actionability using an ensemble of three judge LLMs, achieving Spearman correlation of about 0.7 with three oncologists. Evaluated on a private Chinese CancerEHR dataset (2,000 patients) and a cancer-filtered **MIMIC-IV** cohort, CliCARE significantly outperforms standard RAG, BriefContext, MedRAG, KG2RAG, and GNN-RAG across small open-source and frontier models (e.g., 4.976/4.965 summary/recommendation scores with Gemini 2.5 Pro vs. 2.735/2.818 for standard RAG), with ablations confirming each component's contribution on complex records.

## Research Problem
- LLMs cannot perform reliable **temporal reasoning** over multi-year, fragmented, sometimes multilingual cancer EHRs exceeding 20,000 tokens (lost-in-the-middle, degradation).
- Standard RAG retrieves **isolated text fragments** that miss sequential dependencies in patient trajectories and fail to incorporate **process-oriented clinical guidelines**, leaving an unacceptable clinical hallucination risk.
- Conventional automated metrics (ROUGE/BLEU) are untrustworthy for open-ended clinical generation, blocking reliable validation and clinical trust; LLM judges carry positional/verbosity biases.

## Proposed Solution
- **CliCARE**, an end-to-end framework: (1) structure raw longitudinal EHRs into patient-centric **Temporal Knowledge Graphs**; (2) align patient trajectories with a normative **guideline KG** (similarity matching, LLM reranking, bootstrapped expansion, fusion); (3) generate a grounded **clinical summary** plus **clinical recommendation**.
- Dual deployment paths: the aligned representation supplies **fine-tuning data for a distilled specialist LLM** (privacy-friendly local deployment) and rich context for large generalist models.
- A reliability layer: **Expert-Validated LLM-as-a-Judge** with a three-model ensemble, randomized presentation order, and validation against oncologists.

## Architecture
- Pipeline architecture: Longformer-based extractive compression of historical notes + latest note, BERT event extraction, entity linking to a static biomedical KG, TKG instantiation with hierarchical timestamps (precise timestamps for encounters, relative relations within encounters).
- Guideline side: static normative KG (Cancer, ClinicalSituation, Treatment nodes) from authoritative CPGs; all normative treatment workflows enumerated as candidate paths.
- Alignment engine: global path-level BERT cosine matching (Eq. 3), top-N zero-shot LLM reranking as a "Clinical Reasoner," and consistency-maximizing alignment expansion (Eq. 5) before fusion into the generation context.

## Memory
- Patient history is persisted as a **patient-specific TKG** — a structured longitudinal representation capturing long-range dependencies — but it is a one-shot compression pipeline, not an agentic read/write memory store queried at inference time.

## Planning
- Not a core focus; the workflow is a fixed pipeline rather than agentic planning, though guideline paths encode normative multi-step treatment plans that the system aligns against.

## Reasoning
- Temporal reasoning is externalized into the TKG structure; an LLM performs zero-shot **clinical-plausibility reranking** of candidate trajectory-guideline alignments, and the final generalist/specialist LLM reasons over the fused evidence to produce summary and recommendation.

## Tool Use
- Not a core focus; the framework composes fixed components (Longformer, BERT, entity linker, retriever, LLM) rather than giving an agent dynamic tool-calling ability.

## Multi-Agent
- Not a core focus; a single generation model is used (the paper cites multi-agent systems like ColaCare as related work raising the bar for EHR modeling).

## RAG
- Core focus: positions itself against Standard RAG and **KG-enhanced RAG** (MedRAG, KG2RAG, GNN-RAG, BriefContext), arguing fragment retrieval lacks temporal awareness; replaces retrieval of snippets with **TKG-based compression plus guideline-KG alignment** as a deeper grounding mechanism.

## Healthcare Contribution
- Automates the oncologist workflow of synthesizing multi-year history into a **Clinical Summary** and prospective **Clinical Recommendation**, targeting clinician burnout from fragmented records.
- Validated on real longitudinal data: private CancerEHR (2,000 patients, Liaoning Cancer Hospital, records up to two decades) and cancer-filtered **MIMIC-IV** (MIMIC-Cancer), demonstrating cross-language/cross-structure generalizability.
- Shows even frontier models (GPT-4.1, Gemini 2.5 Pro, DeepSeek-R1) gain substantially (+1.8 to +2.3 judge points on complex records) from structured longitudinal grounding.

## Trustworthy AI
- Hallucination mitigation by **grounding recommendations in guideline knowledge** aligned to the patient's actual trajectory.
- Bias-mitigated evaluation: three-judge ensemble, shuffled ordering, and expert validation (Spearman ρ ≈ 0.7 vs. three oncologists) to make automated judgment trustworthy.
- Addresses the privacy/cost deployment dilemma via distilled local specialist models; however, no per-recommendation verification gate or audit trail is produced.

## Evaluation
- Tasks: retrospective Clinical Summary (TCS) and prospective Clinical Recommendation (TCR), scored 1-5 on a four-dimension rubric co-designed with senior oncologists.
- CliCARE beats all baselines on CancerEHR and MIMIC-Cancer for both Qwen-3-8B and Gemini 2.5 Pro (e.g., 3.173/3.215 vs. 1.485/1.527 StandardRAG for Qwen on CancerEHR).
- Ablations: removing alignment expansion, LLM reranking, or TKG compression degrades complex-record performance; compression can hurt on shorter MIMIC-Cancer records.
- Length-stratified analysis: with CliCARE, Gemini 2.5 Pro scores highest on the longest records, showing effective organization of extensive histories.

## Research Gap
- Prior work treats long-context processing, knowledge grounding, and reliable evaluation as **separate problems**; no unified pipeline addresses all three for real-world longitudinal EHRs.
- Standard and KG-enhanced RAG lack **temporal awareness** and cannot bridge to process-oriented guidelines.

## Key Contributions
- End-to-end framework transforming unstructured longitudinal EHRs into **TKGs aligned with clinical guideline KGs** for grounded summary + recommendation generation.
- Training-free **trajectory-guideline alignment** (semantic matching, LLM reranking, bootstrapped expansion).
- **Expert-validated LLM-as-a-Judge** methodology correlating strongly with oncologists.
- Extensive experiments and ablations on CancerEHR and MIMIC-IV showing significant gains over long-context and KG-RAG baselines.

## Limitations
- One case of minor performance degradation observed; aggressive TKG compression is counterproductive on shorter records.
- Primary dataset is private and Chinese-language, limiting reproducibility; MIMIC-Cancer is the only public testbed.
- Recommendation quality is judged holistically (1-5 rubric) — no per-claim verification against patient evidence, no audit-trail artifact, and no prospective clinical validation.
- Domain-specific to oncology; the authors flag generalization to other clinical domains as future work.

## Important Quotes
- "the unacceptable risk of clinical hallucination, which undermines the potential for reliable decision support" (Sec. 1, p. 2)
- "The retrieval of fragmented text fails to capture the sequential dependencies" (Sec. 1, p. 2)

## Thesis Relevance
- Closest prior work coupling a **longitudinal record to decision-support outputs** (summary + recommendation) on MIMIC-IV — a direct comparator for the thesis's recommendation-generation layer and its MIMIC-IV ICU evaluation.
- The thesis borrows its argument that fragment-level RAG is temporally blind, its guideline-grounding motif, and its expert-validated LLM-judge protocol as an evaluation pattern.
- Key difference: CliCARE **compresses** the record into a TKG offline rather than performing **timestamp-aware retrieval** from the patient's own timeline at query time, as the thesis does.
- CliCARE has **no recommendation-level verification gate**: grounding is structural (alignment before generation), and nothing checks the generated recommendation against the retrieved patient evidence afterward.
- CliCARE produces **no audit trail** and measures no faithfulness of evidence citations; the thesis's measured audit-trail faithfulness fills exactly this gap.
- No human-in-the-loop workflow — clinician involvement is limited to evaluation, whereas the thesis integrates clinician validation into the operational loop.

## References
- Hager, P. et al. "Evaluation and mitigation of the limitations of large language models in clinical decision-making." Nature Medicine 30(9):2613-2622 (2024).
- Lewis, P. et al. "Retrieval-augmented generation for knowledge-intensive NLP tasks." NeurIPS 33:9459-9474 (2020).
- Zhao, X. et al. "MedRAG: Enhancing retrieval-augmented generation with knowledge graph-elicited reasoning for healthcare copilot." Proc. ACM Web Conference 2025, 4442-4457.
- Johnson, A. E. W. et al. "MIMIC-IV, a freely accessible electronic health record dataset." Scientific Data 10(1):1 (2023).
- Zheng, L. et al. "Judging LLM-as-a-judge with MT-Bench and Chatbot Arena." arXiv:2306.05685 (2023).
