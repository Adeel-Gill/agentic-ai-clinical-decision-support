# Paper 016

## Basic Information
- **Title:** Towards Generalist Biomedical AI
- **Authors:** Tao Tu, Shekoofeh Azizi, Danny Driess, Mike Schaekermann, Mohamed Amin, et al.
- **Year:** 2023
- **Venue:** Google Research / Google DeepMind
- **DOI:** N/A
- **Link:** N/A

---

## Abstract Summary (200–300 words)
This paper introduces **Med-PaLM Multimodal (Med-PaLM M)**, a large-scale generative model designed as a proof of concept for **generalist biomedical AI**. Medicine is inherently multimodal, requiring clinicians to interpret data from diverse sources including clinical notes, imaging, and genomics. However, most current AI systems are unimodal and single-task, limiting their utility in real-world clinical workflows where contextual information is vital. To facilitate the development of more versatile models, the authors first curate **MultiMedBench**, a multimodal benchmark consisting of 14 tasks such as medical question answering, radiology report generation, and genomic variant calling.

Med-PaLM M utilizes a flexible sequence-to-sequence architecture that interleaves various data modalities using a single set of model weights. The model reaches performance competitive with or exceeding state-of-the-art specialist models on all MultiMedBench tasks, often by wide margins. Beyond quantitative metrics, the researchers report emergent capabilities such as **zero-shot medical reasoning** and **generalization to novel medical concepts**. In a side-by-side human evaluation of chest X-ray reports, clinicians preferred Med-PaLM M's outputs over those produced by radiologists in up to **40.50% of cases**, with an average of only 0.25 clinically significant errors per report—a rate comparable to human baselines. The study represents a significant milestone toward unified biomedical AI systems capable of cross-modal interpretation and human-AI collaboration.

---

## Research Problem
- **Limits of single-task medical AI:** Current systems are typically narrow specialists that cannot incorporate information from other modalities (e.g., a mammography system cannot look at an MRI or an EHR).
- **Need for general biomedical intelligence:** Medicine requires systems that can flexibly encode and interpret multifaceted data to provide contextualized care delivery.
- **Need for multimodal clinical reasoning:** Specialist models cannot verbally explain predictions or engage in collaborative dialogues, bounding their utility in real-world applications.

---

## Motivation
- **Why Med-PaLM M:** To explore the potential of **Foundation Models** to interpret multimodal data with complex structures and tackle challenging biomedical tasks.
- **Limitations of earlier medical LLMs:** Previous efforts like BiomedGPT or LLaVA-Med either required task-specific finetuning or were limited to small-scale visual question answering tasks.

---

## Proposed Solution
- **Med-PaLM M Architecture:** A multimodal language model built on **PaLM-E**, which combines the Pathways Language Model (PaLM) with a Vision Transformer (ViT) encoder.
- **Multimodal capabilities:** A sequence-to-sequence framework that processes sequences of text, vision, and sensor signals in a unified generative output space.
- **Instruction Tuning:** The model is specialized for the biomedical domain by training on a mixture of distinct tasks simultaneously with task-specific prompts.
- **Evaluation Framework:** Uses the newly curated **MultiMedBench**, spanning language, imaging (CT, MRI, X-ray), pathology, dermatology, and genomics.

---

## Core Analysis
- **Clinical Reasoning:** Large versions of Med-PaLM M (84B and 562B) exhibit **emergent zero-shot multimodal reasoning**, allowing them to localized lesions and describe findings they were not explicitly trained on.
- **Multimodal Understanding:** Encodes imaging (mammography, dermatology, chest X-ray), pathology slides, clinical notes, and genomic variant calling as 3-class image classifications.
- **Memory:** The model acts as an implicit knowledge base. However, it is limited by **context length** (max 710 tokens) and lacks persistent long-term storage across separate clinical encounters.
- **Planning:** While not an autonomous agent, the model handles multi-step reasoning via **Chain-of-Thought (CoT)** prompts.
- **Tool Usage:** Discusses the possibility of LLMs interfacing with specialist encoders or agents via **tool use**, though Med-PaLM M itself is designed as an end-to-end multimodal interpreter.

---

## Healthcare Applications
- **Intelligent Patient Monitoring:** Potential for interpreting **vital signs and observations** as continuous sensor signals (vitals were mentioned as a modality, though the benchmark focused on imaging and text).
- **Clinical Decision Support (CDS):** Assisting clinicians by generating radiology findings, summarizing reports, and answering complex medical questions.
- **Diagnostic Assistance:** High-accuracy classification of dermatology and mammography images.
- **Medical Documentation:** Automating **radiology report generation** (MIMIC-CXR) and summarization (MIMIC-III).
- **Physician Support:** Acting as a "common point of assistance" providing access to expertise across many fields.

---

## Evaluation
- **Benchmarks:** **MultiMedBench** (over 1 million samples across 14 tasks).
- **Clinical tasks:** Visual question answering (VQA-RAD, Slake, Path-VQA), image classification, and report generation.
- **Human evaluation:** Radiologists ranked model reports against reference reports, finding Med-PaLM M comparable to human performance.
- **Safety:** Independent evaluation measured clinical errors related to the presence, location, or severity of findings.
- **Comparison:** Outperformed specialist models on tasks like chest X-ray report generation (by 8%) and medical VQA (by 10%).

---

## Key Contributions
- Curation of **MultiMedBench**, the first comprehensive multimodal biomedical benchmark.
- Development of **Med-PaLM M**, the first generalist biomedical AI system.
- Evidence of **emergent capabilities**, including zero-shot multimodal reasoning and task transfer.
- Successful **radiologist validation** of AI-generated clinical documentation.

---

## Strengths
- **Versatility:** A single model with a single set of weights handles 14 disparate tasks.
- **Groundedness:** Interleaving visual and textual data reduces the limits of narrow, unimodal AI.
- **Scalability:** Performance on reasoning-heavy tasks improves significantly as model size increases.

---

## Limitations
- **Hallucinations:** Prone to hallucinating references to non-existent prior studies due to artifacts in training data.
- **No persistent memory:** The model lacks a mechanism for longitudinal tracking beyond the current context window.
- **Limited autonomous behavior:** Med-PaLM M is a passive generator rather than an active agent.
- **Personalization:** Does not yet incorporate unique patient history over long time horizons.

---

## Research Gap
- **Agentic AI:** Transitioning from a generalist *model* to a **generalist *agent*** capable of active information acquisition.
- **Long-term memory:** Handling patient data that exceeds current context lengths.
- **Multi-agent collaboration:** Coordinating between generalist and specialist AI systems in care delivery.
- **Real-time monitoring:** Evaluating the framework on high-frequency streaming data rather than static datasets.

---

## How This Supports My Thesis

### Concepts to Adopt
- **Multimodal Context Interleaving:** Using the sequence-to-sequence structure to feed **vital sign sensors** alongside EHR text and images into the agentic brain.
- **Zero-shot CoT for Monitoring:** Implementing the CoT reasoning traces observed in Med-PaLM M to explain "why" a patient monitor is alerting a clinician.

### Concepts to Modify
- **Output Objectives:** Instead of focusing on "Report Generation," modify the instruction tuning to generate **Proactive Monitoring Actions** and **Triage Decisions**.

### Concepts Not Suitable
- **Direct End-to-End Classification:** For high-acuity monitoring, classification labels are less useful than the **narrative reasoning** and **action-oriented outputs** required by agents.

### Proposed Improvements
- **RAG for Guidelines:** Integrate Med-PaLM M with a retrieval layer to ground multimodal observations in the latest **Clinical Guidelines**.
- **FHIR API Integration:** Use Med-PaLM M as the central controller to generate **FHIR-compliant queries** based on its visual/textual understanding.
- **Multi-Agent Orchestration:** Use Med-PaLM M as a "Primary Care Agent" that delegates to specialist agents (e.g., a **MedRAG** specialist or a **Toolformer** calculator).

---

## Comparison
Med-PaLM M (P016) represents the **pinnacle of multimodal intelligence** compared to P001–P015. While **Med-PaLM 2 (P013/P015)** set the bar for clinical knowledge in text, **Med-PaLM M** advances this into the visual and genomic domains. It complements agent architectures like **ReAct (P003)** by providing a much more robust "brain" capable of "seeing" patient data. Unlike the sandbox simulation of **Agent Hospital (P011)**, P016 provides the **foundational multimodal encoder** needed to make those virtual doctors truly proficient in interpreting actual patient scans and labs.

---

## Important Figures
- **Figure 1:** Med-PaLM M Overview. **Importance:** Shows how a single set of weights replaces multiple specialist models.
- **Figure 3:** Evidence of emergent zero-shot reasoning. **Importance:** Demonstrates that the model can find TB lesions it was never explicitly trained to detect.
- **Figure 6:** Qualitative comparison of reports. **Importance:** Shows the model's ability to identify medical devices (tubes/lines) in context.

---

## Important Tables
- **Table 1:** MultiMedBench Overview. **Importance:** Lists the 14 tasks used for evaluation.
- **Table 2:** Performance Comparison. **Importance:** Proves Med-PaLM M is competitive with specialists across 7 modalities.
- **Table 3:** Scaling results. **Importance:** Shows that language-heavy tasks benefit more from scale than simple image classification.

---

## Important References
- **Singhal et al. (2022) [Med-PaLM]:** The text-only precursor.
- **Driess et al. (2023) [PaLM-E]:** The base multimodal architecture.
- **Wei et al. (2022) [Chain-of-Thought]:** Foundations for medical reasoning.

---

## Keywords
1. Med-PaLM M
2. Generalist Biomedical AI
3. Multimodal AI
4. MultiMedBench
5. Radiology Report Generation
6. Emergent Capabilities
7. Zero-shot Reasoning
8. Foundation Models
9. Clinical Decision Support
10. Patient Monitoring (Potential)
11. Genomics
12. Pathology
13. Dermatology
14. Instruction Tuning
15. PaLM-E

---

## Personal Notes

### Ideas for My Thesis
- Create a **"Monitoring MultiMedBench"** where tasks include "Predict Sepsis from Vital Streams" and "Detect Lead Displacement in ECG".
- Use the **one-shot exemplar with dummy tokens** (<img>) strategy to train my monitoring agent on sparse medical sensor data.

### Future Research Ideas
- Investigating **"Modality Bottlenecks"**: why does the language model scale better than the vision encoder for complex medical tasks?

### Chapter 2 Citations
- "Med-PaLM M is the first demonstration of a generalist biomedical AI system that can interpret multimodal biomedical data... reaching performance competitive with or exceeding SOTA on all tasks in MultiMedBench".

### Supervisor Questions
- Since the vision encoder (ViT) was a bottleneck, should we consider **hierarchical encoders** for long-horizon patient vital monitoring?
- How can we implement the **"side-by-side radiologist evaluation"** methodology for my real-time monitoring alerts?

---

## Relevance Score
**10/10**
**Justification:** This paper is essential because it provides the **multimodal architectural blueprint** for a generalist clinical assistant. For a thesis on patient monitoring (which is multimodal by nature), Med-PaLM M is the definitive reference for cross-modal integration and emergent clinical reasoning.


| ID | Year | Paper | Category | Research Problem | Proposed Solution | Memory | Planning | Reasoning | Tool Use | Multi-Agent | RAG | Healthcare | Evaluation | Research Gap | Relevance | Contribution to Thesis |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| P016 | 2023 | Towards Generalist Biomedical AI | Framework | Most medical AI models are unimodal, single-task systems that cannot integrate diverse data types (images, genomics) or engage in collaborative dialogue. | Med-PaLM Multimodal (Med-PaLM M), a generalist system that flexibly encodes and interprets multimodal biomedical data using a unified generative framework and a single set of model weights,. | No | No | Yes – Elicited through emergent zero-shot multimodal chain-of-thought (CoT) reasoning and language-enabled combinatorial generalization,,. | No | No | No | Yes | Evaluated on MultiMedBench (14 tasks) against specialist SOTA models and through blinded radiologist assessment of generated reports for clinical utility and error rates,. | Jointly scaling modality-specific encoders with the language model and validating generalist systems in real-world clinical applications,. | 10 | Provides the foundational multimodal "Brain" architecture capable of integrating diverse patient data streams (vitals, imaging, notes) into a unified reasoning process for comprehensive decision support. |