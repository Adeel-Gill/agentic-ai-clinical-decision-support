# DATASET RULES — MIMIC-IV

Governs `03_Dataset/`, every dataset claim in any chapter, and all data handling.

---

## 1. Absolute rule: no patient data in this repository

**No MIMIC-IV data of any kind is ever committed.** This includes:

raw tables · filtered cohorts · engineered feature files · note text · embeddings derived from
note text · resolved cohort ID lists (`subject_id`, `stay_id`) · intermediate extracts ·
per-patient examples · screenshots containing real records · prompt logs · cached retrieval
results.

Only code, schema definitions, configuration, and **aggregate** documentation belong here.
MIMIC-IV is de-identified, but committing it still breaches the DUA's redistribution terms.

`03_Dataset/.gitignore` excludes `*.csv`, `*.csv.gz`, `*.parquet`, `*.pkl`, `*.npy`, `*.faiss`,
`data/`, `notes/`, `embeddings/`, and more. **The ignore rules are a safety net, not a
substitute for care.** Before any commit, confirm with `git status` that no data path is staged.

Point the pipeline at the secured environment through configuration; never copy data into the
project tree.

## 2. What MIMIC-IV actually is

A relational database of hospital and ICU encounters from Beth Israel Deaconess Medical Center,
distributed via PhysioNet [johnson2023mimic; goldberger2000physiobank]. Two facts are the most
common source of error and must never be misstated:

**Fact 1 — Notes are a separate module.** The base download splits into `hosp` (hospital-wide)
and `icu` (ICU) modules. Free-text notes live in **MIMIC-IV-Note**, a distinct credentialed
release that must be requested separately. A researcher who downloads only base MIMIC-IV has
labs, vitals, medications, and diagnoses — and **no note text at all**. Any component depending
on narrative text (the RAG patient index, the Diagnosis Agent's narrative reasoning) requires
MIMIC-IV-Note.

**Fact 2 — There is no `NOTEEVENTS` table.** That was MIMIC-III. In MIMIC-IV, note content is
split by document type inside MIMIC-IV-Note (`discharge`, `radiology`). Any code or documentation
inherited from MIMIC-III that references `NOTEEVENTS` is wrong here.

### Module structure

| Module | Scope | Representative tables |
|---|---|---|
| `hosp` | Full admission, hospital-wide | `patients`, `admissions`, `labevents`, `prescriptions`, `diagnoses_icd`, `procedures_icd`, `microbiologyevents`, `d_labitems` |
| `icu` | ICU-specific, high-frequency | `icustays`, `chartevents`, `inputevents`, `outputevents`, `d_items` |
| MIMIC-IV-Note | Free text (separate release) | `discharge`, `radiology` |

Linking keys: `subject_id` (patient), `hadm_id` (admission), `stay_id` (ICU stay). MIMIC-IV-Note
joins back through `subject_id` and `hadm_id`.

**Never claim a table, column, or field exists without checking `03_Dataset/Data_Dictionary.md`
or the official schema.** If unsure, write `[VERIFY SOURCE]`.

## 3. De-identification and time

Data are de-identified under HIPAA Safe Harbor. **Dates are shifted into the future on a
per-patient basis**: intervals within a patient are preserved, absolute dates are not real.

Therefore the Data Layer works **exclusively in relative time from admission**. Any design,
figure, or example using absolute dates is wrong. The agent message envelope encodes this
(`"timestamp_rel": "P0DT36H"`).

Age is also anonymized at the high end; the cohort criteria guard against age-anonymization
artifacts distorting features.

## 4. Access and credentialing

Prerequisites before any extraction:

1. PhysioNet account with identity verification.
2. CITI Program course "Data or Specimens Only Research"; completion report submitted.
3. Signed PhysioNet Credentialed Health Data Use Agreement for MIMIC-IV.
4. **Each module requested separately** — the base DUA does not grant MIMIC-IV-Note.
5. Download to a secure, access-controlled environment **outside this repository**.

Credentialing takes days to weeks. Status is currently `[IN PROGRESS]`
(`REVIEW/TODO_Prioritized.md` H6). No document may assume access is already granted.

## 5. The demo subset is a different thing

The pilot used the **MIMIC-IV Clinical Database Demo v2.2** — 100 patients, 140 ICU stays,
distributed under an open licence with **no credentialing requirement**.

| | Demo (used for the pilot) | Full MIMIC-IV (Chapter 4) |
|---|---|---|
| Access | Open licence | Credentialed + DUA |
| Size | 100 patients / 140 ICU stays | Tens of thousands of stays |
| Notes | **Excluded** | Requires MIMIC-IV-Note |
| Status | Used, 2026-08-07 | **Not obtained** |

Never let "MIMIC-IV" stand ambiguously for both. Every pilot result is a *demo* result.

## 6. The data pipeline vocabulary

Keep these distinct in every sentence. Conflating them is the most common dataset-writing defect:

| Stage | Meaning | Documented in |
|---|---|---|
| **Raw data** | Source tables as distributed | `03_Dataset/README.md` |
| **Cohort selection** | Which stays qualify (10 criteria) | `Cohort_Definition.md` |
| **Processed data** | Cleaned, unit-harmonized, range-validated | `Preprocessing_Pipeline.md` |
| **Patient timeline** | Chronologically ordered event stream with provenance pointers | `Preprocessing_Pipeline.md`, Ch. 3 §3.3.1 |
| **Feature engineering** | Windowed aggregates over the timeline | `Preprocessing_Pipeline.md` |
| **Model input** | What an agent or baseline actually receives | Ch. 3 / Ch. 4 |
| **Model output** | Predictions, differentials, recommendations | Ch. 3 §3.4 |
| **Evaluation data** | Held-out split, patient-level | `Cohort_Definition.md`, Ch. 4 |

## 7. Cohort rules

Ten inclusion/exclusion criteria are defined in `Cohort_Definition.md`. Load-bearing points:

- **ICU stays, not admissions** — the monitoring substrate is high-frequency ICU chart data.
- **First ICU stay only** — removes intra-patient leakage; fixes "current encounter" semantics.
- **LOS ≥ 24 h** — enough charted observations for windowed features. This is a stated
  survivorship caveat, not an oversight.
- **Must have labs, vitals, and ≥ 1 note** — a stay without notes cannot exercise the RAG index.
- **Ordering matters:** the first-stay filter runs *before* the LOS and availability filters, so
  a patient is never silently promoted to a later stay.
- **Target ~100–500 patients** — bounded by LLM cost, not by statistical power.
- Any positive-case enrichment must be **recorded**, so prevalences are not read as population
  rates.

## 8. Labels

Four supervised targets, all derived from structured tables at extraction time:

| Label | Definition | Reference |
|---|---|---|
| In-hospital mortality | Died before hospital discharge for the admission containing the index stay | Read from `admissions`, not inferred |
| ICU readmission | Return to ICU within a fixed window (commonly 30 days) | Later stays are **label information only**, never features |
| Sepsis onset | Sepsis-3: acute SOFA increase ≥ 2 with suspected infection (culture + antibiotic proximity) | [singer2016sepsis3; vincent1996sofa] |
| Prolonged LOS | ICU stay > 7 days | From `icustays` in/out timestamps |

**Onset time**, not merely presence, is recorded for sepsis so the Monitoring Agent can be
evaluated on early detection.

Known defect D5: these four labels do not match the six experiment tasks (T2 is "ICU
transfer/escalation", which has no cohort label; prolonged LOS has no task). Reconcile once,
in both files, before Chapter 4 is finalized.

## 9. Leakage control

- Train/validation/test splits are **patient-level**; no patient appears in two partitions.
- Label derivations that look beyond the index stay are strictly separated from feature
  construction.
- Retrieval is timestamp-aware: no evidence from after the decision point may enter a decision.
  The pilot verified this property; it must hold in the full evaluation too.
- The cohort is materialized by a **scripted, deterministic, seeded** query so the same patient
  set regenerates from the credentialed database.

## 10. Privacy in downstream artifacts

De-identification reduces but does not eliminate obligations. Figures, tables, model outputs,
error analyses, and case studies must not reproduce information that could single out an
individual. Because the framework passes narrative notes through LLM agents, prompts, logs, and
cached retrieval results must stay inside the same secured environment as the source data.

The DUA forbids re-identification attempts and redistribution. A verification step confirming
de-identification integrity is part of the preprocessing plan.

## 11. Writing about the dataset

- Never claim MIMIC-IV contains information it does not (real dates, provider identities,
  imaging pixels, outpatient records).
- Never state a cohort size as final — the realized count depends on how many first stays pass
  all criteria and is to be reported alongside results.
- Never present the demo pilot's 140 stays as the thesis cohort.
- Always cite `johnson2023mimic` for dataset properties and `goldberger2000physiobank` for
  PhysioNet.
- Always note the single-site, retrospective, critical-care-only nature as a generalizability
  limitation.
