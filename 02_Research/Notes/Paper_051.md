# Paper 051

## Basic Information
- **Title:** SmartAlert — Implementing Machine Learning-Driven Clinical Decision Support for Inpatient Laboratory Utilization Reduction
- **Authors:** April S. Liang, Fatemeh Amrollahi, Yixing Jiang (co-first); Conor K. Corbin, Grace Y.E. Kim, et al.; Stephen P. Ma and Jonathan H. Chen (co-senior)
- **Year:** 2026
- **Venue:** NEJM AI 3(7), AIcs2501086 (case study); preprint arXiv:2512.04354 (Dec 2025)
- **DOI:** 10.1056/AIcs2501086
- **Link:** https://ai.nejm.org/doi/full/10.1056/AIcs2501086
- **PDF:** `02_Research/Papers/Clinical_Decision_Support/P051_SmartAlert_ML_CDS_Inpatient_Lab_Utilization.pdf`
- **Verified:** 2026-08-13 against PubMed 42453199 and the NEJM AI record; full text read from the arXiv PDF.
- **Author-network note:** co-first author Yixing Jiang is also first author of MedAgentBench (P022, `jiang2025medagentbench`) and of the underlying prediction-model paper (the study's ref 17); Stanford ecosystem shared with P039/P049 (Shah) — weigh evidence independence accordingly.

## Abstract Summary (200–300 words)
SmartAlert is an ML-driven clinical decision support system embedded in a production EHR that predicts whether a patient's next complete blood count (CBC) will be "clinically stable," and interrupts clinicians who order repetitive CBCs for such patients with options to cancel, reduce frequency (e.g., every other day), or continue. The architecture follows the DEPLOYR framework: 6-hourly batched FHIR data retrieval (demographics, labs, vitals, medications, diagnoses) feeds a probabilistic regression model on an Azure serverless function; predictions are written to EHR flowsheets; an Epic OurPracticeAdvisory alert fires at order entry, displayed only 07:00–18:00. The model was tuned to 90% precision (clinician-identified as the meaningful threshold), yielding retrospective recall of 29.3% (WBC), 59.5% (hemoglobin), and 100% (platelets). Governance proceeded through a CDS committee concept approval, clinician co-design interviews (n=18) that redefined the prediction target from "normal result" to clinician-defined "clinical stability," a one-week silent prospective validation (PPV 88.1–95.4%), a randomized pilot, a 90-day review, and a formal FURM (Fair, Useful, Reliable AI Models) assessment. In the 7-month randomized controlled pilot (Aug 2024–Mar 2025; 9,270 admissions in eight acute-care units across two hospitals; encounter-level randomization; 486 alerts displayed vs 460 silently triggered), the treatment arm showed 1.54 vs 1.82 CBC results within 52 h of an alert (Poisson, p<0.01; ~15% relative reduction), with no statistically significant differences in ICU transfer, length of stay, readmission, or mortality. Alert criteria were adjusted mid-pilot (excluding recent procedure/transfusion/heparin patients) after user interviews.

## Research Problem
- 20–50% of inpatient laboratory tests are medically unnecessary; repetitive CBCs are a named "Choosing Wisely" wasteful practice.
- Education, audit-and-feedback, and blanket ordering restrictions are imprecise: the institution's 72-hour standing-order limit (a 2021 blood-tube-shortage response) blocked repeat testing even for dynamically changing patients.

## Proposed Solution
- Patient-specific, precision-first ML prediction of lab stability delivered as an interruptive but overridable CDS alert with a reduce-frequency alternative — targeted suppression instead of blanket restriction.

## Core Analysis (capability dimensions)
- **Memory:** none — features from the current record at inference time; no persistent longitudinal patient model.
- **Planning:** none.
- **Reasoning:** none — a probabilistic regression classifier; no LLM anywhere in the system.
- **Tool use:** n/a (the system *is* the tool; FHIR APIs for retrieval).
- **Multi-agent:** no.
- **RAG:** no.
- **Healthcare:** yes — production deployment in two hospitals.
- **Trustworthy AI:** yes, procedurally — clinician-defined acceptable behavior, silent prospective validation, PPV disclosure in the UI, FURM assessment, human override always available. But no per-prediction explanation beyond probability + recent values, and no audit-trail artifact.

## Evaluation
- Randomized controlled pilot (encounter-level randomization via Epic SmartDataElement), 4,592 treatment / 4,678 control encounters; primary outcome CBC count within 52 h of alert; Poisson regression; secondary safety outcomes (ICU transfer, LOS, readmission, mortality) non-significant.
- Institutional extrapolation: >700,000 CBCs/year, >30% repetitive; 15% relative reduction ≈ 31,500 tests ≈ $4.1–13.3M charges.

## Strengths
- One of very few *randomized, prospective, production-EHR* deployments of custom ML-CDS — RCT-grade deployment evidence.
- The governance ladder (concept approval → co-design → silent prospective validation → randomized pilot → 90-day review → FURM) is documented end-to-end and replicable.
- Co-design materially changed the model target ("normal" → clinician-defined "stability"); PPV identified as the trust metric clinicians want.
- Real engineering lesson: FHIR retrieval took minutes per patient → batched 6-hourly precomputation (directly relevant to latency budgeting).

## Limitations (from the paper and from critical reading)
- Encounter-level randomization with shared clinicians → spillover/contamination bias toward the null, undiscussed.
- Headline effect applies to the alerted subset (~10% of treatment encounters), not house-wide; savings extrapolations assume scaling that the low recall (WBC 29.3% at 90% PPV) undercuts.
- Safety outcomes underpowered for rare harms (486 alerts); LOS directionally higher in treatment (118.7 vs 112.7 h, n.s.), unremarked.
- Intervention criteria changed mid-trial; pooled analysis, no ITT discussion.
- Single health system; general med/surg units only; single test type.
- Internal inconsistency: text says 4,590 treatment encounters, Table 1 says 4,592.

## Research Gap (what it does NOT do for longitudinal patient monitoring)
- Single-test, single-decision alert: no longitudinal model of the patient, no reasoning over the trajectory, no retrieval of evidence, no per-recommendation verification, no measured audit trail. It suppresses one order type; it does not monitor, diagnose, recommend, or explain.

## How This Supports My Thesis
- **Adopt:** the governance ladder (esp. silent prospective validation before display) as a template for the Chapter 4 evaluation narrative and the HITL protocol; precision-first thresholds defined by clinician stakeholders (mirrors the verification gate's m-threshold tuning); PPV-forward trust communication.
- **Contrast:** SmartAlert is the deployment-proven *conventional* pole — one model, one test, one decision. The thesis extends the same safety philosophy (precision suppression of low-value/unsupported actions, human override) to evidence-verified recommendations over a longitudinal patient timeline with a measured audit trail.
- **Cite at:** §2.11.5 (deployment evidence ladder, beside COMPOSER-LLM), Chapter 3 HITL/verification design rationale, Chapter 4 evaluation-protocol design (silent phase), Technical_Feasibility latency discussion (batched precomputation precedent).

## Relevance Score
**9/10** — the strongest RCT-grade deployment evidence in the corpus for the safety of ML-driven suppression of low-value clinical actions; methodologically the closest published precedent for how the proposed framework's verification gate should be piloted and governed, while sharing none of the framework's longitudinal, reasoning, or auditability ambitions.
