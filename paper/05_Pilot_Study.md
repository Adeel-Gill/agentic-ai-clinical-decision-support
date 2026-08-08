# 5. Pilot Feasibility Study

## 5.1 Rationale and Scope

The full evaluation of Section 3.6 requires credentialed MIMIC-IV access and an LLM agent
loop; both are in progress. To establish that the framework's distinguishing components are
implementable and behave as designed on de-identified real-world ICU data, we conducted a bounded pilot on the
openly licensed MIMIC-IV Clinical Database Demo (v2.2; 100 patients, 275 admissions, 140 ICU
stays) [johnson2023mimic]. The pilot exercises the non-LLM slice of the architecture
(timeline construction, timestamp-aware retrieval, an alert-generating classical baseline, and
the verification gate with its audit trail) and is reported as feasibility evidence. With
twenty deaths in the cohort, no performance claim survives this sample size, and we make none.

## 5.2 Setup

For each ICU stay, the memory layer assembled a chronological timeline from vitals, laboratory
results, medication starts, and strictly prior admissions, each event carrying a provenance
reference to its source table and row. Retrieval at a decision point (24 h after ICU
admission) scored events by recency, type, and deterioration relevance, and never returned an
event recorded after the query time. A standardized logistic regression over first-24 h
features (5-fold stratified cross-validation) produced an in-hospital mortality risk score,
and the top quintile generated 28 alerts. We define a *true alert* as an alert raised for a
stay whose hospital admission ended in in-hospital death (7 alerts) and a *false alert* as
one raised for a patient discharged alive (21 alerts). In-hospital mortality is a proxy
endpoint chosen because it is unambiguous in the demo tables, not a claim that every
deteriorating patient dies; much of monitoring's clinical value lies in non-fatal events
such as escalation of care, fluid management, or antibiotic titration, which a mortality
proxy cannot see. The planned full evaluation therefore replaces this proxy with Sepsis-3
onset and intervention-concordance labels (Section 3.6). Leakage was controlled at three points: features were computed
only from events time-stamped within the first 24 h of the ICU stay, while the mortality
label derives from the discharge disposition recorded at the end of the admission; prior
admissions entered the timeline only if discharged strictly before the current admission;
and imputation and standardization were fit inside each cross-validation training fold via a
pipeline, never on the full cohort. The verification gate passed an alert only when the patient's retrieved timeline
contained at least *m* distinct deterioration-relevant signals (tachycardia, hypotension,
tachypnea, hypoxemia, temperature derangement, elevated lactate, leukocytosis or leukopenia,
rising creatinine or bilirubin, thrombocytopenia) within the six hours preceding the decision.
Every gate decision logged its evidence references, and trail faithfulness was measured by
re-resolving each logged reference against the raw tables.

## 5.3 Results

Timeline construction processed all 140 stays in 2.9 s (median 438 events per stay,
IQR 236–798); 43% of stays carried at least one prior admission, confirming that longitudinal
context exists to retrieve even in a small cohort. Retrieval answered queries in 11.7 ms
median (17.9 ms p95) with full top-k coverage and returned no future information by
construction. This figure measures the retrieval substrate alone: in the full system, each
recommendation will additionally incur multiple LLM inference calls, so total response time
will be dominated by agentic reasoning, not retrieval, and will be measured separately in
the planned evaluation. The baseline reached a cross-validated AUROC of 0.641 (95% bootstrap CI
0.478–0.792). Because the interval crosses 0.5, the baseline demonstrates no statistically
significant discrimination at this sample size, and we draw no decision-support performance
conclusion from it whatsoever. Its only function in the pilot is to generate a realistic,
imperfect alert stream against which the gate's behavior can be observed.

The gate produced the pilot's most instructive result, with an essential scoping caveat:
everything the gate demonstrates here is demonstrated on a stream of alerts, not on a stream
of validated predictions, since the baseline generating those alerts has no established
predictive validity. As the required number of distinct
recent signals rises from 1 to 6, the pass rate for false alerts falls from 0.90 to 0.05
while the pass rate for true alerts falls more slowly (0.57 to 0.14); at m = 4 the gate
blocks 86% of false alerts while retaining 43% of true ones. Evidence-gating therefore
preferentially suppresses unsupported alerts within this stream, which is the mechanism the
framework relies on.
The same experiment exposes the mechanism's cost: three of the seven true alerts had no
abnormal signal in the six-hour window at all, so the gate imposes a sensitivity floor
governed by the evidence window, a safety parameter to be tuned, and an effect invisible in
exam-style evaluation. All 183 logged evidence references re-resolved exactly against the raw
tables (trail resolvability 1.00). In this deterministic pilot the perfect score is expected
and carries no reliability claim: what the exercise benchmarks is the metric and its
measurement machinery, not the system, and the metric earns its place because it becomes
non-trivial once a non-deterministic LLM writes the trail.

## 5.4 What the Pilot Does and Does Not Show

The pilot shows that the framework's memory, retrieval, and verification mechanisms are
implementable on de-identified real-world ICU records at interactive latency, that evidence-gating discriminates
in the intended direction, and that audit-trail faithfulness is a measurable quantity. It
does not show clinical utility, generalization beyond a 100-patient demo cohort, or anything
about the LLM agent loop, which the full MIMIC-IV evaluation of Section 3.6 will test. The
demo lacks the clinical notes module, so retrieval here is structured-data only.

The relation between the pilot gate and the framework's verification agent deserves explicit
statement. The pilot gate is a deliberately simple heuristic instantiation of the
verification interface: it consumes the same retrieved-evidence set, emits the same
pass-or-block decision, and logs the same evidence references that the LLM-based agent of
Section 3.4 will. What changes in the full system is the decision rule, from counting
distinct deterioration signals to claim-level entailment against the retrieved evidence.
Whether the preferential suppression of false alerts observed here transfers to the
entailment-based form is therefore an explicit hypothesis for the full evaluation, not an
assumption this pilot licenses.
