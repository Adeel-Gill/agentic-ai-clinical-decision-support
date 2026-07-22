# Paper 014

## Basic Information
- **Title:** A Survey of Large Language Models in Medicine: Progress, Application, and Challenge
- **Authors:** Hongjian Zhou, Fenglin Liu, Boyang Gu, Xinyu Zou, Jinfa Huang, Jinge Wu, Yiru Li, Sam Chen, Peilin Zhou, Junling Liu, Yining Hua, Chengfeng Mao, Chenyu You, Xian Wu, Yefeng Zheng, Lei Clifton, Zheng Li, Jiebo Luo, David Clifton
- **Year:** 2024 (Based on references to Llama-3 and Med-Gemini)
- **Venue:** University of Oxford / Tencent / Amazon / MIT / Harvard / Yale (Technical Survey)
- **DOI:** N/A
- **Link:** https://github.com/AI-in-Health/MedLLMsPracticalGuide

---

## Abstract Summary (200–300 words)
This comprehensive survey examines the rapid evolution and deployment of **Large Language Models (LLMs)** in the medical field, addressing the critical gap between research-level capabilities and practical clinical utility. The authors provide a structured overview of **medical LLM principles**, categorizing them by architecture (encoder-only, decoder-only, and encoder-decoder) and development methodologies such as **pre-training from scratch**, **fine-tuning**, and **prompting**. 

The paper highlights that while state-of-the-art models like **Med-Gemini** and **MedPaLM-2** have achieved expert-level performance on USMLE-style exams, their performance often falters in **open-ended clinical tasks** where pre-set options are unavailable. The survey explores diverse healthcare applications, including **clinical decision support (CDS)**, **clinical coding**, **report generation**, and **medical robotics**, while emphasizing the emerging role of **Agentic AI** and **Multimodal LLMs** that integrate time-series data like ECGs. 

The summary also identifies persistent challenges for safe deployment: **hallucinations**, **data privacy** (including personally identifiable information leakage), **ethical biases**, and the **lack of robust clinical benchmarks**. The authors advocate for **interdisciplinary collaboration** and a "**doctor-in-the-loop**" approach to ensure that medical LLMs are aligned with professional standards and clinical workflows. Ultimately, this review serves as a practical guide for practitioners to build and evaluate effective medical LLMs tailored to specific healthcare needs.

---

## Research Problem
- **Importance of LLMs in medicine:** LLMs have moved beyond general NLP tasks to assist in enhancing diagnostics, providing medical education, and improving patient care.
- **Limitations of traditional clinical AI:** Previous AI-based medical technologies were typically tailored to single, specific tasks, whereas LLMs offer a **multi-purpose platform** for diverse clinical needs.
- **Challenges for safe deployment:** The transition from structured exam-taking to **real-world open clinical practice** is difficult due to the unstructured nature of patient care and the high stakes of medical error.

---

## Motivation
- **Why the survey was conducted:** To provide a **comprehensive review** of medical LLM development, practical applications, and outcomes, which remains scarce despite the burgeoning trend in research.
- **Research gaps addressed:** Most existing models focus on dialogue and QA tasks, overlooking **practical utility in clinical workflows**, biomedical understanding beyond QA, and the lack of standardized evaluation datasets for clinical scenarios.

---

## Proposed Solution
- **Survey framework:** The review answers five core study questions: model development practices, performance measurement, real-world employment, arising challenges, and optimization for clinical settings.
- **Taxonomy of applications:** The paper provides a detailed taxonomy covering **discriminative tasks** (QA, entity extraction, text classification) and **generative tasks** (summarization, generation, simplification).

---

## Core Analysis
- **Healthcare Applications:**
    - **CDS:** Systems like **Dr. Knows** and **Foresight** provide evidence-based recommendations and risk forecasting.
    - **Patient Monitoring:** **NYUTron** predicts mortality, readmission, and length of stay. Future directions include using **MLLMs for time-series data** (ECG, PPG).
    - **EHR:** Models like **GatorTron** and **ClinicalBERT** are pre-trained on massive EHR corpora to capture clinical nuances.
    - **Documentation:** **ImpressionGPT** and **MAIRA-1** automate clinical coding and radiology report generation.
- **Clinical Reasoning:** Enhanced through **Chain-of-Thought (CoT)** prompting to simulate diagnostic thought processes and provide interpretable predictions.
- **Memory:** Utilizes **large-scale pre-training** on corpora like PubMed and MIMIC-III to encode vast clinical knowledge.
- **Planning:** **Multi-agent planning systems** are being explored in medical robotics for collaborative surgical tasks.
- **Tool Usage:** **Retrieval-Augmented Generation (RAG)** is used to ground responses in external databases (UpToDate, guidelines) to minimize hallucinations.
- **Agentic AI Perspective:**
    - **Autonomous Agents:** LLM-based agents act as controllers to solve complex tasks through human-like behaviors.
    - **Multi-Agent Collaboration:** The survey proposes a future where specialized agents (e.g., a **radiologist agent** and a **pathologist agent**) collaborate to form a cohesive medical opinion.
    - **Clinical Workflows:** Emphasizes the need to integrate agents into **real-time decision-making** and remote monitoring.

---

## Evaluation
- **Benchmarks:** Traditional benchmarks like **MedQA (USMLE)** and **PubMedQA** are common but criticized for not reflecting real-world clinical proficiency.
- **Metrics:** Lexical metrics (BLEU, ROUGE) are used but found inadequate for clinical context; specialized metrics like **RadGraph** and **RadCliQ** are preferred for radiology.
- **Clinical tasks:** Evaluation across 10 tasks shows LLMs are strong in close-ended QA but underperform in **open-ended generative tasks**.

---

## Key Contributions
1. Provides a **practical guide** and regularly updated repository for constructing medical LLMs.
2. Introduces a **comprehensive taxonomy** of models, tasks, and applications across the medical domain.
3. Highlights the **performance gap** between structured exam performance and unstructured clinical practice.
4. Outlines a roadmap for **Future Directions**, including multimodal integration and the development of **Medical Agents**.

---

## Strengths
- **Multimodal Integration:** Discusses the bridging of visual (images), audio, and textual medical information (e.g., **Med-Gemini**, **RadFM**).
- **Data-Efficient Alignment:** Demonstrates how **Instruction Fine-Tuning (IFT)** and **PEFT (LoRA)** allow general LLMs to specialize with minimal resources.
- **Interpretability:** Encourages the use of CoT to provide "Socratic-style" tutoring and transparent diagnostic reasoning.

---

## Limitations
- **Hallucinations:** Fluent but nonfactual outputs remain a significant risk for misdiagnosis and harmful patient education.
- **Explainability:** LLMs currently lack the **assumption-based perspective** employed by human doctors.
- **Safety:** Risks include incorrect medical advice and the **leakage of PII** from training data.
- **Privacy/Bias:** Under-representation of specialized fields and demographic biases in training data can lead to **discrimination in care**.
- **Regulatory concerns:** The versatility of LLMs challenges traditional "one-for-all" auditing processes, necessitating agile, adaptive frameworks.

---

## Research Gap
- **Agentic AI:** A "pressing need" exists for agents that can effectively communicate, resolve disputes, and maintain **truthfulness during inter-agent dialogue**.
- **Long-term Memory:** Current evaluations lack a focus on **continuous learning through feedback loops** over time.
- **Real-time Monitoring:** There is a scarcity of models capable of processing **continuous time-series data** (ECG, blood pressure) for proactive monitoring.
- **Clinical Workflow Integration:** Large-scale clinical trials specifically targeting LLM integration into daily workflows are currently missing.

---

## How This Supports My Thesis

### Concepts to Adopt
- The **"Medical Agents" collaboration model** where roles mimic diverse specialists (radiologist, pathologist) to enhance diagnostic accuracy.
- The **multimodal integration approach** for incorporating time-series sensor data (ECG) into the monitoring framework.
- The **MIRAGE benchmark** approach for evaluating RAG systems in medical information retrieval.

### Concepts to Modify
- **Selective Evaluation:** Move beyond USMLE-style accuracy to metrics that measure **faithfulness, safety, and adherence to medical guidelines**.
- **User Interface:** Adopt the "**healthcare copilot**" model where the agent serves as an interaction review tool for physicians rather than a replacement.

### Concepts Not Suitable
- **"Pre-training from Scratch"**: Due to the "high-cost and time-consuming" nature, this is not suitable for a thesis project; **PEFT (LoRA)** is the more viable path.
- **Sole Reliance on LLM Weights:** The paper makes it clear that parametric knowledge is often outdated; **RAG is mandatory** for reliable CDS.

### Proposed Improvements
The survey informs an **Agentic AI Framework** by emphasizing that a successful system must integrate **dynamic motion planning** (from medical robotics) with **multimodal time-series analysis**. By adopting the **"Simulacrum-based" approach** (similar to Agent Hospital but mentioned here as simulated scenarios), the framework can evolve through **self-play and automated feedback** before clinical trial.

---

## Comparison
**P014 broadens the perspective** of P001–P013 by:
1. **Verticalizing Agent Concepts:** While P001-P009 discuss general agents, P014 specifically defines the **roles and data pipelines** (ECG, EHR) required for *medical* agents.
2. **Contextualizing Performance:** It provides the critical counter-argument to P013 (Med-PaLM); while Med-PaLM encodes knowledge, P014 highlights that it still fails in **open-ended clinical tasks** compared to lightweight models.
3. **Multimodal Expansion:** Unlike P003 (ReAct) or P012 (MedRAG) which are primarily text-based, P014 bridges the gap to **physiological signals** and medical robotics.

---

## Important Figures
- **Figure 1:** Overview of practical guides. **Importance:** Shows the full lifecycle from pre-training to clinical agents.
- **Figure 3:** Performance Radar Chart. **Importance:** Visually proves that **general LLMs underperform** task-specific fine-tuned models in non-QA tasks.
- **Figure 4:** MedQA Accuracy Over Time. **Importance:** Tracks the "scaling up" of medical models toward expert levels.

---

## Important Tables
- **Table 1:** Summary of General LLMs. **Importance:** Categorizes architectures (encoder/decoder) for selection.
- **Table 2:** Summary of Medical-domain LLMs. **Importance:** Provides a **comprehensive list of datasets and models** for pre-training and fine-tuning.
- **Table 3:** Application-specific Guidelines. **Importance:** Maps specific models (e.g., **NYUTron**, **SuFIA**) to clinical tasks and metrics.

---

## Important References
- **Singhal et al. (2023) [Med-PaLM 2]:** Foundational for expert-level medical reasoning.
- **Touvron et al. (2023) [LLaMA]:** The most common base model for specialized medical agents.
- **Nori et al. (2023) [MedPrompt]:** Demonstrates that prompting can outcompete specialized tuning.
- **Wang et al. (2023) [Voyager]:** Cited as a basis for embodied agents that could apply to healthcare.

---

## Keywords
1. Medical LLM
2. Clinical Decision Support (CDS)
3. Patient Monitoring
4. Agentic AI
5. Multi-Agent Collaboration
6. RAG (Retrieval-Augmented Generation)
7. EHR (Electronic Health Record)
8. Multimodal LLM
9. Time-Series Data (ECG/PPG)
10. PEFT (Parameter-Efficient Fine-Tuning)
11. Hallucination Mitigation
12. Medical Robotics
13. Clinical Reasoning
14. Trustworthy AI
15. Physician-in-the-loop

---

## Personal Notes

### Ideas for My Thesis
- Implement the **"Bilingual Agent"** concept: A framework where one agent specializes in "Clinical Language" (EHR) and another in "Patient-Layperson Language".
- Use the **MIRAGE benchmark** approach to test my RAG implementation against real clinical guidelines.

### Future Research Ideas
- **"Proactive Monitoring Agents"**: Agents that don't just wait for queries but use **time-series integration** to alert clinicians to SOFA/NEWS2 changes.

### Chapter 2 Citations
- "Medical LLMs have achieved expert-level accuracy in USMLE exams, but significant advancement is required for integration into real-world open clinical practice".

### Supervisor Questions
- Since the survey notes that **lexical metrics are biased** for clinical reports, can we develop a "Consensus-based" metric using a MedAgent-style debate?

---

## Relevance Score
**10/10**
**Justification:** This is the most comprehensive healthcare-specific survey in the selection. It explicitly links LLM development to **clinical agents**, **patient monitoring**, and **multimodal data**, providing a direct roadmap for an Agentic AI thesis.


| ID | Year | Paper | Category | Research Problem | Proposed Solution | Memory | Planning | Reasoning | Tool Use | Multi-Agent | RAG | Healthcare | Evaluation | Research Gap | Relevance | Contribution to Thesis |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 014 | 2024 | A Survey of Large Language Models in Medicine: Progress, Application, and Challenge | Survey | A scarcity of comprehensive reviews regarding the development, practical applications, and outcomes of medical LLMs in clinical practice. | A systematic overview of medical LLM principles (pre-training, fine-tuning, prompting), performance across ten tasks, and specific guidelines for seven clinical scenarios. | Yes – Integration of external knowledge bases (UMLS, SNOMED CT) and retrieval components to provide persistent context and mitigate information decay. | Yes – High-level multi-agent planning for surgical collaboration and dynamic motion planning for medical robotics guided by LLM verbal commands. | Yes – Elicited through Chain-of-Thought (CoT) and In-Context Learning (ICL) to simulate diagnostic thought processes and expert-level logic. | External medical knowledge bases (UMLS, SNOMED CT), web search engines (Almanac), radiology vision encoders, and robotic control APIs. | Yes | Yes | Yes | Evaluated via comparison of LLM performance against human experts and lightweight models across professional exams (USMLE) and clinical metrics like AUC, F1, and ROUGE. | The critical need for integrating time-series data (ECG/PPG) and developing real-time monitoring capabilities for autonomous clinical decision-making. | 10 | Provides a foundational taxonomy of medical LLM capabilities and explicitly identifies the integration of time-series data and multi-agent collaboration as essential future directions for intelligent patient monitoring. |