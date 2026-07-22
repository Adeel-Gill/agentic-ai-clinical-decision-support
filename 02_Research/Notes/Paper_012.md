# Paper 012

## Basic Information
- **Title:** MedRAG: Enhancing Retrieval-augmented Generation with Knowledge Graph-Elicited Reasoning for Healthcare Copilot
- **Authors:** Xuejiao Zhao, Siyan Liu, Su-Yin Yang, Chunyan Miao
- **Year:** 2024 (Access dates in references are Oct 2024)
- **Venue:** Nanyang Technological University / Tan Tock Seng Hospital
- **DOI:** N/A
- **Link:** [https://github.com/SNOWTEAM2023/MedRAG](https://github.com/SNOWTEAM2023/MedRAG)

## Abstract Summary (200–300 words)
**MedRAG** is a specialized Retrieval-Augmented Generation (RAG) framework designed to serve as a **healthcare copilot** by significantly reducing misdiagnosis through **knowledge graph (KG)-elicited reasoning**. While standard RAG systems are effective for retrieving information from Electronic Health Records (EHR), they often struggle with diagnostic specificity, particularly when different diseases present with similar clinical manifestations. MedRAG addresses this by systematically constructing a **four-tier hierarchical diagnostic knowledge graph** that captures critical diagnostic differences between diseases.

The framework operates by dynamically integrating similar EHR records retrieved from a database with these structured diagnostic differences, which are then reasoned over by a Large Language Model (LLM). This dual-stream approach—combining raw patient data with inferable medical logic—allows the system to identify subtle clinical nuances. Furthermore, MedRAG includes a **proactive diagnostic questioning mechanism**; when patient data is insufficient or ambiguous, the system generates targeted follow-up questions to clarify manifestations and refine the diagnosis. Evaluated on the public **DDXPlus** dataset and a private **Chronic Pain Diagnostic Dataset (CPDD)**, MedRAG outperformed existing state-of-the-art RAG models in both accuracy and specificity. The study demonstrates that grounding LLM predictions in structured, inferable medical data is essential for delivering reliable clinical decision support in complex medical scenarios.

## Research Problem
- **Hallucinations in medical LLMs:** Existing heuristic-based RAG and fine-tuned LLMs often rely on superficial patterns, leading to incorrect or vague outputs when diseases share similar manifestations.
- **Need for evidence-based reasoning:** Cognitive biases and judgmental mistakes contribute to nearly 800,000 cases of permanent disability or death due to misdiagnosis annually in the U.S. alone.
- **Limits of parametric knowledge:** LLMs alone lack the detailed, structured information necessary for distinguishing between complex cases with overlapping symptoms.
- **Trustworthy clinical AI:** There is a critical need for systems that can ground their predictions in verifiable medical data and structured ontologies.

## Motivation
- **Why MedRAG:** To provide a "Healthcare Copilot" that assists practitioners in navigating the most challenging diagnostic tasks, specifically differentiating between diseases with high manifestation similarity.
- **External medical knowledge:** By utilizing domain-specific private datasets (EHRs) and structured knowledge graphs, the system bypasses the need for costly additional model training.
- **Reliable clinical decision support:** Effective RAG must go beyond simple "retrieve-and-read" to include a reasoning mechanism that can resolve ambiguity.
- **Benefits of RAG:** It grounds predictions in current medical data, providing specificity and context-aware outputs.

## Proposed Solution
- **MedRAG Framework:** Interleaves traditional EHR retrieval with a specialized **Diagnostic Differences KG Searching** module.
- **Retrieval Pipeline:** Uses **FAISS** for efficient approximate nearest neighbor searches across large-scale EHR datasets.
- **Knowledge Integration:** Integrates retrieved documents ($d_r$) with structured diagnostic differences ($K$) to trigger LLM reasoning.
- **Evidence-Based Reasoning:** A four-tier KG (Broader Categories, Subcategories, Diseases, and Features) provides the logical backbone.
- **Answer Generation:** Outputs include precise diagnoses, personalized treatment recommendations, and medication guidance.
- **Hallucination Reduction:** Grounding in strucutred diagnostic differences allows the model to identify subtle differences (e.g., pain alleviated vs. exacerbated by sitting) that prevent misapplication of terminology.
- **Comparison:** Unlike **ReAct** (P003) or **Toolformer** (P004), which focus on general task execution, MedRAG is specifically architected for the **diagnostic granularity** required in clinical medicine.

## Architecture
- **User Query:** Descriptions of patient manifestations (structured EHR or unstructured text).
- **Retriever:** A module that fetches top-$k$ relevant EHR records based on patient embeddings.
- **Medical Knowledge Base:** A hierarchical KG constructed through disease clustering and LLM augmentation.
- **Reranker/Searcher:** A module that performs multi-level manifestation matching and **upward traversal** to identify the most relevant disease subcategory.
- **LLM:** Serves as the "reasoning engine" that synthesizes query, EHR data, and KG logic.
- **Response Generator:** Produces reports following a structured template (Diagnoses, Explanations, Follow-up Questions, Treatments).

## Core Components
- **RAG:** Includes retrieval of EHRs, upward traversal for KG grounding, context injection of diagnostic differences, and response synthesis.
- **Medical Knowledge Sources:** Derived from **EHR databases**, augmented by LLMs, and organized using principles inspired by **ICD-11**.
- **Memory:** Utilizes a persistent **EHR Indexing (FAISS)** and the static **Diagnostic Knowledge Graph** as long-term storage.
- **Planning:** Implemented through the **Proactive Diagnostic Questioning Mechanism**, which ranks features by discriminability to plan follow-up inquiries.
- **Tool Usage:** **FAISS** for vector search, medical chunking for manifestation decomposition, and the **KG Searching module** as an internal expert tool.

## Healthcare Applications
- **Intelligent Patient Monitoring:** Real-time extraction of manifestations from consultation dialogues to provide proactive diagnostic suggestions.
- **Clinical Decision Support:** Differentiating between complex spinal conditions like **lumbar canal stenosis** and **sciatica**.
- **EHR:** Automated extraction of patient manifestations from uploaded JSON medical records.
- **ICU Monitoring (Potential):** Monitoring "passively" to provide real-time suggestions based on dialogue content.
- **Laboratory Interpretation:** "Manifestations" include Measurable clinical data and lab results used for diagnostic reasoning.
- **Medication Safety:** Generating medication guidance based on diagnosed conditions.
- **Chronic Disease Management:** Specifically validated on a **Chronic Pain Diagnostic Dataset**.

## Evaluation
- **Datasets:** **DDXPlus** (1.3M synthesized patients) and **CPDD** (private hospital data).
- **Benchmarks:** Compared against **FL-RAG, FS-RAG, FLARE, DRAGIN**, and **SR-RAG**.
- **Metrics:** Accuracy (L1-L3 granularity), BERTScore, BLEU, ROUGE, and METEOR.
- **Accuracy:** MedRAG outperformed second-best models by **11.32%** on the CPDD dataset.
- **Hallucination Reduction:** Specificity was improved across all levels through KG integration.
- **Baselines:** Naive RAG + CoT was used as a foundational baseline.

## Key Contributions
1. Proposed the **MedRAG framework**, which synergizes KG reasoning with RAG for high-specificity diagnostics.
2. Developed a **systematic 4-tier KG construction method** that organizes diseases by manifestation similarity rather than just traditional ontology.
3. Introduced a **Proactive Diagnostic Questioning Mechanism** based on feature discriminability scores.
4. Demonstrated robust **generalization** across various backbone LLMs (Mixtral, Llama, GPT-4).

## Strengths
- **Granular Specificity:** Capable of differentiating diseases with nearly identical symptoms.
- **Proactive Interactivity:** Doesn't just answer; it asks the *right* questions to reduce clinical ambiguity.
- **Scalability:** The KG construction method is adaptable to various medical specialties and local hospital databases.
- **Interpretability:** Provides a clear reasoning trace that links patient data to specific diagnostic differences.

## Limitations
- **Granularity Conflict:** Smaller models (GPT-3.5) may struggle with very high granularity, leading to knowledge conflicts.
- **Static KG:** While the retrieval is dynamic, the KG construction requires a systematic initial build.
- **Single Modality:** Currently focused on text/EHR data; does not yet incorporate medical imaging or physiological signals.

## Research Gap
- **Real-time retrieval:** While FAISS is fast, the paper identifies "real-world hospital testing" as a future step.
- **Personalized patient knowledge:** The KG is disease-centric; there is a gap in integrating a patient's **unique longitudinal history** into the graph structure.
- **Continuous monitoring:** Current evaluation is episodic; adaptation to **continuous high-acuity data** remains a challenge.
- **Multi-agent RAG:** The framework is primarily single-agent with modular tools; it does not explicitly use a **MedAgent** (P010) style debate.
- **Healthcare interoperability:** Standardized integration via **FHIR APIs** is not explicitly detailed.

## How This Supports My Thesis

### Concepts to Adopt
- **Hierarchical Knowledge Graphs for Monitoring:** Using a 4-tier KG to differentiate between acute deterioration states in patient monitoring.
- **Discriminability-based Questioning:** If monitoring data is noisy or missing, use the agent to request specific nurse observations or lab tests based on which "feature" is most discriminative.

### Concepts to Modify
- **Action Space:** Extend the "Output" to include automated **FHIR-compliant alerts** and updates to the EHR.
- **Knowledge Sources:** Supplement the hospital EHR database with real-time **Vital Sign Streams** as a retrieval source.

### Concepts Not Suitable
- **Topic Aggregation for Disease Clustering:** May be too slow for emergency "on-the-fly" clinical reasoning; a pre-validated medical ontology might be safer for acute care.

### Proposed Improvements
- **MedAgent Integration:** Use a **MedAgent** (P010) style expert team to validate the "Diagnostic Differences" retrieved by the MedRAG module.
- **RAG + ReAct:** Combine MedRAG's evidence-based retrieval with **ReAct** (P003) loops to allow the agent to "act" (e.g., order a test) based on the "Follow-up questions."
- **FHIR RAG:** Implement the retriever to specifically query **FHIR resources** (Observations, Medications) to build a truly interoperable Agentic AI Framework.

## Comparison
- **Vs. ReAct (P003) & Toolformer (P004):** MedRAG provides **structured medical grounding** that simple thought-action loops or general API calls lack.
- **Vs. MedAgent (P010):** While MedAgent mines *internal* LLM knowledge, MedRAG prioritizes **external EHR and KG grounding**, making it more suitable for evidence-based practice.
- **Vs. Agent Hospital (P011):** MedRAG is a **modular reasoning framework** that could be implemented *within* the "Doctor Agents" of Agent Hospital to enhance their expertise.

## Important Figures
- **Figure 1:** Comparison of heuristic-based RAG vs. MedRAG. **Importance:** Visually demonstrates how KG reasoning resolves diagnostic "Vagueness".
- **Figure 2:** Overall MedRAG Framework. **Importance:** Architectural blueprint for integrating KG searching with EHR retrieval.
- **Figure A3:** KG of Lumbar Canal Stenosis vs. Sciatica. **Importance:** Shows how a "Key Diagnostic Difference" (sitting response) is used in reasoning.

## Important Tables
- **Table 1:** Quantitative comparison results. **Importance:** Proves MedRAG's superior accuracy at the L3 (highest specificity) level.
- **Table 2:** Impact of KG-elicited reasoning on different LLMs. **Importance:** Shows that KG integration is the **"reasoning multiplier"** regardless of the backbone model.

## Important References
- **Lewis et al. (2020):** Original RAG paper—the foundation for MedRAG's retrieval.
- **Tang et al. (2024):** MedAgent—the competitive baseline for medical reasoning.
- **Wei et al. (2022):** Chain-of-Thought—the logic foundation for MedRAG's prompts.

## Keywords
1. MedRAG
2. Retrieval-Augmented Generation
3. Knowledge Graph
4. Clinical Decision Support
5. Healthcare Copilot
6. EHR Retrieval
7. Diagnostic Specificity
8. Proactive Questioning
9. Evidence-based AI
10. Misdiagnosis Reduction
11. Manifestation Decomposition
12. Hierarchical Aggregation
13. Discriminability Score
14. Patient Monitoring (Potential)
15. FAISS

## Personal Notes
- **Ideas for Thesis:** Implement a **"Vital-Sign KG"** where the nodes are physiological states (e.g., Tachycardia) and the differences are causes (e.g., Sepsis vs. Dehydration).
- **Future Research:** How does MedRAG handle **conflicting evidence** (e.g., EHR says one thing, patient says another during proactive questioning)?
- **Chapter 2 Citations:** "MedRAG systematically retrieves diagnosis and treatment recommendations by dynamically integrating similar EHRs with a hierarchical diagnostic knowledge graph".
- **Supervisor Questions:** How do we ensure the **"LLM Augmentation"** of the KG (EL4a) doesn't introduce its own hallucinations into the grounded source?

## Relevance Score
**10/10**
**Justification:** For a thesis on clinical decision support, this is the state-of-the-art framework for **evidence-based grounding**. It provides the exact mechanism needed to solve the "hallucination vs. specificity" trade-off in medical agents.

| ID | Year | Paper | Category | Research Problem | Proposed Solution | Memory | Planning | Reasoning | Tool Use | Multi-Agent | RAG | Healthcare | Evaluation | Research Gap | Relevance | Contribution to Thesis |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| P012 | 2024 | MedRAG: Enhancing Retrieval-augmented Generation with Knowledge Graph-Elicited Reasoning for Healthcare Copilot | Framework | Existing RAG models in healthcare lack diagnostic specificity and accuracy, particularly when diseases share similar manifestations. | MedRAG, a framework that integrates a four-tier hierarchical diagnostic knowledge graph (KG) with retrieval-augmented generation to elicit specific clinical reasoning. | Yes – Uses a structured four-tier Diagnostic Knowledge Graph and FAISS-indexed EHR database to provide inferable and verifiable medical context. | Yes – Proactive Diagnostic Questioning Mechanism that identifies missing information by selecting clinical features with high discriminability scores to guide follow-up questions. | Yes – KG-elicited reasoning within an LLM engine that integrates retrieved historical EHRs with critical diagnostic differences extracted from the KG. | EHR databases, FAISS (approximate nearest neighbor search), Knowledge Graphs, and various LLM backbones (e.g., GPT-4o, Llama-3.1). | No | Yes | Yes | Performance was assessed via accuracy and specificity metrics on public (DDXPlus) and private (chronic pain) datasets alongside subjective clinical evaluations. | Incorporating multimodal data (imaging and physiological signals) and integrating speech recognition for real-time passive monitoring during consultations. | 10 | Provides a methodology to ground clinical decision-making in structured medical knowledge, ensuring high specificity and proactive monitoring in an agentic framework. |