# Thesis Consistency Report (Phase 5)

Checks that Research Objectives, Research Questions, Problem Statement, Research Gap, Framework, Architecture, Methodology, and Contributions agree with each other and with the title *"An Agentic AI Framework for Intelligent Patient Monitoring and Clinical Decision Support."*

**Verdict:** the thesis is thematically coherent and **every chapter aligns with the title** — but there are **five concrete internal inconsistencies**, two of them examiner‑visible in seconds. None is fatal; all are mechanical to fix.

---

## 1. Title alignment — PASS

Every chapter is on‑title. Background, problem, gap, framework, architecture, and evaluation all concern an agentic, multi‑agent, MIMIC‑IV‑grounded, human‑supervised clinical decision‑support / monitoring system. The abstract in `build_thesis_docx.py` matches. No drift from the title.

---

## 2. Objectives ↔ Questions ↔ Contributions — mostly consistent

- **Objectives:** 1 primary + **7 specific** (`Chapter_1/Objectives.md:5,11‑23`; identical in `Chapter_1_Revised.md:35`).
- **Research Questions:** **5** (RQ1–RQ5) (`Chapter_1/Research_Questions.md`; `Chapter_1_Revised.md:43‑51`).
- **Contributions:** C1–C6 in `Chapter_5.md:29‑44`, each tagged to an objective (Obj.1–7). Mapping is clean.
- Problem Statement (`Chapter_1/Problem_Statement.md` and `Chapter_1_Revised.md:21‑27`) and both Research‑Gap documents point at the same gap. ✅

---

## 3. INCONSISTENCY #1 — two different Research‑Question schemes (HIGH)

The thesis carries **two incompatible RQ framings**:

- **Chapter 1:** five RQs (RQ1 limitations; RQ2 agentic capabilities; RQ3 multi‑agent + oversight; RQ4 RAG; RQ5 monitoring on MIMIC‑IV).
- **Research‑gap files:** `02_Research/Research_Gap.md:49‑62` and `Chapter_2/Research_Gap_Analysis.md` frame **three** questions (timeline‑RAG vs baselines; patient‑grounded retrieval vs hallucination; verification gate + faithful audit).

These are thematically related but never reconciled into one numbered scheme. An examiner will ask "how many research questions does this thesis have?" and the answer differs by chapter.

**Fix:** keep the five Chapter‑1 RQs as canonical; present the three research‑gap questions explicitly as *evaluation sub‑questions* derived from RQ2/RQ3/RQ4, not as a competing set.

---

## 4. INCONSISTENCY #2 — Chapter 4 reuses "RQ1–RQ5" with different meanings (HIGH)

`06_Experiments/Experimental_Design.md` and `Chapter_4.md` map metrics to "RQ1–RQ5" but the referents differ from Chapter 1:

| RQ | Chapter 1 meaning | Chapter 4 / Experiments meaning |
|---|---|---|
| RQ1 | Limitations of current systems (review) | Accuracy floor / baseline B0 |
| RQ5 | Support monitoring on MIMIC‑IV | **Risk‑prediction discrimination (AUROC/AUPRC vs LR/SOFA)** |

RQ3 and RQ4 align reasonably; RQ2 partially; **RQ5 does not correspond at all.** Using the same labels for different questions is a serious traceability defect in the exact chapter (4) that claims "every metric traces to a research question."

**Fix:** re‑map the Chapter 4 metric‑to‑RQ table to the canonical five RQs, or introduce distinct hypothesis IDs (H1–Hn) and map *those* to the RQs, avoiding label reuse.

---

## 5. INCONSISTENCY #3 — agent count: 7 vs 8 (HIGH, examiner‑visible)

- **Chapter 3 canonical set = 8 specialized agents + Coordinator:** Monitoring, Planner, **Data/Retrieval (added)**, Diagnosis, Risk Prediction, Treatment Recommendation, Explanation, Verification (`Chapter_3.md:63‑133`), plus the **Memory‑Manager** module. Chapter 3 explicitly flags the Data/Retrieval Agent and Memory‑Manager as additions to the original design (L11, L58‑59).
- **But the phrase "seven‑agent" survives** as a stale undercount in: `Chapter_3.md:41` and `:137` ("full seven‑agent pipeline"), `System_Design.md:143`, `Technical_Feasibility.md:7` and §10. The worked trace at `Chapter_3.md:169‑173` actually runs **eight** agents.
- **`04_Architecture/Proposed_Framework.md` is the stale original: only 7 specialized agents, no Data/Retrieval Agent, no Memory‑Manager** (agents at L200‑267; Coordinator L192). It contradicts every downstream document and the examiner already flagged the drift.

**Fix:** (a) globally change "seven‑agent" → "eight specialized agents"; (b) update or delete `04_Architecture/Proposed_Framework.md` (add the two components or replace with a pointer to Chapter 3).

---

## 6. INCONSISTENCY #4 — cohort labels ≠ experiment tasks (HIGH)

- `03_Dataset/Cohort_Definition.md:68‑99` defines **4 prediction labels:** in‑hospital mortality, ICU readmission (30‑day), Sepsis‑3 onset, **prolonged LOS (> 7 days)**.
- `06_Experiments/Experimental_Design.md:18‑24` defines tasks: T1 mortality, **T2 ICU transfer/escalation**, T3 sepsis, T4 30‑day readmission, T5 diagnosis, T6 treatment.
- Mismatch: **prolonged‑LOS** (cohort) has **no task**; **T2 ICU transfer/escalation** (experiments) has **no cohort label**. The metric grid's "T1–T4 risk tasks" therefore does not map cleanly onto the four defined labels.

**Fix:** pick the four risk labels once and use them identically in both files (decide prolonged‑LOS vs ICU‑transfer).

---

## 7. INCONSISTENCY #5 — taxonomy "five vs six" (LOW)

`Chapter_2/Taxonomy.md:3` (stub) says the taxonomy has **"five core themes"** then lists **six** (memory, planning, reasoning, tool use, multi‑agent, healthcare). The full files (`04_Architecture/Taxonomy.md`, `Taxonomy_of_LLM_Based_Agents.md`) correctly say six.

**Fix:** delete the stub (it is superseded); ensure "six capability dimensions" everywhere.

---

## 8. Framework / architecture layer consistency — PASS (with one framing gap)

- Six horizontal layers + one cross‑cutting Trustworthy‑AI layer + HITL: consistent between `Chapter_3.md:14‑15` and `04_Architecture/Proposed_Framework.md:37‑44` (same six names: Data, Memory, Reasoning & Knowledge, Agent Orchestration, Clinical Decision, Clinician Dashboard).
- **Minor:** the "cross‑cutting" framing of the Trustworthy‑AI layer is explicit only in Chapter 3; `04_Architecture/Proposed_Framework.md` presents it as another block (Section 12), not cross‑cutting. Align the framing.

---

## 9. Citation‑format consistency — LOW (see Citation Audit)

Source files use `[key; key2]`; `Compiled/Chapter_1.md`/`Chapter_2.md` use `[key][key2]`. The build script regex handles single `[key]` tokens; the `[a; b]` form is **not** split by `CITE_RE` and will not resolve to numbered references. Standardize to whatever the build script expects (single‑key brackets) or fix the regex.

---

## 10. Documents that are stale / superseded (consolidate)

| Stale file | Superseded by |
|---|---|
| `04_Architecture/Proposed_Framework.md` (7 agents) | `Chapter_3.md` (8 agents) |
| `04_Architecture/Taxonomy.md` | `Chapter_2/Taxonomy_of_LLM_Based_Agents.md` (and Compiled) |
| `Chapter_2/{Taxonomy,Proposed_Framework,Research_Gap,Literature_Review}.md` stubs | full sections / Chapter 3 |
| `Chapter_1/Chapter_1.md` | `Chapter_1_Revised.md` / `Compiled/Chapter_1.md` |
| original Ch2 sections | their `_Revised` siblings |

---

## 11. Summary of fixes (feeds TODO lists)

1. One canonical RQ scheme (five); present the three gap‑questions as derived sub‑questions.
2. Re‑map Chapter 4 metrics to the canonical RQs (stop reusing labels).
3. "Seven‑agent" → "eight specialized agents" everywhere; fix/delete stale architecture doc.
4. One consistent set of four risk labels across cohort + experiments.
5. Delete the "five themes" stub; enforce "six".
6. Standardize citation bracket format for the build pipeline.
