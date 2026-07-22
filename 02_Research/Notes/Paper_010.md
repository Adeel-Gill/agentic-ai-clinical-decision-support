# Paper 010

## Basic Information
- **Title:** MEDAGENTS: Large Language Models as Collaborators for Zero-shot Medical Reasoning
- **Authors:** Xiangru Tang, Anni Zou, Zhuosheng Zhang, Ziming Li, Yilun Zhao, Xingyao Zhang, Arman Cohan, Mark Gerstein
- **Year:** 2024 (based on references to 2024 literature)
- **Venue:** Preprint (Yale University / Shanghai Jiao Tong University)
- **DOI:** N/A (Project link provided)
- **Link:** [https://github.com/gersteinlab/MedAgents](https://github.com/gersteinlab/MedAgents)

---

## Abstract Summary (200–300 words)
**MedAgents** is a novel **multi-disciplinary collaboration framework** designed to overcome the barriers Large Language Models (LLMs) face in medicine, such as specialized terminology and complex knowledge reasoning. Unlike general-purpose prompting, MedAgents utilizes a **role-playing** setting where multiple LLM-based agents participate in a collaborative, multi-round discussion to enhance their proficiency. This framework is **training-free** and operates in the **zero-shot setting**, making it highly applicable to real-world medical scenarios where labeled data may be scarce or private.

The process follows five critical stages: **(i) gathering domain experts** based on the clinical inquiry, **(ii) proposing individual analyses**, **(iii) summarizing these analyses** into a cohesive report, **(iv) iterating over discussions** to reach a consensus, and **(v) making a final decision** based on a unanimous report. The authors evaluated MedAgents across nine diverse medical datasets, including **MedQA (USMLE), MedMCQA, and PubMedQA**. Results demonstrate that this collaborative approach significantly outperforms traditional prompting methods like **Chain-of-Thought (CoT)** and **Self-Consistency (SC)**. Crucially, the framework mitigates **hallucinations** by anchoring the reasoning process in a multidisciplinary debate, effectively mining the medical expertise already embedded within the LLM's parameters without requiring external retrieval-augmented generation (RAG). This architecture provides enhanced **faithfulness and interpretability**, offering a "consultation-like" reasoning trace for clinical decision support.

---

## Research Problem
- **Problem:** LLMs struggle with domain-specific medical tasks that require **complex reasoning** over specialized knowledge and terminologies.
- **Why single LLMs fail:** Medical training data is limited compared to general corpora due to **privacy and cost**, and medical expertise is difficult to elicit via simple prompting.
- **Hallucination risks:** Single-agent strategies like CoT are prone to **hallucination**, where the model misapplies medical terminology or creates spurious rationales.
- **Need for collaborative diagnosis:** Medical reality relies on **multi-disciplinary consultation**; single-agent models lack the collective power to verify information across different medical sub-specialties.

---

## Motivation
- **Why MedAgent:** To simulate the **consultation mechanism** common in hospitals, where experts from different disciplines reach consistent conclusions.
- **Limitations of existing methods:** Closed-source models like **Med-PaLM 2** are inaccessible, and standard CoT often leads to performance degradation in zero-shot medical settings due to a lack of grounded domain knowledge.
- **Importance of reliable healthcare AI:** High-stakes medical decisions require models that are not only accurate but also **interpretable and faithful** to clinical logic.

---

## Proposed Solution
- **MedAgent framework:** A training-free paradigm that leverages a **society of agents** to solve clinical questions.
- **Multi-agent reasoning:** Uses **role-playing** to assign specific clinical roles (e.g., Cardiology, Radiology) to the model.
- **Debate & Consensus:** Agents engage in **multi-round discussions** (Collaborative Consultation) where they vote and propose revisions until a consensus is reached.
- **Evidence gathering:** Instead of external tools, it mines the **intrinsic medical knowledge** latent in the model's parameters.
- **Decision refinement:** The final decision is derived from a **unanimous report** approved by all virtual experts.
- **Comparison:** Unlike **ReAct**, MedAgents focuses on multi-agent social interaction; unlike **AutoGen** or **MetaGPT**, it is specifically tailored to the nuances of clinical reasoning and medical exams.

---

## Architecture
- **Expert Agents:** Divided into **Question Domain experts** (specialized in the patient scenario) and **Option Domain experts** (specialized in the possible diagnoses).
- **Coordinator:** A "Medical Assistant" role that synthesizes reports from individual expert analyses.
- **Discussion:** Iterative review rounds where agents vote **"YES" or "NO"** on the synthesized report.
- **Consensus:** Managed via **Algorithm 1**, which cycles through voting, modification proposals, and report updates until consensus or a maximum attempt threshold is met.
- **Patient information flow:** Input Question → Domain Classification → Expert Analysis → Synthesized Report → Collaborative Discussion → Unanimous Report → Final Answer.

---

## Core Components
- **Medical Reasoning:** Enhanced by **multi-disciplinary perspectives** which prevent "early closure" on a diagnosis.
- **Memory:** Maintained as a **shared conversational context** (The Synthesized Report) that is updated iteratively.
- **Planning:** A structured **5-stage pipeline** (Gathering, Analysis, Summary, Consultation, Decision).
- **Tool Usage:** **Note:** The core MedAgents framework is **training-free and does not use RAG**. However, the paper discusses related work using external tools like **PubMed, NCBI APIs, and Medical Guidelines (Almanac)** as complementary approaches.
- **Multi-Agent Collaboration:** The heart of the system, using **role-playing and communication** to reduce hallucinations.

---

## Healthcare Applications
- **Clinical Decision Support (CDS):** Providing interpreted condition reports for complex cases, such as a 66-year-old with heart history and potential lung tumor.
- **EHR & Medical Knowledge:** Mining implicit knowledge related to **Cardiology, Gastroenterology, Surgery, and Radiology**.
- **Clinical Guidelines:** Mimicking hospital consultation mechanisms to ensure adherence to standards.
- **Lab Results & Imaging:** Interpreting **CT scan** indications and lab-based symptoms.
- **Specialized Care:** Examples provided for **Pediatrics (3-month-old infant)**, **Psychiatry (anxiety/SSRI management)**, and **Otolaryngology**.
- **Drug Interaction Checking:** Discussed in a case study regarding **Citalopram vs. Propranolol** for long-term anxiety management.

---

## Evaluation
- **Datasets:** MedQA (USMLE), MedMCQA, PubMedQA, and 6 MMLU subtasks (Anatomy, Genetics, etc.).
- **Benchmarks:** Outperforms **Zero-shot CoT** and matches **Few-shot CoT + SC** on GPT-4.
- **Metrics:** **Accuracy (Acc)** across nine datasets.
- **Baselines:** Zero-shot, Few-shot, CoT, and Self-Consistency.
- **Clinical accuracy:** Demonstrates "decent correctional capabilities" where collaborative discussion fixes errors made in single-agent turns.

---

## Key Contributions
1. First framework to propose a **multi-agent medical QA system** specifically for multi-disciplinary consultation.
2. Introduction of **multi-disciplinary role-playing** to mine latent LLM knowledge without external training or RAG.
3. Demonstration that **multi-agent consensus** effectively reduces hallucinations and improves medical reasoning faithfulness.

---

## Strengths
- **Interpretability:** Provides a clear, collaborative reasoning trajectory (The Unanimous Report).
- **Zero-shot Performance:** Achieves high accuracy without needing few-shot exemplars, which is ideal for novel clinical scenarios.
- **Robustness:** Role-playing allows the model to act with **accurate knowledge** more effectively than step-by-step CoT.

---

## Limitations
- **Dynamic Knowledge:** Parameterized knowledge in the LLM may become **outdated**.
- **Cost & Latency:** Approximately **$1.41 per 100 questions** with a 40s inference time per example, which is higher than direct prompting.
- **Language Limits:** Limited applicability in **low-resource languages**.
- **Error Types:** Still susceptible to **lack of domain knowledge (45%)** and **mis-retrieval of knowledge (32%)**.

---

## Research Gap
- **Explainability:** While the report is readable, there is a gap in mapping these "thoughts" to **formal clinical standards**.
- **Patient Safety:** Lack of a **hard-stop mechanism** for life-critical errors beyond the consensus loop.
- **Real-time Monitoring:** The framework is currently **static/QA-based** and not integrated for continuous patient monitoring.
- **Hospital Integration:** No formal framework for **FHIR/EHR API** integration in the current study.

---

## How This Supports My Thesis

### Concepts to Adopt
- **Expert Gathering Stage:** Dynamically assigning roles based on patient data (e.g., if vitals show arrhythmia, recruit a Cardiology Agent).
- **Collaborative Consultation:** A mechanism for **conflict resolution** between different clinical agents.

### Concepts to Modify
- **Action Space:** Instead of just outputting an "Answer," the agent should generate **FHIR-compliant orders** or **Monitoring Alerts**. (**Information outside the paper:** Integration with FHIR APIs).
- **Consensus Threshold:** For critical monitoring, the threshold for consensus might need to be **higher** or involve a human clinician.

### Concepts Not Suitable
- **Exclusively Parameterized Knowledge:** In a real clinical setting, relying solely on LLM weights is risky; **RAG integration** is necessary to ensure guidelines are current.

### Proposed Improvements
- **Integration with FHIR:** Use the "Expert Gathering" module to trigger agents that specifically query **EHR/FHIR resources** (e.g., a "Lab Agent" that calls a FHIR `Observation` resource).
- **Long-Term Memory:** Add a **Long-Term Memory** module to store a patient's longitudinal history, which agents can "consult" during the discussion.
- **Reflection & RAG:** Combine MedAgents with **RAG** so the expert analyses are grounded in the latest **Clinical Guidelines** rather than just pre-trained weights.
- **Multi-Agent Monitoring:** Deploy a continuous loop where a **Monitoring Agent** constantly updates the "Initial Report" for the consultation team.

---

## Comparison
- **Vs. ReAct [P003]:** ReAct is a single-agent cycle; MedAgents is a **collaborative multi-agent debate**.
- **Vs. AutoGen [P006]:** AutoGen is a general framework; MedAgents provides a **specialized clinical pipeline**.
- **Vs. CAMEL [P007]:** MedAgents adopts the role-playing concept but applies it to **medical consensus** rather than general task completion.

---

## Important Figures
- **Figure 1:** Diagram of the 5-stage framework. **Importance:** Illustrates the architectural pipeline for collaborative reasoning.
- **Figure 3:** Influence of the number of agents. **Importance:** Shows that **5 question agents and 2 option agents** are optimal for medical accuracy.
- **Figure 4:** Error analysis pie chart. **Importance:** Reveals that **77% of errors** are knowledge-based, justifying the need for future RAG integration.

---

## Important Tables
- **Table 2:** Main Results. **Importance:** Proves MedAgents outperforms zero-shot baselines by a **large margin**.
- **Table 3:** Ablation Study. **Importance:** Shows that **Analysis Proposition** is the most critical step for performance gains.

---

## Important References
- **Singhal et al. (2023a) [Med-PaLM]:** The state-of-the-art medical LLM baseline.
- **Wei et al. (2022) [CoT]:** The foundational reasoning baseline.
- **Kojima et al. (2022) [Zero-shot CoT]:** The primary zero-shot comparison.
- **Li et al. (2023b) [CAMEL]:** Basis for role-playing agents.

---

## Keywords
1. MedAgents
2. Multi-disciplinary Collaboration
3. Multi-Agent Systems
4. Role-playing
5. Clinical Reasoning
6. Zero-shot Medical Reasoning
7. Consensus Decision Making
8. Medical QA
9. Hallucination Reduction
10. Interpretability
11. Faithfulness
12. Multi-round Discussion
13. Expert Gathering
14. Clinical Decision Support
15. Patient Monitoring (Potential)

---

## Personal Notes

### Ideas for Thesis
- Use the **Expert Gathering** module to create a "Virtual ICU Round" where agents representing different specialties (Respiratory, Nursing, Pharmacy) review vital sign trends.
- Implement the **Collaborative Consultation** loop as a "Clinical Safety Gate" for an agentic framework.

### Future Research
- Testing MedAgents on **real-time streaming clinical data** rather than static USMLE questions.
- Integrating a **"Guideline Agent"** that uses RAG to provide a factual anchor for the other role-playing experts.

### Chapter 2 Citations
- "MEDAGENTS outperforms the zero-shot baseline methods by a large margin... effectively mitigating hallucinations associated with the misapplication of medical terminologies".

### Supervisor Questions
- Can we replace the "Option Domain Expert" with a **"Safety Auditor Agent"** for real-time monitoring?
- How do we handle situations where the **Consensus Loop** fails to converge within an acceptable time for emergency care?

---

## Relevance Score (10/10)
**MedAgents** is the most direct application of **Agentic AI** to the core problem of **Clinical Decision Support**. It provides a validated architectural pattern for multidisciplinary collaboration, which is a cornerstone of your proposed thesis framework.