# PhysioNet Access Checklist — Full MIMIC-IV (H2)

**Status: ✅ CREDENTIALED 2026-08-22, 2:25 a.m. (account `adeelmasih`)** — application
submitted 2026-08-14, approved in eight days.

**Training report SUBMITTED 2026-08-25** (correct `citiCompletionReport_*.pdf`, after the
certificate was rejected) — awaiting PhysioNet review; status visible at
`physionet.org/settings/certification/`.

**Remaining steps, in order (author actions):**
1. **Training tab** — confirm the CITI "Data or Specimens Only Research" completion report is
   uploaded and shows as verified. If not done, this blocks the DUAs.
   *(✅ CITI course COMPLETED 2026-08-25 — "Data or Specimens Only Research", Human Research
   curriculum, Basic Course stage, under Massachusetts Institute of Technology Affiliates
   (the free route). Record ID 79074346; valid to 2029-08-25.)*
   **Upload note (learned the hard way 2026-08-25):** PhysioNet rejects the completion
   *certificate* — it requires the *training report* (`physionet.org/about/citi-course/`:
   "upload the training report rather than the certificate"). Get it from CITI → **Records**
   → Completion Record → **View-Print-Share** → the *Report* (filename pattern
   `citiCompletionReport_<userid>_<recordid>.pdf`; 2 pages, all 9 modules with scores).
   Verified content: reported score **97** (minimum 90), and it includes *Research and HIPAA
   Privacy Protections* (ID 14), which PhysioNet's form explicitly requires.
2. ✅ **Both DUAs SIGNED 2026-08-25** (PhysioNet Credentialed Health Data Use Agreement
   **1.5.0**, signed by Adeel Masih):
   - **MIMIC-IV (v3.1)** — core structured tables
   - **MIMIC-IV-Note** — free-text notes (required for the notes-RAG module)
   Signed copies kept by the author outside the repository. Verify anytime at
   `physionet.org/settings/agreements/`.

   **Operative DUA clauses to respect in all project work:** no re-identification attempts
   (1–2); **no sharing access with anyone else (3)**; maintain physical/electronic security
   (4); report any identifying information found to PHI-report@physionet.org (5); lawful
   scientific research use only (6). These are why raw data lives outside the repo, why no
   credentials or data are ever handed to an assistant or third-party service, and why R8
   forbids any patient-level content in the thesis.
3. **Access route** (decided 2026-08-22): selective local download of only the tables in
   `03_Dataset/Data_Dictionary.md` to `C:\data\mimic-iv\` (~206 GB free on C:, subset is a
   few GB compressed — full download unnecessary), plus optional BigQuery access (Cloud tab →
   link Google account) for free-tier cohort SQL without downloading anything.

   **Download scripts (added 2026-08-25, both syntax-checked; 15 tables, URLs verified 403 not 404):**
   - `03_Dataset/download_mimic_subset.ps1` — **PowerShell (use this on this machine)**:
     `cd 03_Dataset; .\download_mimic_subset.ps1`
   - `03_Dataset/download_mimic_subset.sh` — Git Bash equivalent. Note: plain `bash` in
     PowerShell resolves to WSL (no distro installed); use
     `& "C:\Program Files\Git\bin\bash.exe" download_mimic_subset.sh` if you prefer it.

   Both prompt for the PhysioNet password, hold it only in an ACL-restricted per-user temp
   netrc deleted on exit, never pass it as a command-line argument, resume partial files, and
   refuse to write inside the repository. Tables fetched: hosp = patients, admissions,
   labevents, d_labitems, diagnoses_icd, procedures_icd, prescriptions, microbiologyevents;
   icu = icustays, chartevents, inputevents, outputevents, d_items; note = discharge,
   radiology; plus both SHA256SUMS files for provenance.
4. Record DUA acceptance dates here when signed; then H3 (cohort + D5 fix) unblocks.

## Steps, in order

1. **Create/verify a PhysioNet account** at physionet.org with your institutional email
   (adeel@… / university address preferred — institutional affiliation speeds review).
2. **Complete CITI training**: "Data or Specimens Only Research" course via citiprogram.org
   (affiliate as "Massachusetts Institute of Technology Affiliates" — the course PhysioNet
   requires). Takes ~2–4 hours. Save the completion report PDF.
3. **Apply for credentialing** on PhysioNet (Account → Credentialing): supply the CITI report,
   your supervisor's name (Dr. Fawad Nasim) as reference, and research description (use the
   thesis title and one paragraph from `02_Research/Research_Gap.md`). Typical turnaround:
   days to ~2 weeks.
4. **Sign the DUA** for each project after credentialing is approved:
   - `MIMIC-IV` (v3.x) — the core clinical database (required).
   - `MIMIC-IV-Note` — the deidentified free-text notes (required for the notes-RAG module;
     it is a **separate** project with its own DUA click-through).
5. **Record the evidence in this repo** (required by H2's wording "obtain/record"): add the
   credentialing approval date and DUA acceptance dates to this file, and update
   `01_Admin/Progress_Tracker.md`. **Do not add any downloaded data, paths inside the repo, or
   screenshots containing account details — R8 applies.**
6. **Download to a location OUTSIDE this repository** (e.g., `D:\mimic-iv\` — big: ~10s of GB
   for the hosp/icu modules; MIMIC-IV-Note adds more). Configure the pilot/experiment code's
   data root via its existing config mechanism (see `05_Source_Code/README.md`), never by
   copying files into the repo.
7. **Immediately unblocked once data lands**: cohort extraction (H3, spec in
   `03_Dataset/Cohort_Definition.md` + the D5-reconciled labels), then H4/H5.

## Fallback while waiting (from `01_Admin/Timeline.md` risk section)
Start the LLM agent loop (H4) against the open 100-patient demo (already used by the pilot) so
Month-3 work is not blocked; swap the data root when credentialing lands.
