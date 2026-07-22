# Paper 009

## Basic Information
- **Title:** A Survey on Large Language Model based Autonomous Agents
- **Authors:** Lei Wang, Chen Ma, Xueyang Feng, Zeyu Zhang, Hao Yang, Jingsen Zhang, Zhi-Yuan Chen, Jiakai Tang, Xu Chen, Yankai Lin, Wayne Xin Zhao, Zhewei Wei, Ji-Rong Wen
- **Year:** 2025 (Received/Accepted dates pending in source)
- **Journal:** Frontiers of Computer Science
- **DOI:** https://doi.org/10.1007/s11704-024-40231-1
- **Link:** N/A (Provided as a PDF source)

---

## Abstract Summary (200–300 words)
This survey provides a **comprehensive and systematic review** of the rapidly growing field of Large Language Model (LLM)-based autonomous agents. Historically, agents were trained with limited knowledge in isolated environments, making human-like decision-making difficult to achieve. However, by leveraging the vast web knowledge acquired by LLMs, these models now serve as **central controllers** capable of achieving human-level intelligence.

The survey is organized around three primary pillars: **construction, application, and evaluation**. In terms of **construction**, the authors propose a **unified framework** consisting of four modular components: **profiling, memory, planning, and action**. The **profiling module** identifies agent roles, the **memory and planning modules** allow the agent to operate in dynamic environments by recalling past behaviors and strategizing future steps, and the **action module** translates these internal decisions into environmental outputs.

Regarding **applications**, the paper categorizes the use of these agents across **social science, natural science, and engineering**. It highlights how agents can simulate human cognitive processes, assist in scientific documentation, and automate complex engineering tasks like software development. Finally, the survey delves into **evaluation strategies**, distinguishing between **subjective evaluation** (e.g., human annotation and Turing tests) and **objective evaluation** (e.g., success metrics and established benchmarks). The authors conclude by identifying critical **future challenges**, such as the hallucination problem, prompt robustness, and the need for generalized human alignment.

---

## Research Problem
- **Problem addressed:** The divergence between traditional AI agents—which relied on simple heuristic policy functions in restricted environments—and the complex, open-domain decision-making processes of the human mind.
- **Importance of autonomous LLM agents:** LLM-based agents possess **comprehensive internal world knowledge**, allowing them to perform informed actions without domain-specific training while offering flexible natural language interfaces and enhanced explainability.
- **Limitations of current AI:** Traditional models lack the ability to simulate human-like behavior, struggle with long-range reasoning, and are often "static black boxes" compared to agentic systems.
- **Need for a unified survey:** While many models have been proposed independently, there is a lack of holistic comparison and systematic summary to inspire future research.

---

## Motivation
- **Evolution from LLMs to Agentic AI:** Moving beyond simple question-answering (QA) to agents that assume specific roles, perceive their environment, and evolve like humans.
- **Why LLMs alone are insufficient:** Standard LLMs have a limited context window, which impairs their ability to maintain long-term memory or handle complex, multi-step tasks without specialized architectural modules.
- **Need for planning, memory, and tool use:** These modules act as the "hardware" and "software" required for an agent to behave reasonably, powerfully, and reliably in a dynamic world.

---

## Proposed Taxonomy
The authors establish a comprehensive taxonomy for construction, application, and evaluation:
- **Agent Architecture:** A unified framework of Profile, Memory, Planning, and Action modules.
- **Memory:** Categorized by structure (Unified vs. Hybrid), format (Natural Language, Embeddings, Databases, Lists), and operations (Read, Write, Reflect).
- **Planning:** Divided into planning **without feedback** (Single-path, Multi-path, External Planner) and **with feedback** (Environment, Human, Model).
- **Reasoning:** Encompasses strategies like Chain-of-Thought (CoT), Tree-of-Thoughts (ToT), and Algorithm of Thoughts (AoT).
- **Tool Usage:** Part of the **Action Space**, including APIs, Databases, and External Models.
- **Communication:** Essential for multi-agent systems and human-agent interaction.
- **Multi-Agent Systems:** Focus on collaboration, negotiation, and "wisdom of crowds" to enhance capabilities.
- **Evaluation:** Subjective (Human-centric) and Objective (Metric-centric) assessments.
- **Safety:** Discussed as "Generalized Human Alignment" and the risks of malicious use.
- **Applications:** Social Science, Natural Science, and Engineering.

---

## Agent Architecture
- **LLM Brain:** Acts as the central controller leveraging internal knowledge.
- **Profiling Module:** Defines the agent's role (e.g., demographic, personality, social information).
- **Memory Module:** Stores perceptual inputs and historical behaviors to guide future actions.
- **Planner:** Decomposes complex tasks into manageable subtasks.
- **Action Module:** Translates decisions into specific outcomes.
- **Environment & Feedback Loop:** The agent interacts with the world, receives feedback (Environmental, Human, or Model-based), and updates its internal states.

---

## Memory
- **Short-Term:** Analogous to the input information within the LLM's **context window**.
- **Long-Term:** Resembles external storage (e.g., vector databases) that agents can query rapidly.
- **Unified Memory:** Simulates only short-term memory through in-context learning.
- **Hybrid Memory:** Explicitly models both short-term (recent perceptions) and long-term (consolidated knowledge).
- **Retrieval:** Information extraction based on **recency, relevance, and importance**.
- **Updating (Writing):** Managing duplicated information and handling memory overflow (e.g., FIFO buffers).
- **Reflection:** Summarizing past experiences into abstract, high-level insights.

---

## Planning
- **Task decomposition:** Breaking a final goal into intermediate steps.
- **Goal planning:** Creating high-level strategies to solve tasks.
- **Dynamic planning:** Revising plans iteratively based on feedback from the environment or humans.
- **Self-reflection:** Using internal feedback to refine outputs (e.g., Self-refine mechanism).
- **Long-horizon planning:** Necessary for complex, multi-step tasks where initial plans may fail due to unpredictable dynamics.

---

## Reasoning
- **Chain of Thought (CoT):** Solving problems step-by-step using examples in the prompt.
- **Tree of Thoughts (ToT):** Evaluating multiple "thoughts" as intermediate steps in a tree-like structure.
- **ReAct:** Synergizing thought-act-observation triplets to adapt to search results.
- **Self-Consistency (CoT-SC):** Generating multiple reasoning paths and choosing the most frequent answer.
- **Benefits:** Improved interpretability, reduced hallucination, and the ability to solve algorithmic problems.

---

## Tool Usage
- **Search:** Automatically generating queries to extract web content (e.g., WebGPT).
- **APIs:** Strategically harnessing external APIs (e.g., ToolFormer, ToolL-LaMA) to transcend LLM limitations.
- **Databases:** Using SQL statements to query and manipulate domain-specific information (e.g., ChatDB).
- **Python:** Generating and executing code for precise calculations or visual inference (e.g., ViperGPT).
- **Knowledge Bases:** Accessing expert systems for domain-specific information.
- **Importance:** Alleviates hallucination and handles domains requiring expert knowledge.

---

## Multi-Agent Systems
- **Collaboration & Coordination:** Multiple agents (e.g., coders, reviewers) communicate to complete software development cycles (e.g., ChatDev, MetaGPT).
- **Role assignment:** Manually or automatically assigning distinct responsibilities to facilitate collaboration.
- **Negotiation & Consensus:** Using a "wisdom of crowds" approach where agents debate until a consensus is reached.
- **Healthcare Examples (Information outside the paper):**
    - A **Triage Agent** gathers patient symptoms.
    - A **Specialist Agent** retrieves relevant **Clinical Guidelines** via RAG.
    - A **Pharmacy Agent** checks the proposed medication for drug-drug interactions.
    - A **Human Supervisor** (Doctor) provides the final approval.

---

## Evaluation
- **Benchmarks:** Utilizing environments like ALFWorld, Minecraft, and ToolBench for standardized testing.
- **Metrics:**
    - **Task Success:** Success rate, reward/score, accuracy.
    - **Human Similarity:** Coherence, fluency, human acceptance rate.
    - **Efficiency:** Development cost and training efficiency.
- **Reliability & Robustness:** Assessing the agent's ability to maintain performance across diverse tasks.
- **Human Evaluation:** Subjective scoring of user-friendliness and intelligence.

---

## Research Gap
- **Healthcare AI (Gap):** While the survey covers Natural Science and Engineering, it does not explicitly detail a framework for **High-Acuity Healthcare**, which requires extreme reliability.
- **Clinical Decision Support (Gap):** The need for agents to be grounded in **verifiable clinical evidence** rather than general web knowledge.
- **Explainability (Gap):** While LLM agents are more explainable than black boxes, formalizing these traces for medical audits is a gap.
- **Safety & Trustworthiness:** Aligning agents with diverse human values (generalized human alignment) is critical for medical ethics.
- **Real-Time Decision Making:** Slow inference speeds of LLMs pose a challenge for real-time monitoring of unstable patients.

---

## How This Supports My Thesis

### Concepts to Adopt
- The **unified architecture** (Profile, Memory, Planning, Action) for structuring my monitoring framework.
- **Hybrid Memory** to manage both immediate vital sign data (Short-term) and longitudinal patient history (Long-term).
- **Planning with Feedback** to allow the agent to adjust monitoring frequency based on patient deterioration.

### Concepts to Modify
- **Action Space:** Shift from general web APIs to **FHIR-compliant APIs** for secure EHR interaction (Information outside paper).
- **Profiling:** Replace general roles with specific clinical personas (Nurse, Intensivist, Respiratory Therapist).

### Concepts Not Suitable
- **Handcrafted Profiling:** Too labor-intensive for the variety of roles in a hospital; **LLM-generation** or **Dataset Alignment** (from hospital staff directories) is preferred.

### Proposed Improvements
- **Integration with Clinical Guidelines:** Use **RAG** to feed validated medical knowledge into the **Planning Module**.
- **Reflection for Safety:** Implement a **Memory Reflection** step where the agent reviews its proposed clinical action against **EHR data** for safety before execution.
- **Multi-Agent Triage:** Deploy an **AutoGen/CAMEL** style multi-agent team where a "Grounding Agent" specifically looks up drug interactions in the **Action Space**.

---

## Comparison with Previous Papers
*Note: All "P" papers are cited within P009 as seminal works.*
- **ReAct (P003):** P009 classifies this as **Planning with Environment Feedback**, utilizing thought-act-observation triplets.
- **Generative Agents (P002):** P009 uses this as the primary example of **Hybrid Memory** and **Social Simulation**.
- **Toolformer (P004):** P009 cites this as a key development in **Self-supervised Tool Learning**.
- **Voyager (P005):** P009 highlights its use of **Natural Language Skills** in memory and planning with environment feedback.
- **AutoGen (P006) / CAMEL (P007):** Both are cited as benchmarks for **Multi-Agent Conversation** and collaborative task-solving.
- **MetaGPT (P008):** P009 identifies this as a framework for **Software Engineering** that abstracts multiple supervisory roles.

---

## Important Figures
- **Figure 2 / 13:** The **Unified Framework** (Profile, Memory, Planning, Action). It is the structural heart of the survey and my proposed agentic framework.
- **Figure 3 / 35 / 38:** Comparison of **Single-path vs. Multi-path Reasoning**. This matters for choosing how my agent should "think" through a diagnosis.
- **Figure 5 / 77 / 81:** Applications and Evaluation strategies. It provides the global overview of where LLM agents currently succeed.

---

## Important Tables
- **Table 1:** **Taxonomy of Existing Work**. It maps every major agent (including ReAct, Toolformer, etc.) to the four-module architecture, providing a clear comparison of their capabilities.
- **Table 2:** **Representative Applications**. Summarizes which papers apply to which domains (e.g., Psychology, Jurisprudence, Robotics).

---

## Important References
- **Park et al. (2023) [Generative Agents]:** Critical for memory architecture.
- **Wei et al. (2022) [Chain-of-Thought]:** Foundational for the Planning module.
- **Yao et al. (2023) [ReAct]:** Essential for planning with feedback.
- **Schick et al. (2024) [Toolformer]:** Key for tool-augmented agents.

---

## Keywords
1. Autonomous Agents
2. Large Language Models (LLMs)
3. Unified Architecture
4. Memory Module
5. Hybrid Memory
6. Task Decomposition
7. Tool Augmented LLMs
8. Multi-Agent Systems
9. Social Simulation
10. Human-Agent Interaction
11. RAG
12. Hallucination
13. Human Alignment
14. Clinical Decision Support
15. Patient Monitoring

---

## Personal Notes

### Ideas for My Thesis
- Implement a **Hybrid Memory** module where short-term memory is the "Current Shift's Vitals" and long-term memory is the "Patient's Longitudinal EHR."
- Use **Multi-path Reasoning (Tree of Thoughts)** for differential diagnosis to avoid early clinical closure.

### Questions for Supervisor
- How do we define the **"Action Impact"** in a medical setting where the "Environment" is a human body?
- Is the **"Turing Test"** evaluation appropriate for medical agents, or is **"Clinical Validity"** a more important metric?

---

## Relevance Score
**10/10**
This is the **foundational survey** for the entire field. It provides the **architectural blueprint** (Profile-Memory-Planning-Action) needed to design any LLM-based agent. For a thesis on an Agentic AI Framework, this paper is the primary roadmap for construction and evaluation.


| P009 | 2025 | A Survey on Large Language Model based Autonomous Agents | Survey | Traditional agents lack human-like decision-making capabilities because they are typically trained with limited knowledge within isolated and restricted environments. | A unified architectural framework for LLM-based autonomous agents composed of profiling, memory, planning, and action modules. | Yes – Includes short-term memory (in-context learning) and long-term memory (external vector storage) with read, write, and reflection operations. | Yes – Features task decomposition and selection strategies, categorized into planning with and without feedback from environments, humans, or models. | Yes – Elicited through various strategies including single-path and multi-path (tree or graph) reasoning to solve complex problems step-by-step. | External APIs, databases, knowledge bases, web search, and specialized external models. | Yes | Yes | Yes | Evaluated through subjective methods like human annotation and Turing tests alongside objective quantitative metrics across various simulation protocols and benchmarks. | Addressing limitations in role-playing for uncommon domains, ensuring robust prompt engineering, and achieving generalized human alignment across diverse values. | 10 | Provides a comprehensive architectural blueprint and a systematic taxonomy of capability acquisition strategies that serve as the foundational structural components for the proposed patient monitoring framework. |