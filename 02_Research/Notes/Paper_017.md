# Paper 017

## Basic Information
- **Title:** Towards Generalist Biomedical AI
- **Authors:** Tao Tu, Shekoofeh Azizi, Danny Driess, Mike Schaekermann, Mohamed Amin, et al.
- **Year:** 2023
- **Venue:** Google Research / Google DeepMind
- **DOI:** N/A
- **Link:** N/A (Source identifies as a technical report from Google Research)

## Abstract Summary (200–300 words)
This paper introduces **Med-PaLM Multimodal (Med-PaLM M)**, a large-scale generative model designed as a proof-of-concept for a generalist biomedical AI system. Medicine is naturally multimodal, yet most current AI systems are unimodal and limited to specific tasks, which bounds their utility in real-world clinical applications. To address the lack of comprehensive evaluation frameworks, the authors curate **MultiMedBench**, a multimodal benchmark comprising 14 diverse tasks across 12 datasets, including medical question answering (QA), visual question answering (VQA), image classification, radiology report generation/summarization, and genomic variant calling.

Med-PaLM M uses a flexible sequence-to-sequence architecture with a single set of model weights to interleave and interpret diverse data types such as clinical language, imaging (CT, MRI, X-ray), and genomics. The model reaches performance competitive with or exceeding the state-of-the-art (SOTA) on all MultiMedBench tasks, often surpassing specialist models by significant margins. Beyond quantitative success, the study reports emergent capabilities such as **zero-shot medical reasoning**, positive task transfer, and generalization to novel medical concepts like tuberculosis detection from chest X-rays. A blinded radiologist evaluation of model-generated chest X-ray reports found that in up to **40.50% of cases**, clinicians preferred Med-PaLM M's reports over those produced by radiologists, with an average of only **0.25 clinically significant errors** per report. This work represents a major milestone toward unified, multimodal biomedical AI capable of assisting in complex clinical delivery.

## Research Problem
- **Limits of existing medical benchmarks:** Most previous benchmarks were unimodal and task-specific, failing to capture the complexity of generalist biomedical AI.
- **Challenges in evaluating medical LLMs:** Narrow specialist systems cannot incorporate relevant context from other modalities (e.g., matching a mammogram with an EHR) or explain their predictions.
- **Need for comprehensive healthcare evaluation:** There is an unmet need for a unified framework to measure a model's ability to comprehend, recall, and manipulate medical knowledge across disparate tasks simultaneously.

## Motivation
- **Why MultiMedQA/MultiMedBench:** To catalyze AI progress by providing a high-quality, unified benchmark for the development of generalist systems.
- **Problems addressed:** The distribution shift in the biomedical domain makes general-purpose generalist models (like PaLM-E) perform poorly without domain-specific finetuning and specialized benchmarks.

## Proposed Solution
- **MultiMedBench Construction:** A collection of over **1 million samples** covering text, radiology, pathology, dermatology, mammography, and genomics.
- **Included Datasets:** Incorporates three language-only datasets from **MultiMedQA** (MedQA, MedMCQA, and PubMedQA) alongside new multimodal sets like MIMIC-CXR, VinDr-Mammo, and PrecisionFDA.
- **Evaluation Methodology:** Uses task-specific metrics (Accuracy, AUC, F1, ROUGE, BLEU) in few-shot and zero-shot setups.
- **Human Clinician Assessment:** Expert thoracic radiologists performed side-by-side rankings and independent error/omission annotations on generated reports.

## Core Analysis
- **Medical Benchmarks:** Evaluates language comprehension via **MedQA** (USMLE-style), **MedMCQA** (entrance exams), and **PubMedQA** (literature).
- **Clinical Reasoning Evaluation:** Probed via **zero-shot Chain-of-Thought (CoT)** prompts where the model must generate a report describing findings before giving a classification.
- **Safety Evaluation:** Assessed through independent human radiologist review, specifically measuring "clinically significant errors" regarding the presence, location, or severity of findings.
- **Human Evaluation:** Blinded side-by-side preference tests between AI and radiologist reports.
- **Memory:** The architecture is limited by a **max token input length of 710**. No explicit persistent or longitudinal memory module is described beyond the input context.
- **Planning:** Handled via emergent **zero-shot CoT reasoning**, though the model is a passive generator rather than an autonomous actor.
- **Tool Usage:** The paper mentions that LLMs can interface with specialist encoders or agents via **tool use**, but Med-PaLM M is designed to handle modalities end-to-end.

## Healthcare Applications
- **Intelligent Patient Monitoring:** The paper identifies "vital signs and observations" as a core clinical modality that generalist AI should interpret.
- **Clinical Decision Support:** Assisting clinicians with diagnostic assistance, report summarization, and access to expertise across many fields.
- **Multi-Agent Healthcare Systems:** Envisages a future where generalist and specialist AI systems interact with clinicians in a tight feedback loop.
- **Real-Time Patient Monitoring:** Suggested by the architecture's ability to interleave **sensor signals** with text.

## Evaluation
- **Metrics:** F1-RadGraph and Clinical Efficacy (CE) metrics (e.g., micro-F1-14) were used to prioritize factuality over mere text overlap.
- **Results:** Med-PaLM M 562B achieved **69.68% accuracy on MedQA** (USMLE) and **80.00% on PubMedQA** in a few-shot setup.
- **Human Comparison:** Med-PaLM M 84B was preferred over radiologist reference reports in **40.50% of cases**.
- **Benchmark Strengths:** MultiMedBench's generative tasks (VQA, report generation) provide a more rigorous test than simple classification benchmarks.

## Key Contributions
1. Curation of **MultiMedBench**, a first-of-its-kind comprehensive multimodal biomedical benchmark.
2. Demonstration of **Med-PaLM M**, the first generalist biomedical AI capable of handling 14 disparate tasks with one set of weights.
3. Evidence of **emergent zero-shot medical reasoning** and task transfer across modalities.
4. Validation that scaling language models (up to 562B) significantly benefits clinical reasoning tasks.

## Strengths
- **Versatility:** Competent across language, vision, and genomics with zero task-specific architecture customization.
- **Interpretability:** CoT reasoning identifies major lesions (e.g., TB) in correct locations.
- **Human-level Performance:** Error rates in radiology reports are comparable to human baselines.

## Limitations
- **No Longitudinal Scenarios:** The model interprets single studies; it does not explicitly manage multi-encounter patient histories.
- **No Agent Workflows:** The system is evaluated as a static task-solver rather than an autonomous agent in a clinical workflow.
- **Limited Multimodal Evaluation:** Lacks modalities like transcriptomics or proteomics.
- **No Continuous Monitoring Tasks:** While vitals are mentioned, the benchmark focuses on static datasets rather than streaming data.

## Research Gap
- **Agentic AI Evaluation:** A need for benchmarks that evaluate agents effectively communicating, resolving disputes, and maintaining truthfulness during inter-agent dialogue [Information outside the paper: See Paper 006/014].
- **Long-term Memory:** Handling clinical data that exceeds the **710-token context limit**.
- **Workflow Evaluation:** Validation in real-world use cases and clinical trials.
- **Real-time Monitoring:** Scaling encoders to handle high-frequency multimodal streaming data.

## How This Supports My Thesis

### Concepts to Adopt
- **Multimodal Sequence-to-Sequence Architecture:** Feeding vital sign sensor streams alongside text to the LLM "brain".
- **Instruction Task Prompting:** Using one-shot exemplars with **dummy `<img>` tokens** for compute efficiency in training monitoring agents.

### Concepts to Modify
- **Action-Oriented Outputs:** Instead of generating "Report Findings," the agent should generate **"Monitoring Alerts"** or **"Intervention Recommendations."**
- **Evaluation Axes:** Adopt the human evaluation axes (omission rate, significant clinical errors) to audit autonomous monitoring decisions.

### Concepts Not Suitable
- **Unimodal Baselines:** P017 proves that text-only or vision-only models are insufficient for the "multidisciplinary endeavour" of medicine.

### Proposed Improvements
- **Integration with FHIR:** Adapt MultiMedBench tasks to use **FHIR-compliant resources** as the text modality to build an interoperable Agentic AI Framework.
- **RAG-Grounded Reasoning:** Combine Med-PaLM M's multimodal reasoning with a **retrieval layer** (like MedRAG) to ground monitoring alerts in clinical guidelines.

## Comparison
- **Vs. P001–P009:** While general agent papers focus on *how* to act, P017 provides the **multimodal biomedical "brain"** and the **benchmark** needed to ensure those acts are clinically valid.
- **Vs. P010–P016:** P017 (Med-PaLM M) is the direct multimodal successor to **Med-PaLM 2 (P013/P015)**. It provides the foundational encoder needed to make **Agent Hospital (P011)** "see" its patient agents' scans and vitals rather than just reading structured data.

## Important Figures
- **Figure 1:** Overview of tasks and modalities. **Importance:** The structural map for any generalist medical agent.
- **Figure 2:** Instruction prompting with one-shot exemplar. **Importance:** Shows how to format multimodal clinical data for an LLM.
- **Figure 3:** Zero-shot CoT reasoning on TB. **Importance:** Proves scaling language models enables visual reasoning.

## Important Tables
- **Table 1:** MultiMedBench Task Summary. **Importance:** Defines the scope of multimodal clinical evaluation.
- **Table 3:** Scaling results. **Importance:** Shows that vision encoders are currently a bottleneck for image classification compared to language.
- **Table A.3:** Medical QA accuracy. **Importance:** Sets the text-based clinical knowledge baseline for Med-PaLM M.

## Important References
- **Singhal et al. (2022):** The original Med-PaLM study; provides the MultiMedQA baseline.
- **Driess et al. (2023):** PaLM-E, the base multimodal architecture for Med-PaLM M.
- **Wei et al. (2022):** Chain-of-Thought foundation for emergent reasoning.
- **Schick et al. (2023):** Toolformer; relevant for the agentic perspective on tool usage.

## Keywords
1. Med-PaLM M
2. MultiMedBench
3. Generalist Biomedical AI
4. Multimodal reasoning
5. Radiology Report Generation
6. MultiMedQA
7. Zero-shot Medical Reasoning
8. Clinical Decision Support
9. Patient Monitoring
10. Genomics
11. Emergent Capabilities
12. Instruction Tuning
13. Foundation Models
14. AI Safety
15. Human Evaluation

## Personal Notes

### Ideas for My Thesis
- Propose a **"Monitoring MultiMedBench"** that specifically evaluates an agent's ability to detect deterioration from vitals + lab results + clinical notes.
- Use the **F1-RadGraph** methodology to evaluate the "Clinical Faithfulness" of my monitoring agent's reasoning traces.

### Future Research
- How to scale **vision-language models** when training data for specific medical conditions (like rare arrhythmias) is scarce?

### Evaluation Metrics
- Adopt the **Side-by-Side Radiologist Evaluation** protocol for my final thesis defense to compare agentic decisions against human experts.

### Questions for Supervisor
- Since the ViT was a bottleneck in this paper, should we use **specialized medical vision encoders** for our framework instead of generalist ones?
- How can we extend the **710-token context** to support continuous monitoring of an ICU patient over 24 hours?

## Relevance Score
**10/10**
**Justification:** This paper provides the **multimodal architectural blueprint** and the **comprehensive benchmark** necessary for building and evaluating any generalist healthcare assistant. It is the definitive reference for cross-modal integration in Agentic AI for medicine.