# Research Gap

Clinical LLM agents have advanced quickly, but the way they are built and, more importantly, the
way they are evaluated leaves three specific gaps that this thesis targets. The point is not that
no one has combined memory, reasoning, and multi-agent collaboration before — several systems
have. The point is that the capabilities that would make such a system trustworthy on a real
patient are precisely the ones the field has left under-specified and under-evaluated.

The first gap concerns evaluation data. The strongest medical agent systems are measured almost
entirely on static examination question answering. MedAgents assembles a multi-disciplinary panel
of expert agents and reports gains on MedQA, MedMCQA, PubMedQA, and MMLU subtasks
[tang2024medagents]. Agent Hospital lets doctor agents evolve by treating simulated patients and
then benchmarks the learned expertise, again, on MedQA (USMLE) [li2024agenthospital]. AgentClinic
takes a step toward interaction by embedding agents in a simulated clinical dialogue, but the
patients and their trajectories are themselves generated rather than drawn from real records
[schmidgall2024agentclinic]. Exam questions are curated, self-contained, and answerable from a
paragraph of context; a real ICU stay is noisy, longitudinal, incompletely documented, and
internally contradictory. High USMLE accuracy tells us little about whether an agent can track a
deteriorating patient across days of MIMIC-IV observations, where labs, vitals, medications, and
notes accumulate and revise each other [johnson2023mimic]. The gap is not that these systems are
weak, but that their reported strength is measured on a task that does not resemble the deployment
setting.

The second gap concerns what retrieval is grounded in. Retrieval-augmented generation is the
standard answer to hallucination, but in the medical setting it is usually grounded in guidelines,
textbooks, or literature rather than in the specific patient in front of the clinician. MedRAG, one
of the more sophisticated medical RAG systems, couples retrieval with a diagnostic knowledge graph
and proactive questioning, yet its orientation is toward snapshot differential diagnosis and it is
evaluated on DDXPlus and a chronic-pain dataset rather than a longitudinal ICU record
[zhao2025medrag]. Med-PaLM and its successors encode impressive clinical knowledge parametrically
but do not retrieve from a patient's own timeline at all [singhal2023clinical]. EHRAgent is the
notable move in the right direction — it grounds an agent in structured EHR data through code
execution — but it frames the task as answering discrete questions over tabular records rather than
maintaining a running, evidence-linked model of a patient over an admission [shi2024ehragent]. What
is missing is retrieval anchored to the patient timeline: the ability to pull the relevant prior
labs, prior admissions, and trend of a given vital as first-class evidence for a recommendation.

The third gap concerns verification and auditability as first-class, evaluated components. Most
systems treat trustworthiness as a property they hope emerges from better prompting or from expert
role-play consensus [tang2024medagents], or they add a safeguard that checks code rather than
clinical claims. Rarely is there a dedicated verification step that checks a generated
recommendation against the retrieved patient evidence, and even more rarely is the faithfulness of
the resulting audit trail itself measured. In a domain where a wrong recommendation can harm a
patient, "the panel of agents agreed" is not the same as "this recommendation is entailed by the
retrieved evidence, and here is the trace." The absence of an evaluated verification gate and a
faithful audit trail is the difference between a system that sounds safe and one whose safety can
be inspected.

These three gaps yield three concrete questions this thesis answers:

1. Does an agentic framework with patient-timeline RAG and longitudinal memory produce measurably
   better and better-grounded clinical decisions on real ICU data (MIMIC-IV) than the exam-tuned
   and guideline-grounded baselines represented by MedAgents, Agent Hospital, and MedRAG
   [tang2024medagents; li2024agenthospital; zhao2025medrag; johnson2023mimic]?

2. Does grounding retrieval in a patient's own EHR timeline, rather than in guideline or literature
   corpora, reduce unsupported recommendations relative to guideline-only RAG and parametric-only
   models such as Med-PaLM [zhao2025medrag; singhal2023clinical; shi2024ehragent]?

3. Can a dedicated verification gate plus a faithful audit trail catch and flag ungrounded
   recommendations at a rate that materially improves safety, and can that faithfulness be
   measured rather than merely asserted [schmidgall2024agentclinic]?

Answering these questions is the contribution. It requires building the framework, but the novelty
lies in closing the specific evaluation and grounding gaps above, not in the act of integration.
