# Paper 013

## Basic Information
- **Title:** Large Language Models Encode Clinical Knowledge
- **Authors:** Karan Singhal, Shekoofeh Azizi, Tao Tu, S. Sara Mahdavi, Jason Wei, Hyung Won Chung, Nathan Scales, Ajay Tanwani, Heather Cole-Lewis, Stephen Pfohl, Perry Payne, Martin Seneviratne, Paul Gamble, Chris Kelly, Nathaneal Schärli, Aakanksha Chowdhery, Philip Mansfield, Blaise Agüera y Arcas, Dale Webster, Greg S. Corrado, Yossi Matias, Katherine Chou, Juraj Gottweis, Nenad Tomasev, Yun Liu, Alvin Rajkomar, Joelle Barral, Christopher Semturs, Alan Karthikesalingam, and Vivek Natarajan
- **Year:** 2022 (Preprint/December 2022 results)
- **Venue:** Google Research / DeepMind Technical Report
- **DOI:** N/A (Source identifies as Google Research/DeepMind publication)
- **Link:** N/A (Provided as source 12)

---

## Abstract Summary (200–300 words)
This seminal paper addresses the high bar required for medical and clinical applications of Large Language Models (LLMs). The researchers observe that while LLMs show promise in natural language tasks, existing assessments of their clinical knowledge are often limited to narrow benchmarks and lack standardized evaluation for reasoning and factuality. To solve this, they introduce **MultiMedQA**, a comprehensive benchmark combining seven medical question-answering datasets: MedQA (USMLE), MedMCQA, PubMedQA, MMLU clinical topics, LiveQA, MedicationQA, and a new dataset of searched medical questions called **HealthSearchQA**.

The authors evaluate **PaLM** (540-billion parameters) and its instruction-tuned variant, **Flan-PaLM**, finding that Flan-PaLM achieves state-of-the-art (SOTA) accuracy across multiple-choice datasets, notably reaching **67.6% on MedQA (USMLE)**, which exceeded the previous SOTA by over 17%. However, human evaluation by a panel of clinicians revealed critical gaps in Flan-PaLM’s long-form responses, including risks of harm and misalignment with scientific consensus. To bridge this gap, the authors propose **instruction prompt tuning**, a parameter-efficient alignment technique that uses a few expert exemplars to specialize the model. The resulting model, **Med-PaLM**, significantly improves performance, aligning with scientific consensus in 92.6% of responses (comparable to clinicians at 92.9%) and drastically reducing potential harm from 29.7% in Flan-PaLM to 5.8%. The paper concludes that while LLMs demonstrate a powerful capacity to encode clinical knowledge, significant research into safety and evaluation frameworks is required before real-world clinical deployment.

---

## Research Problem
- **Importance of evaluating clinical knowledge:** Providing high-quality medical answers requires complex reading comprehension, recall of expert knowledge, and valid reasoning.
- **Challenges of general-purpose LLMs:** Existing AI models in healthcare are often single-task systems (classification or regression) that lack the expressivity and interactivity required for real-world clinical workflows.
- **Risks of incorrect medical reasoning:** LLMs can hallucinate convincing misinformation, incorporate biases, and produce responses that lead to patient harm if not properly aligned with clinical values.

---

## Motivation
- **Why the evaluation was conducted:** To quantify the "unmet need" for a broad benchmark that assesses LLMs on response factuality, precision, helpfulness, and potential for harm beyond simple automated metrics like BLEU.
- **Need for reliable medical reasoning:** The safety-critical nature of medicine necessitates "thoughtful development of evaluation frameworks" to measure progress and mitigate potential harm.
- **Importance of AI in healthcare:** Foundation models offer the promise of learning generally useful representations from medical corpora at scale, potentially assisting in retrieval, summarization, and decision support.

---

## Proposed Solution
- **MultiMedQA Benchmark:** A diverse benchmark spanning professional exams (MedQA), research (PubMedQA), and consumer queries (HealthSearchQA) to evaluate model reasoning along multiple axes.
- **Med-PaLM Model:** An instruction prompt-tuned version of Flan-PaLM designed to better follow clinical instructions.
- **Instruction Prompt Tuning:** A data-efficient method that learns "soft prompt vectors" while keeping the underlying LLM frozen, allowing for domain alignment with only a few dozen expert examples.
- **Human Evaluation Framework:** A pilot framework assessing performance across axes like scientific consensus, likelihood of harm, comprehension, reasoning, and bias.

---

## Core Analysis
- **LLM Reasoning:** Reasoning ability is found to be an "emergent ability" that improves with model scale and instruction tuning. The use of **Chain-of-Thought (CoT)** and **Self-Consistency (SC)** prompting is key to solving multi-step reasoning challenges.
- **Clinical Knowledge:** LLMs have the capacity to act as "implicit knowledge bases," recalling facts from a vast training corpus including webpages and medical books.
- **Memory:** Performance scaling suggests that models encode vast amounts of information, though they can reflect "past consensus" if the training data is static.
- **Planning:** The paper discusses "deferring" to experts or other sources when uncertainty is high (Selective Prediction), which is a crucial component of agentic planning.
- **Tool Usage:** While the paper focuses on the model as a standalone knowledge assistant, it acknowledges the need for future models to **retrieve from continuously evolving corpora**.

---

## Healthcare Applications
- **Intelligent Patient Monitoring:** Potential for summarizing complex medical communications and augmenting non-critical clinical assessments.
- **Clinical Decision Support (CDS):** Assisting clinicians by providing reasoning explanations and recalling pertinent expert knowledge.
- **Medical QA:** Providing grounded answers to consumer health queries.
- **Diagnostic Assistance:** Eliciting reasoning steps to solve USMLE-style vignettes.
- **Physician Decision Support:** Supplementing physician responses to patient queries by providing more detailed, comprehensive information.
- **Evidence-Based Medicine:** Aligning model outputs with established scientific consensus and clinical practice guidelines.

---

## Evaluation
- **Datasets:** MultiMedQA (MedQA, MedMCQA, PubMedQA, MMLU subtasks, LiveQA, MedicationQA, HealthSearchQA).
- **Benchmarks:** Professional exams (USMLE) and research literature (PubMed).
- **USMLE Performance:** Flan-PaLM 540B achieved **67.6% accuracy** on MedQA (4-option), outperforming previous SOTA (PubMedGPT) by 17.3%.
- **Accuracy:** Reached 82.5% accuracy on MedQA when allowed to "defer" (selective prediction) on uncertain cases.
- **Baselines/Physician Comparison:** Med-PaLM was judged as **aligned with scientific consensus in 92.6%** of cases, nearly on par with human clinicians (92.9%).

---

## Key Contributions
- Creation of the **MultiMedQA** benchmark and the **HealthSearchQA** dataset.
- Proposal of a **pilot human evaluation framework** for safety-critical medical assessments.
- Development of **Med-PaLM** through **instruction prompt tuning**, demonstrating a parameter-efficient alignment method.
- Empirical evidence that **medical reasoning scales** with model size and can be specialized with expert data.

---

## Strengths
- **Massive Scale:** Evaluated using a 540B parameter model, capturing a deep breadth of clinical knowledge.
- **Human-Centric:** Moves beyond automated NLP metrics (BLEU) to nuanced clinician evaluation of harm and reasoning.
- **Safety Focus:** Explicitly identifies and addresses "hallucination," "bias," and "potential harm".
- **Alignment:** Demonstrates that a small number of expert examples (40) can drastically shift model alignment.

---

## Limitations
- **Static Knowledge:** The model reflects scientific consensus at the time of its training, which may be outdated.
- **Language/Geography:** Evaluated only in English and primarily by clinicians from the US, UK, and India.
- **Lack of Interactivity:** Focuses on single-turn QA rather than the multi-turn "closed-loop" interaction typical in real-world workflows.
- **Subjectivity:** Human ratings of harm and bias are subjective and can vary by culture and experience.

---

## Research Gap
- **Agentic AI:** The paper focuses on the model as a knowledge assistant; there is a gap in evaluating it as an **autonomous agent** interacting with live clinical environments.
- **RAG:** Admits the need for **retrieval from continuously evolving corpora** to ensure up-to-date knowledge.
- **Memory:** No evaluation of **long-term patient-specific memory** or state tracking across a care trajectory.
- **Clinical Workflows:** Lacks benchmarks reflecting the "eliciting information from patients" and "synthesizing findings into an assessment and plan" found in daily practice.
- **Real-time Monitoring:** The tasks are static QA; there is no evaluation for **continuous monitoring** or high-frequency data analysis.

---

## How This Supports My Thesis

### Concepts to Adopt
- The **Human Evaluation Framework axes** (Harm, Consensus, Bias) for auditing my agentic framework.
- **Instruction Prompt Tuning** as a way to specialize my monitoring agent for specific ICU or ward-based protocols.
- **Selective Prediction/Uncertainty:** Deferring to a human clinician when the monitoring agent detects an ambiguous or life-threatening signal.

### Concepts to Modify
- **Task Source:** Instead of using medical exam questions, modify the benchmark to include **simulated patient monitoring signals** and triage vignettes.
- **Role Specificity:** Specialize prompts not just for "medical assistant" but for specific roles like "ICU Monitoring Nurse" or "Triage Coordinator".

### Concepts Not Suitable
- **Static Parametric Knowledge:** Relying solely on internal model weights is unsuitable for my thesis's focus on **evidence-based, real-time monitoring**.
- **Single-turn QA:** My framework requires multi-turn, longitudinal interaction rather than isolated question-answer pairs.

### Proposed Improvements
- **RAG Integration:** Combine Med-PaLM’s strong reasoning with a **MedRAG** or **Vector DB** approach to ground decisions in real-time patient charts and the latest guidelines.
- **FHIR/EHR Interoperability:** Connect the model's reasoning capabilities to **FHIR APIs** to allow the agent to "retrieve" and "act" on actual patient data.
- **Multi-Agent Orchestration:** Use a **Med-PaLM-level "Brain"** to coordinate between a Monitoring Agent (vitals) and a Safety Agent (guidelines), similar to the roles in **AutoGen/CAMEL**.
- **Long-Term Memory:** Incorporate a "Patient Context" module to provide the model with longitudinal history, addressing the "patient-specific reasoning" gap.

---

## Comparison
- **Vs. ReAct (P003) & Toolformer (P004):** While P003/P004 focus on the *mechanism* of tool use and action, Paper 013 provides the **foundational clinical knowledge** that makes those actions safe and accurate in a medical context.
- **Vs. MedRAG (P012):** MedRAG addresses the "static knowledge" limitation of Med-PaLM by providing a retrieval layer for current evidence-based grounding.
- **Vs. Agent Hospital (P011) & MedAgent (P010):** P011/P010 focus on *collaboration and simulation*; Paper 013 (Med-PaLM) is the likely "best-in-class" candidate for the **individual model intelligence** that would inhabit those agents.
- **Comparison Summary:** Strong clinical knowledge (as seen in Med-PaLM) is the prerequisite for reliable **Agentic AI**. Without the high reasoning bar set by Med-PaLM, agentic tools (like ReAct) are at higher risk of "hallucinating" incorrect clinical actions.

---

## Important Figures
- **Figure 1:** Overview of MultiMedQA and Med-PaLM contributions. **Importance:** Shows the leap in MedQA (USMLE) performance (67.6%).
- **Figure 5:** Selective prediction/uncertainty analysis. **Importance:** Demonstrates that models "mostly know what they know," allowing for **safe deferral to humans**.
- **Figure 6:** Clinician evaluation of consensus. **Importance:** Proves the necessity of **instruction prompt tuning** to reach clinician-level alignment.

---

## Important Tables
- **Table 2:** Human Evaluation Axes. **Importance:** Provides a standardized rubric for **medical agent auditing**.
- **Table 4:** Comparison on MedQA. **Importance:** Shows Med-PaLM (Flan-PaLM) vastly outperforming PubMedGPT and Galactica.
- **Table 9:** Med-PaLM Response Examples. **Importance:** Illustrates the **detailed, grounded long-form reasoning** required for CDS.

---

## Important References
- **Wei et al. (2022b) [Chain-of-Thought]:** Foundational for the reasoning architecture.
- **Chowdhery et al. (2022) [PaLM]:** The base model architecture.
- **Lester et al. (2021) [Prompt Tuning]:** The technical basis for Med-PaLM specialization.
- **Jin et al. (2021) [MedQA]:** The source of the USMLE-style benchmark.

---

## Keywords
1. Med-PaLM
2. MultiMedQA
3. Clinical Knowledge Encoding
4. Instruction Prompt Tuning
5. Medical Question Answering
6. USMLE Benchmarking
7. Scientific Consensus Alignment
8. Potential Harm Mitigation
9. Safety-Critical LLMs
10. Chain-of-Thought Reasoning
11. Selective Prediction
12. Uncertainty Communication
13. HealthSearchQA
14. Foundation Models in Medicine
15. Clinical Decision Support

---

## Personal Notes

### Ideas for My Thesis
- Use **MultiMedQA** to benchmark the "internal knowledge" of my agent before adding external tools like RAG.
- Implement the **Selective Prediction** mechanism as a "Human-in-the-Loop" trigger: when the model confidence is <0.45, it must alert a clinician rather than acting autonomously.

### Future Research
- Multilingual expansion of medical monitoring agents to support global healthcare equity.
- Continual learning frameworks to keep the "Consensus" current with medical breakthroughs.

### Chapter 2 Citations
- "LLMs demonstrate the ability to act as implicit knowledge bases... however, instruction prompt tuning is required to align these models with scientific consensus and clinical safety".
- "State-of-the-art performance on professional medical exams (MedQA) reached 67.6%, suggesting that medical reasoning is an emergent ability of scale".

### Supervisor Questions
- Can we adapt the **Instruction Prompt Tuning** technique to learn "Monitoring Primitives" from nurse-led patient summaries?
- How do we handle the **Bias axis** (7.9% in Flan-PaLM) in a real-time monitoring system that might be biased toward specific patient demographics?

---

## Relevance Score
**10/10**
**Justification:** This paper defines the **clinical intelligence baseline** for LLMs. For a thesis on an Agentic AI Framework, this paper provides the essential **evaluation methodology** and the **alignment techniques** necessary to ensure the "Brain" of the agent is clinically safe and scientifically grounded.


| ID | Year | Paper | Category | Research Problem | Proposed Solution | Memory | Planning | Reasoning | Tool Use | Multi-Agent | RAG | Healthcare | Evaluation | Research Gap | Relevance | Contribution to Thesis |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| P013 | 2023 | Large Language Models Encode Clinical Knowledge | Framework | Lack of standardized benchmarks and evaluation frameworks to assess medical LLM reasoning, leading to potential harm and misalignment with clinical consensus,. | Introduction of the MultiMedQA benchmark, HealthSearchQA dataset, and "instruction prompt tuning" to create the domain-aligned Med-PaLM model,. | No | No | Yes – Elicited through few-shot Chain-of-Thought (CoT) prompting for step-by-step clinical logic and self-consistency to marginalize reasoning paths,. | No | No | No | Yes | Combined automated accuracy on professional exams with a rigorous human evaluation framework assessing factuality, reasoning, harm, and bias,. | Grounding AI responses in authoritative, time-varying medical sources and developing the ability to communicate uncertainty to human-in-the-loop users. | 10 | Establishes the foundational benchmarking and human-centric evaluation standards required to validate the clinical reasoning and safety of patient monitoring agents. |