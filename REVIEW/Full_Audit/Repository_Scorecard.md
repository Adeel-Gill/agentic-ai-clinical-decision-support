# Repository Scorecard

Scores out of 10. **Convention:** 10 = best. For the two *risk* rows (Plagiarism Risk, AI‑Detection Risk), 10 = **lowest** risk / most defensible.

Because the repo contains both a strong revised core and a weak AI‑draft scaffold, each row shows the **blended (as‑is)** score and, in brackets, the **core‑only** score you would reach after deleting/finishing the drafts (Review Report items 1–7).

---

## 1. Scores

| # | Area | Blended (as‑is) | Core‑only (achievable) | Basis |
|---|---|:--:|:--:|---|
| 1 | Academic Writing | **6** | (8.5) | Revised chapters/Ch3/Ch4 are examiner‑grade; un‑revised drafts are formulaic. |
| 2 | Grammar | **7** | (9) | Core is clean; notes/drafts carry typos and copy artifacts. |
| 3 | Flow | **6** | (8) | Core argues well; drafts are choppy intro→bullets→"however". |
| 4 | Consistency | **4** | (7) | Agent count 7 vs 8; two RQ schemes; cohort labels ≠ tasks; stale architecture doc. |
| 5 | Originality | **5** | (7) | Defensible integrative gap (timeline‑RAG + verification), but literature sections still generic; needs comparison tables + critical analysis. |
| 6 | Plagiarism Risk (10 = low risk) | **5** | (8.5) | Repeated boilerplate + uncited canonical descriptions + copied note abstracts; revised body is clean. |
| 7 | AI‑Detection Risk (10 = human) | **4** | (8.5) | ~13 files HIGH AI‑signature; core reads human. |
| 8 | Research Quality | **6** | (7) | Strong gap analysis and evaluation design; no empirical results yet. |
| 9 | Framework Quality | **7** | (8) | Chapter 3 is genuinely rigorous — per‑agent contracts, DAG routing, arbitration protocol, wired‑in trust layer. |
| 10 | Literature Review | **5** | (7.5) | Matrix + notes solid in coverage; section files half‑revised, triplicated, half‑uncited; duplicate/wrong notes (P016=P017, P018). |
| 11 | Methodology | **6** | (7.5) | Design‑science framing and evaluation protocol are strong; implementation/execution absent. |

**Blended overall ≈ 5.6 / 10.** **Core‑only achievable ≈ 7.5 / 10** after the Critical/High fixes.

This is consistent with the prior `REVIEW/00_Examiner_Report.md` (≈ 46/100 as a *completed* thesis; strong as a *design/proposal* milestone). The scorecard here rates the writing/integrity dimensions the examiner report summarized; it does **not** re‑litigate the empirical gap (no prototype/results), which remains the deepest limitation and caps rows 8–11 until addressed.

---

## 2. What moves each score fastest

| Row | Fastest lever | Target after |
|---|---|---|
| Consistency (4) | Fix agent count + RQ schemes + cohort/task labels (Consistency Report) | 7 |
| AI‑Detection (4) | Delete superseded drafts + finish 6 `_Revised` sections | 8.5 |
| Plagiarism (5) | Delete drafts + de‑dup boilerplate + cite canonical descriptions | 8.5 |
| Originality (5) | Add capability matrix + critical sentences (Improvement H‑2/H‑3) | 7 |
| Literature (5) | Consolidate Chapter 2; fix P016/017/018 notes | 7.5 |

---

## 3. Submission‑readiness gate

**Not yet submission‑ready**, on two independent grounds:
1. **Integrity/writing (this audit):** superseded AI drafts still present, one placeholder citation used ~9×, internal inconsistencies. All fixable in ~1–2 weeks of editing (no new research).
2. **Empirical (prior examiner report):** no prototype, no experimental results — Chapters 4–5 describe a plan, not findings.

For a **design/methodology thesis** framing, ground 1 is the blocker you can clear now; ground 2 depends on whether your program accepts a design‑and‑protocol contribution or requires executed experiments. Confirm this with your supervisor early — it determines whether Chapter 4/5 need results before submission.
