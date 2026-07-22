# Evaluation Metrics: Definitions, Formulas, and Tooling

Companion to Chapter 4 (`07_Thesis/Chapter_4/Chapter_4.md`) and `Experimental_Design.md`. **Planned, not run.** Every metric below is defined precisely enough to be recomputed from a run's output artifacts in `results/`.

Notation: for a run, let each case _i_ produce a prediction and, where relevant, a set of retrieved evidence items and a set of generated claims. Aggregate metrics are computed over the evaluation split defined in the cohort manifest.

---

## 1. Task accuracy (diagnosis and QA)

**Top-k accuracy (T5, diagnosis support).** A case counts as correct if any recorded discharge diagnosis appears in the framework's top-_k_ ranked differential.

$$\text{Top-}k\text{ Acc} = \frac{1}{N}\sum_{i=1}^{N} \mathbb{1}\!\left[\, y_i \in \hat{D}_i^{(k)} \,\right]$$

where $\hat{D}_i^{(k)}$ is the top-_k_ predicted differential and $y_i$ the reference diagnosis set. Report at k = 1, 3, 5.

**Mean reciprocal rank (T5).** Rewards ranking the correct diagnosis higher.

$$\text{MRR} = \frac{1}{N}\sum_{i=1}^{N} \frac{1}{\text{rank}_i}$$

where $\text{rank}_i$ is the position of the first correct diagnosis (∞ → reciprocal 0 if absent).

**MedQA accuracy (C1, control).** Plain multiple-choice accuracy against the answer key [jin2021medqa].

$$\text{Acc} = \frac{\#\text{correct}}{\#\text{questions}}$$

*Tooling:* exact-match scorer for MedQA; a diagnosis-normalization step (mapping free-text differentials to a coding vocabulary) for T5, applied identically across configs. Reference-standard noise on T5 is a known limitation (Chapter 4, §4.8), which is why C1 is reported alongside.

---

## 2. Factual grounding / hallucination

**Faithfulness (RAGAS-style).** Decompose each generated output into atomic claims; a claim is *supported* if it can be entailed from the evidence the framework retrieved for that case. Faithfulness is the supported fraction [es2024ragas].

$$\text{Faithfulness}_i = \frac{\#\text{supported claims}_i}{\#\text{total claims}_i}, \qquad \text{Faithfulness} = \frac{1}{N}\sum_{i=1}^{N}\text{Faithfulness}_i$$

*Tooling:* an LLM-as-judge performs claim decomposition and entailment checking against retrieved evidence, following a fixed rubric; a human spot-check subsample validates the judge. **Caveat:** faithfulness rewards claims grounded in retrieved evidence even when that evidence is wrong, so it is always reported next to task accuracy, never alone.

---

## 3. Risk prediction

**AUROC.** Area under the ROC curve; probability a random positive is ranked above a random negative. Reported for T1–T4 against CLIN (logistic regression) and CLIN-SOFA [vincent1996sofa].

**AUPRC.** Area under the precision–recall curve; reported explicitly because positive classes are rare and AUROC flatters models on imbalanced data. The no-skill AUPRC baseline equals the positive prevalence and is reported for context.

*Tooling:* standard implementations; scores computed on held-out patient-level split. CIs via patient-level bootstrap (§7).

---

## 4. Safety

**Unsafe-recommendation rate (T6), pre/post verification.** Fraction of cases whose recommendation violates a guideline or the safety rubric, measured on the pre-verification output and on the post-verification output.

$$\text{Unsafe} = \frac{\#\text{cases with} \geq 1 \text{ unsafe recommendation}}{N}$$

The reported quantity of interest is the **pre→post reduction**, which attributes safety to the Verification agent (RQ3):

$$\Delta_{\text{safety}} = \text{Unsafe}_{\text{pre}} - \text{Unsafe}_{\text{post}}$$

*Tooling:* rubric-based adjudication; clinician review on the treatment task; an LLM pre-screen may triage cases but does not decide the final label. Rubric shares failure modes with the judge — a stated construct-validity limitation.

---

## 5. Explainability (clinician study)

**Likert ratings, n = 3–5 reviewers.** Each reviewer rates each sampled explanation on two 5-point scales: **faithfulness** (does the explanation reflect the actual basis for the recommendation?) and **usefulness** (would it aid a clinical decision?) [rasheed2022explainable].

$$\bar{s}_{\text{dim}} = \frac{1}{N_s \cdot R}\sum_{i=1}^{N_s}\sum_{r=1}^{R} s_{i,r}^{\text{dim}}$$

for $N_s$ sampled explanations and $R$ reviewers. Report per-dimension means, distributions, and **inter-rater agreement** (e.g., Krippendorff's α or weighted κ) [hayes2007krippendorff].

*Caveat:* with n = 3–5, results are indicative only; the study can surface gross differences and qualitative problems but not support strong quantitative claims (Chapter 4, §4.5, §4.8).

---

## 6. Trustworthiness

**Expected calibration error (ECE).** Bin predicted probabilities into $M$ bins; ECE is the weighted average gap between confidence and accuracy [guo2017calibration].

$$\text{ECE} = \sum_{m=1}^{M} \frac{|B_m|}{N}\,\bigl|\,\text{acc}(B_m) - \text{conf}(B_m)\,\bigr|$$

Reported on risk tasks T1–T4. A reliability diagram accompanies each ECE value. Lower is better; a confidence score that does not track true probability is dangerous in a clinical setting regardless of AUROC.

**Audit-log completeness.** Fraction of decisions for which the framework emitted a complete, replayable trace (retrieved evidence + agent actions + verification outcome + final decision) [jimenez2023trustworthy].

$$\text{Completeness} = \frac{\#\text{decisions with complete trace}}{\#\text{decisions}}$$

*Tooling:* automated schema check over the emitted trace against a required-fields specification.

---

## 7. Runtime and cost

**End-to-end latency.** Wall-clock time per case from input ingestion to final verified decision. Report median and interquartile range per configuration; the tail matters for a monitoring setting, so p95 is also reported.

**Cost per case.** Estimated monetary cost per case (token usage × model price, plus any tool/retrieval cost), reported per configuration so accuracy gains can be weighed against what they cost to obtain.

*Rationale:* a configuration that improves faithfulness at many times the latency and cost of B1 may be clinically impractical; runtime is a first-class outcome, not an afterthought.

---

## 8. Statistical tooling (applies to all metrics)

- **Confidence intervals:** 95%, bootstrap resampled **over patients** (not predictions), to respect within-patient correlation.
- **Paired significance tests** on the shared cohort: DeLong for AUROC differences [delong1988comparing]; McNemar or paired bootstrap for classification and faithfulness differences [dietterich1998approximate].
- **Multiple comparisons:** Benjamini-Hochberg FDR over the pre-registered confirmatory hypotheses only [benjamini1995controlling]; exploratory p-values reported uncorrected and labeled.
- **Underpowered results** are reported as "inconclusive at this cohort size" rather than as null effects.
- **Repeated runs:** headline configurations run multiple times to quantify LLM output variability; variability is reported alongside point estimates.
