# Paper 050

## Basic Information
- **Title:** RGAR: Recurrence Generation-augmented Retrieval for Factual-aware Medical Question Answering
- **Authors:** Sichu Liang, Linhai Zhang, Hongyu Zhu, Wenwen Wang, Yulan He, Deyu Zhou
- **Year:** 2025
- **DOI:** 10.18653/v1/2025.findings-emnlp.214
- **Venue:** Findings of the Association for Computational Linguistics: EMNLP 2025, pp. 4006-4033; arXiv:2502.13361
- **Publisher:** Association for Computational Linguistics
- **Link:** https://arxiv.org/abs/2502.13361

## Abstract Summary (200–300 words)
RGAR reframes medical RAG through **Bloom's taxonomy**, distinguishing **factual knowledge** (patient-specific information residing in EHRs) from **conceptual knowledge** (medical expertise in corpora), alongside procedural and metacognitive knowledge embedded in advanced RAG systems. The authors argue existing medical RAG (MedRAG, i-MedRAG, GAR) concatenates the whole EHR plus question into one query, so retrieval is diluted by extraneous record content and the factual side of retrieval is ignored — a critical failure for **EHR-integrated, factual-aware QA** where records reach 5,782 tokens. RGAR is a **dual-end, recurrent retrieval framework**: (1) **Conceptual Knowledge Retrieval (CKR)** prompts a train-free LLM generator to expand the basic query into possible answers, contexts, and titles, averaging normalized MedCPT similarities for stable retrieval from a textbook corpus; (2) **Factual Knowledge Extraction (FKE)** uses the retrieved conceptual chunks to run a reading-comprehension-style span extraction over the raw EHR, filtering question-relevant facts and summarizing/interpreting them (e.g., reading numerical labs against retrieved knowledge); (3) the **recurrence pipeline** updates the basic query with the enriched factual representation and iterates (default two rounds), letting factual and conceptual knowledge refine each other before a final LLM reader answers using only the retrieved chunks. On MedQA-USMLE, MedMCQA, and **EHRNoteQA** (real MIMIC-IV discharge summaries), RGAR with Llama-3.2-3B-Instruct achieves the best average accuracy (61.04%, +11.91 over zero-shot), beating GAR, MedRAG, and the far costlier i-MedRAG; gains grow with context length (+7.8% over GAR on EHRNoteQA). With Llama-3.1-8B-Instruct, RGAR (69.52%) surpasses RAG-enhanced GPT-3.5 (66.22%). Ablations confirm both components and show two recurrence rounds suffice, mimicking multi-hop reranking.

## Research Problem
- Medical RAG systems treat retrieval as purely **conceptual** (corpus-side), concatenating entire lengthy EHRs into queries; irrelevant record content degrades dense retrieval, and **factual knowledge in the patient record is never itself treated as a retrieval target**.
- Query-expansion (GAR) and decomposition methods still ignore patient-specific facts and often depend on fine-tuning, limiting scalability.
- Real-world EHR benchmarks (EHRNoteQA, up to 5,782 tokens from MIMIC-IV) expose these failures much more than exam-style QA.

## Proposed Solution
- **RGAR**: a recurrence generation-augmented retrieval framework retrieving from **dual sources** — the patient's EHR (factual) and a medical corpus (conceptual) — with an iterative loop in which each refines the other's queries; no LLM fine-tuning required.
- Factual extraction as **text-span reading comprehension** over the un-chunked EHR (avoiding chunking discontinuity), followed by conceptual-knowledge-informed summarization/interpretation of raw findings (e.g., flagging platelet 14,200/mm3 as low).
- Extracted facts serve only to improve retrieval; the final answer is generated from the question, original EHR, options, and retrieved chunks — keeping evidence traceable.

## Architecture
- Three modules in a loop: CKR (multi-query generation: answers/contexts/titles → MedCPT retrieval with normalized similarity averaging over 125.8k textbook chunks) → FKE (LLM extractor: filter F_s then enrich F_e, single-stage prompting) → query update q_b = Q ⊕ F_e; two rounds by default, then LLM reader answers.

## Memory
- Not a core focus; no persistent memory — the EHR is per-question input, and iteration state lives only in the updated query within a single QA episode.

## Planning
- Not a core focus; the recurrence schedule is fixed (predefined rounds), not agentic planning, though the Bloom's-taxonomy framing maps planning to "procedural knowledge" in other systems.

## Reasoning
- Supports **multi-hop clinical reasoning**: retrieved conceptual knowledge generates explainable new factual knowledge (interpreting numeric labs), and two recurrence rounds cover multi-hop needs; more rounds cause over-inference.

## Tool Use
- Not a core focus; the retriever and extractor are fixed pipeline components rather than dynamically invoked tools.

## Multi-Agent
- Not a core focus; a single LLM plays generator/extractor/reader roles within one pipeline — no inter-agent collaboration.

## RAG
- Core focus: extends GAR into **recurrent dual-end retrieval**; argues retrieval from EHRs is a form of query filtering; establishes new SOTA among medical RAG systems and analyzes retrieval stability (multi-query t-SNE, chunk-count sensitivity N=4-32).

## Healthcare Contribution
- Best average accuracy on three **factual-aware medical QA** benchmarks including EHRNoteQA built from real MIMIC-IV discharge summaries — the setting closest to genuine clinical consultation.
- Enables an 8B open model to beat RAG-enhanced GPT-3.5, supporting **local, privacy-preserving deployment** of clinical QA.
- Fine-grained analysis: gains concentrate on the longest EHR contexts (up to +31 points over zero-shot in long bins), i.e., precisely the realistic-record regime.

## Trustworthy AI
- Argues retrieval-grounded answers are preferable because RAG "relies on retrievable documents that provide traceable and trustworthy reasoning"; the ethics statement recommends rigorous validation of all outputs by qualified medical professionals — but the system itself implements no verification, uncertainty, or audit mechanism.

## Evaluation
- Datasets: MedQA-USMLE (1,273), MedMCQA (4,183), EHRNoteQA (962); metric: accuracy; option-free retrieval, zero-shot, greedy decoding; MedCPT retriever, Textbooks corpus, 32 chunks default.
- Main result (Llama-3.2-3B): RGAR 61.04% average vs. i-MedRAG 58.47%, GAR 57.96%, MedRAG 56.13%, RAG 55.05%, zero-shot 49.13%; on EHRNoteQA 73.28% (i-MedRAG 74.22% but ~4x inference time).
- Model-family sweep (Llama/Qwen 1B-8B): RGAR best on average; retrieval hurts sub-2B models; Llama-3.1-8B + RGAR = 69.52% on MedQA-USMLE.
- Ablations: removing FKE or CKR degrades accuracy; round analysis shows one iteration gives the main jump, two rounds optimal (75.78% at N=8), more rounds over-infer.

## Research Gap
- Fills: the underrepresentation of **factual (patient-record) knowledge** as a first-class retrieval target in RAG.
- Leaves open: temporal structure of the record is ignored; no answer verification; corpus-scale latency; reliance on instruction-following ability of the base model; EHRs beyond context limits need chunk-free methods.

## Key Contributions
- First analysis of RAG systems through **Bloom's taxonomy**, exposing the factual-knowledge blind spot.
- **RGAR** dual-end recurrent retrieval enabling factual-conceptual interaction without any fine-tuning.
- New SOTA among medical RAG systems on three factual-aware benchmarks; 8B open model surpassing RAG-enhanced GPT-3.5.
- Evidence that improvements scale with EHR context length, plus stability analyses of multi-query retrieval.

## Limitations
- Retrieval time scales with corpus size (inherent to RAG); fixed rounds without early stopping (though far cheaper than i-MedRAG).
- Interactions with CoT/self-consistency prompting unexplored.
- Assumes the full EHR fits the LLM context window (~128k); extreme records need chunk-free integration.
- Zero-shot operation depends on instruction-following capability; MCQ accuracy is the only metric — no faithfulness or safety evaluation.

## Important Quotes
- "retrieval methods often fail to adequately consider factual information in real-world medical scenarios" (Sec. 1, p. 1)
- "RGAR establishes a new state-of-the-art performance among medical RAG systems" (Abstract, p. 1)

## Thesis Relevance
- Directly validates the thesis's **dual retrieval design**: coupling retrieval from the patient's own record (factual) with retrieval from medical knowledge (conceptual), and letting them interact — the thesis borrows this factual/conceptual distinction for its RAG layer.
- Its EHRNoteQA results on **MIMIC-IV** discharge summaries provide a comparator and precedent for grounding QA in real MIMIC records, and its finding that gains grow with record length supports the thesis's focus on long ICU timelines.
- The demonstration that a well-orchestrated 8B open model beats RAG-enhanced GPT-3.5 supports the thesis's privacy-preserving local-deployment argument.
- Key difference: RGAR's factual extraction is **temporally blind** — it filters spans by relevance with no timestamp awareness — whereas the thesis performs timestamp-aware retrieval over a longitudinal timeline.
- RGAR answers single multiple-choice questions; it has **no recommendation-level verification** — extracted facts steer retrieval but generated answers are never checked against the evidence — and **no audit trail**; the ethics statement defers verification entirely to human professionals, which the thesis operationalizes as a measured verification gate plus human-in-the-loop.
- The record is consumed per-question (compressed into an extracted representation) rather than persisted as longitudinal patient memory across encounters as in the thesis.

## References
- Xiong, G. et al. "Benchmarking retrieval-augmented generation for medicine (MedRAG/MIRAGE)." ACL Findings 2024.
- Xiong, G. et al. "Improving retrieval-augmented generation in medicine with iterative follow-up questions (i-MedRAG)." (2024).
- Kweon, S. et al. "EHRNoteQA: An LLM benchmark for real-world clinical practice using discharge summaries." NeurIPS Datasets and Benchmarks Track (2024).
- Mao, Y. et al. "Generation-augmented retrieval for open-domain question answering (GAR)." ACL 2021.
- Jin, Q. et al. "MedCPT: Contrastive pre-trained transformers with large-scale PubMed search logs for zero-shot biomedical information retrieval." Bioinformatics 39(11) (2023).
