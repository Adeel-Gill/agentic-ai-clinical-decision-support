# LITERATURE REVIEW

Chapter 2 and `02_Research/` are governed here. The standard is **analytical, not descriptive**.

---

## 1. The failure mode this file exists to prevent

> ✗ "Paper X proposed A. Paper Y proposed B. Paper Z proposed C."

This is a catalogue, not a review. It scores badly on originality, matches every other paper's
description of the same systems (similarity risk), and shows no judgment.

> ✓ "Existing approaches increasingly combine retrieval, reasoning, and multi-agent
> collaboration; these capabilities are generally evaluated independently rather than within a
> longitudinal patient-monitoring workflow [tang2024medagents; zhao2025medrag;
> jiang2025medagentbench]."

Organize by **theme, capability, and disagreement** — not by paper. A paper may appear in
several places; it need not have its own paragraph anywhere.

## 2. The nineteen analysis dimensions

Every paper in this project is analyzed on the same schema. It is the column set of
`02_Research/Literature_Matrix/Literature_Matrix.md` and the heading set of the newer notes
(`02_Research/Notes/Paper_021.md` onward):

| # | Dimension | What to record |
|---|---|---|
| 1 | Research problem | What the authors say is broken |
| 2 | Proposed solution | Their answer, in one sentence |
| 3 | Architecture | Structure; pipeline vs agentic vs monolithic |
| 4 | Memory | Type, persistence, whether patient-longitudinal |
| 5 | Planning | Decomposition, sequencing; or "not a core focus" |
| 6 | Reasoning | CoT / ReAct / reflection / none |
| 7 | Tool use | Dynamic tool calling, or fixed components |
| 8 | Multi-agent | Topology, roles, communication |
| 9 | RAG | Corpus grounded in *what* — guidelines, literature, or the patient |
| 10 | Healthcare relevance | Real clinical task, or benchmark proxy |
| 11 | Trustworthy AI | Verification, calibration, audit, safety |
| 12 | Evaluation | Benchmark, data, metrics, and whether data are real |
| 13 | Limitations | Authors' stated limits and the ones they omit |
| 14 | Research gap | What remains open after this paper |
| 15 | Relevance to thesis | Comparator? precedent? method to borrow? |
| 16 | Novelty / key innovation | The one thing that is genuinely new |
| 17 | Key contributions | Their claimed contributions |
| 18 | Important quotes | Short, exact, page-located, quote-marked |
| 19 | References | Works to follow up |

"Not a core focus" is an honest and frequent answer. Do not manufacture a memory story for a
paper that has none.

## 3. Writing analytical review prose

For each named system, three moves:

1. **What it does** — one sentence, cited, in your own words.
2. **What it establishes** — the finding the thesis can build on.
3. **What it does not do** for longitudinal patient monitoring — the critical sentence.

Then **compare across systems** rather than listing them:

- Where do they agree? (Tool-augmented medical reasoning works — TxAgent, RiskAgent, MedRAX.)
- Where do they diverge? (Retrieval grounded in guidelines vs. in the record.)
- What does no one do? (Recommendation-level verification with a *measured* audit trail.)

## 4. Recency requirement

The supervisor's 26 July 2026 action item was explicit: the review must foreground **2025 and
2026** work. The repository holds P021–P050 for exactly this reason
(`02_Research/Literature_Matrix/Literature_2025_2026.md`, Chapter 2 §2.11).

Rules:

- Any claim about the state of the field must engage with the 2025–2026 papers, not stop at
  2023–2024 classics.
- Foundational works (ReAct, RAG, MIMIC-IV, CoT) stay — they are foundations, not currency.
- If a claim about "no existing system does X" is made, it must survive a check against
  P021–P050. The five longitudinal-EHR systems (CliCARE, Traj-CoA, TrajOnco, TIMER, RGAR) are
  the closest prior work and the most dangerous to overlook.

## 5. Solved / partially solved / open

`02_Research/Research_Gap.md` uses this three-way sort. Maintain it. A gap claim is only
credible if the review has explicitly conceded what the field *has* settled:

- **Effectively solved** — tool-augmented medical reasoning; agent interoperability protocols;
  guideline-grounded RAG.
- **Partially solved** — realistic evaluation (MedAgentBench, HealthBench are synthetic;
  revisited MIMIC-IV is one-shot); longitudinal reasoning (AMIE on scripted visits);
  prospective deployment (COMPOSER-LLM, one narrow task); safety measurement (general
  propensity, not per-recommendation entailment).
- **Still open — claimed by this thesis** — patient-timeline retrieval as a first-class corpus;
  longitudinal evaluation on real ICU records; recommendation-level verification paired with a
  *measured* audit trail.

Conceding ground makes the remaining claim stronger, not weaker.

## 6. Canonical files and their roles

| File | Role |
|---|---|
| `02_Research/Papers/<Category>/` | PDFs, six categories |
| `02_Research/Notes/Paper_nnn.md` | Per-paper analysis; the project's record of what a paper says |
| `Literature_Matrix/Literature_Matrix.md` | 50 rows × 19 columns |
| `Literature_Matrix/Comparative_Analysis_Table.md` | General vs **differentiating** capabilities |
| `Literature_Matrix/Research_Gap_Matrix.md` | Theme → current state → limitation → gap → contribution |
| `Literature_Matrix/Taxonomy.md` | Capability-dimension mapping |
| `Literature_Matrix/Literature_2025_2026.md` | The recency update summary |
| `Literature_Matrix/Recommended_Additional_Papers.md` | Cited-but-not-yet-in-matrix works |
| `07_Thesis/Compiled/Chapter_2.md` | **Canonical** Chapter 2 — de-AI'd, cited, renumbered |
| `07_Thesis/Chapter_2/*_Revised.md` | Revised sections; canonical over their originals |
| `07_Thesis/Chapter_2/*.md` (unrevised) | Superseded drafts — do not extend, do not cite from |

**Before editing any Chapter 2 file, check whether a `_Revised` or `Compiled` sibling exists.**
Editing the superseded original is wasted work.

## 7. Two note templates exist

- **P001–P020** use an older schema (Motivation / Core Concepts / Strengths / Relevance Score /
  Final Verdict). Leave them; do not retrofit unless asked.
- **P021 onward** use the 19-dimension schema above. **New notes use this one.**

Note quality bar: the abstract summary is 200–300 words in your own words. Near-verbatim
abstract text is a recorded single-source plagiarism risk in Paper_003, 004, 005, 016, 017,
and 019 — do not add more, and never carry that text into thesis prose.

## 8. The comparative table is the gap's proof

`Comparative_Analysis_Table.md` carries two blocks:

- **General capabilities** — nearly every system ticks every box. This is exactly why "we
  integrate memory, planning, reasoning, and multi-agent collaboration" is a weak novelty claim.
- **Differentiating capabilities** — patient-timeline RAG · dedicated verification gate ·
  longitudinal memory · real ICU data · faithful audit trail. No prior row carries more than one.

Rules for this table:

- Every ❌ must be defensible. The file already documents its honest ratings (MetaGPT and Agent
  Hospital *do* have some persistent memory; MedRAG *does* retrieve from EHR databases). Keep
  that paragraph — without it the table is a strawman.
- If a new paper ticks one of the five differentiating columns, **add the row and say so**.
  Suppressing a competitor is fabrication by omission.
- The 2025–2026 longitudinal-EHR systems (CliCARE, Traj-CoA, TrajOnco, TIMER, RGAR) are the
  strongest current challengers and are already analyzed in Notes 046–050. Any gap claim must
  be checked against them explicitly.

## 9. Adding a paper — the seven-step chain

Incomplete integration is worse than no integration; see [WORKFLOW.md](WORKFLOW.md)
"Special workflow: adding a new paper". Short form:

PDF → note → matrix row → taxonomy → `References.bib` → style-guide key table →
`build_thesis_docx.py` IEEE dict → only then cite in prose.

Skipping the last step is a live defect in this repository (`.ai/README.md` D1).
