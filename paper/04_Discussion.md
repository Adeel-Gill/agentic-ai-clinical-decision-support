# 4. Discussion

## 4.1 What the Framework Claims and What It Does Not

The framework's novelty is deliberately narrow. Tool-using medical agents exist
[gao2025txagent; liu2025riskagent; fallahpour2025medrax]; multi-agent coordination exists
[wu2024autogen; tran2025collaboration]; clinical RAG exists and works within its grounding
assumptions [zhao2025medrag; ke2025ragfitness]; and longitudinal grounding itself is
emerging in trajectory and guideline-alignment systems
[li2026clicare; zeng2025trajcoa; cui2025timer]. We do not claim any of these components.
What we claim is their integration, and the instrumentation of that integration:
timestamp-aware retrieval from the patient's own timeline coupled to recommendation-level
verification, an audit trail whose faithfulness is measured rather than assumed, and
evaluation that scores longitudinal tracking on de-identified real-world ICU records. Within
the literature reviewed for this study, no system combines these, and none measures them
together. If the ablations show these components do not improve grounded decision quality,
the framework's thesis fails honestly; the components are separable and testable by design.

## 4.2 Relation to Contemporary Evaluation Practice

Contemporary benchmarks report two findings we take as fixed points: agents placed in a
virtual EHR with physician-authored tasks succeed on only about seventy percent of them
[jiang2025medagentbench], and rubric-based grading of open-ended health conversations exposes
quality variation that multiple-choice scoring conceals [arora2025healthbench]. Our reading
of those results, which the benchmark authors do not themselves draw, is that the remaining
distance to bedside readiness is a substrate problem as much as a capability problem:
synthetic records and scripted tasks cannot exhibit the revision, contradiction, and
accumulation that make real admissions hard. Our evaluation design therefore keeps their
instruments, task framing and rubric grading, while changing the substrate to real
longitudinal MIMIC-IV admissions [johnson2023mimic; lovon2025mimic]. The trade-off runs the
other way too. MIMIC-IV is retrospective and single-region, and no retrospective design can
establish the prospective safety that has so far been demonstrated for exactly one narrow
task [shashikumar2025sepsis]. We position retrospective longitudinal evaluation on real
records as the missing rung between exam benchmarks and prospective trials, not as a
substitute for the trials themselves.

## 4.3 Safety, Oversight, and Regulation

Each safety mechanism in the framework answers a failure mode the literature has documented
rather than one we hypothesize. Clinician-annotated evidence that hallucinated medical
content reaches practice [kim2025hallucinations] is why the gate screens recommendations
before delivery; the argument that clinical systems owe users calibrated uncertainty, not
bare answers [atf2025uncertainty], is why every recommendation carries a calibrated
confidence estimate;
adversarial findings that open shared communication channels are the most vulnerable
multi-agent design [chen2025medsentry] are why the framework eliminates side channels and
routes every message through one auditable point; and the
demonstration that unconstrained model output already meets medical-device criteria
[weissman2025unregulated] is why we treat regulatory alignment as a design input. We read
the meta-analytic evidence on clinician–LLM teaming [wang2026collaboration] as supporting a
stronger conclusion than its authors state: oversight only earns its safety role when it is
structured, which is why review in this framework is a protocol with mandatory reasons
rather than an optional glance. Mapping the guardrails onto proposed UNDCS requirements
[tan2026undcs] is our attempt to make a research prototype legible to that regulatory
conversation; we expect the mapping, not the architecture, to need revision as the rules
mature.

## 4.4 Limitations

Five limitations bound the claims. First, empirical evidence so far is a pilot on the
100-patient MIMIC-IV demo without the LLM loop (Section 5); the full retrospective evaluation
is designed but not executed, and no claim of prospective clinical benefit is made. Second,
the gate's sensitivity floor is a patient-safety concern in its own right: at its strictest
informative threshold the pilot gate blocked three of seven true alerts, and a deployed
system that suppressed half of the alerts preceding death would be clinically unacceptable.
We treat the evidence window and signal threshold as safety parameters that clinical
governance, not engineering, must set, and the full evaluation will report gate operating
points with sensitivity alongside false-alert suppression so that this trade-off is chosen
deliberately rather than inherited. Third, MIMIC-IV's critical-care population limits
generalization to other care settings [johnson2023mimic]. Fourth, verification quality is
bounded by the entailment methods used to measure it [es2024ragas]; a verification gate can
only be as trustworthy as its own evaluation, which is why trail faithfulness is spot-audited
by humans as well. Fifth, LLM API costs and latency constrain the monitoring cadence the
prototype can sustain, a practical ceiling the agent-evaluation literature identifies as
generally under-reported [yehudai2025evaluation].

## 4.5 Future Work

Beyond executing the evaluation of Section 3.6, three directions follow. Prospective
shadow-mode deployment in the style of the deployed sepsis system is the natural next
evidence level [shashikumar2025sepsis]. On-premises open models [toma2023clinicalcamel]
would address the privacy constraints that hosted LLMs impose on real EHR timelines. And the
verification gate invites formalization: moving from entailment heuristics toward auditable,
possibly symbolic, checking of clinical claims against structured evidence, a direction the
trustworthy-agent literature identifies as open [yu2025trustagent; tan2026undcs].
