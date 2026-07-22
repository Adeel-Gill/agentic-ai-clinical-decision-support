# Dataset: MIMIC-IV

This directory documents the data foundation for the proposed framework, *An Agentic
AI Framework for Intelligent Patient Monitoring and Clinical Decision Support*. All
experimentation and evaluation draw on **MIMIC-IV**, a large, de-identified critical-care
database curated from the intensive care units of the Beth Israel Deaconess Medical Center
[johnson2023mimic] and distributed through the PhysioNet platform [goldberger2000physiobank].
The material here specifies how the data are obtained, which modules are used, and the
ethical and technical constraints that govern their handling. It is documentation only: no
patient record, extract, or derived file is stored in this repository, and none ever should be.

## What MIMIC-IV is (and is not)

MIMIC-IV is a relational database of hospital and ICU encounters recorded over roughly a
decade. It is the successor to MIMIC-III, and its organization differs in ways that matter
for this project. Two points deserve emphasis because they are common sources of error.

First, MIMIC-IV is split into distinct **modules**, and the free-text clinical notes are not
part of the base download. The core database is organized into a hospital-wide module
(`hosp`) and an ICU module (`icu`). Narrative documentation, such as discharge summaries and
radiology reports, lives in a **separate module, MIMIC-IV-Note**, which must be requested and
downloaded under its own credentialed release. A researcher who downloads only base MIMIC-IV
will have structured labs, vitals, medications, and diagnoses, but will have no note text at
all. Any component of the proposed framework that depends on narrative text, in particular
the Retrieval-Augmented Generation (RAG) patient index, therefore requires MIMIC-IV-Note in
addition to the base modules.

Second, MIMIC-IV does **not** carry forward the single monolithic `NOTEEVENTS` table that
MIMIC-III used to hold all note text. That design was replaced. In MIMIC-IV, note content is
split by document type inside the MIMIC-IV-Note module (for example, `discharge` and
`radiology` tables) rather than concentrated in one table. Documentation and code inherited
from MIMIC-III that references `NOTEEVENTS` will not work here and must be rewritten against
the MIMIC-IV-Note schema.

## Module structure

| Module | Scope | Representative tables | Role in the framework |
|---|---|---|---|
| `hosp` | Hospital-wide records spanning the full admission | `patients`, `admissions`, `labevents`, `prescriptions`, `diagnoses_icd`, `procedures_icd`, `microbiologyevents`, `d_labitems` | Demographics, admission context, laboratory trends, medication timelines, coded diagnoses and procedures, culture results |
| `icu` | ICU-specific, high-frequency records | `icustays`, `chartevents`, `inputevents`, `outputevents`, `d_items` | ICU stay boundaries, charted vital signs, infusions and fluids, the monitoring substrate |
| `MIMIC-IV-Note` | Free-text clinical narratives (separate credentialed release) | `discharge`, `radiology` | Unstructured evidence for diagnosis reasoning and the RAG patient index |

The `hosp` and `icu` modules are linked by shared identifiers: `subject_id` identifies a
patient, `hadm_id` a hospital admission, and `stay_id` a single ICU stay. MIMIC-IV-Note is
linked back to the structured data through the same `subject_id` and `hadm_id` keys, which is
what allows a patient's notes to be aligned with the time-ordered clinical events used for
monitoring.

## Access and credentialing

MIMIC-IV is credentialed data, not open data. Obtaining it is a prerequisite before any
extraction described in `Preprocessing_Pipeline.md` can begin, and the same requirements apply
to the MIMIC-IV-Note module.

1. **Create a PhysioNet account** and complete identity verification on the PhysioNet
   platform [goldberger2000physiobank].
2. **Complete the required human-subjects training.** PhysioNet requires the CITI Program
   course "Data or Specimens Only Research"; the completion report must be submitted to
   PhysioNet.
3. **Sign the PhysioNet Credentialed Health Data Use Agreement (DUA)** for MIMIC-IV. The DUA
   binds the user to defined responsible-use terms, including a prohibition on attempting to
   re-identify individuals and on redistributing the data.
4. **Request each module separately.** Acceptance of the base MIMIC-IV DUA does not
   automatically grant MIMIC-IV-Note; the note module is a distinct credentialed project and
   must be requested on its own.
5. **Download to a secure, access-controlled environment** outside this repository. The data
   must reside only on approved local or institutional storage, never in version control.

Credentialing typically takes days to weeks depending on training and review turnaround, so
it should be initiated early in the project timeline.

## Ethics and responsible use

The data are de-identified in accordance with HIPAA Safe Harbor provisions, and dates are
shifted into the future on a per-patient basis so that intervals within a patient are
preserved while absolute dates are not real. De-identification reduces but does not eliminate
obligations: the DUA still forbids re-identification attempts, and any downstream artifact
(figures, tables, model outputs, error analyses) must avoid reproducing information that could
single out an individual. Because the framework processes narrative notes through LLM agents,
particular care is needed that prompts, logs, and cached retrieval results are held only in
the same secured environment as the source data and are excluded from the repository. A
verification step confirming de-identification integrity is built into the preprocessing plan
(see `Preprocessing_Pipeline.md`).

## No PHI in the repository

**No patient data of any kind is committed to this repository.** This includes raw MIMIC-IV
tables, filtered cohorts, engineered feature files, note text, embeddings derived from note
text, and any intermediate extract. Only code, schema definitions, configuration, and
aggregate documentation belong here. Even though MIMIC-IV is de-identified, committing it
would violate the DUA's redistribution terms.

## `.gitignore` reminder

A `.gitignore` in this directory (`03_Dataset/.gitignore`) excludes the common data file
formats and the working `data/` directory so that extracts cannot be added by accident.
Before any commit, confirm with `git status` that no `.csv`, `.csv.gz`, `.parquet`, or
`data/` path is staged. The ignore rules are a safety net, not a substitute for care: keep
the actual database and all derived files in the secured environment described above, and
point the pipeline at that location through configuration rather than by copying data into the
project tree.

## Files in this directory

| File | Purpose |
|---|---|
| `README.md` | This overview: access, credentialing, ethics, module structure |
| `Cohort_Definition.md` | Inclusion/exclusion criteria and label definitions for the prototype cohort |
| `Data_Dictionary.md` | The specific tables and columns used, and their role in the framework |
| `Preprocessing_Pipeline.md` | ETL and feature-engineering plan, including the patient-timeline construction |
| `.gitignore` | Rules that keep data files out of version control |
