# Paper 007

## Basic Information
- **Title:** CAMEL: Communicative Agents for “Mind” Exploration of Large Language Model Society
- **Authors:** Guohao Li, Hasan Abed Al Kader Hammoud, Hani Itani, Dmitrii Khizbullin, Bernard Ghanem
- **Year:** 2023
- **Journal:** 37th Conference on Neural Information Processing Systems (NeurIPS 2023)
- **DOI:** N/A (Project Website: [https://www.camel-ai.org](https://www.camel-ai.org))
- **Link:** [https://github.com/camel-ai/camel](https://github.com/camel-ai/camel)

## Abstract Summary (200–300 words)
The paper introduces **CAMEL**, a novel communicative agent framework centered on **"role-playing"** to facilitate autonomous cooperation among large language models (LLMs). While chat-based LLMs have made significant strides in task-solving, their success often depends on heavy human intervention to guide conversations, which is time-consuming and requires domain expertise. To address this, CAMEL utilizes **inception prompting** to guide agents toward completing complex tasks with minimal human supervision while maintaining alignment with human intentions.

The framework typically involves two main agents: an **AI user** who provides instructions and an **AI assistant** who executes them. A third agent, the **task specifier**, takes a preliminary idea from a human and brainstorms a concrete, specific task to initiate the process. The authors demonstrate that this multi-agent cooperative approach generates higher-quality solutions than single-shot prompts, as verified by both human and GPT-4 evaluations. 

Beyond task-solving, the authors use CAMEL to generate massive conversational datasets (AI Society, Code, Math, and Science) for studying the behaviors and "cognitive" processes of agent societies. They also introduce **"critic-in-the-loop"** and **embodied agents** to enhance controllability and tool-use capabilities. By open-sourcing their library, the researchers provide a scalable foundation for investigating communicative AI and its potential risks and opportunities in a social context.

## Research Problem
- **Problem addressed:** The reliance of LLMs on human input to guide conversations toward complex task completion, which can be challenging and expertise-dependent.
- **Why LLM agent communication is challenging:** Autonomous cooperation often leads to issues such as **role flipping**, **infinite loops** of meaningless messages (e.g., repeatedly saying "thank you"), and **flake replies** where an agent promises action but fails to follow through.
- **Importance of role-based interactions:** Assigning distinct roles allows agents to apply specific expertise to a common goal, improving efficiency and decision-making for problems beyond the reach of a single agent.

## Motivation
- **Why CAMEL?** To explore if human intervention can be replaced by autonomous communicative agents capable of steering conversations toward task completion.
- **Limitations of previous multi-agent systems:** Previous systems often required precise human-crafted prompts or suffered from misalignments where agents deviated from their intended roles.
- **Benefits of autonomous collaboration:** Scalable generation of instructional data and the ability to solve complex tasks through high-level expertise-driven dialogue.

## Proposed Solution
- **CAMEL framework:** A cooperative agent paradigm using **role-playing** and **inception prompting**.
- **Role-playing and task solving:** Agents autonomously negotiate subtasks through multi-turn conversations until the AI user determines the task is done.
- **Differences from previous methods:** Unlike **ReAct** (which focuses on internal reasoning/acting loops), CAMEL focuses on the **social interaction** and communication protocols between distinct agents. **[Information outside the paper]:** While **AutoGen** and **Voyager** emphasize orchestration and lifelong learning respectively, CAMEL's unique contribution is the **inception prompt** that hard-codes role consistency and communication boundaries to prevent conversational collapse.

## CAMEL Architecture

### Role-Playing Framework
- **Role assignment:** A human provides a preliminary idea and designates roles (e.g., Physician and Patient Monitoring Agent).
- **Inception prompting:** System messages passed to agents at the start to define their roles, tasks, and communication constraints.
- **Agent responsibilities:** The AI user acts as a **task planner**; the AI assistant acts as a **task executor**.
- **Example:** A Stock Trader (User) instructing a Python Programmer (Assistant) to build a trading bot.
- **Benefits:** Prevents role-flipping and ensures a consistent conversational structure.

### Agent Communication
- **Conversation protocol:** Agents communicate in an instruction-following loop ($I_t, S_t$).
- **Information exchange:** The AI user takes the history $M_t$ to produce a new instruction $I_{t+1}$.
- **Negotiation:** The assistant provides specific solutions and implementations for each instruction.
- **Conflict resolution:** The **critic agent** can select between proposals or provide feedback to guide the decision-making process.
- **Decision making:** Assisted by a **tree-search-like** process where a critic selects the best "option" from multiple agent proposals.

### Task Decomposition
- **Goal decomposition:** A **task specifier agent** takes a vague idea and converts it into a concrete, multi-step task.
- **Role-specific responsibilities:** The user determines feasible steps, while the assistant provides the technical solutions.
- **Sequential collaboration:** Tasks are solved milestone-by-milestone through the message loop.

### Memory
- **Conversation history:** Agents maintain a set of conversational messages $M_t$ used to generate the next response.
- **Shared context:** Both agents have access to the historical message set to ensure consistency.
- **Context management:** Conversations are terminated if they exceed the **token limit** of the underlying model (e.g., gpt-3.5-turbo).

### Planning
- **Collaborative planning:** The AI user engages in interactive planning to determine the next steps.
- **Dynamic planning:** Agents can be equipped with a **task planner** that breaks down tasks into smaller subtasks in advance.
- **Decision updates:** The user decides when the task is solved and sends a `<CAMEL_TASK_DONE>` token.

### Tool Usage
- **External APIs:** Agents can be assigned roles that require calling external APIs (e.g., Twitter API, Yahoo Finance).
- **Programming tools:** The "Code" scenario specifically explores agents assisting in writing and executing code in various languages.
- **Embodied agents:** Physical entities that can browse the internet, read documents, and execute code based on role "thoughts".
- **Benefits:** Significantly improves LLM capabilities by grounding actions in the physical world or digital tools.

### Multi-Agent Collaboration
- **Communication workflow:** Human Input → Task Specifier → Role Assignment → AI User/Assistant Loop.
- **Role specialization:** Agents areAlphabetically sorted from a list of 50 diverse roles (including **Doctor**, **Nurse**, **Pharmacist**, and **Researcher**).
- **Team coordination:** Can be extended to **multi-stage role assignment** where different "experts" collaborate across different stages of a project.

## Healthcare Adaptation
**CAMEL** provides a clear pathway for **Intelligent Patient Monitoring** and **CDS** through role specialization.

### Applications:
- **Intelligent Patient Monitoring:** An agent role designated for **"Patient Monitoring"** was already identified in the paper's data analysis of tasks.
- **Clinical Decision Support:** A **"Doctor" assistant** can collaborate with an **"Artist" user** to create medical illustrations of digestive disease states (e.g., GERD), balancing accuracy and visual clarity.
- **Multidisciplinary Care Teams:** Using **multi-stage role assignment**, a **Physician** could collaborate with a **Pharmacist** to refine a medication plan, which is then passed to a **Nurse** for implementation.

### Healthcare Agents & Communication:
- **Physician (Assistant):** Provides specialized medical knowledge and treatment solutions.
- **Nurse (User):** Provides real-time observations of the patient and requests instructions for care.
- **Pharmacist (Assistant):** Checks for **drug interactions** and provides dosage implementation.
- **Clinical Guideline Agent (Assistant):** A specialized role that ensures all instructions from the Physician align with evidence-based standards. **[Information outside the paper]:** This agent would function as a "Critic-in-the-loop."
- **Documentation Agent:** Automatically extracts the "Final Solution" from the multi-agent chat to create a clinical note.

## Evaluation
- **Benchmarks:** MATH, Science, Code, and AI Society datasets.
- **Tasks:** Instruction-following, mathematical problem-solving, and code generation.
- **Performance:** CAMEL solutions outperformed gpt-3.5-turbo single-shot solutions in **76.3%** of human evaluations and **73.0%** of GPT-4 evaluations.
- **Major findings:** Multi-agent cooperative approaches are significantly more effective than single-shot LLM prompts for complex task completion.

## Key Contributions
1.  **Role-Playing Framework:** Facilitates autonomous agent collaboration with minimal human intervention.
2.  **Inception Prompting:** A scalable approach to steer and align multiple agents.
3.  **Instructional Datasets:** Open-sourced massive datasets for "mind exploration" of LLMs.
4.  **Embodied and Critic Agents:** Demonstrated enhanced controllability and tool-use in a society of agents.

## Limitations
- **Communication overhead:** Conversation costs grow **quadratically** with length, necessitating message limits.
- **Role conflicts:** **Role flipping** can occur if prompts are not carefully engineered.
- **Error propagation:** Hallucinations or "flake replies" can derail a conversation.
- **Scalability:** Evaluating complex, domain-specific tasks requires many human experts.
- **Hallucinations:** Models may produce false information during the task-solving process.

## Research Gap
- **Healthcare Specifics:** The paper lacks discussion on **HIPAA compliance**, **FHIR API** integration, or **secure clinical data sharing**.
- **Patient Safety:** Termination conditions in CAMEL are cost/token-based; a healthcare framework needs **safety-based termination**.
- **Clinical Validation:** The "Doctor" role in the paper is illustrative; real-world CDS requires grounding in **curated medical knowledge bases** to prevent harmful advice.

## How This Supports My Thesis

### Concepts to Adopt
- **Role-Playing for Multidisciplinary Teams:** Mirroring a real hospital ward where different agents (Physician, Nurse, Lab) communicate.
- **Task Specifier for Triage:** Using an agent to take a vague symptom ("chest pain") and specify a concrete monitoring/diagnostic task.

### Concepts to Modify
- **Action Space:** Move from general Python libraries to **FHIR-compliant medical APIs** for EHR interaction.
- **Critic Criteria:** Modify the "Professor" critic to a **"Senior Consultant"** role that validates treatment plans against clinical guidelines.

### Concepts Not Suitable
- **Infinite Looping:** The "thank you" loop must be strictly prohibited in a medical context where time-to-action is critical.
- **Random Role Generation:** Healthcare roles must be strictly **authenticated and verified**, not stochastically generated.

### Proposed Improvements
- **RAG + Inception:** Integrate **Retrieval-Augmented Generation** within the system prompt so the "Physician Agent" always cites clinical guidelines.
- **Long-Term Patient Memory:** Extend the conversation history to include a persistent **EHR-based memory** that spans multiple role-playing sessions.
- **Human-in-the-Loop Critic:** Allow a human doctor to act as the "Critic Agent" to sign off on multi-agent plans before execution.

## Important Figures
- **Figure 1:** The Role-Playing Framework. Importance: Shows the interaction between human idea, task specifier, and the agent loop.
- **Figure 2:** Inception Prompt Templates. Importance: Provides the "source code" for maintaining agent roles and alignment.
- **Figure 18:** Critic Tree Search. Importance: Explains how to introduce **clinical oversight** and structured decision-making.

## Important References
- **Minsky (1988):** *The Society of Mind*—Foundational concept for multi-agent intelligence.
- **Yao et al. (2022) [ReAct]:** Contextual baseline for reasoning/acting.
- **Kojima et al. (2022) [Zero-Shot-CoT]:** Comparison point for reasoning performance.
- **Schick et al. (2023) [Toolformer]:** Baseline for tool-use capabilities.

## Keywords
1. CAMEL
2. Multi-Agent Collaboration
3. Role-Playing
4. Inception Prompting
5. Agentic AI
6. Autonomous Cooperation
7. Task Specifier
8. Critic-in-the-loop
9. Embodied Agents
10. Clinical Decision Support
11. Patient Monitoring
12. LLM Society
13. Instruction Following
14. Mind Exploration
15. Conversational AI

## Personal Notes

### Ideas for My Thesis
- Implement a **"Code-Role-Playing"** scenario where a **Nurse** (User) asks a **Physician** (Assistant) for a diagnosis, and a **Pharmacist** (Critic) validates the resulting medication order.
- Use the **Task Specifier** to help junior clinicians formulate better queries for complex EHR data.

### Future Research Ideas
- Investigating the impact of **"Role Flipping"** in medical errors: Does the agent's tendency to switch roles reflect clinical uncertainty?
- Developing a **"Misalignment Dataset"** specifically for medical malpractice simulations to improve agent safety.

### Possible Citations for Chapter 2
- "CAMEL utilizes role-playing with inception prompting to autonomously guide the communicative agents toward task completion".
- "Multi-agent cooperative approach is more effective than gpt-3.5-turbo’s single shot solution".

### Questions for Supervisor
- How can we enforce **HIPAA privacy** when agents are passing "historical conversation message sets" between different hospital systems?
- Can we pre-train the **"Task Specifier"** on a library of 100,000 successful clinical cases to ensure high-quality task generation?