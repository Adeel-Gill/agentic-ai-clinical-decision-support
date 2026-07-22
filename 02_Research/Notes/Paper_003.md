# Paper 003

## Basic Information
- **Title:** ReAct: Synergizing Reasoning and Acting in Language Models
- **Authors:** Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik Narasimhan, Yuan Cao
- **Year:** 2022
- **Journal:** Published at ICLR 2023 (Source notes it as a 2022 preprint)
- **DOI:** N/A
- **Link:** [https://react-lm.github.io/](https://react-lm.github.io/)

---

## Abstract Summary (200–300 words)
The paper introduces **ReAct**, a novel paradigm for large language models (LLMs) that combines **verbal reasoning traces** and **task-specific actions** in an interleaved manner. While previous research treated reasoning (e.g., Chain-of-Thought) and acting (e.g., action plan generation) as separate capabilities, ReAct explores their **synergy**. In this framework, reasoning traces allow the model to induce, track, and update action plans while handling exceptions, whereas actions enable the model to interface with external sources like **knowledge bases or environments** to gather grounded information.

The authors evaluate ReAct across a diverse set of tasks, including multi-hop question answering (**HotpotQA**), fact verification (**FEVER**), and interactive decision-making benchmarks (**ALFWorld and WebShop**). On knowledge-intensive tasks, ReAct mitigates common LLM issues such as **hallucination and error propagation** by interacting with a Wikipedia API to ground its reasoning in factual observations. On interactive decision-making tasks, it significantly outperforms traditional imitation and reinforcement learning methods—achieving absolute success rate improvements of up to **34%**—while requiring only a few in-context examples. Furthermore, ReAct enhances **interpretability and trustworthiness**, as the generated trajectories provide a human-readable decision basis for every action taken. The study concludes that the combination of internal "inner speech" and external interaction is a fundamental mechanism for general-purpose AI agents.

---

## Research Problem
- **Problem addressed:** The separation of **reasoning and acting** in LLMs. Reasoning-only models (like CoT) operate as "static black boxes" without external grounding, leading to **hallucinations**, while acting-only models lack high-level abstract reasoning and a mechanism to maintain a working memory.
- **Importance:** For autonomous systems, the inability to ground reasoning in reality or to plan abstractly limits their utility in complex, dynamic, or knowledge-intensive environments.

---

## Motivation
- **Why this research?** Human intelligence is characterized by the seamless combination of **task-oriented actions with verbal reasoning** (inner speech), which helps in self-regulation, strategy formulation, and maintaining working memory. 
- **Limitations of previous work:** Previous LLM methods either focused on static reasoning paths (CoT) that propagate errors without factual checks, or on direct action prediction that fails to comprehend complex contexts or decompose high-level goals.

---

## Proposed Solution
- **Detailed explanation:** **ReAct** prompts LLMs to generate a trajectory consisting of interleaved **Thoughts, Actions, and Observations**.
- **Overall idea:** By augmenting the action space to include language-based reasoning (thoughts), the model can "reason to act" (adjust plans) and "act to reason" (use environment feedback to inform thoughts).
- **How ReAct differs from previous LLM prompting methods:** Unlike **Chain-of-Thought (CoT)**, which is internal and static, ReAct is **grounded and interactive**. Unlike **Act-only** models, ReAct uses language to maintain a **working memory** and track subgoals.

---

## ReAct Architecture

### Thought
- **Purpose:** To decompose task goals, create action plans, inject commonsense, and track progress.
- **Reasoning:** Thoughts allow the model to process current context and determine what information is missing or what the next logical step should be.
- **Example:** "I need to search Colorado orogeny, find the area... then find the elevation range".

### Action
- **Purpose:** To interact with the external environment or knowledge base.
- **Action types:** In knowledge tasks, actions include `search[entity]`, `lookup[string]`, and `finish[answer]`. In decision tasks, they involve environment-specific commands like `go to [location]` or `take [object]`.
- **Example:** `search[Milhouse]` or `go to fridge 1`.

### Observation
- **Purpose:** To provide feedback from the external environment (e.g., API results or state changes).
- **Influence on reasoning:** Observations provide the factual evidence needed to update the next "Thought," preventing the model from relying on potentially hallucinated internal data.
- **Example:** "The eastern sector extends into the High Plains...".

### Thought → Action → Observation Loop
1.  **Thought:** Model reasons about the goal and decides on an action.
2.  **Action:** Model executes the action in the environment.
3.  **Observation:** Environment returns feedback/data.
4.  **Repeat:** The new observation is appended to the context for the next reasoning step.

---

## Reasoning Process
- **Chain-of-Thought:** Integrated into the "Thought" steps, but grounded by observations.
- **Decision making:** The model uses **sparse thoughts** to identify likely locations for objects or to plan multi-step maneuvers in text games.
- **Iterative reasoning:** Reasoning is not a single path but is reformulated based on search results or failures.
- **Error correction:** ReAct can recover from incorrect paths (like search errors) by reformulating search queries.
- **Benefits:** Improved **factuality**, reduced **hallucination**, and higher **interpretability**.

---

## Tool Usage
- **External tools:** Wikipedia API, web browsers (simulated), and interactive environments.
- **Search:** `search[entity]` tool for Wikipedia.
- **APIs:** Simple web API for information retrieval.
- **Knowledge bases:** Wikipedia serves as the primary external knowledge base.
- **Environment interaction:** Interacts with simulated households (ALFWorld) and shopping sites (WebShop).
- **Healthcare applications:** **[Information outside the paper]**: While the paper uses general benchmarks, the ReAct framework is highly applicable to healthcare for interacting with **EHR APIs, medical databases (PubMed), and diagnostic tools**.

---

## Memory
- **Does the paper include long-term memory?** **No**, the paper focuses on a **working memory** maintained within the current context window (trajectory).
- **Proposed integration:** **[Information outside the paper]**: To support long-term patient monitoring, ReAct could be integrated with a **vector database** or a persistent **patient summary module** to store historical clinical data that exceeds the LLM's token limit.
- **Limitations:** Current context is limited by the LLM's **input length limit**, making very long clinical trajectories difficult to manage without summarization or external storage.

---

## Planning
- **Goal decomposition:** Breaking high-level tasks (e.g., "put a clean lettuce in diningtable") into sub-steps.
- **Sequential planning:** Generating steps one-by-one based on the evolving state.
- **Dynamic replanning:** Handling exceptions (e.g., "I don't have salt") and adjusting the plan based on what is found in the environment.
- **Decision updates:** Using reasoning to realize when more information is needed before proceeding.

---

## Multi-Agent Collaboration
- **Support for multiple agents?** **No**, the paper focuses on a single-agent paradigm.
- **Extensions:** **[Information outside the paper]**: ReAct could be extended where one agent specializes in "Clinical Reasoning" and another in "Environment Interaction" (EHR data retrieval), collaborating via shared observations.
- **Healthcare applications:** This would allow for a **Human-in-the-loop** setup where a clinician can edit the agent's "Thoughts" to correct its clinical reasoning.

---

## Evaluation
- **Datasets:** HotpotQA (multi-hop QA), FEVER (fact verification).
- **Benchmarks:** ALFWorld (text-based game), WebShop (online shopping).
- **Tasks:** Knowledge retrieval, fact checking, and interactive decision-making.
- **Performance:** Outperformed Act-only models consistently; outperformed RL/IL methods on ALFWorld by **34%**.
- **Baselines:** Standard prompting, Chain-of-Thought (CoT), Act-only, and RL/IL models.
- **Major findings:** ReAct reduces hallucinations but can be more structurally constrained than CoT; the best performance often comes from **combining ReAct and CoT-SC**.

---

## Key Contributions
1.  Introduction of the **ReAct paradigm** for synergizing reasoning and acting.
2.  Empirical evidence of performance gains across diverse language and decision-making tasks.
3.  Demonstration that **interleaving reasoning and acting** reduces hallucination in knowledge tasks.
4.  Analysis showing that **finetuning** on ReAct trajectories is more effective than memorizing facts.

---

## Strengths
- **Interpretability:** Reasoning traces provide a clear "audit trail" for clinical or task-based decisions.
- **Trustworthiness:** Grounded in external facts rather than just internal weights.
- **Few-shot capability:** Works effectively with as few as **one or two examples**.
- **Human-controllability:** Allows humans to **edit thoughts** to redirect agent behavior.

---

## Limitations
- **Repetitive loops:** The model can sometimes get stuck repeating the same thought/action.
- **Search dependency:** If the search tool returns poor information, the reasoning process can fail.
- **Context window:** Long horizons are limited by the model's maximum token count.

---

## Research Gap
While ReAct addresses hallucination and grounding, there is a clear gap in applying this to **high-stakes domains like healthcare** where:
- **Explainability** must be mapped to clinical standards.
- **Safety and Reliability** require rigorous constraints beyond simple "thoughts".
- **Clinical Decision Support** requires integration with structured **EHR data** and **Clinical Guidelines**, which was not explored.

---

## How This Supports My Thesis

### Concepts to Adopt
- The **interleaved Thought-Action-Observation cycle** for autonomous patient monitoring agents.
- The use of **external knowledge retrieval** to support clinical reasoning and reduce medical hallucinations.

### Concepts to Modify
- **Action Space:** Replace Wikipedia-style actions with **EHR queries**, **vital sign monitoring**, and **medication order tools**.
- **Thought Types:** Focus thoughts on **clinical synthesis**, **triage logic**, and **risk assessment**.

### Concepts Not Suitable
- **Greedy Decoding:** For critical patient monitoring, more robust search/decoding strategies (like beam search) may be necessary to avoid repetitive reasoning loops.
- **General Wikipedia Knowledge:** Must be replaced with specialized **medical knowledge bases**.

### Proposed Improvements
- **Long-term Memory:** Integrate a persistent memory module to track patient history over days/weeks.
- **Planning:** Use **Goal Decomposition** to break down a "Discharge Plan" into hourly monitoring tasks.
- **Reflection:** Add a "Self-Correction" thought step where the agent reviews its proposed medication order against **Clinical Guidelines**.
- **RAG + EHR:** Use ReAct to query the **EHR** (Action), observe trends (Observation), and reason about the patient's deteriorating state (Thought).
- **Multi-Agent Systems:** One agent monitors vitals while another cross-references **Medical Knowledge Bases**, using ReAct to coordinate their findings for the clinician.

---

## Important Figures
- **Figure 1:** Shows the comparison of prompting methods (Standard, CoT, Act, ReAct). It matters because it visually demonstrates how **ReAct's synergy** solves problems where others fail.
- **Figure 3:** Scaling results for prompting vs. finetuning. It shows that **finetuning on ReAct trajectories** is the most effective way to improve performance on smaller models.
- **Figure 5:** Human-in-the-loop example. It highlights the potential for **clinicians to correct an agent's reasoning** on the fly.

---

## Important References
- **Wei et al. (2022):** Chain-of-Thought prompting—the foundation ReAct seeks to ground.
- **Ahn et al. (2022) [SayCan]:** Grounding language in robotic affordances—related to ReAct's interaction with environments.
- **Huang et al. (2022b) [Inner Monologue]:** Embodied reasoning—a close relative to the ReAct paradigm.
- **Yang et al. (2018):** HotpotQA dataset—used for evaluating multi-hop reasoning.

---

## Keywords
1. ReAct
2. Agentic AI
3. Synergistic Reasoning
4. Grounded Acting
5. LLM Agents
6. Hallucination Reduction
7. Working Memory
8. Chain-of-Thought
9. Interactive Decision Making
10. Knowledge-Intensive NLP
11. Fact Verification
12. Interpretability
13. Human-in-the-loop
14. Goal Decomposition
15. Autonomous Agents
16. Clinical Reasoning (Proposed)
17. Patient Monitoring (Proposed)

---

## Personal Notes

### Ideas for My Thesis
- Implement a **"Clinical ReAct"** prompt that uses observations from a patient's vital sign stream to generate diagnostic "Thoughts" before taking a "Notification Action" to the nurse.
- Use the **human-in-the-loop** feature of ReAct to let doctors "sign off" on the agent's reasoning traces.

### Future Research Ideas
- Investigating how ReAct behaves when the "Observation" is noisy or conflicting (common in medical sensors).
- Combining ReAct with **Clinical Guidelines** stored in a vector database for RAG-based acting.

### Possible Citations for Chapter 2
- "ReAct overcomes prevalent issues of hallucination and error propagation... by interacting with a simple Wikipedia API".
- "Reasoning traces help the model induce, track, and update action plans as well as handle exceptions".

### Questions for Supervisor
- How can we formally validate the "Thought" traces to ensure they follow **standard medical protocols**?
- Is the **7-step limit** observed in the paper sufficient for complex clinical workflows, or do we need a more persistent memory structure?