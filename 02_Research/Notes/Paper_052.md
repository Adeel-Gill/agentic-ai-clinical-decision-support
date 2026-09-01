# Paper 052

## Basic Information
- **Title:** Holistic Evaluation of Large Language Models for Medical Tasks with MedHELM
- **Authors:** Suhana Bedi, Hejie Cui, Miguel Fuentes, Alyssa Unell, Michael Wornow, et al. (79 authors; Stanford-led)
- **Year:** 2026 (published online 2026-01-20)
- **Venue:** Nature Medicine 32(3):943–951
- **DOI:** 10.1038/s41591-025-04151-2
- **Link:** https://www.nature.com/articles/s41591-025-04151-2 (open PMC copy: PMC13267972)
- **PDF:** `02_Research/Papers/LLM_Healthcare/P052_MedHELM_Holistic_Evaluation_of_LLMs_for_Medical_Tasks.pdf` (arXiv:2505.23802)
- **Verified:** 2026-08-13 against the PMC record and PubMed 41559415; full text read.
- **Author-network note:** Bedi/Cui/Unell/Shah — same Stanford cluster as TIMER (P049, Cui first author), MedAgentBench (P022), the MIMIC-IV revisit ecosystem, and black2026nonclinician (which maps usage onto this taxonomy). Weigh evidence independence accordingly.

## Abstract Summary (200–300 words)
MedHELM extends the HELM evaluation framework to medicine, arguing that near-perfect licensing-exam scores say little about real clinical work. It contributes three things. First, a clinician-validated taxonomy of medical LLM applications: 5 categories (clinical decision support; clinical note generation; patient communication and education; medical research assistance; administration and workflow), 22 subcategories, and 121 tasks. Validation used 29 clinicians from 14 specialties across 4 institutions: 96.7% of subcategories were correctly assigned to their intended categories, mean comprehensiveness 4.21/5, and 107 comments expanded the task set from 98 to 121. Second, a suite of 37 benchmarks covering all 22 subcategories — 19 existing, 5 reformulated, 13 newly built (12 of the new ones EHR-based); 16 public, 7 gated, 14 private; roughly a third use real EHR data from Stanford Health Care and partners. Third, an evaluation of 9 frontier LLMs. Closed-ended tasks use exact match; open-ended tasks use a three-model LLM jury scoring accuracy, completeness, and clarity, validated against 20 clinicians on 56 instances (ICC 0.47, matching clinician–clinician agreement of 0.43 and exceeding ROUGE-L at 0.36 and BERTScore-F at 0.44); jury composition robustness >0.85 correlation across seven judge combinations. Reasoning models led (DeepSeek R1 and o3-mini, 66% win rate), with Claude 3.5 Sonnet comparable at lower cost. Models scored best on note generation (0.74–0.85) and patient communication (0.76–0.89), worst on administration/workflow (0.53–0.63) and quantitative record tasks (medical calculation, EHR SQL, ICD-10 coding). General-benchmark rank poorly predicted medical rank (Gemini 2.0 Flash dropped 42 percentile points). Evaluation cost $805–$1,850 per model.

## Research Problem
- Exam-style benchmarks saturate and do not reflect the breadth of clinical work; no shared, clinically grounded taxonomy existed for organizing what medical LLM evaluation should cover.

## Proposed Solution
- A clinician-validated task taxonomy + benchmark suite mapped onto it + a validated LLM-jury protocol for open-ended medical text, packaged in the open-source HELM infrastructure with a public leaderboard.

## Core Analysis (capability dimensions)
- **Memory:** not evaluated; notably, the authors could not run small local models on long patient timelines because memory requirements exceeded available hardware.
- **Planning / Reasoning:** reasoning-optimized models win overall, but the framework evaluates outputs, not reasoning processes.
- **Tool use:** not evaluated — and the worst results are exactly where tools would help (calculation, SQL, coding), which the authors do not operationalize.
- **Multi-agent:** no.
- **RAG:** no retrieval grounding evaluated.
- **Healthcare:** yes — the point of the paper; ~12 benchmarks on real EHR data.
- **Trustworthy AI:** partially — rubric dimensions include accuracy/completeness/clarity, but the framework "does not systematically assess model calibration or uncertainty quantification" (author-stated).

## Evaluation
- 9 models × 37 benchmarks; win-rate (pairwise) + macro-average per category; LLM-jury for 13 open-ended benchmarks; cost accounting per model.

## Strengths
- Taxonomy validation is real methodology (29 clinicians, quantified agreement), not decoration.
- First large benchmark suite to reach beyond exam QA into EHR-grounded tasks at scale.
- LLM-jury honestly benchmarked against clinician agreement rather than asserted; robustness across judge combinations tested.
- Cost transparency and open infrastructure (leaderboard, HELM codebase).

## Limitations (author-stated and from critical reading)
- Jury validated on only 2 of 13 open-ended benchmarks; ICC 0.47 is a low absolute ceiling (human–human is 0.43 — agreement in this domain is weak, full stop).
- Judge circularity: jurors are drawn from the evaluated frontier-model pool; combination-robustness mitigates ranking instability, not family-level self-preference.
- 14/37 benchmarks private → a large fraction of the leaderboard is not externally reproducible; 15/22 subcategories have a single benchmark.
- No calibration, uncertainty, or safety assessment; no human or task-specific ML baselines (cf. lovon2025mimic on tabular baselines).
- Static, single-turn evaluation: no agents, no longitudinal tracking, no verification of outputs against source records.

## Research Gap (what it does NOT do for longitudinal patient monitoring)
- MedHELM scores answers, not conduct: nothing in it follows a patient over time, verifies a recommendation against retrieved evidence, measures an audit trail, or assesses calibrated confidence — the framework's own limitations section concedes the calibration/uncertainty half of this explicitly.

## How This Supports My Thesis
- **Adopt:** the LLM-jury protocol with clinician-agreement validation (ICC framing included) as the methodological precedent for the Chapter 4 rubric-graded recommendation-quality metric (alongside arora2025healthbench and jiang2025medagentbench); the taxonomy as the map for stating which cell of medical-LLM evaluation the thesis's tasks occupy (clinical decision support).
- **Evidence for design choices:** worst model performance sits on quantitative record work — direct support for the validated-tool delegation principle (liu2025riskagent; gao2025txagent) in the framework's agents.
- **Contrast (gap):** completes the 2.11.5 evaluation triad and sharpens it — even the broadest medical evaluation framework measures static answers on (mostly) single time points, with calibration, uncertainty, longitudinal tracking, verification, and audit faithfulness all outside its scope.
- **Cite at:** §2.11.5 (evaluation instruments), Chapter 4 evaluation-protocol design when written (LLM-jury + rubric metric), Evaluation_Metrics.md when the rubric metric is specified.

## Relevance Score
**8/10** — the benchmark-taxonomy backbone for the evaluation thread of Chapter 2 and the strongest published precedent for the thesis's LLM-jury/rubric evaluation methodology; zero overlap with the thesis's longitudinal/verification/audit contributions, which its own limitations section leaves open.
