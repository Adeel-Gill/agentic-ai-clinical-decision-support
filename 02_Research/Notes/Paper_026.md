# Paper 026

## Basic Information
- **Title:** Advancing Conversational Diagnostic AI with Multimodal Reasoning
- **Authors:** Khaled Saab, Jan Freyberg, Chunjong Park, Tim Strother, Yong Cheng, Wei-Hung Weng, et al.
- **Year:** 2025
- **DOI:** 10.48550/arXiv.2505.04653
- **Venue:** arXiv preprint (arXiv:2505.04653)
- **Publisher:** Google DeepMind / Google Research (arXiv)
- **Link:** https://arxiv.org/abs/2505.04653

## Abstract Summary (200–300 words)
This paper extends **AMIE (Articulate Medical Intelligence Explorer)**, Google's LLM-based conversational diagnostic AI, with the ability to gather, interpret, and reason about **multimodal medical data** (smartphone skin photos, ECG tracings, and PDFs/screenshots of clinical documents) during diagnostic conversations. Built on **Gemini 2.0 Flash**, the system implements a **state-aware dialogue phase transition framework** in which conversation flow is dynamically controlled by intermediate model outputs that represent evolving **patient states** — a structured patient profile, an internal evolving **differential diagnosis (DDx)**, and a prioritized list of information gaps. Follow-up questions and multimodal artifact requests are strategically directed by **uncertainty** in these states, emulating the structured history-taking of experienced clinicians. The system progresses through three phases: (1) History Taking, (2) Diagnosis & Management, and (3) Answer Follow-up Questions, ending with a structured post-questionnaire (final DDx, management plan grounded via web search, and salient artifact findings). The authors also built a **simulation environment** with synthetic patient scenarios grounded in real image datasets (SCIN, PAD-UFES-20, PTB-XL, clinical documents), turn-by-turn doctor/patient agent dialogues, and a Gemini-based **auto-rater** that scores DDx accuracy, information gathering, management appropriateness, and **hallucination**. In a randomized, double-blind, OSCE-style study with 25 patient actors across 105 multimodal scenarios (210 consultations, each rated by 3 of 18 specialists), AMIE was superior to primary care physicians (PCPs) on 7 of 9 multimodal-handling axes and on 29 of 32 non-multimodal axes, including top-k diagnostic accuracy (p < 0.001). The authors stress that real-world translation requires substantial further research.

## Research Problem
- LLM-based diagnostic conversation systems have been studied almost exclusively as **text-only chatbots**, deviating from real remote care where patients share **multimodal artifacts** (skin photos, ECGs, lab reports) via messaging platforms.
- Whether LLMs can **request, interpret, and reason about multimodal medical data mid-conversation** — while preserving history-taking quality, diagnostic accuracy, and empathy — had not been investigated or evaluated.
- Text-only input risks diagnostic errors (patients cannot accurately transcribe lab values or describe rashes) and can exacerbate telehealth access disparities.

## Proposed Solution
- **Multimodal AMIE**: a state-aware, inference-time reasoning layer on top of Gemini 2.0 Flash that orchestrates diagnostic conversations across three phases and strategically requests multimodal artifacts when the internal patient state indicates uncertainty or information gaps.
- The authors explicitly argue that for a **safety-critical, dynamic task**, an explicit state-aware system layered on the LLM gives better dialogue control, more reliable tracking of diagnostic state and uncertainty, and more dependable clinical reasoning than sophisticated prompting alone (validated by ablation).

## Architecture
- **Dialogue phase transition controller**: Phase 1 History Taking → Phase 2 Diagnosis & Management (with a DDx validation sub-phase) → Phase 3 Follow-up Questions; transitions are triggered when a decision module (querying Gemini 2.0 Flash) judges the current phase's objectives met.
- **Internal patient state**: a continuously updated structured patient profile (chief complaint, HPI, demographics, symptoms, histories, medications, knowledge gaps), an evolving internal DDx (hidden from the patient), and information-gap-driven question generation.
- **Post-dialogue synthesis**: a structured post-questionnaire (final ranked DDx, management plan grounded with web search, salient artifact findings) serving as a standardized record for evaluation and potential clinical handoff.
- **Simulation environment**: scenario generator (real images + Gemini-imputed clinical metadata), doctor agent vs. patient agent turn-by-turn dialogue, and auto-rater agent.

## Memory
- Not persistent/longitudinal memory; state is **within-consultation**: the evolving patient profile and dialogue history act as a condensed working memory of the encounter, discarded per session. No cross-visit patient memory is modeled.

## Planning
- **State-driven dialogue planning**: a continuation decision module plans whether to keep gathering history or transition phases; targeted question generation plans the next information-gathering action to fill prioritized knowledge gaps and reduce DDx uncertainty.

## Reasoning
- **Uncertainty-directed clinical reasoning**: intermediate DDx and patient-state outputs guide questioning and artifact requests; DDx explanations are explicitly grounded in evidence from the dialogue and multimodal findings (e.g., referencing ST-segment changes on a shared ECG).
- Inference-time reasoning is preferred over fine-tuning: domain SFT improved ECG-specific tasks but degraded management-plan appropriateness (catastrophic-forgetting risk).

## Tool Use
- **Web search tool** used for grounding management plans in current medical knowledge/guidelines and for imputing plausible clinical metadata during scenario generation; multimodal perception of images/documents is native to the base model rather than an external tool.

## Multi-Agent
- Multi-agent structure appears in the **evaluation pipeline** (doctor agent, patient agent, auto-rater agent), not in the deployed diagnostic system itself, which is a single state-aware agent.

## RAG
- Not a core focus; grounding uses web search at management-plan formulation rather than a retrieval-augmented pipeline over a curated corpus or the patient's own record.

## Healthcare Contribution
- First systematic evidence that a conversational diagnostic AI can **request and reason about multimodal artifacts** during consultations at a level superior or non-inferior to PCPs.
- A dedicated **Multimodal Understanding & Handling (MUH) OSCE rubric** for assessing artifact engagement, interpretation, and artifact-grounded reasoning by both AI and clinicians.
- 105 specialist-designed scenarios across dermatology (SCIN), cardiology (PTB-XL ECG images), and clinical documents, deliberately constructed so both image and history are required for diagnosis, including realistic degradations (smartphone photos of screens).

## Trustworthy AI
- **Hallucination** of image findings is evaluated as an explicit, safety-critical binary metric in both auto-rating and specialist review; diagnostic accuracy stratified by hallucination presence.
- Randomized, **double-blind** comparison design; robustness testing over simulated patient personality, demographics, and semantic perturbations; subgroup analysis by image quality showed AMIE more robust to poor-quality images than PCPs.
- Auto-rater calibration against human expert judgments reported; authors emphasize AMIE is a research system not intended for clinical use.

## Evaluation
- **Expert OSCE study**: 105 scenarios, 25 patient actors (India/Canada), 19 PCPs, 210 blinded randomized consultations, each rated by 3 of 18 specialists (dermatology, cardiology, internal medicine) plus patient-actor questionnaires (PACES/GMCPQ/PCCBP-derived rubrics + MUH).
- Results: AMIE superior on 7/9 multimodal axes and 29/32 non-multimodal axes; top-k DDx accuracy superior across k = 1–10 (p < 0.001, mixed-effects models with scenario random intercepts).
- **Automated evaluation**: perception tests on SCIN, PAD-UFES-20, PTB-XL, ECG-QA, and a ClinicalDoc-QA dataset; simulated-dialogue auto-rating with ablations of the state-aware framework.

## Research Gap
- Evaluation remains on **simulated, single-encounter OSCE consultations with patient actors** — not longitudinal real patient records or ICU data; no persistent memory across visits.
- Chat-based interaction limits (no video, no physical exam), possible unblinding via stylistic differences, and absence of real-world clinical validation are acknowledged.
- Grounding is in web/medical knowledge, not in a patient's own historical timeline.

## Key Contributions
- Multimodal state-aware reasoning framework at inference time for diagnostic dialogue.
- Simulation environment (scenario generation, dialogue simulation, auto-rater) for rapid multimodal dialogue evaluation.
- Dedicated MUH rubric for multimodal OSCE evaluation.
- Randomized, blinded expert OSCE study showing AMIE matches or exceeds PCPs, including on diagnostic accuracy and multimodal handling.

## Limitations
- Synchronous text-chat setting restricts non-verbal cues, dynamic visual assessment, and physical examination; findings may not generalize to video or in-person care.
- Scenarios were created post-hoc around artifacts and may not reflect true case histories.
- Structured phase design can be rigid when critical new information (e.g., an allergy) emerges after the plan is delivered.
- Domain SFT experiments showed trade-offs; system not validated in real-world clinical workflows; authors state clinical translation requires further research.

## Important Quotes
- "conversation flow is dynamically controlled by intermediate model outputs reflecting patient states" (Abstract)
- "AMIE remains an evolving research system, not intended for clinical use" (Section 6, Discussion)

## Thesis Relevance
- Direct precedent for the thesis's **state-aware agent orchestration**: explicit patient-state tracking (profile, evolving DDx, information gaps) is a template for the framework's patient-context layer over ICU data.
- Confirms thesis gap (1): even a state-of-the-art system is evaluated on **OSCE-style actor scenarios**, not longitudinal real ICU records — motivating MIMIC-IV-based evaluation.
- Its **hallucination-as-first-class-metric** and blinded specialist rubric evaluation inform the thesis's verification gate and audit-trail faithfulness evaluation design.
- The simulation + **auto-rater** pipeline is a reusable pattern for scalable automated evaluation before human-in-the-loop expert review.
- Evidence that an explicit reasoning layer beats prompting alone in safety-critical dialogue supports the thesis's layered architecture with a dedicated verification component.
- Its within-encounter-only patient state highlights the thesis's differentiator: **persistent longitudinal patient memory** across encounters.

## References
- Tu, T., Schaekermann, M., Palepu, A., et al. "Towards conversational diagnostic artificial intelligence." Nature (2025). [original AMIE]
- Palepu, A., Liévin, V., Weng, W.-H., et al. "Towards conversational AI for disease management." (2025). [AMIE management reasoning]
- Schmidgall, S., Ziaei, R., Harris, C., et al. "AgentClinic: a multimodal agent benchmark to evaluate AI in simulated clinical environments." arXiv:2405.07960 (2024).
- Mukherjee, S., Gamble, P., Ausin, M. S., et al. "Polaris: A safety-focused LLM constellation architecture for healthcare." (2024).
- Wagner, P., et al. "PTB-XL, a large publicly available electrocardiography dataset." (used for ECG scenarios).
