# 2. Related Work

We organize prior work around four questions that any clinical decision-support agent must
answer: how agents are built, what medical agents actually do, what their retrieval is
grounded in, and how anyone would know whether to trust them. Reading the literature through
these questions, rather than system by system, makes the unoccupied territory visible.

## 2.1 How Agents Are Built

The technical substrate of agentic systems accumulated in three recognizable waves. The first
gave single agents their core competencies: interleaving reasoning with action
[yao2023react], acquiring tool use without hand-labeled supervision [schick2023toolformer],
and, as surveys of the period document, coupling these with memory, planning, and
self-reflection into a general architecture [wang2024survey; shinn2023reflexion]. A second
wave asked how several such agents should work together, and its answers differ mainly in
where coordination logic lives: in conversation itself [wu2024autogen], in assigned social
roles [li2023camel], or in codified standard operating procedures [hong2024metagpt]. The
third wave is consolidation. Collaboration patterns now have a formal taxonomy
[tran2025collaboration], cognitive modules a brain-inspired reference blueprint
[liu2025foundationagents], memory a construction–management–retrieval decomposition
[wu2025memory], and inter-agent communication a set of emerging wire protocols
[ehtesham2025protocols]. The distinction between a tool-using agent and an orchestrated
agentic ecosystem has itself been formalized, with healthcare cited among the application
domains where the orchestrated form matters most [sapkota2025agents].

For present purposes the significance of this maturation is double-edged. It means a clinical
framework can be assembled from settled components, so integration alone earns no novelty.
It also means the open problems are no longer architectural: nothing in this infrastructure
literature says what a *clinical* agent should be grounded in, or how its outputs should be
verified before they reach a patient. Those questions belong to the application layer, and
the infrastructure work is silent on them by design.

## 2.2 What Medical Agents Do

Work applying language models to medicine splits into two generations distinguished by where
capability resides. In the first, capability is parametric: models encode clinical knowledge
[singhal2023clinical], answer examination questions at expert level [singhal2025medpalm2],
extend across modalities [tu2024generalist], and are reproduced in open weights
[toma2023clinicalcamel]. The second generation externalizes capability into structure around
the model, and the choice of structure is what differentiates otherwise similar systems.
Some externalize *deliberation*, convening role-played specialist panels or simulated
clinical environments in which diagnostic behavior can develop
[tang2024medagents; li2024agenthospital; schmidgall2024agentclinic]. Some externalize
*record access*, generating executable queries over structured EHR tables [shi2024ehragent].
Some externalize *computation*, delegating therapeutic reasoning, risk scoring, or image
analysis to hundreds of validated tools rather than trusting generation
[gao2025txagent; liu2025riskagent; fallahpour2025medrax]. Others externalize the
*interaction policy* itself, learning when to ask rather than answer [feng2025doctoragent],
or extend dialogue systems toward multi-visit management and multimodal evidence gathering
[palepu2025disease; saab2025multimodal].

Viewed together, these design choices share an assumption that none of the papers states:
the patient exists only for the duration of a prompt. Whatever is externalized — deliberation,
queries, tools, or dialogue policy — patient state is reassembled from the scenario at each
step, and no system carries an evidence-linked model of one real patient forward through an
admission. The broadest survey of the area finds the research effort concentrated on clinical
decision-making while naming implementation barriers among the field's central open
challenges [wang2025baymax]. The gap this paper targets sits at the intersection of those
two observations.

## 2.3 What Retrieval Is Grounded In

Retrieval-augmented generation earned its place as the default hallucination mitigation
[lewis2020rag; gao2023rag], and its refinements track a single trajectory: giving the model
more control over its own evidence, first through self-critique of retrieved passages
[asai2024selfrag], then by folding planning, iteration, and reflection over retrieval into
the agent loop itself [singh2025agenticrag]. Medical instantiations follow the same
trajectory while narrowing the corpus to curated clinical knowledge, whether a diagnostic
knowledge graph [zhao2025medrag] or perioperative guidelines, where grounding measurably
outperformed clinicians in a bounded assessment task [ke2025ragfitness]. What has not varied
across any of this work is the direction of grounding: external knowledge is the corpus and
the patient is the query. A monitoring system needs the reverse as well, retrieval *from* the
patient's accumulated record: yesterday's lactate trend, the previous admission, the
medication that was stopped. Within the literature reviewed here, we find no system that
treats the patient timeline as a retrieval corpus in its own right, and that omission
defines the opening this work occupies.

## 2.4 How Trust Would Be Established

Whether these systems can be trusted is being addressed by three literatures that do not yet
meet. Evaluation research is moving benchmarks toward realism, placing agents inside a
FHIR-compliant virtual EHR with physician-authored tasks [jiang2025medagentbench], grading
open-ended conversations against physician-written rubrics [arora2025healthbench], and
cataloguing which agent capabilities current benchmarks measure — with safety flagged as the
persistent omission [yehudai2025evaluation]. On de-identified real-world records, the evidence is thinner and
more sobering: revisited MIMIC-IV baselines find fine-tuned language models merely
competitive with tabular classifiers on one-shot prediction, with zero-shot models trailing
both [lovon2025mimic], and the single prospective deployment, an LLM adjudicating
high-uncertainty sepsis alerts in silent mode, earns that role by augmenting a conventional
predictor rather than replacing it [shashikumar2025sepsis].

Safety research, meanwhile, characterizes the failure modes that evaluation should be
catching: taxonomies of medical hallucination grounded in clinician annotation
[kim2025hallucinations], the case that clinical systems must communicate calibrated
uncertainty rather than bare answers [atf2025uncertainty], threat models spanning an agent's
reasoning, memory, and tools [yu2025trustagent], and adversarial evidence that multi-agent
topology determines how far a compromised agent's influence spreads [chen2025medsentry].
Regulatory analysis converges from a third direction: general-purpose models already emit
output meeting medical-device criteria [weissman2025unregulated], prompting proposed
governance for unconfined non-deterministic clinical software built on guardrails,
moderation, and inspectability [tan2026undcs]. Even the human backstop is less settled than
assumed; the sole meta-analysis of clinician–LLM collaboration reports gains that are
statistically fragile alongside non-trivial error rates in collaborative outputs
[wang2026collaboration].

Each literature names a requirement: grounded recommendations, calibrated confidence,
inspectable trails, structured oversight. To the best of our knowledge, none reports a
system in which those requirements are implemented together and *measured* end-to-end on
de-identified real-world patient records. That
measurement, rather than any single component, is what the framework presented next is
designed to make possible.
