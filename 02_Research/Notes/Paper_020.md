# Paper_020.md

## Basic Information
- **Title:** AI Agents vs. Agentic AI: A Conceptual taxonomy, applications and challenges
- **Authors:** Ranjan Sapkota, Konstantinos I. Roumeliotis, Manoj Karkee
- **Year:** 2026
- **Journal:** Information Fusion
- **DOI:** https://doi.org/10.1016/j.inffus.2025.103599
- **Link:** [Elsevier / ScienceDirect](www.elsevier.com/locate/inffus)

## Abstract Summary (250–350 words)
This review provides a structured **conceptual taxonomy** to distinguish between **AI Agents** and **Agentic AI** in the Generative AI era. **AI Agents** are characterized as modular, task-specific systems enabled by Large Language Models (LLMs) and Large Image Models (LIMs) for automation, building upon foundational generative AI through tool integration and enhanced reasoning. In contrast, **Agentic AI** represents a more advanced paradigm shift marked by **multi-agent collaboration**, dynamic task decomposition, **persistent memory**, and coordinated autonomy.

The paper outlines the architectural evolution of these systems, mapping their operational mechanisms and autonomy levels. AI Agents are typically deployed for modular tasks such as customer support, scheduling, and data summarization. Agentic AI, however, is utilized for higher-complexity orchestrated operations, including research automation, robotic coordination, and **medical decision support**. 

The authors examine significant challenges unique to both paradigms, such as **hallucination, brittleness, emergent behavior, and coordination failures**. To address these, they propose targeted solutions including **ReAct loops, Retrieval-Augmented Generation (RAG)**, and causal modeling. By formalizing these distinctions, the article provides a roadmap for developing robust and explainable AI systems, ensuring that system design aligns with problem complexity. Ultimately, the paper bridges the gap between isolated task automation and scalable, collaborative multi-agent intelligence required for mission-critical domains like **healthcare**.

## Research Problem
- **Limits of traditional AI:** Classical agent-like systems were primarily reactive or deliberative, relying on symbolic reasoning or predefined rules with minimal adaptability to dynamic environments. 
- **Emergence of AI Agents:** Modern AI Agents emerged to overcome the statelessness and lack of goal-following in standalone LLMs by adding infrastructure like tool-calling APIs and reasoning chains.
- **Why Agentic AI:** Single-agent models prove insufficient for use cases demanding **context retention, task interdependence, and adaptability** across dynamic environments.
- **Need for a conceptual taxonomy:** Existing literature often conflates AI Agents and Agentic AI, leading to conceptual ambiguity and misaligned system design. 

## Motivation
- **Taxonomy Proposal:** The taxonomy aims to clarify the divergent design philosophies and capabilities of modular vs. orchestrated systems.
- **Distinction Importance:** It prevents "under-engineering" complex scenarios that require coordination or "over-engineering" simple tasks that a single agent could solve. It also allows for more appropriate **benchmarking, evaluation, and safety protocols**.

## Core Analysis

### AI Agents vs Agentic AI
- **Traditional AI:** Rule-based systems with limited autonomy.
- **AI Assistants:** Often reactive prompt-followers without internal state management.
- **AI Agents:** Single-entity systems performing goal-directed tasks via external tools and sequential reasoning.
- **Agentic AI:** Orchestrated ecosystems of multiple specialized agents that communicate and coordinate toward shared objectives.
- **Autonomy, Planning, Reasoning, Memory, Collaboration:** Agentic AI moves from modular tool-use to **distributed cognition and system-level intelligence**.

### Taxonomy
- **Agent types:** AI Agents (modular) vs. Agentic AI (collaborative).
- **Autonomy levels:** High autonomy within specific tasks for agents; broad system-wide autonomy for Agentic AI.
- **Memory:** AI Agents use context buffers; Agentic AI uses **shared episodic and task memory**.
- **Planning:** AI Agents have single-step/narrow horizons; Agentic AI handles **multi-step, complex task decomposition**.
- **Reasoning:** AI Agents use tool-based reasoning; Agentic AI uses **collaborative reasoning**.
- **Tool use:** Modular for agents; **coordinated multi-agent access** for Agentic AI.
- **Multi-agent systems:** Essential and collaborative in Agentic AI.

### Agent Architecture
- **LLM Brain:** Serves as the primary decision-making and reasoning engine.
- **Perception:** Intakes signals from users or sensors (e.g., vital sign streams).
- **Memory:** Persistent subsystems (Episodic, Semantic, Vector).
- **Planning:** Task decomposition into actionable subtasks.
- **Reasoning:** KRR module applying symbolic or statistical logic.
- **Reflection:** Reflexive and self-critique mechanisms to evaluate outputs.
- **Action:** Translation of decisions into external actions via an action library.
- **Feedback Loop:** The "Under-stand, Think, Act, Learn" operational cycle.

### Memory
- **Short/Long-term:** Short-term context window vs. persistent external storage.
- **Episodic/Semantic:** Task-specific history vs. long-term facts/structured data.
- **Retrieval:** Similarity-based retrieval from vector-based memory for **RAG**.
- **Reflection:** Agents evaluate past decisions to iteratively refine strategies.

### Planning
- **Task decomposition:** Automatically parsing a user goal into manageable subtasks.
- **Goal planning:** Formulating and evaluating possible action plans.
- **Replanning:** Dynamic sequencing that adapts to environmental changes or partial failures.
- **Hierarchical planning:** Orchestration layers (meta-agents) managing subordinate agent cycles.

### Reasoning
- **CoT:** Chain-of-Thought prompting to simulate deliberative processes.
- **ReAct:** Synergizing reasoning and acting via iterative loops.
- **ToT:** Tree of Thoughts for multi-stage reasoning.
- **Reflection:** Inter-agent evaluation and self-critique.
- **Self-consistency:** (Implied via inter-agent evaluation/consensus mechanisms).

### Tool Usage
- **Search:** Real-time information access (e.g., ChatGPT search).
- **APIs:** Integration of external platforms (e.g., Salesforce, Notion).
- **Python:** Executing scripts for complex computations.
- **Databases:** Interfacing with vector stores like FAISS or Pinecone.
- **Knowledge Bases:** Organizational policy repositories and manuals.
- **RAG:** Grounding outputs in real-time external facts to mitigate hallucinations.
- **Medical Information Systems:** Integration with **EHRs and lab data**.

### Multi-Agent Collaboration
- **Communication:** Mediated through messaging queues, shared memory, or decentralized protocols.
- **Role assignment:** specialized functions (summarizer, retriever, planner).
- **Delegation:** Dynamic subtask allocation across the agent network.
- **Consensus:** Collective decision-making and inter-agent evaluation.
- **CAMEL:** Simulates agent societies with negotiation and emergent behavior.
- **AutoGen:** Hierarchical orchestration where one agent plans while others retrieve and synthesize.
- **CrewAI:** Accomplishing decision-making across distributed roles.

## Applications
- **Healthcare:** **Collaborative Medical Decision Support** (ICU management, radiology triage).
- **Robotics:** Intelligent Robotics Coordination (swarm drones, harvesting robots).
- **Education:** Virtual assistants and adaptive learning.
- **Finance:** Autonomous scheduling, logistics, and risk analysis.
- **Software Engineering:** Multi-agent code generation and debugging (e.g., ChatDev, GPT-Engineer).

## Healthcare Perspective
- **Intelligent Patient Monitoring:** Specialized agents continuously analyzing vitals and lab data (e.g., sepsis risk).
- **Clinical Decision Support:** Multi-agent systems synchronizing diagnostics, treatment planning, and EHR analysis.
- **Medical Diagnosis:** Diagnostic agents validating findings against guidelines.
- **Clinical Documentation:** Synthesizing plausible clinical notes from long patient-physician conversations.
- **Hospital Workflow Automation:** Triage and registration orchestration in "Agent Hospitals".
- **Physician Assistance:** Surfacing conflicts and summarizing comorbidities for human review.
- **Medical Knowledge Retrieval:** History retrieval agents accessing EHRs to provide shared context.

## Evaluation
- **Reliability:** Success in mission-critical environments.
- **Robustness:** Ability to adapt under uncertainty or partial failure.
- **Efficiency:** Reducing cognitive load and shortening decision times.
- **Explainability:** Tracing reasoning paths through role-specialized designs.
- **Safety:** Verifiable output logging and ethical guardrails.
- **Human evaluation:** Physician feedback used to refine reasoning in persistent memory.
- **Generalization:** Emergent neural architectures generalizing across unstructured tasks.

## Key Contributions
1.  **First structured taxonomy** formally separating AI Agents from Agentic AI paradigms.
2.  Analysis of **architectural evolution** from monolithic loops to coordinated multi-agent ecosystems.
3.  Comprehensive mapping of **challenges and solutions** across both paradigms.
4.  A **forward-looking roadmap** for integrating agentic systems into high-stakes domains like healthcare.

## Strengths
- **Conceptual Clarity:** Establishes a shared vocabulary to reduce development inefficiencies.
- **Healthcare Focus:** Explicitly highlights medical decision support as a high-stakes application for Agentic AI.
- **Multimodal Support:** Emphasizes the role of **LIMs** (vision models) for tasks like robotic orchard inspection or radiology.

## Limitations
- **Limited implementation details:** Some real-world Agentic AI implementations are still "lacking" due to the field's nascent nature.
- **Limited healthcare evaluation:** Early deployments (ICU, oncology) show promise, but broad verification is still needed.
- **Scalability:** Multi-agent scaling increases cognitive load and noise without robust orchestration.
- **Cost:** High computational cost and latency due to repeated LLM invocations.
- **Safety:** Lack of formal verification tools for open-ended agents in safety-critical domains.
- **Regulatory issues:** Ambiguity in accountability and legal liability for multi-agent decisions.

## Research Gap
- **Healthcare Agentic AI:** Need for trustworthy, scalable systems in high-stakes clinical environments.
- **Long-term patient memory:** Developing persistent memory models for longitudinal operations.
- **Clinical reasoning:** Addressing the **lack of causal understanding** in multi-agent medical workflows.
- **Explainability:** Tracing inter-agent communication for accountability in diagnosis.
- **Real-time monitoring:** EfficientServing engines to reduce latency in vital sign processing.
- **Multi-agent collaboration:** Standardized protocols for agent interoperability (e.g., A2A).
- **Trustworthy AI:** Verifiable reasoning and alignment with medical ethical norms.

## Future Research Directions
- **AZR (Absolute Zero):** Reinforced self-play reasoning to remove dependency on human-annotated datasets.
- **Proactive Intelligence:** Agents initiating tasks based on contextual cues rather than waiting for prompts.
- **Simulation Planning:** Modeling hypothetical decision trajectories to forecast clinical consequences.
- **Domain-Specific Systems:** Tailoring agentic architectures specifically for sectors like **medicine** and law.

## How This Supports My Thesis

### Concepts to Adopt
- **Orchestration Layer:** Using a meta-agent to coordinate "Diagnostic," "History Retrieval," and "Treatment Planning" agents.
- **Persistent Memory:** Storing longitudinal patient context across monitoring shifts.
- **Task Decomposition:** Breaking down a high-level goal like "Monitor for Sepsis" into vitals analysis and EHR retrieval.

### Concepts to Modify
- **Role-Bound Agents:** Strictly defining roles (e.g., "Nurse Agent," "Physician Agent") but ensuring they share a **Shared Context** via messaging queues.
- **Feedback Loops:** Modifying physician-in-the-loop triggers to prioritize high-acuity alerts.

### Concepts Not Suitable
- **Stateless Generative AI:** Avoid using simple prompt-response loops for clinical monitoring.
- **Purely Reactive AI Agents:** Modular agents without shared memory are insufficient for ICU workflows.

### Proposed Improvements
- **Clinical RAG:** Integrating **MedRAG** pipelines within the Agentic AI system to ground decisions in guidelines.
- **FHIR API Integration:** Ensuring the "Action Module" translates agentic decisions into **FHIR-compliant orders** or data updates.
- **Explainability Pipelines:** Implementing timeline visualizations of inter-agent clinical dialogue for physician review.
- **Causal Modeling:** Embedding counterfactual reasoning (e.g., "What if we increase fluids?") into the treatment planning agent.

## Comparison
- **Vs. P001-P019:** While previous papers (e.g., **AutoGen [P006]**, **MedRAG [P012]**, **Agent Hospital [P011]**) provide specific framework implementations, Paper 020 provides the **unifying conceptual taxonomy** that classifies these into modular vs. orchestrated paradigms.
- **Contribution:** It bridges the technical specifics of **ReAct [P003]** and **Toolformer [P004]** with the high-level **multi-agent orchestration** required for your thesis's "Intelligent Patient Monitoring" framework.

## Important Figures
- **Fig. 8:** Architectural evolution from AI Agents to Agentic AI. **Importance:** Shows the addition of Persistent Memory and Orchestration.
- **Fig. 11c:** ICU Application Scenario. **Importance:** Directly illustrates your thesis topic in practice [98/104].
- **Fig. 14:** Roadmap Mind Map. **Importance:** Delineates future trajectories like "Simulation Planning" and "Multi-Agent Scaling" [144/148].

## Important Tables
- **Table 1:** Structural and operational differences. **Summary:** Distinguishes definition, autonomy, and complexity.
- **Table 10/11:** Representative models. **Summary:** Lists AutoGen, BabyAGI, and "World's first AI hospital".

## Important References
- **Wu et al. (2023) [AutoGen]:** Foundation for multi-agent conversation [98/184].
- **Acharya et al. (2025) [Agentic AI]:** Foundational survey on autonomous intelligence [22/160].
- **Yao et al. (2023) [ReAct]:** Foundational reasoning/acting framework [136/196].

## Keywords
1. Agentic AI
2. AI Agents
3. Conceptual Taxonomy
4. Multi-agent Systems
5. Healthcare
6. Persistent Memory
7. Orchestration
8. Task Decomposition
9. RAG
10. Clinical Decision Support
11. Patient Monitoring
12. Autonomy
13. Human-in-the-loop
14. Causal Reasoning
15. FHIR (Inferred via Enterprise API)
16. ICU Management

## Personal Notes
- **Key Takeaways:** Agentic AI is the "system-level intelligence" required for my thesis, not just isolated LLM tools.
- **Ideas for Thesis:** Implement the "Shared Memory Buffer" to synchronize the Triage agent and the Physician agent.
- **Future Research:** Explore the "Absolute Zero" (AZR) paradigm to evolve my clinical agents using simulated patient cases from Paper 011.
- **Supervisor Questions:** How do we establish the "Agent-to-Agent" (A2A) protocol in a hospital setting with mixed vendor EHRs?.

## Relevance Score
**10/10**
**Justification:** This is the definitive taxonomy paper. It provides the **architectural and conceptual blueprint** for differentiating your "Agentic AI Framework" from simple medical chatbots or single-agent LLM systems.

## Final Verdict
- **Why this paper matters:** It formalizes the shift from "tools" to "ecosystems" in AI.
- **Contribution to the thesis:** Provides the "Multi-Agent Orchestration" logic specifically for ICU/Monitoring scenarios.
- **Concepts to adopt:** The four-tier architecture (Perception, Reasoning, Persistent Memory, Orchestration).
- **Research gaps addressed:** Addresses the "conflation" problem and sets a roadmap for safe, collaborative clinical AI.