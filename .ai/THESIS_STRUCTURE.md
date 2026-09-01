# THESIS STRUCTURE

The authoritative scheme. Anything contradicting this file is a defect to fix, not a variant
to accommodate.

---

## 1. Chapter numbering

| Chapter | Title | Content | Status |
|---|---|---|---|
| 1 | Introduction | Background, problem statement, objectives, RQs, scope, significance | Drafted + revised |
| 2 | Literature Review | Background, taxonomy, systems review, **research gap** | Drafted; partly revised |
| 3 | Proposed Framework & Methodology | **The architecture lives here (Figure 3.x)**, agents, memory, RAG, orchestration, trust layer, worked trace | Drafted |
| 4 | Experimental Design & Evaluation | Cohort, baselines, ablations, metrics, hypotheses, threats to validity | Design only — **not executed** |
| 5 | Conclusion & Future Work | Contributions, RQ answers, limitations, future work | Outline with stubs |

Any label placing the framework in Chapter 4, or a "Figure 4.1" on the architecture, is **wrong**
and predates the standardization. Fix on sight.

## 2. Research questions — five, canonical

Source of truth: `07_Thesis/Chapter_1/Research_Questions.md`.

| RQ | Question |
|---|---|
| RQ1 | What limitations exist in current LLM-based healthcare systems for intelligent patient monitoring and clinical decision support? |
| RQ2 | How can Agentic AI improve reasoning, planning, memory management, and autonomous collaboration in healthcare applications? |
| RQ3 | How can multiple specialized agents collaborate to support clinical decision making while maintaining explainability and physician oversight? |
| RQ4 | How can RAG and external medical knowledge improve the reliability and transparency of AI-generated clinical recommendations? |
| RQ5 | How can the proposed framework support intelligent patient monitoring using the MIMIC-IV dataset? |

### The three gap questions are derived, not competing

`02_Research/Research_Gap.md` frames three testable questions (timeline-RAG vs baselines;
patient-grounded retrieval vs hallucination; verification gate + faithful audit). These are
**evaluation sub-questions derived from RQ2/RQ3/RQ4** — present them that way, always. Two
competing RQ schemes is a documented HIGH-severity inconsistency
(`REVIEW/Full_Audit/Consistency_Report.md` §3).

### Chapter 4 must not reuse RQ labels loosely

Chapter 4 and `06_Experiments/` previously mapped metrics to "RQ1–RQ5" with different referents
(notably RQ5 = risk-prediction discrimination, which is not what RQ5 asks). Use the
**hypothesis IDs H1–H10** as the primary handle and map *those* to the canonical RQs. Never
re-define an RQ label locally.

## 3. Objectives — one primary, seven specific

Source: `07_Thesis/Chapter_1/Objectives.md`.

**Primary:** design an Agentic AI framework for intelligent patient monitoring and clinical
decision support using MIMIC-IV.

1. Investigate recent advances in Agentic AI, LLMs, and intelligent healthcare systems.
2. Identify limitations and research gaps in existing CDSS.
3. Develop a layered framework integrating memory, reasoning, planning, RAG, and multi-agent
   collaboration.
4. Design specialized agents for monitoring, diagnosis support, risk prediction, treatment
   recommendation, and explanation.
5. Incorporate trustworthy-AI principles: explainability, transparency, safety, auditability,
   HITL validation.
6. Use MIMIC-IV as the primary data source for design and validation.
7. Provide a conceptual architecture plus a bounded prototype and evaluation plan.

## 4. Contributions — C1 to C6

Source: `07_Thesis/Chapter_5/Chapter_5.md` §5.2. Each is tagged to the objective it satisfies.

| ID | Contribution | Objectives |
|---|---|---|
| C1 | Critical synthesis and defensible research gap | 1, 2 |
| C2 | Taxonomy of LLM-based agents (six capability dimensions) | 1 |
| C3 | Layered agentic framework | 3 |
| C4 | Specialized clinical agents under a Coordinator | 4 |
| C5 | Trustworthy-AI layer embedded structurally | 5 |
| C6 | MIMIC-IV grounding + bounded prototype + evaluation plan | 6, 7 |

**Every claimed contribution needs evidence.** C6's "bounded prototype" is currently evidenced
by the pilot and the clinician platform, not by the LLM agent loop. Say so.

## 5. The traceability chain

```
Research Questions (5)
        ↓
Objectives (1 + 7)
        ↓
Research Gap (3 derived sub-questions)
        ↓
Methodology (Ch. 3, design science)
        ↓
Framework (6 layers + trust layer + HITL)
        ↓
Experiments (B0–B3, A1–A4, T1–T6, C1)
        ↓
Results (pilot done; full evaluation pending)
        ↓
Conclusions (C1–C6, RQ answers)
```

Invariants to check after any structural edit:

- [ ] Every RQ is eventually answered (Ch. 5 §5.3), or explicitly marked *(pending Chapter 4)*.
- [ ] Every objective has corresponding work somewhere.
- [ ] Every contribution has evidence, or is downgraded.
- [ ] Every experiment traces to a hypothesis, and every hypothesis to an RQ.
- [ ] The gap stated in Ch. 2 is the gap the framework addresses in Ch. 3 and tests in Ch. 4.

`REVIEW/Full_Audit/Improvement_Checklist.md` M-1 recommends a single layer → objective → RQ →
metric traceability table. If asked to strengthen coherence, build that table — it fixes several
inconsistencies at once.

## 6. Gap vs Contribution vs Future Work

Three distinct things. Keep them separate.

| | Answers | Lives in | Test |
|---|---|---|---|
| **Research Gap** | What the field has not done | Ch. 2 §2.9, `02_Research/Research_Gap.md` | Emerges from the literature; survives a check against P021–P050 |
| **Contribution** | What *this thesis* does about it | Ch. 1, Ch. 5 §5.2 | Has evidence in this repository |
| **Future Work** | What remains after this thesis | Ch. 5 §5.5 | Explicitly out of scope, tied to a named limitation |

A gap must not be manufactured to justify the thesis. It must identify what existing systems
solve, what they partly solve, what remains unresolved, why that matters, how the framework
addresses it, and what stays out of scope. `02_Research/Research_Gap.md` does exactly this —
match its rigor.

## 7. Canonical vs superseded files

| Canonical | Superseded |
|---|---|
| `07_Thesis/Compiled/Chapter_1.md` | `Chapter_1/Chapter_1.md` *(deleted 2026-08-14)* |
| `07_Thesis/Chapter_1/Chapter_1_Revised.md` | — (the remaining `Chapter_1/*.md` content files — Objectives, Problem_Statement, Research_Questions, Scope — are canonical sources, not superseded) |
| `07_Thesis/Compiled/Chapter_2.md` | all `Chapter_2/*.md` originals and stubs *(16 files deleted 2026-08-14)* |
| `07_Thesis/Chapter_2/*_Revised.md` + `Recent_Advances_2025_2026.md` + `Research_Gap_Analysis.md` | their non-revised siblings *(deleted 2026-08-14)* |
| `07_Thesis/Chapter_3/Chapter_3.md` | `04_Architecture/Proposed_Framework.md` (working summary; aligned 2026-08-13) |
| `07_Thesis/Compiled/Chapter_2.md` §2.5 (taxonomy) | `Chapter_2/Taxonomy_of_LLM_Based_Agents.md` *(deleted)*; `04_Architecture/Taxonomy.md` *(bannered; retained only as the taxonomy-figure home)* |

**Deletion record (2026-08-14, author-approved):** the 17 bannered superseded originals and
one-line stubs (16 in `Chapter_2/` plus `Chapter_1/Chapter_1.md`) were deleted per the
`TODO_AI.md` recommendation; each carried a SUPERSEDED banner and every one is recoverable
from git history. What remains on disk in those directories is canonical.

## 8. Front matter

Order per `07_Thesis/Thesis_Formatting_Guide.md`: Title page → Author's Declaration →
Certificate → Dedication → Acknowledgements → Abstract → Table of Contents → List of Figures →
List of Tables → Abbreviations → Chapters 1–5 → References → Annexure/Appendix.

Front matter is `[PLANNED]` — Progress_Tracker records 0%. Write it after the full draft is
stable.
