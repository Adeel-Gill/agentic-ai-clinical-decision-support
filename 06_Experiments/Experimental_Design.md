# Experimental Design (Condensed Protocol)

Companion to Chapter 4 (`07_Thesis/Chapter_4/Chapter_4.md`). **Planned, not run.** These tables pin the confirmatory design so results cannot be reverse-engineered after the fact.

## Cohort at a glance

| Item | Value |
|---|---|
| Source | MIMIC-IV [johnson2023mimic] via PhysioNet [goldberger2000physiobank] |
| Cohort size | ~100–500 adult ICU stays (bounded prototype) |
| Sampling | Stratified on outcome + coarse acuity; patient-level splits |
| Rationale | Clinician-scored metrics are expensive per case; per-case LLM cost scales linearly; stratification guarantees positive-class coverage for rare outcomes |

## Tasks

| ID | Task | Type | Reference standard |
|---|---|---|---|
| T1 | In-hospital mortality | Binary classification | Recorded outcome |
| T2 | ICU transfer / escalation | Binary classification | Recorded outcome |
| T3 | Sepsis onset | Binary classification | Sepsis-3-style operational definition [singer2016sepsis3] |
| T4 | 30-day readmission | Binary classification | Recorded outcome |
| T5 | Diagnosis support | Ranked differential | Recorded discharge diagnoses (imperfect) |
| T6 | Treatment recommendation | Open-ended actions | Guideline concordance + safety rubric + clinician review |
| C1 | MedQA (accuracy control) | Multiple choice | Answer key [jin2021medqa] |

## Baseline ladder

Each rung adds exactly one capability over the rung below, so gaps isolate contributions.

| Config | Retrieval | Multi-agent | Verification | Memory | Coordinator | Isolates |
|---|---|---|---|---|---|---|
| B0 single LLM zero-shot | none | no | no | no | n/a | RQ1 floor |
| B1 LLM + guideline RAG | guidelines only | no | no | no | n/a | value of retrieval (RQ4) |
| B2 MedAgents-style [tang2024medagents] | guidelines | yes | **no** | no | flat | value of multi-agent reasoning (RQ2/RQ3) |
| B3 full framework | guidelines + patient timeline | yes | yes | yes | orchestrated | value of verification + remaining components |
| CLIN logistic regression | structured features | — | — | — | — | strong cheap risk baseline |
| CLIN-SOFA severity score | — | — | — | — | — | clinical risk comparator [vincent1996sofa] |

CLIN and CLIN-SOFA apply to risk tasks T1–T4 only.

## Ablations (all relative to B3, one component removed)

| Config | Change from B3 | Question |
|---|---|---|
| A1 −Verification | Verification agent off | Does the safety layer reduce unsafe recommendations? (RQ3) |
| A2 −patient-timeline RAG | guideline-only retrieval | Does patient-specific grounding change outputs? (RQ4) |
| A3 −Memory | persistent memory off | Does long-term context help longitudinal tasks? (RQ2) |
| A4 flat Coordinator | fixed sequence, no delegation | Does orchestration earn its overhead? (RQ2) |

Every baseline and ablation is run across all applicable tasks; component value is reported per task, never averaged into one figure.

## Metric grid

| Dimension | Metric | Tasks | RQ |
|---|---|---|---|
| Task accuracy | Top-k accuracy, MRR; MedQA accuracy | T5; C1 | RQ1, RQ2 |
| Factual grounding | Faithfulness (RAGAS-style) [es2024ragas] | T5, T6, C1 | RQ4 |
| Risk prediction | AUROC, AUPRC | T1–T4 | RQ5 |
| Safety | Unsafe-recommendation rate, pre/post verification | T6 | RQ3 |
| Explainability | Clinician Likert (faithfulness, usefulness), n=3–5 | T5, T6 | RQ3 |
| Trustworthiness | ECE [guo2017calibration]; audit-log completeness | T1–T4; all | RQ3, RQ4 |
| Runtime | End-to-end latency; cost per case | all | RQ2, RQ5 |

## Pre-registered hypotheses

Confirmatory hypotheses are corrected together under a Benjamini-Hochberg FDR procedure [benjamini1995controlling]. Each has a directional prediction and a null that a negative result would confirm.

| ID | Hypothesis | Comparison | RQ | Primary metric |
|---|---|---|---|---|
| H1 | Guideline retrieval improves grounding over zero-shot | B1 > B0 | RQ4 | Faithfulness |
| H2 | Multi-agent reasoning improves task accuracy over single-LLM retrieval | B2 > B1 | RQ2 | Top-k accuracy / MRR (T5) |
| H3 | Verification reduces unsafe recommendations | B3 < B2 | RQ3 | Unsafe-recommendation rate (T6) |
| H4 | The full framework improves grounding over unverified multi-agent | B3 > B2 | RQ4 | Faithfulness |
| H5 | The framework matches or beats logistic regression on risk discrimination | B3 ≥ CLIN | RQ5 | AUROC/AUPRC (T1–T4) |
| H6 | The Verification agent, ablated, raises unsafe-recommendation rate | A1 > B3 | RQ3 | Unsafe-recommendation rate (T6) |
| H7 | Patient-timeline retrieval changes/improves outputs vs. guideline-only | B3 vs. A2 | RQ4 | Faithfulness, task accuracy |
| H8 | Persistent memory improves longitudinal task performance | B3 > A3 | RQ2 | AUROC/AUPRC (T4 readmission) |
| H9 | Orchestration improves outcomes over flat coordination (may be null) | B3 vs. A4 | RQ2 | Task accuracy, latency |
| H10 | The framework produces more complete/better-calibrated trust signals | B3 vs. B0–B2 | RQ3 | ECE, audit-log completeness |

Exploratory analyses (e.g., per-subgroup risk performance) are reported separately and carry no confirmatory weight.

## Statistical plan

- 95% bootstrap CIs, resampled over patients, on every headline metric.
- Paired tests on the shared cohort: DeLong for AUROC [delong1988comparing]; McNemar / bootstrap paired for classification and faithfulness [dietterich1998approximate].
- Multiple-comparison control via Benjamini-Hochberg FDR over the confirmatory set only [benjamini1995controlling].
- Underpowered comparisons are reported as "inconclusive at this cohort size."

## Related-benchmark scope

| System | Capability exercised | Covered here? |
|---|---|---|
| AgentClinic [schmidgall2024agentclinic] | Interactive diagnostic dialogue in simulation | No — static snapshots only |
| EHRAgent [shi2024ehragent] | Code-generating queries over structured EHR | Partially — structured-data reasoning |
| AMIE [tu2025amie] | Clinician-comparison diagnostic dialogue at scale | No — out of thesis scope/resourcing |
