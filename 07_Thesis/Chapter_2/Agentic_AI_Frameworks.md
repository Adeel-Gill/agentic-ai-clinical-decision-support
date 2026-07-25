# 2.5 Agentic AI Frameworks and Architectures

The rapid development of Large Language Models (LLMs) has transformed artificial intelligence systems from passive response-generation models into intelligent systems capable of autonomous decision-making, reasoning, planning, and interaction with external environments. These systems are commonly referred to as **LLM-based Agents** or **Agentic AI systems**.

Unlike traditional artificial intelligence models that perform specific tasks based on predefined instructions, Agentic AI systems are designed to achieve complex goals by combining multiple capabilities, including reasoning, planning, memory management, tool utilization, and collaboration between multiple specialized agents.

An agentic AI architecture generally consists of several interconnected components:

- **Memory Module:** Maintains historical information, previous interactions, and learned knowledge.
- **Reasoning Engine:** Enables logical analysis and decision-making.
- **Planning Module:** Decomposes complex objectives into smaller executable tasks.
- **Tool Integration Layer:** Allows agents to access external resources and APIs.
- **Multi-Agent Communication:** Enables collaboration among specialized agents.
- **Knowledge Retrieval:** Provides access to external knowledge sources through techniques such as Retrieval-Augmented Generation (RAG).

These capabilities make Agentic AI highly suitable for healthcare applications where intelligent systems must continuously analyze patient information, retrieve medical knowledge, reason about clinical conditions, and support healthcare professionals in decision-making.

---

# 2.5.1 ReAct Framework

The **ReAct (Reasoning and Acting)** framework introduced an important paradigm shift in LLM-based agent development by combining reasoning processes with external actions.

Traditional LLMs generate responses based only on their internal knowledge. However, they often struggle with tasks requiring external information retrieval, dynamic planning, and interaction with external environments.

ReAct addresses this limitation by introducing an iterative reasoning-action cycle:

1. Reasoning about the current situation
2. Selecting an appropriate action
3. Receiving observations from the environment
4. Updating reasoning based on new information

The framework enables an agent to generate intermediate reasoning steps before performing actions such as searching external databases or calling APIs.

The general workflow of ReAct can be represented as:


User Goal
↓
Reasoning
↓
Action Selection
↓
External Tool Interaction
↓
Observation
↓
Updated Reasoning
↓
Final Decision


The ReAct approach is highly relevant to healthcare decision-support systems because clinical decisions often require continuous evaluation of new evidence. For example, a clinical agent can analyze patient symptoms, retrieve relevant medical guidelines, evaluate possible diagnoses, and update recommendations.

However, ReAct has limitations. It primarily depends on the current context window and does not provide a dedicated long-term memory mechanism. This limitation makes it challenging for applications requiring continuous patient monitoring over extended periods.

---

# 2.5.2 AutoGen Framework

The **AutoGen framework** introduces a flexible architecture for developing applications based on multiple interacting LLM agents.

Instead of depending on a single intelligent agent, AutoGen enables the creation of specialized agents that communicate and collaborate to solve complex tasks.

The major components of AutoGen include:

- Agent specialization
- Conversation-based communication
- Human-in-the-loop interaction
- External tool execution
- Task decomposition

A typical AutoGen workflow involves multiple agents with different responsibilities:

Coordinator Agent
|

| | |
Planning Reasoning Verification
Agent Agent Agent


In healthcare applications, this architecture can support collaborative clinical workflows:

- Monitoring Agent analyzes patient vitals.
- Diagnosis Agent evaluates possible medical conditions.
- Treatment Agent suggests interventions.
- Verification Agent checks recommendations against medical guidelines.

The primary advantage of AutoGen is its ability to create scalable multi-agent systems. However, challenges remain regarding communication efficiency, computational cost, and ensuring reliable coordination among autonomous agents.

---

# 2.5.3 CAMEL Framework

The **CAMEL (Communicative Agents for Mind Exploration of Large Language Model Society)** framework focuses on autonomous communication and cooperation between multiple LLM agents.

The central idea of CAMEL is role-based agent collaboration. Each agent receives a specific role and responsibility, allowing multiple agents to cooperate without continuous human guidance.

Examples of agent roles include:

- Planner Agent
- Domain Expert Agent
- Critic Agent
- Execution Agent

The role-playing approach improves task organization and reduces ambiguity during collaboration.

For healthcare applications, CAMEL provides a foundation for developing specialized clinical agents representing different healthcare roles.

For example:


Medical Agent Team

Cardiology Agent
|
Diagnosis Agent
|
Pharmacy Agent
|
Clinical Review Agent


Such collaboration can support complex medical reasoning by combining knowledge from multiple specialized agents.

However, CAMEL still faces challenges related to communication loops, incorrect reasoning propagation, and maintaining alignment with human objectives.

---

# 2.5.4 MetaGPT Framework

The **MetaGPT framework** introduces structured multi-agent collaboration by incorporating software engineering principles such as workflows, predefined roles, and Standard Operating Procedures (SOPs).

Unlike unrestricted agent communication, MetaGPT provides controlled workflows where each agent follows a specific responsibility.

The framework includes:

- Role-based agent design
- Shared information management
- Structured workflows
- SOP-driven task execution

The use of SOPs is particularly important for healthcare environments because medical systems require adherence to established clinical protocols.

A healthcare implementation inspired by MetaGPT could define workflows such as:


Patient Data Analysis
↓
Clinical Assessment
↓
Diagnosis Generation
↓
Treatment Recommendation
↓
Safety Verification


This structured approach can reduce hallucinations and improve reliability in clinical decision-support systems.

However, MetaGPT requires further research to support continuous learning and adaptation in highly dynamic healthcare environments.

---

# 2.5.5 Agent Hospital Framework

The **Agent Hospital framework** represents one of the earliest attempts to apply agentic AI concepts specifically within healthcare environments.

The framework introduces a simulated hospital environment where autonomous medical agents interact with virtual patients.

The system includes agents responsible for:

- Patient consultation
- Diagnosis
- Treatment planning
- Clinical reasoning
- Medical knowledge improvement

A significant contribution of Agent Hospital is the ability of agents to learn from previous experiences.

The framework maintains:

- Medical case memory
- Successful treatment experiences
- Failure-based learning rules

This enables agents to improve future decisions by reflecting on previous outcomes.

The concept is highly relevant to intelligent patient monitoring because healthcare systems require continuous learning from patient history, previous treatments, and clinical outcomes.

However, current limitations include:

- Limited real-world clinical validation
- Lack of multimodal patient data integration
- Need for stronger safety mechanisms

---

# 2.5.6 Comparison of Agentic AI Frameworks

The major agentic AI frameworks provide different capabilities that contribute toward building intelligent healthcare systems.

| Framework | Main Capability | Healthcare Application |
|---|---|---|
| ReAct | Reasoning and external action interaction | Evidence-based clinical reasoning |
| AutoGen | Multi-agent communication | Collaborative clinical workflows |
| CAMEL | Role-based agent collaboration | Specialized healthcare agents |
| MetaGPT | SOP-driven execution | Guideline-based medical workflows |
| Agent Hospital | Healthcare agent simulation | Autonomous clinical learning |

---

# 2.5.7 Research Gap in Existing Agentic AI Frameworks

Although existing frameworks demonstrate significant progress, they do not provide a complete solution for intelligent patient monitoring and clinical decision support.

Current limitations include:

- Limited long-term patient memory management
- Insufficient integration with real clinical datasets
- Lack of continuous patient monitoring capabilities
- Limited explainability of autonomous decisions
- Challenges in ensuring trustworthy AI behavior
- Need for human-in-the-loop clinical validation

Existing frameworks mainly focus on general-purpose task completion rather than healthcare-specific decision support.

Therefore, this research proposes an **Agentic AI Framework for Intelligent Patient Monitoring and Clinical Decision Support** that integrates:

- MIMIC-IV clinical data
- Patient memory management
- Retrieval-Augmented Generation (RAG)
- Clinical reasoning agents
- Multi-agent collaboration
- Trustworthy AI mechanisms
- Human validation

The proposed framework aims to bridge the gap between general-purpose LLM agents and reliable healthcare decision-support systems.