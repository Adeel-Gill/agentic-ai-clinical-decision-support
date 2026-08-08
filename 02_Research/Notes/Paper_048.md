# Paper 048

## Basic Information
- **Title:** TrajOnco: A Multi-Agent Framework for Temporal Reasoning over Longitudinal EHR for Multi-Cancer Early Detection
- **Authors:** Sihang Zeng, Young Won Kim, Wilson Lau, Ehsan Alipour, Ruth Etzioni, Meliha Yetisgen, et al.
- **Year:** 2026
- **DOI:** 10.48550/arXiv.2604.10386
- **Venue:** arXiv preprint arXiv:2604.10386 (submitted 12 Apr 2026)
- **Publisher:** arXiv (work done during first author's internship at Truveta Inc.)
- **Link:** https://arxiv.org/abs/2604.10386

## Abstract Summary (200–300 words)
TrajOnco scales the chain-of-agents-plus-memory recipe (the authors' earlier Traj-CoA) into a **training-free, multi-agent LLM framework for multi-cancer early detection** across 15 cancer types on de-identified **Truveta EHR data** spanning 30+ US health systems (120M+ patients). Patient trajectories — structured conditions, observations, labs, medications, procedures — are converted to a unified time-ordered **XML representation** and split by **time-aware chunking** (16k tokens per chunk). Sequential **worker agents** process chunks, extracting salient cancer-related events into a deduplicated, timestamped **long-term memory (LTM)** and maintaining an evolving summary with low/moderate/high risk assessments and rationale. A **manager agent** synthesizes the final worker summary and the full LTM into a 1-10 risk score, an **evidence-based narrative justification**, and the final set of identified cancer-related events. Prediction targets cancer diagnosis at one year, with a 1-year gap and 6-month washout to isolate early detection from near-term diagnosis. In zero-shot evaluation on 500-case/500-control matched cohorts per cancer, TrajOnco achieves AUROCs of **0.64-0.80** (highest for liver and lung); on a lung cancer benchmark it reaches 0.785, beating a single-agent baseline (0.765) and logistic regression, approaching supervised XGBoost (0.796). Sensitivity analyses show smaller models (GPT-4.1-mini) suffice because the architecture decomposes reasoning; performance scales with trajectory length (0.614 at 2k → 0.789 at 256k tokens); a parallel two-stage variant cuts latency 25% at some cost to summary fidelity. **Human evaluation** of 113 identified events found 90.27% correct (Cohen's kappa 0.72), with errors from temporal or interpretive inaccuracies. LLM-as-a-judge comparisons show the largest advantage in temporal reasoning (68% wins), and topic-model aggregation of summaries recovers clinically established risk-factor themes per cancer.

## Research Problem
- **Multi-cancer early detection** from routine EHRs requires temporal reasoning over subtle, evolving signals across years — supervised ML needs heavy feature engineering and training data, and yields limited interpretability (hazard ratios, SHAP).
- Single-agent LLMs fail on long trajectories due to the **lost-in-the-middle** effect, omitting evolving EHR signals; prior LLM oncology work addressed only short-context tasks.
- Prior EHR early-detection studies relied on single national health systems; multi-system generalization was untested.

## Proposed Solution
- **TrajOnco**: chain-of-agents + long-term memory over time-aware XML chunks, generating per-patient risk scores (1-10), evidence-linked rationales, and identified cancer-related events, zero-shot.
- One shared prompt template generalizes across **15 cancer types** by swapping only the cancer name — no cancer-specific feature engineering or curated knowledge.
- An optional **two-stage variant** adds parallel preprocessor agents that condense chunks before the sequential chain, trading summary fidelity for 25% lower latency.

## Architecture
- Stage one: sequential workers S_i, E_i = W_i(I_W, S_{i-1}, c_i, M[-k:]), each updating a running narrative, risk level, and rationale while appending deduplicated timestamped events to LTM.
- Stage two: manager O = M(I_M, S_C, M) outputs patient-level narrative, final risk score, and final event set — explicitly separating **local signal extraction from global reasoning**.
- Default base model GPT-4.1-mini (Pareto-optimal on cost/latency/AUROC among GPT-4o/4.1/5 families); 16k-token chunks.

## Memory
- Core focus: the **LTM module** stores deduplicated, timestamped risk factors and key events with an intentionally inclusive extraction heuristic, providing the manager a distilled global clinical timeline and preventing forgetting/over-abstraction of early events across long chains.

## Planning
- Not a core focus; workflow is a fixed sequential chain (plus an engineered parallel preprocessing variant), not dynamic agent planning.

## Reasoning
- Progressive **temporal reasoning**: workers interpret temporal patterns and status changes chunk-by-chunk, dynamically updating risk (case study: smoking in 2012 raises baseline; pulmonary nodules + COPD in 2016 escalate to high); LLM-judge results show temporal reasoning is where the multi-agent design most outperforms a single agent (68% vs. 23%).

## Tool Use
- Not a core focus; the discussion proposes integrating tool use, agent skills, and modality-specialized subagents (e.g., for labs) as future work.

## Multi-Agent
- Core focus: worker chain + manager (+ optional parallel preprocessor agents); the paper argues its longitudinal temporal reasoning could enrich otherwise cross-sectional medical multi-agent deliberation frameworks.

## RAG
- Not a core focus; no retrieval component — the full record is processed sequentially, and external knowledge access is left to future work (the framework relies on the LLM's internal knowledge of disease patterns).

## Healthcare Contribution
- Zero-shot risk prediction across **15 solid and hematologic cancers** at 1-year horizon with AUROC 0.64-0.80; comparable to supervised XGBoost on lung cancer without any training.
- Multi-system generalization: Truveta data from 30+ US health systems, 900 hospitals — beyond prior single-system studies.
- **Population-level insight generation**: aggregating patient summaries via TopicGPT-style topic modeling and UMAP recovers established risk-factor themes (e.g., viral hepatitis for liver, GI bleeding/iron-deficiency anemia for colorectal, smoking shared by lung/bladder) and cross-cancer relationships.

## Trustworthy AI
- Strongest element among the trajectory papers: **fidelity of outputs was human-validated** — two annotators (biomedical informatics PhD candidate + MD) judged 90.27% of 113 identified events correct (kappa 0.72), with error taxonomy (temporal inaccuracies, minor hallucinations, overly assertive inferences, lost clinical uncertainty).
- Evidence-linked rationales and extracted events embed interpretability directly in inference; LLM-as-a-judge with position-bias mitigation assesses summary quality.
- Still no automated verification gate: inaccuracies "should be interpreted or used with caution," and validation is a one-off study, not a per-decision mechanism.

## Evaluation
- 15 case-control cohorts (500/500, 1:1 age/sex matched; two-code phenotyping with 6-month washout); primary metric AUROC (0.64-0.80).
- Lung benchmark: TrajOnco 0.785 vs. single-agent 0.765, LR 0.731, KNN 0.584, XGBoost 0.796 (XGBoost trained on 337k patients); unmatched 1:250 cohort AUROC 0.871; stable 0.78-0.80 across visit-frequency quartiles (utilization-intensity check).
- Sensitivity analyses: base model families (GPT-5 gains marginal over GPT-4.1-mini), trajectory length scaling (0.614 → 0.789 from 2k to 256k tokens), two-stage latency/fidelity trade-off, time-gap analysis (0.5-5 years) showing cancer-specific signal evolution.
- LLM-as-a-judge (GPT-5, high reasoning, averaged over both candidate orders) on five dimensions; human fidelity evaluation of events.

## Research Gap
- Fills: interpretable, training-free, generalizable modeling of long trajectories for early detection across many cancers and health systems.
- Leaves open: unstructured data (notes, imaging reports) unused; registry-confirmed outcomes; external knowledge integration; per-decision verification of generated evidence.

## Key Contributions
- A zero-shot **multi-agent + LTM framework** generalizing across 15 cancers with only prompt-level adaptation.
- Demonstration that architecture substitutes for scale: effective temporal reasoning with small models (GPT-4.1-mini) rivaling GPT-5 within the framework.
- **Human-validated output fidelity** (90.27% event correctness) with an explicit error-mode taxonomy.
- Population-level, clinically coherent theme discovery from aggregated agent outputs; favorable scaling with record length.

## Limitations
- Algorithmic (code-based) outcome definition without registry confirmation risks endpoint misclassification.
- Structured data only; clinical notes and imaging reports excluded.
- 1:1 matching does not reflect real incidence; performance may partly reflect documentation volume (cases have longer records), though visit-frequency stratification mitigates the concern.
- Residual hallucinations and lost clinical uncertainty in summaries; sequential chain latency for very long records.

## Important Quotes
- "Of the 113 evaluated events, 102 (90.27%) were annotated as correct." (Sec. 2.3.2, p. 9)
- "This design separates local signal extraction from global reasoning" (Sec. 2.1, p. 4)

## Thesis Relevance
- The nearest prior work to the thesis's **measured audit trail**: TrajOnco human-scores the factual fidelity of its evidence-linked outputs (90.27% event correctness) — but as a one-off validation study of 113 events, not an automated, per-recommendation faithfulness metric as in the thesis.
- The thesis borrows its LTM/timeline design lineage (with P047), its evidence-linked rationale format, and its error taxonomy (temporal vs. interpretive inaccuracies) for designing verification checks.
- Key difference: TrajOnco **compresses the record through sequential agents** rather than retrieving timestamped evidence from the patient's timeline on demand; the whole record must be re-processed per prediction.
- No **recommendation verification gate**: identified events flow directly into the risk narrative with no automated cross-check against source EHR — precisely the hallucination modes it documents (unsupported qualifiers, overconfident inference) are what the thesis's verifier targets.
- Task is risk scoring for screening, not clinical decision support with actionable recommendations and human-in-the-loop validation; data is structured Truveta EHR, not MIMIC-IV ICU records with waveform-adjacent longitudinal signals.
- Its finding that multi-agent decomposition lets small models match large ones supports the thesis's layered-agent economy argument.

## References
- Zhang, Y. et al. "Chain of agents: Large language models collaborating on long-context tasks." NeurIPS 37:132208-132237 (2024).
- Cui, H. et al. "TIMER: Temporal instruction modeling and evaluation for longitudinal clinical records." npj Digital Medicine 8:577 (2025).
- Li, R. et al. "CARE-AD: a multi-agent LLM framework for Alzheimer's disease prediction using longitudinal clinical notes." npj Digital Medicine 8:541 (2025).
- Zhao, W. et al. "An agentic system for rare disease diagnosis with traceable reasoning." Nature (2026).
- Zheng, L. et al. "Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena." arXiv:2306.05685 (2023).
