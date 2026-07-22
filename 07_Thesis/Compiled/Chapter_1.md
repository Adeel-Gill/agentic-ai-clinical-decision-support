# CHAPTER ONE: INTRODUCTION

This chapter introduces the research and sets out its motivation, aims, and structure. It opens with the background that frames clinical data overload and the shift from passive Large Language Models to Agentic AI, then states the problem the thesis addresses and the specific gap it targets. The chapter next presents the research objectives and the five research questions that guide the investigation, defines the scope and boundaries of the work, and explains its significance for both research and clinical practice. It then gives an overview of the design-oriented research methodology, describes how the remaining chapters are organized, and closes with a summary of the argument developed here. Together these sections establish why an integrated, supervised Agentic AI framework for intelligent patient monitoring is needed and how the rest of the thesis develops it.

## 1.1 Background

Modern hospitals produce clinical data faster than clinicians can read it. A single intensive care admission generates streams of vital signs, laboratory panels, medication orders, imaging reports, and free-text notes, and each of these has to be interpreted under time pressure and often at odds with an already heavy caseload. The bottleneck is no longer the availability of data but the cognitive work of turning it into a decision. This tension has made healthcare one of the most studied application areas for artificial intelligence, where the promise is not to remove the clinician but to reduce the load of synthesis that precedes every judgment [thirunavukarasu2023llms].

Large Language Models (LLMs) sharpened that promise considerably. They read clinical narratives, answer medical questions, and summarize records with a fluency that earlier natural-language systems never reached, and specialized models such as Med-PaLM have shown that this competence extends to expert-level medical question answering [singhal2023clinical][thirunavukarasu2023llms]. Yet fluency is not the same as competence in a clinical workflow. A conventional LLM assistant waits for a prompt, answers once, and forgets the exchange. It holds no persistent record of the patient, plans nothing beyond the current turn, and cannot consult an external guideline unless a human hands it one. For episodic question answering these limits are tolerable; for continuous patient monitoring, where context accumulates over days and a missed trend can matter, they are disqualifying.

Agentic AI reframes the model as one component inside a larger loop rather than the whole system. An agent perceives its environment, reasons about a goal, plans a sequence of steps, calls external tools, writes to and reads from memory, and revises its approach when feedback contradicts its expectations [xi2023rise][wang2024survey]. The reasoning-and-acting pattern formalized in ReAct, the multi-agent coordination demonstrated by AutoGen and CAMEL, and the emergent social behavior of Generative Agents each supplied a piece of this machinery [yao2023react][wu2024autogen][li2023camel][park2023generative]. Sapkota and colleagues argue that the shift from a single tool-using model to a coordinated society of specialized agents is a genuine architectural break rather than a rebranding, and that distinction matters for a domain as compartmentalized as medicine [sapkota2025agents].

Healthcare-oriented agent systems have started to appear, and they are instructive precisely because they remain partial. MedAgents stages a role-played consultation among specialist agents to improve medical reasoning [tang2024medagents]; MedRAG couples retrieval with structured medical knowledge to raise diagnostic specificity [zhao2025medrag]; Agent Hospital simulates an entire care setting populated by autonomous agents [li2024agenthospital]; and Clinical Camel adapts an open model for medical dialogue [toma2023clinicalcamel]. Each advances one capability well. None assembles reasoning, persistent patient memory, evidence retrieval, multi-agent collaboration, and physician oversight into a single architecture aimed at longitudinal monitoring, and that omission is the space this thesis occupies.

This research proposes an Agentic AI framework for intelligent patient monitoring and clinical decision support. The proposed framework organizes memory management, Retrieval-Augmented Generation (RAG), multi-agent collaboration, reasoning, planning, and trustworthy-AI safeguards into a layered design, and it uses the publicly available MIMIC-IV critical-care database as its data source [johnson2023mimic][lewis2020rag]. The design goal is deliberately modest about autonomy and firm about accountability: the framework generates explainable recommendations, but a clinician reviews and authorizes every one of them through a human-in-the-loop step.

## 1.2 Problem Statement

Healthcare organizations accumulate structured and unstructured records at a scale that outpaces manual interpretation. Electronic Health Records (EHRs), laboratory reports, medication histories, physiological measurements, and clinical notes each carry part of the picture, and a clinician must reconcile them quickly to reach a defensible decision about diagnosis, treatment, and ongoing management. Volume and heterogeneity together make that reconciliation slow and error-prone, and the cost of the delay falls hardest in critical care.

LLM-based tools address only the surface of this problem. They read and generate clinical language well, but most deployed systems behave as passive responders: they answer the prompt in front of them and retain nothing afterward [thirunavukarasu2023llms]. They rarely plan across steps, seldom maintain a durable model of the patient, and do not, on their own, coordinate with other specialized components. The consequence is a landscape of narrow tools, each solving one prediction or extraction task, with little that supports a clinical workflow end to end [zhou2024survey].

Existing clinical decision support inherits these weaknesses and adds its own. Systems that achieve strong predictive accuracy often cannot explain a recommendation, cannot retrieve and cite current medical evidence, and cannot preserve long-term patient context across encounters. Where retrieval is added, as in RAG-based medical systems, it is typically applied to isolated question answering rather than to continuous monitoring under supervision [zhao2025medrag][gao2023rag]. What is missing is not another accurate classifier but an integrated architecture.

This thesis therefore targets a specific gap: the absence of a unified Agentic AI framework that combines memory management, reasoning, planning, Retrieval-Augmented Generation, multi-agent collaboration, and trustworthy-AI principles for intelligent patient monitoring, and that is designed and evaluated against real-world critical-care data such as MIMIC-IV [johnson2023mimic].

## 1.3 Research Objectives

The primary objective is to design an Agentic AI framework for intelligent patient monitoring and clinical decision support, developed and assessed using the MIMIC-IV dataset [johnson2023mimic].

The specific objectives follow from it. The first is to survey recent work on Agentic AI, LLMs, and intelligent healthcare systems, and to read that literature critically rather than descriptively so that the review yields a defensible gap. The second is to characterize the concrete limitations of existing clinical decision support, distinguishing genuine architectural shortfalls from problems that are merely unsolved engineering. The third is to develop a layered framework that integrates memory, reasoning, planning, RAG, and multi-agent collaboration as interacting layers rather than bolted-on features. The fourth is to design the specialized agents that populate that framework, with distinct responsibilities for monitoring, diagnostic support, risk prediction, treatment recommendation, and clinical explanation. The fifth is to embed trustworthy-AI principles, explainability, transparency, safety verification, auditability, and human-in-the-loop validation, into the architecture rather than treating them as an afterthought. The sixth is to ground the whole design in MIMIC-IV as the primary data source. The seventh, and the one that keeps the thesis honest about its limits, is to deliver a conceptual architecture together with a bounded prototype and a concrete evaluation plan that later work can implement and test at scale.

## 1.4 Research Questions

Five questions structure the investigation, and each maps onto a chapter of analysis rather than a single claim.

**RQ1.** What specific limitations of current LLM-based healthcare systems obstruct intelligent patient monitoring and clinical decision support, and which of them are architectural rather than incidental?

**RQ2.** How can Agentic AI improve reasoning, planning, memory management, and autonomous collaboration in a clinical setting without eroding physician control?

**RQ3.** How can multiple specialized agents collaborate on a clinical decision while preserving explainability and physician oversight at every step?

**RQ4.** How can Retrieval-Augmented Generation and external medical knowledge improve the reliability and transparency of AI-generated recommendations, and where does retrieval fail to help?

**RQ5.** How can the proposed framework support intelligent patient monitoring when instantiated on the MIMIC-IV dataset [johnson2023mimic]?

The framing of RQ1 and RQ4 is intentional: each asks not only what a capability adds but where it stops working, because a review that only catalogs strengths cannot locate a real gap.

## 1.5 Scope of the Research

This work is a design study. Its deliverable is a conceptual Agentic AI framework, supported by a bounded prototype, rather than production software installed in a hospital. The framework integrates autonomous reasoning, memory management, RAG, planning, and multi-agent collaboration, and it is built around MIMIC-IV, which supplies anonymized critical-care records under a credentialed data-use agreement [johnson2023mimic].

The design covers both structured and unstructured inputs, including demographics, admissions, laboratory results, vital signs, medications, diagnoses, procedures, and clinical notes. A clinician validation layer is part of the architecture by construction, so that recommendations assist rather than replace medical judgment.

Three things fall outside the scope, and naming them protects the claims that remain inside it. The thesis does not deliver production-ready hospital software, does not integrate with live EHR systems, and does not conduct a prospective clinical trial on real patients. What it does deliver is a framework specification and evaluation plan detailed enough to guide the implementation and validation that a follow-on project would undertake.

## 1.6 Significance of the Research

The contribution is integrative rather than atomic. Reasoning strategies, memory architectures, retrieval, and multi-agent coordination already exist as separate research threads, and each has been demonstrated in isolation [yao2023react][wu2024autogen][zhao2025medrag]. The value here lies in specifying how they compose into a single clinical architecture and in making the seams between them explicit, because the seams are where most integrated systems fail. Layering trustworthy-AI mechanisms, explainability, transparency, auditability, and human oversight, into that composition is part of the same argument rather than a separate feature list.

For practice, the framework describes a system that watches patient state over time, retrieves relevant evidence, assesses risk, drafts recommendations, and explains each one in terms a clinician can check and overrule. Its stance toward the clinician is supportive by design: the human keeps final authority, and the architecture is arranged so that authority is easy to exercise rather than nominal.

The study also lays groundwork. By anchoring the design to MIMIC-IV and pairing it with an evaluation plan, it gives later researchers a concrete starting point for implementation and empirical testing rather than a diagram to reinterpret [johnson2023mimic].

## 1.7 Research Methodology Overview

The methodology is design-oriented and proceeds in four phases. The first is a critical literature review spanning Agentic AI, LLMs, multi-agent systems, RAG, reasoning frameworks, and intelligent healthcare applications, read with the aim of exposing limitations rather than cataloging achievements [xi2023rise][zhou2024survey].

The second phase converts that reading into a research gap through comparative analysis of recent systems, and organizes the findings as a taxonomy of LLM-based agents that classifies architectural components and research trends. The third phase proposes the layered framework itself, integrating MIMIC-IV data handling, memory management, reasoning modules, multi-agent orchestration, clinical decision support, and trustworthy-AI mechanisms; the full architecture is presented in Chapter 3. The fourth phase analyzes the proposed design conceptually and against existing approaches, and specifies how a bounded prototype would be evaluated, with the experimental design detailed in Chapter 4.

## 1.8 Thesis Organization

The thesis runs to five chapters. Chapter 1 sets out the background, problem, objectives, questions, scope, significance, and methodology. Chapter 2 reviews the literature on LLMs, Agentic AI, reasoning methods, multi-agent systems, RAG, healthcare AI, and trustworthy AI, presents the taxonomy of LLM-based agents, and identifies the research gap. Chapter 3 presents the proposed framework and methodology, describing the layered architecture, the MIMIC-IV data source, and the interaction among the agents. Chapter 4 sets out the experimental design and evaluation, including the setup, metrics, and planned analysis. Chapter 5 concludes by summarizing the contributions, revisiting the research questions, stating the limitations honestly, and outlining future work.

Note that the architecture is documented in Chapter 3, not Chapter 4; earlier draft labels that placed the framework figures in Chapter 4 are corrected throughout this revision.

## 1.9 Chapter Summary

This chapter argued that the obstacle to useful clinical AI is integration, not raw model capability. LLMs read and write medical language well but act as passive, memoryless responders, and existing decision support tends to be accurate yet narrow, opaque, and disconnected from current evidence. Agentic AI supplies the missing machinery, reasoning, planning, memory, tool use, and collaboration, but the healthcare systems built on it so far each solve only one part of the problem. The proposed framework answers that gap by composing these capabilities into a layered, supervised architecture grounded in MIMIC-IV. The next chapter reviews the underlying literature in depth, builds the taxonomy of LLM-based agents, and states the research gap that the framework is designed to close.
