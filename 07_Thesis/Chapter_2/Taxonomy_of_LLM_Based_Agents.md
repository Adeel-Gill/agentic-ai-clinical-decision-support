# 2.X Taxonomy of Large Language Model (LLM)-Based Agents

## 2.X.1 Introduction

The rapid advancement of Large Language Models (LLMs) has resulted in the development of intelligent agent architectures capable of performing complex reasoning, planning, and decision-making tasks. However, LLM-based agents differ significantly in their capabilities, architectures, and application domains. To systematically understand these differences, researchers have proposed various taxonomies that classify agents based on their functional components and operational capabilities.

A taxonomy provides a structured representation of how LLM-based agents are designed, what capabilities they possess, and how these capabilities contribute to autonomous behavior. For the proposed research, understanding these categories is essential because an intelligent healthcare agent requires multiple capabilities, including memory management, clinical reasoning, planning, tool interaction, and collaboration among specialized agents.

Based on the reviewed literature, LLM-based agents can be categorized into six major capability dimensions:

1. Memory
2. Planning
3. Reasoning
4. Tool Use
5. Multi-Agent Collaboration
6. Healthcare Applications

The proposed taxonomy organizes existing research works according to these dimensions and identifies their relevance to healthcare-oriented Agentic AI systems.

---

# 2.X.2 Memory-Based Agents

Memory is one of the fundamental components that enables LLM-based agents to maintain context and perform long-term interactions. Traditional LLMs mainly rely on the current input context, which limits their ability to remember previous interactions or experiences.

Memory-based agents overcome this limitation by incorporating external memory mechanisms that allow storage, retrieval, and utilization of historical information.

Memory mechanisms are generally divided into:

- Short-term memory
- Long-term memory
- Semantic memory
- Episodic memory
- Vector-based memory

Short-term memory maintains the current conversation or task context, while long-term memory stores historical experiences and knowledge that can be retrieved when required.

## Generative Agents

Generative Agents introduced a memory stream architecture that enables agents to record experiences, retrieve relevant information, and perform reflection. The memory mechanism allows agents to maintain consistent behavior over extended interactions.

The concept is highly relevant to healthcare systems because patient monitoring requires maintaining historical information such as:

- Previous diagnoses
- Medication history
- Treatment responses
- Clinical observations

A memory-enabled healthcare agent can use previous patient information to provide more personalized recommendations.

---

## Autonomous Agent Surveys

Recent surveys on LLM-based autonomous agents identify memory as a critical capability for intelligent systems. These studies categorize memory into different forms and highlight its importance for improving agent autonomy, personalization, and decision consistency.

For clinical decision support, memory mechanisms enable continuous patient understanding rather than isolated analysis of individual clinical events.

---

# 2.X.3 Planning-Based Agents

Planning enables agents to transform high-level goals into executable sequences of actions. Unlike traditional LLMs that directly generate responses, planning-based agents analyze objectives, divide them into smaller tasks, and determine appropriate execution strategies.

Planning approaches include:

- Task decomposition
- Hierarchical planning
- Feedback-based planning
- Multi-step reasoning

## ReAct

The ReAct framework introduced a reasoning and acting paradigm where agents alternate between internal reasoning and external actions.

The agent follows an iterative process:

1. Understand the objective.
2. Generate reasoning steps.
3. Select an action.
4. Observe results.
5. Update the plan.

This approach allows agents to dynamically adapt their strategies based on new information.

---

## AutoGen

AutoGen provides a framework for building multi-agent workflows where agents can collaborate through conversation-based programming. It supports task decomposition, agent coordination, and human interaction.

In healthcare applications, AutoGen-inspired architectures can enable coordination between monitoring, diagnosis, and treatment recommendation agents.

---

## MetaGPT

MetaGPT introduces structured workflows by embedding Standard Operating Procedures (SOPs) into multi-agent collaboration. Each agent performs a specialized role according to predefined processes.

This concept is valuable for healthcare because clinical workflows often follow standardized guidelines and protocols.

---

# 2.X.4 Reasoning-Based Agents

Reasoning capability allows agents to analyze complex problems, evaluate evidence, and generate informed decisions.

Healthcare applications require advanced reasoning because clinical decisions depend on multiple factors, including:

- Patient history
- Symptoms
- Laboratory results
- Medical guidelines
- Previous treatment outcomes

---

## ReAct Reasoning

ReAct combines chain-of-thought reasoning with external actions. The agent reasons about a problem while simultaneously interacting with external information sources.

This capability improves transparency because intermediate reasoning steps can provide insight into how decisions are generated.

---

## MedAgents

MedAgents applies multi-agent collaboration for medical reasoning. It simulates discussions among specialized medical experts, allowing agents to analyze clinical problems from different perspectives.

The framework demonstrates that collaborative reasoning can improve diagnostic accuracy and reduce individual model errors.

---

## MedRAG

MedRAG integrates Retrieval-Augmented Generation with medical knowledge graphs to improve clinical reasoning.

The system retrieves relevant medical information and combines it with reasoning processes to generate more accurate diagnostic suggestions.

This approach is particularly relevant for clinical decision support systems requiring evidence-based recommendations.

---

# 2.X.5 Tool-Using Agents

LLMs have limited knowledge boundaries because their internal parameters may not contain updated or domain-specific information. Tool-using agents address this limitation by connecting language models with external resources.

Common tools include:

- Search engines
- Databases
- APIs
- Calculators
- Knowledge repositories

---

## Toolformer

Toolformer introduced a self-learning approach where language models learn when and how to call external tools.

The framework demonstrates that tool usage can improve factual accuracy and reduce hallucination.

For healthcare applications, similar approaches can allow agents to access:

- Drug databases
- Clinical guidelines
- Electronic Health Records
- Medical calculators

---

## RAG-Based Tool Integration

Retrieval-Augmented Generation has become one of the most important tools for healthcare agents. RAG allows agents to retrieve relevant information before generating responses.

This improves:

- Knowledge accuracy
- Clinical reliability
- Explainability

---

# 2.X.6 Multi-Agent Systems

Multi-agent systems consist of multiple specialized agents that communicate and collaborate to solve complex problems.

Instead of relying on a single general-purpose model, multi-agent architectures distribute responsibilities among different agents.

---

## CAMEL

CAMEL introduced role-playing-based communication between autonomous agents. Agents receive specific roles and collaborate to complete tasks.

This approach demonstrates how specialized agents can maintain structured communication.

---

## AutoGen

AutoGen enables flexible multi-agent conversations where agents can exchange information, execute tools, and involve humans when necessary.

---

## MetaGPT

MetaGPT applies role-based collaboration using predefined workflows and software engineering-inspired processes.

The same concept can be adapted for healthcare workflows where different agents represent different clinical functions.

---

## Agent Hospital

Agent Hospital introduces a simulated healthcare environment where medical agents interact with patient agents and improve through experience.

This demonstrates the possibility of creating autonomous healthcare ecosystems.

---

# 2.X.7 Healthcare-Oriented LLM Agents

Healthcare represents one of the most important application domains for Agentic AI because medical decision-making requires continuous monitoring, reasoning, and evidence integration.

Important healthcare-focused agent systems include:

---

## MedAgents

MedAgents demonstrates collaborative medical reasoning through multiple expert agents. It provides a foundation for designing clinical consultation systems.

---

## MedRAG

MedRAG combines retrieval mechanisms with medical knowledge graphs to improve diagnostic accuracy and evidence-based reasoning.

---

## Med-PaLM

Med-PaLM focuses on improving medical question answering capabilities through specialized training and evaluation frameworks.

---

## Clinical Camel

Clinical Camel explores open medical language models designed for privacy-aware healthcare conversations.

---

## Agent Hospital

Agent Hospital demonstrates autonomous medical agents operating in a simulated hospital environment.

---

## Med-PaLM M

Med-PaLM M introduces multimodal biomedical intelligence by combining different healthcare data types, including medical images and clinical text.

---

# 2.X.8 Relationship with Proposed Framework

The proposed thesis framework, **"An Agentic AI Framework for Intelligent Patient Monitoring and Clinical Decision Support,"** integrates multiple taxonomy dimensions.

The proposed architecture combines:

| Taxonomy Dimension | Proposed Framework Component |
|---|---|
| Memory | Patient history memory, vector database, clinical context storage |
| Planning | Task planner and workflow coordinator |
| Reasoning | ReAct-based clinical reasoning engine |
| Tool Use | RAG, medical knowledge retrieval, database access |
| Multi-Agent | Specialized healthcare agents |
| Healthcare | Patient monitoring and clinical decision support |

This integration enables the proposed framework to move beyond conventional AI prediction models toward an adaptive and autonomous clinical assistant.

---

# 2.X.9 Chapter Summary

This section presented a taxonomy of LLM-based agents based on six major capability dimensions: memory, planning, reasoning, tool use, multi-agent collaboration, and healthcare applications.

The reviewed studies demonstrate that modern Agentic AI systems rely on the combination of these capabilities to achieve autonomous behavior. The taxonomy provides the theoretical foundation for designing the proposed healthcare agent framework, where multiple specialized agents collaborate with memory, reasoning, and retrieval capabilities to support intelligent patient monitoring and clinical decision-making.