# Defense — Anticipated Examiner Questions & Answers

Q&A preparation bank for the MS thesis proposal defense. Companion to
[Defense_Presentation.md](Defense_Presentation.md) (slides) and
[Defense_Speaker_Notes.md](Defense_Speaker_Notes.md) (spoken script). Answers are grounded in the
drafted [Chapter 1](../07_Thesis/Compiled/Chapter_1.md) and
[Chapter 2](../07_Thesis/Compiled/Chapter_2.md).

---

## On the choice of approach

**Q1. Why a complex Agentic AI architecture rather than just fine-tuning a single medical LLM?**
A fine-tuned model such as Med-PaLM excels on static, episodic queries but remains a passive
responder — it has no persistent memory and cannot plan across a multi-day admission. Fine-tuning
improves the *answer*; it does not add memory, planning, retrieval, or oversight *across a workflow*.
The gap I target is architectural, and only an agentic loop supplies that machinery.

**Q2. What is genuinely novel here? Every component already exists.**
That is exactly the point — and the honest framing. The novelty is *integrative and structural*, not
a new component in isolation. Specifically: (a) composing memory, reasoning, RAG, and multi-agent
collaboration into a single supervised architecture and making the *seams* explicit, because seams
are where integrated systems fail; (b) applying retrieval at the patient-timeline level rather than
only to generic guidelines; and (c) treating trustworthy AI — verification, auditability, HITL — as
a first-class structural layer rather than an add-on.

## On safety and correctness

**Q3. How does the framework address the severe risk of LLM hallucination in a safety-critical setting?**
Structurally, through three layers. First, retrieval anchors reasoning to the patient's actual EHR
history and to external literature, so decisions rest on inspectable evidence. Second, a dedicated
verification agent acts as a gatekeeper, checking outputs against clinical guidelines before they
surface. Third, human-in-the-loop validation ensures a clinician reviews the surfaced evidence before
any action is authorized. No single layer is sufficient alone; the defense is in depth.

**Q4. How do you prevent errors propagating between agents?**
I treat the inter-agent interfaces as the primary risk surface. Mitigations: the verification agent
between reasoning and action, mandatory human review at the output boundary, and tamper-evident audit
logging of every hand-off — which data was used, what was retrieved, and how agents interacted — so
an error can be traced to its origin rather than silently compounding.

**Q5. Are the explanations faithful? A fluent explanation can still misrepresent the real reasoning.**
Correct, and I don't claim guaranteed faithfulness — a plausible explanation can be unfaithful. That
is precisely why review is mandatory and why the system *surfaces the retrieved evidence itself*, not
only prose. The clinician checks the recommendation against the evidence, not against the narrative.
Measuring explanation faithfulness is named as a limitation and a target of the evaluation plan.

## On data and generalizability

**Q6. MIMIC-IV is retrospective and single-institution. How do you defend clinical generalizability?**
I don't — and I say so explicitly in the scope. MIMIC-IV reflects one institution's practice at one
time and cannot stand in for prospective, multi-site evidence. Its purpose is to supply the rich,
longitudinal EHR complexity needed to *design and validate the architecture and retrieval
mechanisms*. Establishing true clinical generalizability is the job of the prospective, multi-site
trials this design study lays the groundwork for.

**Q7. Why MIMIC-IV specifically rather than another dataset?**
It is publicly available under a credentialed data-use agreement, it is critical-care focused where
the data-overload problem is most acute, and it provides genuinely *longitudinal* records across
structured and unstructured modalities — demographics, admissions, labs, vitals, medications,
diagnoses, procedures, and notes — which is what a monitoring framework needs to reason over time.

## On feasibility and evaluation

**Q8. What about latency and cost in real-time monitoring with multiple agents and retrieval?**
A recognized limitation, characterized in the thesis rather than hidden. A multi-agent, retrieval-
heavy pipeline has real latency and compute cost. Mitigation directions — smaller specialist models,
caching, and selective retrieval — are named as future optimization work; the current deliverable is
a bounded prototype and evaluation plan, not a latency-optimized production system.

**Q9. How exactly will the bounded prototype be evaluated?**
Against baselines and ablations, with metrics spanning recommendation accuracy, retrieval quality,
explanation faithfulness, and latency. The experimental design is detailed in Chapter 4; the intent
is that ablations isolate the contribution of each layer (e.g., with vs. without patient-timeline
retrieval, with vs. without the verification agent).

**Q10. This is a lot for a Master's thesis — is the scope achievable?**
Yes, because the scope is deliberately bounded. The deliverable is a conceptual framework, a *bounded*
prototype, and an evaluation plan — not production software, live EHR integration, or a clinical
trial. Naming those exclusions up front is what keeps the work achievable within the timeframe while
still making a defensible research contribution.

## On positioning

**Q11. How is this different from MedAgents, MedRAG, Agent Hospital, or Clinical Camel?**
Each advances one capability well and stops there: MedAgents stages role-played specialist
consultation; MedRAG couples retrieval with structured knowledge for specificity; Agent Hospital
simulates a care setting; Clinical Camel adapts an open model for dialogue. None assembles reasoning,
persistent patient memory, evidence retrieval, multi-agent collaboration, *and* physician oversight
into a single architecture aimed at *longitudinal monitoring*. That omission is the space this thesis
occupies.

**Q12. Isn't "human-in-the-loop" just a disclaimer to avoid liability?**
No — it is a design commitment, and the architecture is arranged so the authority is real rather than
nominal. The clinician is given the surfaced evidence and the reasoning path, an explicit
approve/modify/reject decision, and an audit trail. The framework is deliberately modest about
autonomy and firm about accountability: it generates explainable recommendations, but a clinician
authorizes every one.
