# Paper 045

## Basic Information
- **Title:** Human–large language model collaboration in clinical medicine: a systematic review and meta-analysis
- **Authors:** Guoyong Wang, Kaijun Zhang, Jiyue Jiang, Chaonan Wang, Hui Bi, Haojun Liang, et al.
- **Year:** 2026
- **DOI:** 10.1038/s41746-026-02382-2
- **Venue:** npj Digital Medicine (2026) 9:195, Article
- **Publisher:** Nature Portfolio (Springer Nature)
- **Link:** https://www.nature.com/articles/s41746-026-02382-2

## Abstract Summary (200–300 words)
This **PRISMA 2020** systematic review and meta-analysis (PROSPERO CRD420251068272) rigorously tests whether **human + AI (H+AI) collaboration** with LLMs actually outperforms human-only (H) clinical workflows, moving beyond the a priori assumption that collaboration is inherently beneficial. Searching MEDLINE, Embase, Cochrane Library, and Web of Science through June 28, 2025, the authors included **ten peer-reviewed studies** (nine RCTs, one non-randomized; three medRxiv preprints for sensitivity analyses only), spanning diagnostic reasoning, ICU/critical-illness differential diagnosis, radiologic and electrodiagnostic interpretation, documentation, and cross-disciplinary communication, using GPT-4/ChatGPT, AMIE, DeepSeek-R1, and PEACH. Pooled results are sobering: diagnostic/interpretation accuracy (k=2) showed a directionally positive but non-significant risk ratio of **1.59 (95% CI 0.08–32.74)** with prediction intervals crossing the null; composite diagnostic/management scores (k=2) improved significantly by **+4.88 percentage points** (95% CI +0.65 to +9.12) but with an extremely wide prediction interval (−31.65 to 41.42); time efficiency (k=3) showed **no overall difference** (+0.40 min; I²=70.1%). Documentation quality improved, yet **factual error rates of ~26–36%** undermined the gains. Critically, three-arm studies revealed a **"collaboration paradox"**: H+AI did not universally outperform AI-only (synergy ratio ≈ 1), while AI-only underperformed humans in EMG reporting — collaboration value depends on task, interface, training, and workflow embedding. GRADE certainty ranged from very low to moderate; most evidence came from "near-clinical" simulations rather than real workflows. The authors propose a **2×2 task complexity/structure framework** for deployment, recommend clinicians shift from information generators to **expert verifiers**, and call for preregistered pragmatic multicenter trials with harmonized safety/error-focused core outcomes and interfaces that surface uncertainty and support verification.

## Research Problem
- Most prior research evaluates LLMs' **standalone diagnostic capability** or head-to-head AI-vs-clinician comparisons; direct comparisons of **H+AI versus H and/or AI-only** on clinical task performance are scarce.
- Early RCT evidence is mixed, and a prior 106-study meta-analysis found human–AI teams often perform **worse than the best single agent** (Hedges' g = −0.23), so when and how collaboration adds value is unknown.
- Institutions are deploying "co-pilot/centaur" collaboration models on the untested assumption that keeping a human in the loop guarantees safety and benefit.

## Proposed Solution
- Not a system paper: a **systematic review and meta-analysis** directly comparing H+AI vs H (and AI-only where available), with common-effect and random-effects models (Paule–Mandel τ², **HKSJ adjustment** for small k), 95% prediction intervals, RoB 2/ROBINS-I risk-of-bias appraisal, and GRADE certainty rating.
- A deployment-guiding **2×2 framework** (task complexity × task structure): collaborative value is greatest for high-complexity/low-structure tasks (ambiguous differentials) and minimal for low-complexity/high-structure tasks (templated documentation).
- Recommendations for task-differentiated workflows: AI-only with "human-on-exception" oversight for structured low-variance tasks; deliberately engineered teaming with uncertainty display, traceable evidence chains, and mandatory verification for high-stakes ambiguity.

## Architecture
- Not a core focus; the reviewed interventions are chat/assistant interfaces (ChatGPT/GPT-4, AMIE, DeepSeek-R1, PEACH LLM-CDSS) embedded in clinician workflows rather than novel agent architectures.

## Memory
- Not a core focus; none of the pooled studies involve persistent patient memory, and longitudinal designs (skill retention, de-skilling) are flagged only as future research.

## Planning
- Not a core focus; no planning mechanisms are analyzed — the unit of analysis is the clinician–LLM workflow, not agent internals.

## Reasoning
- Reviewed tasks center on **diagnostic reasoning and multistep management** (composite reasoning scores, DDx accuracy), and the discussion analyzes cognitive mechanisms — anchoring on incorrect AI suggestions, automation and confirmation bias, cognitive dissonance — that break human–AI reasoning synergy.

## Tool Use
- Not a core focus; the LLM itself is the tool used by clinicians, with role delineation advice (AI handles retrieval and recall; clinicians ensure calibration and gatekeeping).

## Multi-Agent
- Not a core focus; the "team" studied is human + single AI system, not multi-agent LLM architectures.

## RAG
- Not a core focus; retrieval-augmented systems are not separately analyzed, though AI's "retrieval, computation, and information-integration capabilities" motivate the collaboration-first narrative.

## Healthcare Contribution
- First meta-analytic synthesis dedicated to **LLM-enabled H+AI vs human-only clinical workflows**, covering diagnosis, triage, ICU DDx, imaging, EMG reporting, documentation, and communication.
- Establishes the **collaboration paradox** in clinical settings: human-in-the-loop is not a universal safeguard and can introduce new failure modes (anchoring on wrong AI advice, diluting strong AI outputs via inconsistent overrides).
- Documents that documentation-quality gains coexist with **~26–36% factual error rates**, dissociating structural quality from factual correctness.
- Real-world pragmatic deployment (PEACH perioperative study) showed near-null efficiency effects, warning that simulated-task gains may not translate to complex clinical workflows.

## Trustworthy AI
- Recommends **safety-critical metrics** (user error detection/correction rates, hallucination rates) as primary endpoints instead of trading efficiency for safety.
- Prescribes guardrails for diagnostic/triage use: **uncertainty disclosure, de-anchoring mechanisms, mandatory review**, tiered enablement by seniority, plus governance, audit, and traceability to support the clinician's "vigilance tax".
- Uses GRADE transparency: low certainty for accuracy, moderate for composite scores, very low/low for time — explicitly cautioning against overgeneralization.

## Evaluation
- 1235 records screened; 10 peer-reviewed studies pooled (8 two-arm, 2 with AI-only arms); 3 preprints in sensitivity analyses only.
- Effects: accuracy RR 1.59 (95% CI 0.08–32.74; I²=63.8%); composite scores MD +4.88 pp (95% CI +0.65 to +9.12; PI −31.65 to 41.42); time MD +0.40 min (95% CI −4.18 to +4.97; I²=70.1%).
- Methods: Paule–Mandel random effects with HKSJ CIs, prediction intervals, Luo/Wan median-to-mean conversion, RoB 2 (2 low risk, 7 some concerns) and ROBINS-I (moderate), GRADE; R 4.5.2 meta package, code on Zenodo.
- Three-arm synergy ratio ≈ 1 (no evidence H+AI beats AI-only); McDuff/AMIE paired study (Top-1 29.2%→59.1%) cited as external consistency but not pooled.

## Research Gap
- Evidence relies on **"near-clinical" simulations** (vignettes, standardized cases) rather than patient-facing trials, severely limiting external validity — real workflows with time pressure and interruptions are untested.
- Small k (≤3 per outcome), heterogeneous endpoints and scales, and unstable variance estimates preclude strong conclusions; publication-bias tests underpowered.
- No harmonized core outcome sets prioritizing safety/error metrics; interfaces supporting traceability and bias mitigation remain undesigned; longitudinal effects (de-skilling, calibration, cost) unstudied.

## Key Contributions
- First PRISMA/PROSPERO meta-analysis isolating the **marginal value of collaboration** (H+AI vs H vs AI-only) for LLMs in clinical medicine.
- Quantified, uncertainty-honest effect estimates showing benefits are **statistically suggestive but highly uncertain and context-dependent**.
- The **collaboration paradox** finding with mechanistic explanation (anchoring, automation bias) and its sociotechnical design implications.
- The **2×2 complexity/structure deployment framework** and the role shift of clinicians to **expert verifiers**.
- Concrete methodological agenda: preregistered pragmatic multicenter trials, core outcome sets emphasizing safety, HCI studies for traceable interfaces, equity analyses, real-time safety monitoring.

## Limitations
- Only 10 studies, several outcomes pooled from just 2 trials; crossover/pre–post designs susceptible to learning and sequence effects; inconsistent blinding.
- Heavy reliance on simulated settings; only one real-clinic pragmatic trial (PEACH) included.
- English-only search; k < 10 prevented formal publication-bias testing; variance estimates unstable despite HKSJ/multiple τ² estimators.
- Heterogeneity in "correctness" definitions, rater composition, model versions, and prompting limits comparability.

## Important Quotes
- "Human–AI collaboration is, fundamentally, a complex sociotechnical process." (Discussion, p. 6)
- "merely placing an AI tool in clinicians' hands does not guarantee consistent net benefit" (Discussion, p. 6)

## Thesis Relevance
- Supplies the strongest evidence base for the thesis's **human-in-the-loop validation layer** — and its most important caveat: HITL is not a universal safeguard, so the thesis must engineer verification workflows (uncertainty display, de-anchoring, mandatory review) rather than merely inserting a clinician.
- Directly supports thesis gap (3): the review calls for interfaces with **traceable evidence chains and verification protocols** — precisely the thesis's verification gate and audit trail evaluated as first-class components.
- Reinforces thesis gap (1): pooled evidence comes from vignettes and simulations, not longitudinal real ICU records — the thesis's MIMIC-IV evaluation answers the review's call for realistic workflow-embedded assessment.
- The ~26–36% factual error rates justify the thesis's decision to treat **verification and hallucination detection** as primary evaluation endpoints, matching the review's recommendation to prioritize safety/error metrics over efficiency.
- The **2×2 task framework** helps position the thesis's ICU monitoring/decision-support tasks in the high-complexity, low-structure quadrant where engineered collaboration adds the most value.
- Its included ICU/critical-illness study (Wu 2025, DeepSeek-R1 DDx) and the collaboration-paradox analysis provide direct comparators and design cautions for the thesis's clinician-facing evaluation.

## References
- Goh, E. et al. "Large language model influence on diagnostic reasoning: a randomized clinical trial." JAMA Netw. Open 7, e2440969 (2024).
- McDuff, D. et al. "Towards accurate differential diagnosis with large language models." Nature 642, 451–457 (2025).
- Vaccaro, M., Almaatouq, A. & Malone, T. "When combinations of humans and AI are useful: a systematic review and meta-analysis." Nat. Hum. Behav. 8, 2293–2303 (2024).
- Hager, P. et al. "Evaluation and mitigation of the limitations of large language models in clinical decision-making." Nat. Med. 30, 2613–2622 (2024).
- Asgari, E. et al. "A framework to assess clinical safety and hallucination rates of LLMs for medical text summarisation." npj Digital Medicine 8, 274 (2025).
