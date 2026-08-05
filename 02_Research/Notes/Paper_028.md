# Paper 028

## Basic Information
- **Title:** HealthBench: Evaluating Large Language Models Towards Improved Human Health
- **Authors:** Rahul K. Arora, Jason Wei, Rebecca Soskin Hicks, Preston Bowman, Joaquin Quiñonero-Candela, Foivos Tsimpourlas, et al. (OpenAI)
- **Year:** 2025
- **DOI:** 10.48550/arXiv.2505.08775
- **Venue:** arXiv preprint (arXiv:2505.08775)
- **Publisher:** OpenAI (arXiv)
- **Link:** https://arxiv.org/abs/2505.08775

## Abstract Summary (200–300 words)
**HealthBench** is an open-source benchmark for measuring the performance and safety of LLMs in healthcare. It consists of **5,000 realistic multi-turn conversations** between a model and either an individual user or a healthcare professional, where the task is to respond to the final user message. Rather than multiple-choice or short-answer scoring, HealthBench uses **conversation-specific, physician-written rubrics** — 48,562 unique criteria authored by **262 physicians** who have practiced across 60 countries and 26 specialties. Each criterion has a point value between -10 and 10, and a **model-based grader** (validated against physician judgment) checks each criterion independently, summing points and normalizing by the maximum. Examples are organized into **seven themes** (emergency referrals, context-seeking, global health, health data tasks, expertise-tailored communication, responding under uncertainty, response depth) and **five behavioral axes** (accuracy, completeness, communication quality, context awareness, instruction following). Results show rapid recent progress: GPT-3.5 Turbo 16%, GPT-4o 32%, and o3 60%; smaller models improved dramatically (GPT-4.1 nano beats GPT-4o at ~1/25 the cost). The authors release two variants: **HealthBench Consensus** (34 physician-consensus-validated criteria) and **HealthBench Hard** (1,000 hard examples where the top score is only 32%). Human-baseline experiments show recent models outperform unassisted physicians, and physicians could not improve on April-2025 model responses. A **meta-evaluation** finds model-physician grading agreement comparable to physician-physician agreement, supporting the benchmark's trustworthiness. Substantial headroom remains, particularly in worst-case reliability and context-seeking.

## Research Problem
- Existing health LLM evaluations fall short on three dimensions: **meaningful** (multiple-choice/narrow exams poorly reflect real workflows), **trustworthy** (not validated against expert opinion), and **unsaturated** (no headroom to drive progress).
- Need a realistic, expert-grounded, extensible standard to measure whether LLMs perform well and behave safely in diverse high-stakes health situations.

## Proposed Solution
- A large-scale **rubric-based benchmark** of realistic conversations graded against per-conversation physician-written criteria, with a validated model-based grader; plus Consensus and Hard variants and a meta-evaluation of grader trustworthiness.

## Architecture
- Not a system architecture paper; the "architecture" is the evaluation pipeline: conversation + physician rubric → model produces response → **model-based grader** scores each criterion independently → normalized per-example score → aggregated overall score, stratified by theme and axis.

## Memory
- Not applicable; conversations are up to 19 turns but there is no persistent cross-conversation memory. Evaluates single model responses to multi-turn contexts.

## Planning
- Not a focus; no agentic planning is evaluated. Themes like context-seeking implicitly probe whether a model plans to gather missing information.

## Reasoning
- Evaluates reasoning quality indirectly via accuracy and "responding under uncertainty"; reasoning models (o3) score notably higher (60%), showing reasoning benefits health-task performance.

## Tool Use
- Not a focus; the benchmark tests plain conversational responses without external tools. The grader itself is a tool (model-based classifier) used for evaluation, not by the evaluated models.

## Multi-Agent
- No. Single-model responses are evaluated; no multi-agent systems are tested or built.

## RAG
- Not a focus; models respond from parametric knowledge. Some HealthBench data derives from HealthSearchQA (frequently-searched queries) but no retrieval augmentation is part of the task.

## Healthcare Contribution
- A meaningful, trustworthy, unsaturated **open benchmark** grounded in 262 physicians' judgment across 60 countries — a shared standard for safe, beneficial health LLMs.
- Seven themes cover high-stakes real-world tasks (emergency referrals, global health, **health data tasks** such as drafting documentation and clinical decision-support), directly relevant to clinical workflows.
- Released openly via OpenAI simple-evals with Consensus and Hard variants for continued progress.

## Trustworthy AI
- **Trustworthiness is a first-class design goal and is explicitly measured** via meta-evaluation: model-physician grading agreement (~55–75%) is comparable to physician-physician agreement.
- Safety-oriented criteria (negative point values for harmful behavior; emergency-referral escalation criteria; over/under-escalation both penalized).
- Reliability/worst-case analysis: even frontier models are unreliable in worst-case; consensus criteria give higher-precision failure detection.
- Physician red-teaming contributes examples targeting model weaknesses.

## Evaluation
- 5,000 conversations, 48,562 rubric criteria, mean 11.5 criteria/example, mean 2.6 turns.
- Frontier scores: GPT-3.5 Turbo 16% → GPT-4o 32% → o3 60%; GPT-4.1 nano beats GPT-4o at ~25x lower cost; HealthBench Hard top ~32%.
- Human baselines: models beat unassisted physicians; physicians improved Sept-2024 model responses but not April-2025 ones.
- Stratified reporting by theme and axis; reliability via worst-of-k analysis; meta-evaluation with macro-F1 across grader models.

## Research Gap
- Prior medical benchmarks are narrow (exam questions), saturated, or weakly validated against diverse expert judgment — HealthBench targets all three.
- HealthBench itself evaluates **single model responses**, not full multi-response workflows, and does **not measure downstream health outcomes**; example-specific (non-consensus) criteria are not multi-physician-validated.

## Key Contributions
- 5,000-conversation, 48,562-criterion physician-authored rubric benchmark across 7 themes and 5 axes.
- HealthBench Consensus (34 consensus criteria) and HealthBench Hard (1,000 hard examples).
- Meta-evaluation validating the model-based grader against physicians.
- Human-baseline study and cross-model progress/cost/reliability analysis; open data and code.

## Limitations
- Grading of consensus criteria shows inherent physician disagreement (55–75% agreement); example-specific criteria not cross-validated.
- Physician-written response baseline is an unusual task for physicians; interpret with caution.
- Does not evaluate specific deployed workflows or measure real health outcomes; captures today's interaction distribution, which will shift.

## Important Quotes
- "model-physician agreement is similar to physician-physician agreement" (Contributions / Section 8)
- "no model we evaluated scored above 32%" on HealthBench Hard (Section 3)

## Thesis Relevance
- Provides a rigorous template for the thesis's **rubric-based, physician-grounded evaluation** and its **model-grader meta-evaluation** — directly usable for evaluating verification-gate faithfulness (gap 3).
- Confirms thesis gap (1): reinforces that exam-style QA benchmarks are saturated/unrepresentative, motivating evaluation on realistic longitudinal ICU records rather than MCQs.
- The "health data tasks" theme (documentation, decision support) and "emergency referrals" theme align with the thesis's clinical-decision-support and patient-monitoring goals.
- Its safety framing (negative-point harmful behaviors, escalation criteria, worst-case reliability) informs the thesis's human-in-the-loop and audit-trail safety metrics.
- HealthBench evaluates single-turn responses without memory/tools/multi-agent structure — highlighting the thesis's differentiators (persistent memory, tool verification, multi-agent orchestration).
- Reasoning models scoring far higher supports the thesis's use of ReAct-style reasoning agents.

## References
- Singhal, K., et al. "Large language models encode clinical knowledge." (Med-PaLM / HealthSearchQA source).
- Pfohl, S. R., et al. "A toolbox for surfacing health equity harms and biases in large language models." (physician red teaming).
- Nori, H., et al. "Capabilities of GPT-4 on medical challenge problems." (2023).
- Fleming, S. L., et al. "MedAlign: real-world clinician-instruction evaluation." (realistic workflow evaluation).
- Scale AI. "VISTA" / Starace et al. "PaperBench" / Lin et al. "WildBench" (rubric-based grading precedents).
