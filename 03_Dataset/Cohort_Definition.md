# Cohort Definition

This document defines the patient cohort used to build and evaluate a bounded prototype of the
proposed framework. MIMIC-IV contains tens of thousands of ICU stays [johnson2023mimic], far
more than a thesis-scale prototype needs or can meaningfully process through LLM agents at
reasonable cost. The purpose of the cohort is therefore to carve out a small, well-characterized
slice of the database that exercises every part of the framework, monitoring, diagnosis, risk
prediction, treatment reasoning, and note-based retrieval, without incurring the compute and
storage burden of the full dataset. The design goal is representativeness within tractability,
not statistical power for a clinical trial.

## Design rationale

The cohort is deliberately anchored on ICU stays rather than hospital admissions, because the
monitoring substrate of the framework is built from high-frequency ICU chart data, and a
patient with no ICU stay would have no vital-sign stream to monitor. Restricting to a single
stay per patient, the first one, removes the ambiguity of which stay a longitudinal memory
should be keyed to and avoids leakage between what the framework treats as history and what it
treats as the current encounter. A minimum length-of-stay threshold guarantees that enough
signal has accumulated for windowed feature engineering to be meaningful; a stay of only a few
hours yields too few charted observations to resample into trends.

The requirement that a stay carry at least one clinical note is what distinguishes this cohort
from a purely structured-data study. Because the note module is separate and not universally
populated for every stay, this criterion also implicitly requires that MIMIC-IV-Note has been
downloaded and joined (see `README.md`). Stays lacking any usable note are excluded rather than
imputed, since the RAG patient index and the Diagnosis Agent's narrative reasoning cannot be
demonstrated on an empty document set.

A target of roughly 100 to 500 patients keeps the prototype affordable while retaining enough
positive cases for the rarer labels. Mortality and sepsis onset are minority outcomes, so the
lower end of that range risks having very few positives; the cohort is assembled toward the
upper end and then, if needed, mildly enriched for positive cases during sampling so that each
prediction task has a usable number of events. Any such enrichment is recorded so that reported
prevalences are not mistaken for population rates.

## Inclusion and exclusion criteria

| # | Criterion | Type | Rationale |
|---|---|---|---|
| 1 | Adult patient at ICU admission (age >= 18 at first ICU stay) | Inclusion | Pediatric physiology and reference ranges differ; the framework's reasoning targets adults |
| 2 | First ICU stay only (earliest `stay_id` per `subject_id`) | Inclusion | Removes intra-patient leakage and fixes the "current encounter" for memory keying |
| 3 | ICU length of stay >= 24 hours | Inclusion | Ensures enough charted vitals and labs for windowed feature engineering |
| 4 | Has laboratory results during the stay (>= 1 `labevents` row linked to the admission) | Inclusion | Required for lab-trend features and the Diagnosis and Risk agents |
| 5 | Has charted vital signs during the stay (>= 1 `chartevents` vital row) | Inclusion | Provides the monitoring substrate; a stay with no vitals cannot be monitored |
| 6 | Has at least one clinical note (>= 1 `discharge` or `radiology` document) | Inclusion | Enables the RAG patient index and narrative diagnosis reasoning; requires MIMIC-IV-Note |
| 7 | Non-adult, or age recorded as anonymized high-age placeholder inconsistent with adult care, is excluded | Exclusion | Guards against age-anonymization artifacts distorting features |
| 8 | ICU stay < 24 hours (including stays ending in early transfer or very early death) | Exclusion | Too little longitudinal signal for windowed features; noted as a known survivorship caveat |
| 9 | Stays with no labs, no vitals, or no notes | Exclusion | Cannot exercise the full framework pipeline |
| 10 | Duplicate or non-first ICU stays for a patient already included | Exclusion | Enforces the one-stay-per-patient design |

The ordering matters: the first-stay filter is applied before the length-of-stay and
data-availability filters so that a patient is not silently promoted to a later stay when the
first one fails a threshold. A patient whose first ICU stay is shorter than 24 hours is
excluded outright rather than represented by a later, longer stay, which keeps the cohort's
"first encounter" semantics clean at the cost of some sample loss.

## Target size

The prototype targets **approximately 100 to 500 patients** (one ICU stay each). This range is
a compromise between exercising the multi-agent pipeline on genuinely varied cases and keeping
LLM inference, embedding, and storage costs bounded for a single-researcher project. The exact
final count depends on how many first stays satisfy all criteria and on any positive-case
enrichment applied for the rarer labels; the realized count and per-label prevalence are to be
reported alongside results, not fixed in advance.

## Prediction labels

Four supervised targets are derived from the cohort. They are computed from the structured
tables at extraction time and attached to each patient's timeline; none is taken from an
external source. Where a label depends on a clinical definition, that definition is stated so
the derivation is reproducible.

**In-hospital mortality.** A binary label set from the admission disposition: whether the
patient died before hospital discharge for the admission containing the index ICU stay. This is
read from the `admissions` discharge/expiry information rather than inferred, and it is the
primary deterioration outcome for the Risk Prediction Agent.

**ICU readmission.** A binary label indicating whether the patient returned to the ICU within a
fixed window (commonly 30 days) after discharge from the index ICU stay. Although the cohort
uses only each patient's first stay for feature construction, later stays are still consulted
solely to determine whether a readmission occurred; they are used as label information, not as
input features, to avoid leakage.

**Sepsis onset (Sepsis-3).** A binary label following the Sepsis-3 clinical definition, an
acute increase of two or more points in the Sequential Organ Failure Assessment (SOFA) score in
the presence of suspected infection. Suspected infection is operationalized from the
combination of culture sampling in `microbiologyevents` and antibiotic administration in
`prescriptions` within a defined proximity window, and SOFA is computed from the relevant labs
and vitals over the stay. The onset time, not merely the presence of sepsis, is recorded so
that the Monitoring Agent can be evaluated on early detection. The precise SOFA component
mappings and the infection-window parameters follow the published Sepsis-3 operationalization
[singer2016sepsis3], using the SOFA score as originally defined [vincent1996sofa].

**Prolonged length of stay.** A binary label flagging ICU stays whose length exceeds a
threshold (for the prototype, greater than seven days). This is computed directly from the
`icustays` in and out timestamps and serves as a resource-utilization outcome that is more
prevalent than mortality or sepsis and therefore useful for sanity-checking the pipeline on a
less skewed target.

## Reproducibility and leakage control

Every criterion above is expressed against columns documented in `Data_Dictionary.md`, and the
cohort is materialized by a scripted, deterministic query so that the same patient set can be
regenerated from the credentialed database. Label derivations that look beyond the index stay,
readmission in particular, are strictly separated from feature construction, and the
train/validation/test split is performed at the patient level (see `Preprocessing_Pipeline.md`)
so that no patient contributes to more than one partition. As with all other artifacts, the
resolved cohort, the list of `subject_id` and `stay_id` values, is data and is never committed
to the repository.
