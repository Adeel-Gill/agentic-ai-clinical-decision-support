# Paper 008

## Basic Information
*   **Title:** MetaGPT: Meta Programming for a Multi-Agent Collaborative Framework
*   **Authors:** Sirui Hong, Mingchen Zhuge, Jiaqi Chen, Xiawu Zheng, Yuheng Cheng, Ceyao Zhang, Jinlin Wang, Zili Wang, Steven Ka Shing Yau, Zijuan Lin, Liyang Zhou, Chenyu Ran, Lingfeng Xiao, Chenglin Wu, Jürgen Schmidhuber
*   **Year:** 2024
*   **Venue:** Not explicitly stated; associated with DeepWisdom and King Abdullah University of Science and Technology
*   **DOI:** Not provided in the source.
*   **Link:** [https://github.com/geekan/MetaGPT](https://github.com/geekan/MetaGPT)

## Abstract Summary (250–350 words)
**MetaGPT** is an innovative **meta-programming framework** designed to enhance the collaborative capabilities of Large Language Model (LLM)-based multi-agent systems by incorporating efficient human workflows. While existing multi-agent systems can handle simple dialogue, complex tasks often lead to logic inconsistencies and **cascading hallucinations** caused by the naive chaining of LLMs. To address this, MetaGPT introduces **Standardized Operating Procedures (SOPs)** into agent collaborations, mimicking an **assembly line paradigm** where diverse, specialized roles are assigned to various agents.

The framework encodes SOPs into prompt sequences, allowing agents with human-like domain expertise to verify intermediate results and reduce errors. Unlike previous "chat-based" systems that rely on unconstrained natural language, MetaGPT emphasizes **structured communication**. Agents interact through documents, design artifacts, flowcharts, and interface specifications rather than just dialogue, which helps maintain consistency and minimizes ambiguity. 

The architecture utilizes a **Shared Message Pool** and a **publish-subscribe mechanism**. This allows agents to access relevant directional information based on their specific profiles while filtering out irrelevant "information overload". MetaGPT also introduces an **executable feedback mechanism** during runtime, allowing agents to self-correct by debugging and executing code iteratively. Evaluated on collaborative software engineering benchmarks like **HumanEval** and **MBPP**, MetaGPT achieved state-of-the-art performance (85.9% and 87.7% Pass@1, respectively) and a **100% task completion rate** on more complex development tasks, highlighting the robustness of SOP-driven multi-agent frameworks.

## Research Problem
*   **Limits of single-agent LLMs:** Standalone LLMs often struggle with complex, multi-step tasks and maintaining consistency over long workflows.
*   **Collaboration challenges:** Existing multi-agent systems frequently oversimplify complexities and fail to achieve accurate problem-solving when meaningful collaborative interaction is required.
*   **Hallucinations & coordination:** "Naive chaining" of agents leads to logic inconsistencies and cascading hallucinations; furthermore, agents often engage in "idle chatter" (e.g., Alice asking Bob if he's had lunch) rather than task-oriented work.
*   **Need for structured workflows:** There is a lack of effective workflows with structured output formats in current frameworks, making it difficult to address complex engineering issues.

## Motivation
*   **Why MetaGPT:** To replication human success in task decomposition and coordination through the use of established SOPs.
*   **Human software-team inspiration:** Humans use roles like Product Managers and Architects who produce standardized deliverables (e.g., PRDs) to guide development.
*   **SOP-driven collaboration:** Standardized procedures improve consistency, alignment with quality standards, and accountability.
*   **Specialized AI roles:** Assigning LLMs to specific, specialized personas with distinct goals and constraints improves performance on granular tasks.

## Proposed Solution
*   **Multi-agent architecture:** A "simulated software company" consisting of specialized agents (PM, Architect, etc.).
*   **Role specialization:** Each agent is initialized with a specific profile, goal, and constraints.
*   **SOP workflow:** Task execution follows a strictly defined, sequential, or parallel operational procedure.
*   **Shared workspace:** A global **Shared Message Pool** where all communication is stored.
*   **Communication mechanism:** A **publish-subscribe interface** where agents subscribe to relevant messages based on their role and publish structured deliverables.

## Core Analysis

### Multi-Agent Architecture
The framework defines five primary roles that simulate a software company hierarchy:
*   **Product Manager:** Conducts requirement analysis and creates structured **Product Requirement Documents (PRDs)**.
*   **Architect:** Translates requirements into system designs, including file lists, data structures, and interface definitions.
*   **Project Manager:** Handles task distribution based on the system design.
*   **Engineer:** Executes code based on designated classes and functions.
*   **QA Engineer:** Formulates test cases and enforces code quality.

### Agent Communication
*   **Message passing:** Agents pass **structured messages** (documents and diagrams) rather than simple text dialogue.
*   **Shared workspace:** The message pool acts as a transparent environment for all agents.
*   **Coordination:** Coordinated via role-specific interests; agents activate actions only after receiving prerequisite dependencies (e.g., the Architect waits for the PRD).
*   **Conflict resolution:** Managed by structured interfaces that prevent the "distortion" of information seen in traditional dialogue-based "telephone games".

### Planning
*   **Goal decomposition:** Complex goals are decomposed into PRDs, system designs, and finally specific tasks.
*   **Task assignment:** The Project Manager decomposes the project into a functional task list for Engineers.
*   **Scheduling:** Workflow execution is sequential (PM $\to$ Architect $\to$ Engineer $\to$ QA).
*   **Workflow execution:** Enhanced by **executable feedback**, where the system runs code and uses test results to trigger debugging cycles.

### Memory
*   **Shared memory:** Provided by the message pool where every agent's output is recorded.
*   **Context preservation:** Agents retrieve required information directly from the pool, maintaining context across the entire "software company".
*   **State synchronization:** Agents maintain internal "execution and debugging memory" to avoid repeating errors during iterative programming.

### Tool Usage
*   **Code & documentation generation:** Primary output of Engineers and PMs.
*   **Testing:** QA Engineers use **unit test cases** as tools for verification.
*   **APIs:** MetaGPT can integrate external APIs; Product Managers specifically use **web search tools**.
*   **Knowledge retrieval:** Agents retrieve context from the shared pool to maintain consistency.

### SOPs
*   **Purpose:** To streamline workflows, provide task decomposition, and establish standards for intermediate outputs.
*   **Reliability:** Reduces unproductive collaboration and "idle chatter," resulting in a **100% task completion rate** in evaluations.
*   **Hallucination reduction:** Structured templates and "guided thinking" on granular tasks minimize broad task errors.
*   **Standardized collaboration:** Every handover must comply with established standards, ensuring the team stays aligned with the overall goal.

### Collaboration Strategy
*   **Role specialization:** Divergent roles contribute specialized outputs (e.g., the Architect provides technical specs, the PM provides user stories).
*   **Parallel/Sequential execution:** Agents work in a "strict and streamlined workflow".
*   **Team reasoning:** Multi-round "mindstorms" or collaborative interactions allow for more coherent problem-solving than single-agent approaches.

## Evaluation
*   **Experimental setup:** Evaluated using **HumanEval** (164 tasks), **MBPP** (427 tasks), and a new **SoftwareDev** dataset (70 complex engineering tasks).
*   **Benchmarks:** Compared against AutoGPT, LangChain, AgentVerse, and ChatDev.
*   **Performance:** 
    *   State-of-the-art Pass@1: **85.9%** (HumanEval) and **87.7%** (MBPP).
    *   Significant improvement over vanilla GPT-4 (67% baseline).
*   **Success rate:** 100% completion on SoftwareDev tasks.
*   **Cost:** High efficiency; uses only **124–126 tokens per line of code**, nearly half of ChatDev's token usage.
*   **Comparison:** Outperformed ChatDev in **executability** (3.75 vs 2.25) and required fewer human revisions.

## Key Contributions
1.  Introduction of the **MetaGPT framework**, which treats multi-agent collaboration as a "simulated software company".
2.  Innovative integration of **SOPs** into agent workflows to reduce logic inconsistencies and hallucinations.
3.  Implementation of **structured communication** (publish-subscribe) interfaces to manage information overload.
4.  Development of the **executable feedback mechanism** to elevate code generation quality through runtime debugging.

## Strengths
*   **Robustness:** Achieves high success rates and SOTA performance through specialized roles.
*   **Efficiency:** Reduces communication overhead and token waste per line of code.
*   **Transparency:** Natural language logs and structured artifacts allow humans to observe and control the entire process.
*   **Open-Source:** Highly flexible platform for developing LLM-based multi-agent systems.

## Limitations
*   **Cost:** While efficient per line, complex multi-agent simulations can still consume a large number of total tokens (up to 31k per project).
*   **Communication overhead:** Managing the publish-subscribe pool for very large agent teams can become complex.
*   **Latency:** Iterative feedback loops (up to 3 retries) can increase total running time.
*   **Scalability:** Currently limited to around 5–10 roles; larger societies may face different coordination issues.
*   **LLM dependency:** Highly dependent on strong backends like GPT-4; performance drops significantly with GPT-3.5 or smaller open-source models.
*   **Limited domain validation:** Primary focus is on software engineering; applications to fields like healthcare are not explicitly evaluated.

## Research Gap
*   **Healthcare multi-agent systems:** A need exists to see if the software-centric roles (PM, Architect) translate to clinical roles.
*   **Clinical workflow automation:** Exploring how medical SOPs (guidelines) can be encoded like software SOPs.
*   **Medical reasoning:** Applying the "executable feedback" loop to medical logic (e.g., verifying a diagnosis against a medical knowledge base).
*   **Long-term patient memory:** MetaGPT agents currently lack persistent learning across different patient encounters (independent execution).
*   **Explainable collaboration:** Visualizing the "clinical call flow" for inter-agent communication in a hospital.
*   **Human-in-the-loop:** Better mechanisms for clinicians to "checkpoint" or interrupt the agentic reasoning process.
*   **Trustworthy AI:** Formalizing accountability when an "Engineer agent" executes a clinical order.

## Healthcare Adaptation
Adapting MetaGPT for your thesis requires replacing the software development team with a **Clinical Multi-Disciplinary Team (MDT)**:

*   **Intelligent Patient Monitoring:** Continuous background monitoring of the message pool for "Observations" from sensors.
*   **Clinical Decision Support:** Using the "Architect" and "Engineer" logic to propose treatment plans.
*   **Hospital Workflow:** Automating the "assembly line" from triage to prescription.
*   **Care Coordination:** Using the "Project Manager" role to distribute nursing, physician, and pharmacy tasks.
*   **Clinical Documentation:** The "PM" role focuses on generating **Electronic Health Records (EHR)** and summaries rather than PRDs.

### Suggested Agents:
*   **Patient Monitoring Agent (PM equivalent):** Analyzes patient data and vitals to create a "Clinical Requirement Document".
*   **Clinical Reasoning Agent (Architect equivalent):** Translates requirements into a "Clinical System Design" (differential diagnoses and intervention plans).
*   **Drug Interaction Agent (QA equivalent):** Specifically reviews the medication list for interactions and safety.
*   **Medical Knowledge Agent:** A specialized RAG-enabled role that provides "Shared Knowledge" about guidelines to all agents.
*   **Alert Agent:** Monitors the message pool for critical vitals and publishes high-priority alerts to human staff.
*   **Physician Assistant Agent:** The "Engineer" who synthesizes the final clinical note and proposes orders.
*   **Clinical Validation Agent:** Final "QA" role that ensures the proposed plan aligns with medical guidelines.

## How This Supports My Thesis

### Concepts to Adopt
*   **SOP-driven Workflows:** Mirror clinical practice where doctors follow standardized guidelines.
*   **Role Specialization:** Creating distinct personas for Nurse, Doctor, and Pharmacist agents to minimize clinical hallucinations.
*   **Publish-Subscribe Message Pool:** A robust way to manage information in a busy hospital environment where multiple sensors and clinicians provide data.

### Concepts to Modify
*   **Deliverable Formats:** PRDs and System Designs should be replaced with **Clinical Notes, Lab Orders, and Differential Diagnosis Trees**.
*   **Feedback Loops:** "Executable feedback" should involve simulating the clinical outcome or checking against **Evidence-Based Medicine (EBM)** databases rather than running code.

### Concepts Not Suitable
*   **Metaprogramming focus:** The "programming to program" aspect is too specific; focus instead on the **orchestration of agents**.
*   **Software Benchmarks:** HumanEval and MBPP are not suitable for clinical validation; you will need clinical benchmarks.

### Proposed Improvements
*   **Clinical Guidelines as SOPs:** Encode hospital-specific protocols (e.g., Sepsis bundles) directly into the agent prompt sequences.
*   **Medical RAG integration:** The "Medical Knowledge Agent" should use **RAG** to query UpToDate or PubMed during the "System Design" phase.
*   **EHR/FHIR APIs:** Use the "Action" module of the Engineer agent to call **FHIR APIs** for real-time patient data retrieval and updates.
*   **Long-Term Memory:** Implement the "Self-improvement mechanism" (Appendix A.1) where agents learn from past patient cases to become more "successful over time".
*   **Explainable AI:** Adopt the **Program Call Flow (Sequence Diagrams)** to provide clinicians with a visual reasoning trace of how the agents reached a decision.
*   **Trustworthy AI:** Use the "QA Engineer" role as a strict **Safety Auditor** that must sign off on every clinical order before it reaches the human interface.
*   **Human-in-the-loop:** Allow doctors to set "Checkpoints" (Appendix D.1) before any high-risk medical order is "executed".

## Comparison with P001–P007
*   **Vs. AutoGPT (P001 reference):** MetaGPT overcomes AutoGPT's lack of "systematically deconstructing requirements" and failure to generate complex executable systems.
*   **Vs. ReAct (P001 reference):** MetaGPT *integrates* ReAct behavior within its agents but adds a multi-agent orchestration layer that ReAct lacks.
*   **Vs. CAMEL (P007):** Both use role-playing, but CAMEL is more focused on "mind exploration" and general dialogue, whereas MetaGPT is strictly task-oriented with **structured artifacts** and **SOPs**.
*   **Vs. AutoGen (P006):** While AutoGen focuses on flexible "conversations," MetaGPT prioritizes **workflows and standardized handovers**, making it more suitable for high-compliance healthcare environments.
*   **Memory:** Similar to Generative Agents (P002), it uses shared history, but MetaGPT's memory is more "deliverable-centric" than "social-centric".
*   **Planning:** MetaGPT's planning is **hierarchical and document-driven**, which is more robust for clinical workflows than the simple chains in early agents.

## Important Figures
*   **Figure 1:** Shows the transition from human SOPs to MetaGPT's multi-agent SOPs. **Importance:** The core thesis for using human workflows in AI.
*   **Figure 2:** Illustrates the **Shared Message Pool** and **Executable Feedback**. **Importance:** Defines the communication and self-correction architecture.
*   **Figure 3:** Detailed diagram of the SOP workflow with deliverables. **Importance:** Blueprint for clinical task decomposition.
*   **Figure 8 & 9:** Visualizes system interfaces and call flows. **Importance:** Demonstrates how to achieve **Explainability** in a multi-agent system.

## Important Tables
*   **Table 1:** Statistical analysis on SoftwareDev. **Summary:** Shows MetaGPT's superiority in executability and cost over ChatDev.
*   **Table 2:** Comparison of capabilities across frameworks. **Summary:** Highlights PRD and Technical Design generation as MetaGPT's unique strengths.
*   **Table 3:** Ablation study on roles. **Summary:** Proves that adding specialized roles (PM, Architect) significantly increases **executability** and reduces human revisions.

## Important References
*   **Yao et al. (2022) [ReAct]:** Foundational for agent internal reasoning.
*   **Park et al. (2023) [Generative Agents]:** Reference for agent societies and collective memory.
*   **Schick et al. (2023) [Toolformer]:** Foundational for learning tool usage.
*   **Belbin (2012):** Source for human "Team Roles" theory.

## Keywords
1. MetaGPT
2. Multi-Agent Collaborative Framework
3. Standard Operating Procedures (SOPs)
4. Meta-Programming
5. Role Specialization
6. Structured Communication
7. Shared Message Pool
8. Publish-Subscribe Mechanism
9. Executable Feedback
10. Task Decomposition
11. Software Engineering Automation
12. LLM Hallucination Reduction
13. Human-like Workflows
14. Clinical Decision Support (Adapted)
15. Electronic Health Records (Adapted)
16. Multi-Disciplinary Care (Adapted)

## Personal Notes

### Key Takeaways
*   MetaGPT moves from "agent conversation" to "agent workflows."
*   Structured deliverables (PRDs, designs) are superior to raw dialogue for maintaining team alignment.
*   Specialized roles reduce hallucinations by forcing agents to focus on granular expertise.

### Ideas for Thesis
*   Implement a **"Clinical SOP Prompt"** where a Nurse Agent identifies symptoms, a Doctor Agent proposes a plan, and a Pharmacist Agent reviews the plan using the publish-subscribe pool.
*   Use the "QA Engineer" logic to build a **Clinical Safety Monitor** that runs checks on every drug order.

### Future Research
*   Investigating how "Agent Economies" (Appendix A.2) could be used to prioritize clinical tasks based on patient acuity scores.
*   Testing the "Self-referential self-improvement" of clinical agents as medical knowledge evolves.

### Chapter 2 Citations
*   "MetaGPT utilizes an assembly line paradigm to assign diverse roles to various agents, efficiently breaking down complex tasks into subtasks".
*   "MetaGPT requires agents to generate structured outputs... which significantly increases the success rate... and minimizes ambiguities".

### Supervisor Questions
*   How do we define the "executability" metric in a clinical setting where there is no "code compiler"?
*   Can we implement the "Shared Message Pool" in a way that remains HIPAA compliant?

## Relevance Score
**9/10**
**Justification:** MetaGPT provides the strongest architectural blueprint for **orchestrating multiple specialized agents** in a complex environment. Its emphasis on **SOPs and structured deliverables** is a perfect fit for the highly regulated and guideline-driven field of healthcare.

## Final Verdict
*   **Why this paper matters:** It provides a solution to "logic inconsistencies" in multi-agent systems through structured human-inspired workflows.
*   **Contribution to Agentic AI:** Moves the field toward **coordinated system intelligence** rather than isolated agent dialogue.
*   **Healthcare applicability:** Extremely high; clinical pathways are essentially medical SOPs.
*   **Impact on the proposed framework:** It provides the "Assembly Line" logic needed to automate the transition from patient monitoring to clinical intervention.

| P008 | 2024 | MetaGPT: Meta Programming for a Multi-Agent Collaborative Framework | Framework | Cascading hallucinations and logic inconsistencies in multi-agent systems when performing complex tasks. | A meta-programming framework that incorporates Standard Operating Procedures (SOPs) and structured artifacts into role-based agent collaborations. | Yes – Maintains a shared global message pool for asynchronous information retrieval and local execution/debugging history. | Yes – Implements task decomposition and automated sequential workflows based on role-specific specialized outputs and dependencies. | Yes – Agents follow ReAct-style internal reasoning to monitor environment triggers and fulfill goal-directed subtasks. | Web search tools, code execution and debugging environments, and diagram generation tools. | Yes | No | No | Evaluated on HumanEval, MBPP, and a SoftwareDev dataset using Pass@1 accuracy, code executability scores, and human revision costs. | Agents currently operate independently per project without cross-project recursive self-improvement or dynamic communication protocol optimization. | 9 | Offers a blueprint for orchestrating specialized clinical roles through standardized workflows and structured data handovers to ensure consistency in complex medical monitoring tasks. |