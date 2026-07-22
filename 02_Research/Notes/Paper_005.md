# Paper 005

## Basic Information
- **Title:** VOYAGER: An Open-Ended Embodied Agent with Large Language Models
- **Authors:** Guanzhi Wang, Yuqi Xie, Yunfan Jiang, Ajay Mandlekar, Chaowei Xiao, Yuke Zhu, Linxi “Jim” Fan, Anima Anandkumar
- **Year:** 2023
- **Journal:** arXiv preprint (Project website: https://voyager.minedojo.org)
- **DOI:** N/A
- **Link:** [https://voyager.minedojo.org](https://voyager.minedojo.org)

---

## Abstract Summary (200–300 words)
**VOYAGER** is introduced as the first LLM-powered embodied **lifelong learning agent** capable of continuous exploration, skill acquisition, and novel discovery without human intervention within the Minecraft environment. The framework addresses a critical limitation in current AI: while LLM-based agents can generate action plans, they typically lack the ability to progressively accumulate and transfer knowledge over extended time spans. 

The system is composed of three primary modules: 1) an **automatic curriculum** that proposes increasingly difficult tasks to maximize exploration; 2) an ever-growing **skill library** that stores successful behaviors as executable code; and 3) an **iterative prompting mechanism** that refines these programs based on environment feedback and self-verification. VOYAGER interacts with GPT-4 via blackbox queries, removing the need for model fine-tuning. By representing skills as **temporally extended and compositional code**, the agent rapidly compounds its abilities while mitigating the "catastrophic forgetting" common in gradient-based lifelong learning. 

Empirical results show that VOYAGER significantly outperforms prior state-of-the-art agents (like ReAct and AutoGPT), obtaining 3.3× more unique items and unlocking tech tree milestones up to 15.3× faster. Crucially, the agent demonstrates **zero-shot generalization**, utilizing its learned skill library to solve novel tasks in entirely new environments. This paradigm of autonomous, code-based skill accumulation offers a robust blueprint for general-purpose agents in complex, open-ended domains.

---

## Research Problem
- **Problem addressed:** The lack of **lifelong learning** capabilities in embodied agents. Most agents struggle with systematic exploration and cannot progressively acquire or transfer skills over time.
- **Why existing LLM agents cannot continuously learn:** Previous agents often operate on primitive actions or static plans that do not evolve; they do not have a mechanism to "commit mastered skills to memory" for future reuse in diverse situations.
- **Importance of lifelong learning:** For an agent to be truly autonomous and effective in open-ended worlds, it must be able to propose its own goals based on its current state and build a repertoire of reusable knowledge.

---

## Motivation
- **Why this work?** To build "generally capable embodied agents" that mimic human-like learning—starting with basics and advancing to complex tasks through self-driven exploration.
- **Limitations of previous agent frameworks:** Classical reinforcement learning (RL) and imitation learning (IL) struggle with systematic exploration and interpretability. Existing LLM planners (like ReAct) are often "not lifelong learners".
- **Importance of autonomous lifelong learning:** It allows agents to adapt to new environments and solve long-horizon tasks by composing simpler, previously mastered skills.

---

## Proposed Solution
- **Voyager framework:** An embodied agent that uses **code as the action space** to represent complex, temporally extended behaviors. 
- **Continuous skill learning without fine-tuning:** It uses in-context learning to build a skill library of programs, bypassing the need for gradient-based updates or parameter access.
- **Differences from ReAct and Toolformer:** Unlike ReAct, which generates reasoning and action plans for immediate tasks, VOYAGER maintains a **persistent skill library** and an **automatic curriculum** for long-term progress. While Toolformer teaches models to use static APIs, VOYAGER **generates its own tools (skills)** in the form of code.

---

## Voyager Architecture

### Automatic Curriculum
- **Purpose:** To ensure a manageable but challenging learning process and maximize exploration.
- **Task generation:** GPT-4 generates a steady stream of tasks based on the overarching goal of "discovering as many diverse things as possible".
- **Progressive difficulty:** It considers the agent's current state and exploration progress to suggest "suitably hard" next steps (e.g., mining wood before iron).
- **Autonomous exploration:** Driven by an "in-context form of novelty search".
- **Example:** If the agent is in a desert, the curriculum might suggest harvesting sand and cactus.

### Skill Library
- **Skill definition:** Each skill is represented by **executable Javascript code**.
- **Storage:** Skills are stored in a **vector database**.
- **Retrieval:** Indexed by the embedding of the skill's description; the agent retrieves the top-5 most relevant skills for any new task.
- **Reuse:** Complex skills are synthesized by **composing simpler programs**.
- **Example:** `craftStoneSword()` or `combatZombieWithSword()`.
- **Importance:** Alleviates catastrophic forgetting and facilitates rapid capability compounding.

### Iterative Prompting
- **Prompt generation:** Combines directives, agent state, completed/failed tasks, and retrieved skills.
- **Action generation:** GPT-4 produces the executable code.
- **Feedback:** Incorporates **environment feedback** (e.g., missing items) and **execution errors** (e.g., syntax/API bugs).
- **Error correction:** GPT-4 uses feedback for "rounds of code refinement".
- **Continuous improvement:** Repeats the loop until the self-verification module confirms success.

### Environment Interaction
- **Observation:** Includes inventory, equipment, nearby blocks/entities, biome, time, health, and hunger.
- **Action:** Execution of the generated Javascript program.
- **Feedback loop:** Program execution produces a "chat log" and "error trace" used for refinement.
- **Environment updates:** The agent's state (position, inventory) changes as code is executed.

---

## Lifelong Learning
- **Continuous learning:** Acquisition of new skills without a human-defined end goal.
- **Knowledge accumulation:** Building a library that persists and grows.
- **Experience reuse:** Applying mastered skills to solve novel tasks zero-shot.
- **Skill evolution:** Moving from basic resource gathering to complex 3D construction.
- **Self-improvement:** Refined through iterative feedback and "human-in-the-loop" critique.

---

## Memory
- **Long-term memory:** Represented by the **Skill Library**.
- **Skill memory:** Programs are stored as vector-embedded knowledge.
- **Experience storage:** Successful trajectories are committed to the library.
- **Retrieval:** Uses GPT-3.5 to generate queries for the vector database.
- **Role in lifelong learning:** Enables "knowledge accumulation" that other agents (like AutoGPT) lack.

---

## Planning
- **Goal decomposition:** GPT-4 breaks down high-level exploration goals into specific tasks.
- **Task planning:** Proposing a sequence of "suitable tasks" based on current capabilities.
- **Dynamic replanning:** The automatic curriculum adapts to exploration failures or unexpected environmental changes.
- **Sequential execution:** Solving tasks milestone-by-milestone.

---

## Tool Usage
- **External tools:** VOYAGER creates its own "tools" as reusable code.
- **Environment APIs:** Interacts with the **Mineflayer Javascript API** for motor control.
- **Code generation:** Directly leverages GPT-4 to write situated task plans.
- **Program execution:** Uses a code interpreter to provide error traces for refinement.
- **Benefits:** Code naturally represents "temporally extended and compositional actions" essential for long-horizon tasks.

---

## Multi-Agent Collaboration
- **Support?** No, the current work focuses on a **single embodied agent**.
- **Extensions (Information outside the paper):** In a healthcare setting, VOYAGER's framework could be extended to a **Multi-Agent Clinical Team**. For example, a "Monitoring Agent" could propose curriculum tasks (detecting patient vitals), while a "Clinical Decision Agent" retrieves skills (treatment protocols) from a shared library to generate action code (adjusting a medication pump).

---

## Healthcare Adaptation (Information outside the paper)
- **Intelligent Patient Monitoring:** The "Automatic Curriculum" could be adapted to a "Monitoring Schedule," proposing tasks like "Analyze ECG every 5 minutes" or "Alert if BP drops."
- **Clinical Decision Support:** The "Skill Library" would store **clinical protocols** (e.g., ACLS algorithms) as executable code modules.
- **EHR:** The environment would be the EHR database. VOYAGER could generate code to query longitudinal history or update patient charts.
- **Clinical Guidelines:** Could be retrieved as "skills" to ground an agent's reasoning in evidence-based medicine.
- **RAG:** Used to retrieve relevant medical knowledge to populate the context for iterative clinical prompting.
- **FHIR APIs:** These would serve as the "Control Primitive APIs" that the agent calls to interact with hospital systems.
- **Continuous Patient Monitoring:** VOYAGER's lifelong learning allows it to "evolve" its monitoring strategy as a patient's condition changes over days.

---

## Evaluation
- **Environment:** MineDojo (Minecraft AI framework).
- **Benchmarks:** Comparisons against ReAct, Reflexion, and AutoGPT.
- **Tasks:** Open-ended exploration, tech tree mastery, and zero-shot generalization.
- **Metrics:** Number of unique items, distance traveled, and tech tree level reached.
- **Performance:** VOYAGER obtained **3.3× more unique items** and traveled **2.3× longer distances** than baselines.
- **Major findings:** VOYAGER was the **only agent** to reach the Diamond level of the tech tree. The skill library is the "versatile tool" that even boosts other methods like AutoGPT.

---

## Key Contributions
1.  Introduction of **VOYAGER**, the first lifelong learning agent that explores and develops skills without human intervention.
2.  The **Automatic Curriculum** for novelty search and progressive difficulty management.
3.  The **Skill Library** as a persistent, compositional, code-based long-term memory.
4.  The **Iterative Prompting Mechanism** incorporating environment feedback and self-verification for robust program synthesis.

---

## Strengths
- **Lifelong learning:** Knowledge accumulation without catastrophic forgetting.
- **Interpretability:** Skills are human-readable code.
- **Generalization:** Strong zero-shot performance in unseen environments.
- **Autonomous improvement:** Self-verification module allows the agent to learn from its own mistakes.

---

## Limitations
- **Computational cost:** GPT-4 API is expensive (15× more than GPT-3.5).
- **Hallucinations:** Proposing non-existent items (e.g., "copper sword") or using invalid code (e.g., cobblestone as fuel).
- **Inaccuracies:** Occasional failures in the self-verification module's reasoning.
- **Real-world deployment:** Requires human-implemented safety constraints for physical robotics.

---

## Research Gap
While VOYAGER is revolutionary for exploration, its current implementation lacks:
- **Safety Constraints:** In **healthcare**, an agent cannot "explore" unverified medical actions (like "randomly" giving a drug).
- **Trustworthy Clinical Reasoning:** Reasoning traces must be grounded in **Clinical Validation**, not just game mechanics.
- **Real-time processing:** Minecraft is discrete; **patient monitoring** requires real-time, low-latency feedback loops.

---

## How This Supports My Thesis

### Concepts to Adopt
- **Code as Action:** Representing clinical workflows (e.g., "If SPO2 < 90%, Increase O2") as **executable programs**.
- **Skill Library:** A persistent repository of **medical protocols** that the agent retrieves and executes based on the patient's state.
- **Iterative Prompting with Verification:** Refining a proposed treatment plan through multiple rounds of checking against medical guidelines.

### Concepts to Modify
- **Curriculum Goal:** Shift from "Discovering diverse things" to "**Optimizing Patient Outcomes**" and "**Early Detection of Deterioration**."
- **Environment Feedback:** Transition from Minecraft chat logs to **EHR/FHIR API feedback** and **real-time sensor data**.

### Concepts Not Suitable
- **Novelty Search:** Random exploration is dangerous in clinical decision support; it must be replaced by **Curated Guideline Adherence**.

### Proposed Improvements
- **Integration with ReAct:** Use ReAct's reasoning traces to explain *why* a certain "Skill" (clinical protocol) was retrieved and executed.
- **RAG with Clinical Knowledge Bases:** Use RAG to ensure the "Iterative Prompting" is grounded in UpToDate or PubMed rather than general LLM weights.
- **FHIR Skill Library:** Build a library specifically for **FHIR resource manipulation**, allowing the agent to "learn" how to interact with any hospital's digital infrastructure.
- **Multi-Agent CDS:** A "Doctor Agent" verifies the "Skill Agent's" proposed code before it is executed on a medical device.

---

## Important Figures
- **Figure 2:** Illustrates the **three key components** (Curriculum, Skill Library, Prompting). *Importance:* The core architectural diagram for an Agentic AI system.
- **Figure 4:** Shows the **Skill Library** indexing and retrieval. *Importance:* Explains how long-term memory is structured using embeddings.
- **Table 1:** Tech tree mastery comparison. *Importance:* Quantifies the massive performance gap between VOYAGER and non-lifelong learning agents.

---

## Important References
- **Wei et al. (2022):** Chain-of-thought prompting—the logic used inside the Iterative Prompting Mechanism.
- **Fan et al. (2022) [MineDojo]:** The simulation environment used for evaluation.
- **Liang et al. (2022) [Code as Policies]:** Using LLMs to generate executable code—the inspiration for VOYAGER's action space.
- **Park et al. (2023) [Generative Agents]:** A related agent framework that uses memory retrieval, though not for executable code.

---

## Keywords
1. Voyager
2. Lifelong Learning
3. Agentic AI
4. Skill Library
5. Automatic Curriculum
6. Code as Action
7. Embodied AI
8. GPT-4
9. Zero-Shot Generalization
10. Iterative Prompting
11. Self-Verification
12. Vector Database
13. Mineflayer
14. Open-Ended Exploration
15. Clinical Decision Support (Proposed)
16. Patient Monitoring (Proposed)

---

## Personal Notes

### Ideas for My Thesis
- Use the **Skill Library** idea to create a "Clinical Protocol Library." Instead of "Craft Stone Sword," a skill could be "Manage Hyperkalemia."
- The **Automatic Curriculum** could become a "Patient Triage Curriculum," where the agent prioritizes monitoring tasks based on acuity.

### Future Research Ideas
- Can an agent "self-verify" its medical decisions by querying a separate, frozen **Clinical Guideline Agent**?
- How to manage "Skill Explosion" in a hospital setting where there are thousands of unique patient scenarios?

### Possible Citations for Chapter 2
- "VOYAGER is the first LLM-powered embodied lifelong learning agent that... acquires diverse skills... without human intervention".
- "Complex skills can be synthesized by composing simpler programs, which... alleviates catastrophic forgetting".

### Questions for Supervisor
- How do we handle **legal accountability** if the agent's "code-as-action" contains a clinical error?
- Can we pre-populate the **Skill Library** with the entire **ACLS/BLS manual** as code before the agent starts monitoring?


| ID | Year | Paper | Category | Research Problem | Proposed Solution | Memory | Planning | Reasoning | Tool Use | Multi-Agent | RAG | Healthcare | Evaluation | Research Gap | Relevance | Contribution to Thesis |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 005 | 2023 | VOYAGER: An Open-Ended Embodied Agent with Large Language Models | Agent Architecture | LLM-based agents lack lifelong learning capabilities, struggling to acquire, accumulate, and transfer skills over long time horizons without human intervention or fine-tuning. | VOYAGER, an agent framework comprising an automatic curriculum for exploration, an executable skill library for knowledge storage, and an iterative refinement mechanism. | Yes – Maintains an ever-growing skill library of executable code indexed by embeddings in a vector database for reuse in similar situations. | Yes – An automatic curriculum that proposes suitable tasks bottom-up based on the agent's current state and exploration progress to maximize novelty. | Yes – Uses Chain-of-Thought prompting for reasoning before code generation and a self-verification module to reflect on failures and success. | Code execution (JavaScript) and Mineflayer JavaScript APIs for environmental control. | No | Yes | No | Evaluated based on exploration performance, tech tree mastery, and zero-shot generalization to novel tasks in Minecraft against state-of-the-art baselines. | High computational costs associated with GPT-4 and model hallucinations where the agent proposes tasks for non-existent items. | 8 | Provides a lifelong learning architecture with a reusable skill library and iterative verification that can be adapted to manage and update complex clinical monitoring and decision support protocols. |