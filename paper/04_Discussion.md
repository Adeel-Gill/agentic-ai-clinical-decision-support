# 4. Discussion

## 4.1 What the Framework Claims and What It Does Not

The framework's novelty is deliberately narrow. Tool-using medical agents exist
[gao2025txagent; liu2025riskagent; fallahpour2025medrax]; multi-agent coordination exists
[wu2024autogen; tran2025collaboration]; clinical RAG exists and works within its grounding
assumptions [zhao2025medrag; ke2025ragfitness]. We do not claim these components. We claim the
three things the 2025–2026 literature documents as absent: retrieval grounded in the patient's
own timeline, evaluation that scores longitudinal tracking on real ICU records, and a
verification gate whose audit trail is itself measured. If the ablations show these components
do not improve grounded decision quality, the framework's thesis fails honestly — the
components are separable and testable by design.

## 4.2 Relation to Contemporary Evaluation Practice

MedAgentBench and HealthBench moved evaluation toward realism — synthetic FHIR records and
physician rubrics respectively [jiang2025medagentbench; arora2025healthbench] — and the best
agents complete only about seventy percent of virtual-EHR tasks, which counsels humility about
bedside readiness. Our evaluation design borrows their instruments (task framing, rubric
grading) but changes the substrate to real, longitudinal MIMIC-IV admissions
[johnson2023mimic; lovon2025mimic]. The trade-off is acknowledged: MIMIC-IV is retrospective
and single-region, and retrospective evaluation cannot establish the prospective safety that
COMPOSER-LLM's deployment begins to demonstrate for one task [shashikumar2025sepsis].
Retrospective longitudinal evaluation on real records is nonetheless the missing rung between
exam benchmarks and prospective trials, and it is the rung this work supplies.

## 4.3 Safety, Oversight, and Regulation

The safety design responds to documented failure modes rather than hypothetical ones: medical
hallucinations reach practice [kim2025hallucinations]; uncommunicated uncertainty erodes
appropriate reliance [atf2025uncertainty]; multi-agent topologies can amplify a single
compromised agent [chen2025medsentry]; and unconstrained LLM output already meets medical-device
criteria [weissman2025unregulated]. Structured human oversight is a load-bearing component, not
a disclaimer — the meta-analytic evidence shows collaboration gains are fragile when oversight
is unstructured [wang2026collaboration]. Mapping the framework's guardrails onto proposed UNDCS
requirements [tan2026undcs] is an early attempt to make a research prototype legible to the
regulatory conversation; we expect the mapping, not the architecture, to need revision as rules
mature.

## 4.4 Limitations

Four limitations bound the claims. First, empirical evidence so far is a pilot on the
100-patient MIMIC-IV demo without the LLM loop (Section 5); the full retrospective evaluation
is designed but not executed, and no claim of prospective clinical benefit is made. Second,
MIMIC-IV's critical-care population limits generalization to other care settings
[johnson2023mimic]. Third, verification quality is
bounded by the entailment methods used to measure it [es2024ragas]; a verification gate can
only be as trustworthy as its own evaluation, which is why trail faithfulness is spot-audited
by humans as well. Fourth, LLM API costs and latency constrain the monitoring cadence the
prototype can sustain, a practical ceiling the agent-evaluation literature identifies as
generally under-reported [yehudai2025evaluation].

## 4.5 Future Work

Beyond executing the Chapter 4 evaluation, three directions follow. Prospective shadow-mode
deployment in the style of COMPOSER-LLM is the natural next evidence level
[shashikumar2025sepsis]. Federated or on-premises open models [toma2023clinicalcamel] would
address the privacy constraints that cloud LLMs impose on real EHR timelines. And the
verification gate invites formalization: moving from entailment heuristics toward auditable,
possibly symbolic, checking of clinical claims against structured evidence — the direction the
trustworthy-agent literature identifies as open [yu2025trustagent; tan2026undcs].
