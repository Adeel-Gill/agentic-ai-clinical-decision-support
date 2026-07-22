# Data Dictionary

This document lists the specific MIMIC-IV tables the proposed framework consumes, the module
each belongs to, the key columns used, the role the table plays in the framework, and any
volume caveats that shape how the data are handled. It is not a full reproduction of the
MIMIC-IV schema, which is published on PhysioNet [goldberger2000physiobank]; it records only
the subset this project actually reads and why. All column and table names follow the MIMIC-IV
v2/v3 naming convention [johnson2023mimic]. As stated in `README.md`, none of these tables or
any extract of them is stored in this repository.

## Identifier keys

Three identifiers thread through every table and are the basis for all joins. `subject_id`
identifies a unique patient. `hadm_id` identifies a single hospital admission. `stay_id`
identifies a single ICU stay. Laboratory and note tables are keyed to the patient and admission
level, while ICU chart and input tables are keyed additionally to the stay. The dictionary
tables `d_labitems` and `d_items` are lookup tables that translate the numeric `itemid` codes
in the event tables into human-readable labels; they carry no patient data and are safe to
inspect freely.

## Tables used

| Table | Module | Key columns | Role in the framework | Volume / caveats |
|---|---|---|---|---|
| `patients` | `hosp` | `subject_id`, `gender`, `anchor_age`, `anchor_year`, `dod` | Demographics for cohort filtering and case-mix; feeds long-term patient memory | Small (one row per patient). `anchor_age` is anonymized; ages are shifted and high ages capped |
| `admissions` | `hosp` | `subject_id`, `hadm_id`, `admittime`, `dischtime`, `deathtime`, `hospital_expire_flag`, `admission_type` | Admission context; source of the in-hospital mortality label | Small (one row per admission). Times are date-shifted per patient |
| `icustays` | `icu` | `subject_id`, `hadm_id`, `stay_id`, `intime`, `outtime`, `los` | Defines ICU stay boundaries; source of prolonged-LOS label; anchors the monitoring window | Moderate (one row per stay). First-stay-per-patient filter applied here |
| `labevents` | `hosp` | `subject_id`, `hadm_id`, `itemid`, `charttime`, `valuenum`, `valueuom`, `flag` | Laboratory trends for the Diagnosis and Risk agents; SOFA components for sepsis labeling | Large. Filter by cohort and by the `itemid` set of interest via `d_labitems` |
| `chartevents` | `icu` | `subject_id`, `stay_id`, `itemid`, `charttime`, `valuenum`, `valueuom` | Charted vital signs; the core monitoring substrate consumed by the Monitoring Agent | **Very large** (the largest table by far). Must be windowed and item-filtered; see below |
| `inputevents` | `icu` | `subject_id`, `stay_id`, `itemid`, `starttime`, `endtime`, `amount`, `rate` | Infusions and fluids for treatment context and SOFA (e.g., vasopressors) | Large. Filter by cohort and relevant `itemid` set |
| `outputevents` | `icu` | `subject_id`, `stay_id`, `itemid`, `charttime`, `value` | Fluid output (e.g., urine) for fluid-balance and organ-function features | Moderate to large; cohort-filtered |
| `prescriptions` | `hosp` | `subject_id`, `hadm_id`, `drug`, `starttime`, `stoptime`, `dose_val_rx`, `route` | Medication timeline for the Treatment agent; antibiotics for sepsis suspected-infection window | Large. Free-text `drug` names need normalization/mapping |
| `diagnoses_icd` | `hosp` | `subject_id`, `hadm_id`, `icd_code`, `icd_version`, `seq_num` | Coded diagnoses for case-mix, comorbidity features, and ICD mapping | Small to moderate. Mixed ICD-9 and ICD-10; requires version-aware mapping |
| `procedures_icd` | `hosp` | `subject_id`, `hadm_id`, `icd_code`, `icd_version`, `chartdate` | Coded procedures for treatment/severity context | Small to moderate. Mixed ICD-9/ICD-10 |
| `microbiologyevents` | `hosp` | `subject_id`, `hadm_id`, `charttime`, `spec_type_desc`, `org_name`, `ab_name` | Culture sampling and results; defines the suspected-infection component of Sepsis-3 | Moderate. Many null organism fields (negative cultures) |
| `d_labitems` | `hosp` | `itemid`, `label`, `fluid`, `category` | Lookup: resolves lab `itemid` to a readable name | Tiny dictionary; no patient data |
| `d_items` | `icu` | `itemid`, `label`, `category`, `unitname` | Lookup: resolves ICU chart/input `itemid` to a readable name | Tiny dictionary; no patient data |
| `discharge` | MIMIC-IV-Note | `subject_id`, `hadm_id`, `note_id`, `charttime`, `text` | Discharge summaries: primary narrative evidence for diagnosis reasoning and the RAG patient index | Large free text; **separate credentialed download**; segment and chunk before embedding |
| `radiology` | MIMIC-IV-Note | `subject_id`, `hadm_id`, `note_id`, `charttime`, `text` | Radiology reports: imaging narrative for diagnosis context and RAG | Large free text; separate credentialed download |

## Mapping tables to framework functions

The tables above are not consumed uniformly; each supports specific layers and agents of the
proposed framework. The demographic and admission tables (`patients`, `admissions`,
`icustays`) establish the encounter skeleton and populate long-term patient memory. The
high-frequency ICU tables (`chartevents`, `inputevents`, `outputevents`) form the **monitoring**
substrate that the Monitoring Agent watches for abnormal or changing values. Laboratory data
(`labevents`) together with the notes feed **diagnosis** reasoning. The **risk** targets draw on
labs, vitals, cultures, and medications jointly, since mortality, readmission, sepsis, and
prolonged stay each depend on a different combination of these signals. Medication, procedure,
and diagnosis codes (`prescriptions`, `procedures_icd`, `diagnoses_icd`) inform **treatment**
context and case-mix. Finally, the MIMIC-IV-Note tables (`discharge`, `radiology`) are the raw
material for **RAG**: after segmentation and chunking they become the per-patient document
index that the retrieval module searches during reasoning.

| Framework function | Primary tables |
|---|---|
| Monitoring | `chartevents`, `inputevents`, `outputevents`, `icustays` |
| Diagnosis | `labevents`, `diagnoses_icd`, `discharge`, `radiology` |
| Risk prediction | `labevents`, `chartevents`, `microbiologyevents`, `prescriptions`, `admissions`, `icustays` |
| Treatment | `prescriptions`, `procedures_icd`, `diagnoses_icd` |
| RAG (patient index) | `discharge`, `radiology` |
| Patient memory / context | `patients`, `admissions`, `icustays`, `diagnoses_icd` |

## Why `chartevents` forces windowing

`chartevents` is by a wide margin the largest table in MIMIC-IV: it records every charted
observation for every ICU stay at the resolution the bedside monitors and nurses documented,
which runs to hundreds of millions of rows across the full database [johnson2023mimic]. Loading
it in full is neither necessary nor practical for a prototype of a few hundred patients, and it
would dominate both storage and processing time while most of its rows correspond to `itemid`
codes the framework never uses.

Two reductions make it tractable, and both are applied at extraction rather than after loading.
The first is a **cohort filter**: only rows whose `stay_id` belongs to the selected cohort are
pulled, which alone removes the overwhelming majority of the table. The second is an **item
filter**: only the `itemid` values corresponding to the vital signs the Monitoring Agent needs,
resolved through `d_items`, are retained, discarding the long tail of rarely used parameters.
On top of these, the monitoring pipeline **windows** the retained observations relative to each
stay's `intime` and resamples them onto a regular grid (see `Preprocessing_Pipeline.md`), so
that irregular, high-frequency charting is compressed into fixed-interval trends. The same
cohort-and-item discipline applies, to a lesser degree, to `labevents`, `inputevents`, and the
note tables, all of which are large enough that unfiltered extraction would be wasteful. The
practical rule is that no large table is ever read in full: the cohort and item sets are pushed
down into the extraction query so that only the needed slice ever leaves the database.
