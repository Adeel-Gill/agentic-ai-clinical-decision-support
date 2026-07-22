# 2.X Agentic AI: Concept, Characteristics, and Evolution from LLM Agents

## 2.X.1 Introduction to Agentic AI

Large Language Models made text generation cheap and fluent, and in doing so they exposed how little fluency alone accomplishes when a task requires acting over time. Out of that gap grew Agentic AI: systems that do not merely produce text but analyze a situation, form a plan, take actions, and adjust when the environment answers back [xi2023rise; wang2024survey]. The distinction is easy to blur, and Sapkota and colleagues take pains to separate a single tool-using model from a coordinated collection of specialized agents, arguing that only the latter earns the label "agentic" [sapkota2025agents]. That separation is not pedantic. A monitoring task that spans a multi-day admission cannot be served by a model that forgets each exchange, so the architectural difference has direct clinical consequences.

Where a task-specific model is trained to do one thing, an agent is organized around a goal it decomposes on its own. It reads a complex objective, breaks it into steps, chooses a strategy, reaches for external tools when its own knowledge runs out, and coordinates with other agents when the problem exceeds any single role [wang2024survey]. In healthcare this proactive stance matters because clinical work is itself a loop of observation, hypothesis, evidence-gathering, and revision rather than a one-shot answer.

The critical caveat, easy to lose in the enthusiasm, is that autonomy is a liability as much as a feature in medicine. The same initiative that lets an agent chase down evidence also lets it compound an early error across several steps before anyone notices, which is precisely why the sections that follow treat oversight as a design constraint rather than an add-on.

---

## 2.X.2 Evolution from Traditional AI to Agentic AI

The path to Agentic AI runs through several stages, and each stage solved a problem while leaving another untouched. Early clinical AI was rule-based: expert systems encoded medical knowledge as explicit if-then logic. They worked inside narrow, well-specified scenarios, but they demanded painstaking manual knowledge engineering and broke whenever a guideline changed or a patient failed to match a coded pattern. Because real medicine is thick with uncertainty and interacting factors, rule-based systems could never cover the space they were meant to serve.

Machine learning shifted the burden from hand-written rules to learned patterns, which enabled risk prediction, readmission estimation, and early-warning scores drawn from historical data. Deep learning pushed further, extracting features automatically from notes, images, and physiological signals. What neither delivered was reasoning that a clinician could follow or interaction that extended beyond a fixed prediction. The output was a number; the justification stayed inside the network.

LLMs then loosened the format constraint by handling open-ended language, but the earliest ones were conversational engines with no persistent memory, no planning, and no way to touch the world outside their context window. Agentic AI closes these gaps by wrapping an LLM in additional machinery, memory across short and long horizons, planning and task decomposition, explicit reasoning, tool use, Retrieval-Augmented Generation, multi-agent collaboration, and self-reflection [yao2023react; shinn2023reflexion; lewis2020rag]. The important point is that these components are not merely accumulated; they are what convert a response generator into a system that can pursue a goal. That said, each added component is also an added failure mode, and the literature has been quicker to demonstrate the capabilities than to characterize how they fail together.

---

## 2.X.3 Characteristics of Agentic AI Systems

Several properties separate an agentic system from a conventional model, and they are worth examining individually because a clinical framework has to earn each one.

### Autonomous Decision-Making

An agent decides with limited human intervention: it reads a goal, weighs the available information, and chooses an action from its own reasoning [wang2024survey]. In monitoring, that autonomy could surface an abnormal trend, flag a deteriorating risk profile, or draft a recommendation before a clinician has asked for one. The obvious tension is that unsupervised autonomy in a safety-critical setting can act on a wrong inference as readily as a right one, so the value of autonomy here is bounded by how tightly it is coupled to review.

### Goal-Oriented Planning

Agents are built around achieving objectives rather than emitting answers, and they can split a complex objective into an ordered set of steps. A clinical support agent might analyze vital signs, retrieve relevant history, compare findings against guidelines, assess risk, and only then draft a recommendation for review. Planning of this kind is what lets an agent handle multi-step workflows, yet a plan is only as sound as the model's grasp of the domain, and a confidently wrong plan is harder to catch than a single wrong answer.

### Memory and Context Awareness

Memory is the property most obviously missing from a plain LLM exchange, where prior turns need not persist. Agentic systems keep short-term conversational state, long-term patient history, and vector-based semantic stores so that later decisions draw on earlier context. For longitudinal monitoring this is not optional; a system that cannot remember yesterday's trajectory cannot reason about today's change. The open question, largely unresolved in the current literature, is how to keep such memory both clinically faithful and privacy-compliant as it grows.

### Reasoning and Self-Reflection

Agents interpose reasoning between observation and action. The ReAct pattern interleaves reasoning traces with tool calls so an agent can think, act, observe, and think again [yao2023react], while reflection mechanisms such as Reflexion let an agent critique a prior attempt and revise it [shinn2023reflexion]. In a domain where a wrong recommendation carries real cost, this capacity to reconsider is valuable, but self-reflection also risks rationalizing an initial error rather than correcting it, and the framework treats it as a support for human review rather than a substitute.

### Tool Utilization

Agents extend past their internal knowledge by calling external systems, databases, and APIs, an ability formalized in work such as Toolformer [schick2023toolformer]. A clinical agent might query a drug-information service, retrieve records, or consult a guideline repository. Tool use is what grounds an agent in current, verifiable information rather than stale training data, though it also imports the reliability and latency of whatever it calls, which becomes a real constraint in a monitoring loop.

### Multi-Agent Collaboration

Complex problems can be divided among specialized agents that communicate to reach a joint result, an approach demonstrated by AutoGen and CAMEL in general settings [wu2024autogen; li2023camel]. A clinical configuration might pair a monitoring agent with diagnostic, risk-prediction, treatment, explanation, and verification agents under a coordinator. Division of labor mirrors how clinical teams actually work, but it also multiplies the communication surface, and errors that pass silently between agents are among the least studied risks in this line of research.

---

## 2.X.4 Agentic AI Architecture

A typical agentic architecture stacks several cooperating layers, and mapping them onto healthcare clarifies both the fit and the strain.

The **perception layer** ingests information from the environment, which in a clinical system means EHR records, demographics, laboratory results, vital signs, notes, and medication history. The **memory layer** stores that information and maintains context, combining short- and long-term stores with vector databases and knowledge repositories so that agents can recall relevant prior experience. The **reasoning layer** analyzes what perception and memory supply, drawing on Chain-of-Thought prompting, ReAct-style reasoning, and retrieval-augmented inference to reach a decision [wei2022chain; yao2023react; lewis2020rag]. The **planning and orchestration layer** sequences tasks and routes them among agents, with a coordinator deciding which agent acts and when. The **action layer** carries decisions back out, generating recommendations, updating records, or communicating results.

Presented this cleanly, the layered picture can imply more maturity than exists. In practice the boundaries between reasoning, memory, and orchestration are contested, and most published architectures specify the layers far more precisely than they specify how the layers fail when one of them returns something wrong. The framework proposed in this thesis inherits that risk and addresses it by placing verification and human review across the orchestration and action layers rather than trusting the stack to be self-correcting.

---

## 2.X.5 Agentic AI in Healthcare

Healthcare is a natural target for agentic methods because medical decisions demand exactly what agents supply: continuous observation, multi-step reasoning, and the fusion of diverse information sources. A cluster of recent systems shows both the promise and the limits. MedAgents organizes a role-played consultation among specialist agents and reports gains on medical reasoning benchmarks, though its evaluation centers on question answering rather than on monitoring a patient over time [tang2024medagents]. MedRAG fuses retrieval with structured medical knowledge to improve diagnostic specificity, which helps most when candidate diagnoses share symptoms, yet it remains a diagnostic reasoning system rather than a full workflow [zhao2025medrag]. Agent Hospital simulates a whole care environment populated by autonomous agents and is valuable as a testbed, but a simulation of patients is not evidence about real ones [li2024agenthospital]. Clinical Camel adapts an open model for medical dialogue and lowers the barrier to healthcare-specific LLMs, while inheriting the memory and planning limits of the underlying model [toma2023clinicalcamel].

Read together, these systems make a consistent point: each demonstrates one capability convincingly and stops short of integrating the rest. The field has strong components and few architectures that combine them under clinical supervision, which is the gap the proposed framework targets.

---

## 2.X.6 Challenges and Limitations of Agentic AI

Several obstacles stand between these demonstrations and clinical deployment, and none is fully solved. Reliability is the first: agents can generate unsupported recommendations, and in medicine such errors reach the patient. Retrieval grounding reduces but does not eliminate the problem, because a confidently reasoned chain can still rest on a mis-retrieved fact [zhao2025medrag]. Explainability is the second: clinicians will not accept a black-box recommendation, so an agent that cannot show its evidence and reasoning is, for practical purposes, unusable regardless of its accuracy. Data privacy is the third, since agentic systems accumulate sensitive patient information in memory and logs, and secure, compliant handling is a precondition rather than a nicety. Safety and alignment form the fourth: autonomous agents must stay inside clinical guidelines and ethical bounds, which is why human oversight remains necessary for consequential decisions. The fifth is cost: memory, reasoning, retrieval, and multiple coordinated agents together impose a computational and latency burden that a real-time monitoring setting can ill afford. The honest summary is that the research literature has demonstrated capability far more thoroughly than it has demonstrated safety, and a clinical framework has to make up that difference deliberately.

---

## 2.X.7 Relevance to Proposed Research

Agentic AI supplies the theoretical foundation for the proposed framework, "An Agentic AI Framework for Intelligent Patient Monitoring and Clinical Decision Support." The framework adopts agentic principles concretely: it processes MIMIC-IV records, manages patient context in memory, retrieves clinical knowledge through RAG, coordinates specialized agents, applies clinical reasoning, and routes every recommendation through human-in-the-loop validation [johnson2023mimic; lewis2020rag]. The intent is not to add another capable component to the pile but to compose the existing ones into an architecture that is intelligent, adaptive, and, above all, accountable to the clinician who signs off on its output.

---

## 2.X.8 Chapter Summary

This section traced Agentic AI from rule-based systems through machine learning and early LLMs to goal-directed agents built from memory, planning, reasoning, tool use, and collaboration. Those properties make the paradigm a strong fit for clinical work, and a set of healthcare-specific systems has begun to demonstrate it, each convincingly but partially. The recurring limitation is integration under supervision: the field has capable parts and few safe wholes. That imbalance motivates the layered, human-supervised framework developed in the chapters that follow.
