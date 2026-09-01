# Skill — Dataset Analyst

**Load with:** [DATASET_RULES.md](../DATASET_RULES.md),
[RESEARCH_INTEGRITY.md](../RESEARCH_INTEGRITY.md), [METHODOLOGY_RULES.md](../METHODOLOGY_RULES.md)

**Use when:** working on `03_Dataset/`, cohort definitions, preprocessing, or any MIMIC-IV claim.

---

## Role

Be the person who knows what MIMIC-IV actually contains, and who never lets a patient record
touch version control.

## Rule zero

**No patient data enters this repository.** Not raw tables, not filtered cohorts, not feature
files, not note text, not embeddings derived from notes, not resolved `subject_id`/`stay_id`
lists, not a single example row. Only code, schemas, configuration, and aggregate metrics.

`03_Dataset/.gitignore` is a safety net, not a substitute for care. Verify with `git status`
before every commit.

## The two facts most often stated wrong

**Notes are a separate module.** Base MIMIC-IV = `hosp` + `icu`. Free text lives in
**MIMIC-IV-Note**, a distinct credentialed release requested separately. Download base only and
you have labs, vitals, medications, diagnoses — and **no note text at all**. The RAG patient index
and the Diagnosis Agent's narrative reasoning both depend on it.

**There is no `NOTEEVENTS` table.** That was MIMIC-III. MIMIC-IV splits note content by document
type (`discharge`, `radiology`). Any inherited code or documentation referencing `NOTEEVENTS` is
wrong here.

## Time is relative

Dates are shifted into the future per patient. Intervals within a patient are preserved; absolute
dates are not real. The Data Layer works **exclusively in relative time from admission**. Any
figure, example, or schema using absolute dates is a defect. Age is anonymized at the high end,
and the cohort criteria guard against that artifact.

## Never invent a table or column

Check `03_Dataset/Data_Dictionary.md` or the official schema. If unsure, write `[VERIFY SOURCE]`.
Confirmed tables:

- `hosp`: `patients`, `admissions`, `labevents`, `prescriptions`, `diagnoses_icd`,
  `procedures_icd`, `microbiologyevents`, `d_labitems`
- `icu`: `icustays`, `chartevents`, `inputevents`, `outputevents`, `d_items`
- MIMIC-IV-Note: `discharge`, `radiology`

Keys: `subject_id` (patient) · `hadm_id` (admission) · `stay_id` (ICU stay).

## Demo ≠ full MIMIC-IV

| | Demo v2.2 (pilot) | Full MIMIC-IV (Chapter 4) |
|---|---|---|
| Access | Open licence | Credentialed + DUA |
| Size | 100 patients / 140 ICU stays | Tens of thousands of stays |
| Notes | Excluded | Requires MIMIC-IV-Note |
| Status | Used 2026-08-07 | **Not obtained** |

Never let "MIMIC-IV" stand ambiguously for both.

## Keep the pipeline vocabulary distinct

raw data → cohort selection → processed data → patient timeline → feature engineering →
model input → model output → evaluation data

Conflating these is the most common dataset-writing defect.

## Cohort discipline

Ten criteria in `03_Dataset/Cohort_Definition.md`. Load-bearing points:

- ICU stays, not admissions.
- **First ICU stay only** — no intra-patient leakage.
- LOS ≥ 24 h — a stated survivorship caveat, not an oversight.
- Must have labs, vitals, **and ≥ 1 note**.
- **Filter ordering matters**: first-stay before LOS and availability, so a patient is never
  silently promoted to a later stay.
- Target ~100–500 patients — bounded by LLM cost, not statistical power.
- Any positive-case enrichment is **recorded**, so prevalences are not read as population rates.
- The realized count is reported alongside results, never fixed in advance.

## Labels

Mortality (from `admissions`, not inferred) · ICU readmission (later stays are **label
information only**) · Sepsis-3 onset with **onset time** [singer2016sepsis3; vincent1996sofa] ·
prolonged LOS (> 7 days).

Known defect D5: these four do not match the six experiment tasks. Reconcile in both files.

## Leakage control

Patient-level splits. Label derivations looking beyond the index stay stay separate from feature
construction. Retrieval is timestamp-aware — no post-decision evidence. Cohort materialized by a
scripted, seeded, deterministic query.

## Deliver

What was changed, which dataset claims were verified against which source, whether any claim
needed `[VERIFY SOURCE]`, and confirmation that `git status` shows no data staged.
