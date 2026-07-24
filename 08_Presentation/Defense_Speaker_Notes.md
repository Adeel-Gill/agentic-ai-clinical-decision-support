# Defense — Speaker Notes

Spoken script for the ~20-minute MS thesis proposal defense. Companion to
[Defense_Presentation.md](Defense_Presentation.md) (slides) and
[Defense_Examiner_QA.md](Defense_Examiner_QA.md) (anticipated questions). Notes are written to be
*spoken*, not read off the slides. Content is grounded in the drafted
[Chapter 1](../07_Thesis/Compiled/Chapter_1.md) and [Chapter 2](../07_Thesis/Compiled/Chapter_2.md).

**Pacing (~20 min):** Slides 1–4 ≈ 4 min (framing) · 5–7 ≈ 5 min (literature + gap, the crux) ·
8–10 ≈ 3 min (objectives/method) · 11–14 ≈ 6 min (the framework, the centerpiece) ·
15–17 ≈ 2 min (contributions, scope, close). Leave ~10 min for questions.

---

### Slide 1 — Title (~30 s)
Good morning, respected committee members and faculty. My name is Adeel Gill, and I am presenting my
MS Artificial Intelligence thesis proposal defense, titled *An Agentic AI Framework for Intelligent
Patient Monitoring and Clinical Decision Support*. I thank my supervisor, Dr. Fawad Nasim, for their
continuous guidance. Today I will move from a concrete clinical problem — data overload in critical care —
to the architectural gap in current clinical AI, and then to the framework I propose to close it.
My emphasis throughout is not raw diagnostic accuracy on static exams, but a verifiable,
memory-persistent architecture for longitudinal monitoring under physician oversight.

### Slide 2 — Clinical Data Overload (~1 min)
Modern hospitals produce clinical data far faster than clinicians can read and synthesize it. A
single ICU admission generates a heterogeneous stream: vital signs, laboratory panels, medication
orders, imaging reports, and unstructured free-text notes. The bottleneck in modern care is no
longer the *availability* of data but the *cognitive work* of turning it into a timely, defensible
decision. This is why healthcare has become one of the most studied application areas for AI — and
the framing matters: the goal is not to remove the clinician, but to reduce the load of synthesis
that precedes every judgment. That is the foundational motivation for this work.

### Slide 3 — The Shift to Agentic AI (~1 min)
Large Language Models sharpened that promise. Models such as Med-PaLM reach expert-level medical
question answering. But fluency is not competence in a *workflow*. A conventional LLM assistant
waits for a prompt, answers once, and forgets the exchange — it holds no persistent record of the
patient, plans nothing beyond the current turn, and cannot consult a guideline unless a human hands
it one. For episodic question answering that is tolerable; for continuous monitoring, where context
accumulates over days and a missed trend matters, it is disqualifying. Agentic AI reframes the model
as one component inside a larger loop: it perceives, reasons about a goal, plans steps, calls
external tools, reads and writes memory, and revises when feedback contradicts its expectations.
That shift — from a single tool-using model to a coordinated society of specialized agents — is a
genuine architectural break, and it matters for a domain as compartmentalized as medicine.

### Slide 4 — Problem Statement (~1 min)
Healthcare organizations accumulate structured and unstructured records at a scale that outpaces
manual interpretation — EHRs, lab reports, medication histories, physiological measurements, notes.
A clinician must reconcile all of it quickly to reach a defensible decision, and volume plus
heterogeneity make that slow and error-prone, most acutely in critical care. LLM-based tools address
only the surface: they read and generate clinical language well, but most deployed systems behave as
passive responders that retain nothing afterward. They rarely plan across steps, seldom maintain a
durable patient model, and do not coordinate with other components on their own. Existing clinical
decision support inherits these weaknesses and adds its own — strong predictive accuracy, but often
no explanation, no current-evidence retrieval, and no long-term context. What is missing is not
another accurate classifier but an integrated architecture.

### Slide 5 — Agentic Frameworks (~1.5 min)
My literature review examined the foundational agentic frameworks critically. ReAct was a major
breakthrough — it interleaves reasoning traces with external actions — but it leans on the
short-term context window and lacks dedicated long-term memory. AutoGen and CAMEL introduced
multi-agent coordination and role-play, letting specialized agents decompose tasks the way clinical
teams do, though they can fall into unproductive communication loops. MetaGPT advanced this by
encoding Standard Operating Procedures, which aligns naturally with strict medical protocols. But
reading these critically exposes a shared shortcoming: they are *general-purpose*. They offer limited
long-term patient memory, no integration with real clinical datasets, and no built-in
human-in-the-loop validation. They cannot be deployed out-of-the-box for longitudinal healthcare
monitoring.

### Slide 6 — RAG & Healthcare AI (~1.5 min)
In healthcare specifically, specialized models like Med-PaLM show expert-level QA, yet they depend
on internal parametric knowledge and lack continuous integration with patient-specific data. To
combat hallucination — a critical failure mode in medicine — Retrieval-Augmented Generation
separates *knowing* from *remembering*: it retrieves relevant material from external sources before
generating, so the output rests on inspectable evidence. MedRAG uses this to couple retrieval with
structured medical knowledge and raise diagnostic specificity. But the boundary is scope: current
medical RAG is applied predominantly to *episodic* question answering and snapshot differential
diagnosis. It is rarely applied *continuously* over a longitudinal patient workflow. That boundary
is a large part of the gap.

### Slide 7 — Research Gap (~2 min) — THE CRUX
This is the heart of the argument, so I'll be precise. The gap is not merely "no integrated system
exists" — it is *how narrowly* current capabilities are grounded and evaluated. First, existing
multi-agent systems report gains on static examination benchmarks, not longitudinal clinical
records. High exam accuracy gives little assurance that an agent can follow a *deteriorating* patient
across days of noisy observations. Second, where RAG is used, it typically pulls general medical
literature and is rarely anchored to the patient's *own* longitudinal EHR timeline. Third — and most
critically for medicine — verification and auditability are treated as future aspirations rather
than measured, first-class components. Agent *consensus* is not the same as evidential *entailment*:
several agents can agree and still be wrong. An architecture that treats verifiable safety as a
structural layer, evaluated on longitudinal data, is what is missing. That intersection is the space
this thesis occupies.

### Slide 8 — Research Objectives (~1 min)
The primary objective is to design an Agentic AI framework for intelligent patient monitoring and
clinical decision support, developed and assessed using MIMIC-IV. The specific objectives follow:
develop a layered architecture that integrates memory, ReAct-style reasoning, and RAG as
*interacting layers* rather than bolted-on features; design the specialized agents that populate it,
with distinct responsibilities for monitoring, diagnosis, risk prediction, treatment, and
explanation; embed trustworthy-AI principles — explainability, safety verification, auditability,
and human-in-the-loop validation — into the architecture rather than as an afterthought; and deliver
a bounded prototype plus a concrete evaluation plan that later work can implement and test at scale.

### Slide 9 — Research Questions (~1 min)
Five questions structure the investigation, and each is framed to locate limits, not just catalog
strengths. RQ1 asks which limitations of current LLM systems are *architectural* rather than
incidental. RQ2 and RQ3 address the agentic mechanics — how specialized agents improve reasoning,
planning, and memory, and collaborate, *without eroding physician control or explainability*. RQ4
examines RAG deliberately from both sides: how external knowledge improves reliability, and *where
retrieval fails to help*. RQ5 asks how the framework supports monitoring when instantiated on the
real-world MIMIC-IV critical-care dataset.

### Slide 10 — Methodology (~1 min)
The methodology is design-oriented, in four phases. Phase 1 is a critical literature review across
Agentic AI, LLMs, multi-agent systems, RAG, reasoning frameworks, and healthcare AI — read to expose
limitations, not to catalog achievements. Phase 2 converts that reading into a research gap via
comparative analysis and organizes it as a taxonomy of LLM-based agents. Phase 3 is the core
contribution: the layered framework itself, integrating MIMIC-IV data handling, memory, reasoning,
multi-agent orchestration, decision support, and trustworthy-AI mechanisms — detailed in Chapter 3.
Phase 4 analyzes the design conceptually and against existing approaches and specifies how a bounded
prototype would be evaluated — detailed in Chapter 4.

### Slide 11 — Architecture Overview (~1.5 min) — CENTERPIECE
This is the heart of the thesis. The architecture stacks cooperating layers. At the base, the
Perception layer ingests heterogeneous EHR information — vitals, labs, unstructured notes. The Memory
layer stores it and maintains short- and long-term context, so agents can recall relevant prior
state rather than reasoning from an instant. Above that, the Reasoning and Orchestration layer
analyzes data with ReAct-style reasoning and sequences tasks, with a coordinator deciding which
specialized agent acts when. The Action layer carries decisions out as recommendations. Crucially,
the seams between layers are safeguarded: verification and human review are embedded across the
orchestration and action layers, so the stack cannot propagate unverified errors. The seams are
where integrated systems usually fail, so I make them explicit.

### Slide 12 — Specialized Agents (~1.5 min)
Because clinical work is compartmentalized, the framework mirrors that structure. At the center, the
Coordinator agent routes tasks by the patient's condition and resolves conflicting recommendations.
The Monitoring agent tracks patient state and vital trends over time. The Diagnosis agent retrieves
similar cases and weighs candidate conditions; the Treatment agent proposes evidence-based
interventions. And critically, an Explanation agent renders the reasoning path legible, while a
dedicated Verification agent acts as a safety gatekeeper — checking recommendations against
guidelines before they reach the clinician. That gatekeeper is how I ensure multi-agent consensus is
tested against evidence, not just assumed to equal accuracy.

### Slide 13 — RAG & MIMIC-IV (~1.5 min)
To ground the design in reality, the framework uses the publicly available MIMIC-IV critical-care
database, which supplies the longitudinal records — admissions, labs, medications, notes — needed to
reason about a patient *over time* rather than at a single instant. The framework applies retrieval
at the patient level: rather than retrieving only generic guidelines, agents also retrieve from the
patient's own historical timeline, anchoring reasoning to their evolving condition. Records are
processed into vector embeddings so the retriever can surface similar prior cases and relevant
history by semantic search, fusing external medical literature with patient-specific evidence for
contextualized decision support.

### Slide 14 — Trustworthy AI & HITL (~1.5 min)
Accuracy is necessary but insufficient in medicine — a recommendation cannot be acted on if the
reasoning is opaque. So trustworthy AI is engineered as a first-class layer. The explainability
module forces agents to surface the evidence and reasoning behind every output. The safety
verification module checks for contradictions and guideline compliance. Auditability is maintained by
logging exactly which data was used, which evidence was retrieved, and how agents interacted — a
tamper-evident trail. And most importantly, human-in-the-loop validation is enforced: the system is
an assistant, not an autonomous doctor. The clinician reviews the recommendation and retains final
authority to approve, modify, or reject it — which mitigates automation bias and keeps that authority
real rather than nominal.

### Slide 15 — Contributions (~45 s)
The contributions are integrative and structural. First, a coherent, verifiable architecture that
composes memory, ReAct reasoning, and multi-agent collaboration for longitudinal decision support.
Second, a methodological choice — pairing patient-timeline retrieval with a dedicated verification
agent as an explicit mechanism to reduce hallucination and enforce safety. Third, rather than a
theoretical diagram, a reproducible design, a bounded prototype, and a concrete evaluation protocol
on MIMIC-IV, giving later researchers a concrete starting point for implementation and empirical
clinical evaluation.

### Slide 16 — Scope Boundaries (~45 s)
It is vital to name the limits, because doing so protects the claims that remain inside them. This is
a *design study*. The deliverables are a conceptual framework, a bounded prototype, and an evaluation
plan on retrospective MIMIC-IV data. Explicitly out of scope: production-ready hospital software,
integration with live real-time EHR systems, and prospective clinical trials on real patients.
Naming these keeps the thesis focused and achievable within the Master's timeframe.

### Slide 17 — Conclusion & Q&A (~45 s)
In conclusion: the obstacle to useful clinical AI is *integration, not raw model capability*. LLMs
handle medical language well but act as passive, memoryless responders, and the healthcare systems
built on agents so far each solve only one part of the problem. By composing persistent memory,
patient-level RAG, ReAct reasoning, and specialized multi-agent collaboration into a layered,
supervised architecture grounded in MIMIC-IV and secured by human-in-the-loop validation, this
framework closes that gap — delivering transparent, evidence-based recommendations that assist,
rather than replace, clinical judgment. Thank you; I welcome your questions.
