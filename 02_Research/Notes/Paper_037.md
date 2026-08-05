# Paper 037

## Basic Information
- **Title:** Medical Hallucination in Foundation Models and Their Impact on Healthcare
- **Authors:** Yubin Kim, Hyewon Jeong, Shan Chen, Shuyue Stella Li, Chanwoo Park, Mingyu Lu, et al.
- **Year:** 2025
- **DOI:** 10.48550/arXiv.2503.05777
- **Venue:** arXiv preprint (arXiv:2503.05777v2); collaboration led by MIT, Harvard Medical School, University of Washington
- **Publisher:** arXiv
- **Link:** https://arxiv.org/abs/2503.05777

## Abstract Summary (200–300 words)
This paper provides the first holistic characterization of **medical hallucination** in foundation models, defined as any model output that is factually incorrect, logically inconsistent, or unsupported by authoritative clinical evidence in ways that could alter clinical decisions. The authors argue hallucinations stem from autoregressive training objectives that prioritize token likelihood over epistemic accuracy, producing overconfidence and poor calibration. Four contributions are made: (1) a five-cluster taxonomy of medical hallucinations (factual errors, outdated references, spurious correlations, incomplete chains of reasoning, fabricated sources/guidelines); (2) experiments across 11 foundation models (7 general-purpose, 4 medical-specialized) on the Med-HALT benchmark plus a physician-audited annotation study on 20 NEJM case reports; (3) a global clinician survey (n=70, 15 specialties); and (4) an assessment of mitigation strategies. Key findings: general-purpose models achieved far higher hallucination-free rates than medical-specialized models (median 76.6% vs 51.3%; p=0.012). Chain-of-thought prompting significantly reduced hallucinations in 86.4% of comparisons after FDR correction, and top models like Gemini-2.5 Pro exceeded 97% accuracy with CoT. Crucially, physician audits found 64-72% of residual hallucinations arose from causal or temporal reasoning failures rather than knowledge gaps, and tasks demanding factual/temporal extraction (chronological ordering, lab data understanding) produced higher hallucination rates than diagnosis prediction. The clinician survey found 91.8% had encountered medical hallucinations and 84.7% believed they could cause patient harm. The paper concludes medical hallucination is a reasoning-driven failure mode, that domain-specific fine-tuning alone is insufficient, and that safety requires reasoning transparency, continuous evidence retrieval, and calibrated uncertainty management. It also reviews regulatory and legal frameworks (FDA SaMD, HIPAA, liability models).

## Research Problem
- Foundation models integrated into clinical workflows generate plausible but incorrect medical information that can directly harm patients (wrong dosages, contraindicated drugs, false imaging interpretations).
- Medical hallucinations are harder to detect than general hallucinations because they use domain-specific terminology and appear clinically coherent, and knowledge asymmetry means end-users cannot verify them.
- There was no unified taxonomy, benchmark-plus-physician-audit characterization, or clarity on whether hallucination is a knowledge problem or a reasoning problem.

## Proposed Solution
- A structured taxonomy of medical hallucination types anchored to clinical tasks and severity/risk levels.
- A mixed-methods evaluation: quantitative Med-HALT benchmarking, physician-led qualitative annotation of NEJM case reports, and a multinational clinician survey.
- Empirical testing of mitigation strategies (system prompting, chain-of-thought, RAG/MedRAG, internet search) plus a review of data-centric, model-centric, external-knowledge, uncertainty-quantification, and prompt-engineering approaches.

## Architecture
- Not an architecture paper; it evaluates existing foundation models. The evaluation pipeline parses NEJM case records into structured elements, feeds them to LLMs for three reasoning tasks, then routes outputs to physician annotators who label hallucination type and clinical risk (Fig. 6). UMLSBERT embeddings compute semantic similarity to ground truth.

## Memory
- Not a core focus. The taxonomy includes "Memory-Based Hallucination" (inaccurately recalling or fabricating information the model was trained to retrieve, e.g. citing non-existent guidelines), which is a diagnostic category rather than a memory mechanism.

## Planning
- Not a core focus; the paper concerns single-shot and prompted LLM outputs, not planning agents. It notes multi-step/multi-agent deliberation as a possible uncertainty-refinement direction.

## Reasoning
- Central theme: medical hallucination is reframed as a **reasoning-driven failure mode**. Physician audits attribute 64-72% of residual hallucinations to causal or temporal reasoning failures, not knowledge gaps.
- Chain-of-thought reasoning traces enable self-verification and error detection, significantly cutting hallucinations; general models' broad reasoning outperforms narrow medical fine-tuning.
- Reasoning failures map to the "incomplete chains of reasoning" cluster (reasoning, decision-making, diagnostic hallucinations).

## Tool Use
- Not an agentic tool-use paper. It evaluates internet search (SerpAPI/LangChain) and MedRAG retrieval as mitigation tools; search helped weaker models most but sometimes degraded strong models via retrieval-generation conflicts.

## Multi-Agent
- Not a core focus; multi-LLM collaboration and consensus/voting are discussed as uncertainty-reduction strategies that cross-verify reasoning and mitigate individual model bias.

## RAG
- Reviewed substantially as a mitigation strategy. RAG grounds outputs in external medical knowledge and improves interpretability/citation, and MedRAG/i-MedRAG improve complex medical QA. But RAG can introduce errors via low-quality retrieval and retrieval-generation conflicts; benefits vary by model tier (largest relative gains for weaker/medical-specialized models, minimal or negative for strong models). Medical knowledge graphs are also covered for provenance and traceability.

## Healthcare Contribution
- First unified taxonomy plus physician-audited, survey-validated characterization of medical hallucination.
- Empirical evidence that medical-specialized models underperform general-purpose models on hallucination resistance, challenging the domain-specialization assumption.
- Actionable insight that fundamental extraction tasks (temporal sequencing, lab interpretation) are more error-prone than diagnosis, with high-risk errors persisting even in low-aggregate-rate models.
- Regulatory/legal analysis (FDA SaMD pathways, HIPAA, GMLP, distributed liability) for deploying generative AI in healthcare.

## Trustworthy AI
- The paper's core is trustworthy AI: hallucination, overconfidence, poor calibration, patient-safety risk, and erosion of trust.
- Advocates reasoning transparency, adaptive uncertainty management (conformal prediction, abstention thresholding, calibration), and human-in-the-loop workflows with task-specific validation.
- Emphasizes that any current LLM in clinical settings requires continuous monitoring and human oversight; over 60% of surveyed clinicians stressed human supervision.

## Evaluation
- **Med-HALT** (350 sampled cases, 7 tasks): general-purpose median hallucination-free 76.6% vs medical-specialized 51.3% (diff 25.2%, p=0.012); Gemini-2.5 Pro 87.6% baseline → 97.9% with CoT; MedGemma 28.6-61.9%.
- **CoT** significant in 71% of models (p<0.05); 86.4% retention after Benjamini-Hochberg FDR correction (q<0.05).
- **NEJM physician audit** (20 cases, 7 MD annotators, risk levels 0-5): GPT-4o highest hallucination in Chronological Ordering (24.6%) and Lab Data Understanding (18.7%); Claude-3.5 and o1 achieved 0% on Diagnosis Prediction; inter-rater Jaccard-like index 0.272 (type) and 0.347 (risk), moderate agreement.
- **Clinician survey** (n=70): 91.8% encountered hallucinations; 84.7% considered them capable of causing harm; 85% cross-reference to verify.

## Research Gap
- Lack of standardized definitions, principled metrics, and reliable ground truth for medical hallucination (compounded by Hickam's dictum and inter-clinician disagreement).
- Need for longitudinal, real-world clinical-workflow evaluation linking benchmark performance to patient outcomes.
- Need for rigorous benchmarking against expert clinicians to separate uniquely algorithmic reasoning failures from shared human errors.
- Uncertainty quantification and calibration in medical LLMs remain immature.

## Key Contributions
- A five-cluster taxonomy plus granular type/risk categorization of medical hallucinations.
- Multi-model Med-HALT benchmark showing general > medical-specialized models and CoT efficacy with statistical rigor.
- Physician-audited NEJM case-report study localizing hallucinations to causal/temporal reasoning and factual-extraction tasks.
- A multinational clinician survey documenting real-world prevalence, perceived harm, and verification behavior.
- A review of mitigation strategies and a regulatory/legal analysis for clinical generative AI.

## Limitations
- Small annotation set (20 NEJM cases) and moderate inter-rater agreement; survey n=70 skewed toward Asia/North America.
- Med-HALT sample limited to 50 examples per task; some noted data discrepancies (e.g. Gemini-2.0-flash-exp diagnosis rate).
- Mitigation experiments cover a representative subset (prompting, retrieval), not all strategies reviewed.
- Findings are on curated exam/case-report data, not deployed longitudinal patient records.

## Important Quotes
- "medical hallucination as a reasoning-driven failure mode rather than a knowledge deficit" (Abstract)
- "91.8% had encountered medical hallucinations, and 84.7% considered them capable of causing patient harm" (Abstract)

## Thesis Relevance
- Provides the core justification for the thesis's **verification gate and audit trail**: hallucination is a reasoning-driven, high-stakes failure that must be caught as a first-class evaluated component, not assumed away.
- Directly supports thesis gap (3): faithfulness/verification is rarely evaluated as a first-class component; this paper operationalizes physician-audited risk-level annotation the thesis can adapt.
- The finding that **temporal ordering and lab-data extraction** are the most error-prone tasks is critical for the thesis's longitudinal ICU monitoring — it argues persistent, structured patient memory and temporal reasoning checks are essential.
- Supports the thesis's **RAG grounding in the patient's own timeline**: the paper shows guideline/KG RAG helps but suffers retrieval-generation conflict, motivating patient-timeline-grounded retrieval and provenance tracking.
- Motivates the thesis's **human-in-the-loop validation** and **uncertainty/calibration** mechanisms (conformal prediction, abstention), which the paper identifies as necessary for safe deployment.
- Cautions that domain fine-tuning alone is insufficient — reinforcing the thesis's agentic reasoning-plus-verification design over a single specialized model.

## References
- Pal, A. et al. (2023). Med-HALT: Medical domain hallucination test for large language models. (primary benchmark used)
- Xiong, G. et al. (2024). Benchmarking retrieval-augmented generation for medicine (MedRAG). (medical RAG toolkit)
- Farquhar, S. et al. (2024). Detecting hallucinations in large language models using semantic entropy. Nature. (uncertainty-based detection)
- Hegselmann, S. et al. (2024). A data-centric approach to generate faithful patient summaries with LLMs. (hallucination typology adapted for annotation)
- Wei, J. et al. (2022). Chain-of-thought prompting elicits reasoning in large language models. (key mitigation method)
