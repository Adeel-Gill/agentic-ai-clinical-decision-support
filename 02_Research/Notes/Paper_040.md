# Paper 040

## Basic Information
- **Title:** Development and Prospective Implementation of a Large Language Model based System for Early Sepsis Prediction
- **Authors:** Supreeth P. Shashikumar, Sina Mohammadi, Rishivardhan Krishnamoorthy, Avi Patel, Gabriel Wardi, Joseph C. Ahn, et al.
- **Year:** 2025
- **DOI:** 10.1038/s41746-025-01689-w
- **Venue:** npj Digital Medicine, 8:290 (2025)
- **Publisher:** Nature Publishing Group (in partnership with Seoul National University Bundang Hospital); UC San Diego
- **Link:** https://www.nature.com/articles/s41746-025-01689-w

## Abstract Summary (200–300 words)
This study develops and prospectively deploys **COMPOSER-LLM**, a multimodal early sepsis prediction system that augments the previously validated COMPOSER deep-learning model (structured EHR data) with a locally deployed open-source LLM (**Mixtral 8x7B**) that analyzes unstructured clinical notes. The key design idea is selective LLM invocation: COMPOSER generates hourly sepsis risk scores, and only for predictions in a **high-uncertainty band** (risk score between θ2=0.5 and θ1=0.75) is the LLM-based **differential diagnosis (DDx) tool** triggered, saving compute (on average ~10 LLM calls/day). The DDx tool uses **retrieval-augmented generation** (Chroma vector store, Instructor embeddings, chunk size 1000/overlap 300, K=5) to extract clinical signs and symptoms from notes into JSON, runs each query three times taking a majority vote (temperature 0.3) to reduce hallucination, then feeds extracted signs into a **Bayesian likelihood calculator** that ranks 19 differentials (severe sepsis plus sepsis-mimics such as cardiogenic shock, pulmonary embolism, DKA). An alarm fires only if "Severe Sepsis" is in the top-5 differentials and the LLM identifies a suspicion of bacterial infection. Evaluated on ~2500 ED encounters, COMPOSER-LLM(DDx) achieved sensitivity 72.1%, PPV 52.9%, F1 61.0%, and 0.0087 false alarms per patient hour — substantially better PPV/FAPH than standalone COMPOSER (PPV 22.6%, FAPH 0.037). Prospective deployment (silent mode, two UCSD EDs, FHIR/HL7v2 cloud pipeline) yielded similar results (sensitivity 70.8%, PPV 58.2%, F1 63.9%). Clinician chart review of 50 false positives found 62% had suspicion of bacterial infection, suggesting the alerts retain clinical utility. The work shows LLMs integrated with traditional models can improve prediction by leveraging unstructured data.

## Research Problem
- Most sepsis prediction models use only structured EHR data and miss contextual information in unstructured notes; commercial models (Epic Sepsis Score, TREWS) show poor PPV and high false-alarm burden.
- Prior note-based approaches (ClinicalBERT embeddings, LDA topics, tf-idf) capture document-level signal but lack local context, interpretability, and are prone to copy-paste redundancy and domain shift.
- False alarms cause alert fatigue and unnecessary treatment, demanding higher precision without losing sensitivity.

## Proposed Solution
- **COMPOSER-LLM:** couple the structured-data COMPOSER neural net with an LLM DDx tool invoked only on high-uncertainty predictions to add contextual reasoning from notes.
- Use RAG-based sign/symptom extraction plus a Bayesian likelihood calculator over 19 differentials to distinguish sepsis from sepsis-mimics and confirm suspicion of bacterial infection before alarming.
- Deploy locally (HIPAA-compliant cloud, Mixtral 8x7B) with intermittent GPU usage to control cost.

## Architecture
- **Two-stage pipeline (Fig. 1–2):** (1) COMPOSER microservice consumes FHIR-queried structured features (labs, vitals, comorbidities, meds, demographics) to produce an hourly risk score with a conformal-prediction module rejecting out-of-distribution samples; (2) for scores in [0.5, 0.75], a DDx-tool microservice runs LLM extraction → likelihood calculators → ranked differentials.
- **Deployment:** cloud (AWS EC2 g5.12xlarge, NVIDIA A10G GPUs), FHIR APIs with OAuth 2.0, risk scores written back to EHR via HL7v2 flowsheet triggering a nurse-facing Best Practice Advisory (silent mode during study).

## Memory
- Not a core focus in the persistent-longitudinal sense; the system aggregates **all clinical notes from admission to prediction time** per encounter and stores their embeddings in a Chroma **vector database** for retrieval. This is per-encounter retrieval memory, not cross-encounter patient memory.

## Planning
- Not an explicit agentic planner. The control flow is a fixed **uncertainty-gated decision policy**: alarm directly if score > θ1; invoke DDx tool if θ2 ≤ score < θ1; suppress otherwise.

## Reasoning
- **Probabilistic reasoning over differentials:** a Bayesian likelihood calculator computes posterior disease probability from LLM-extracted signs/symptoms, producing a ranked top-k differential list.
- The LLM is used deliberately as an **information-retrieval/extraction tool, not a diagnostic reasoner**; the authors note standalone LLM diagnosis (COMPOSER-LLM baseline) underperformed (sensitivity 34.4%). DDx reasoning is framed as mitigating anchoring/automation bias.

## Tool Use
- **Core mechanism.** The LLM sign/symptom extractor is wrapped as a callable microservice with a structured JSON output contract, orchestrated via the **LangChain** framework; downstream Bayesian likelihood calculators act as computational tools consuming the LLM output.
- Majority voting over three LLM runs per query improves output stability.

## Multi-Agent
- Not a core focus; a single LLM extractor feeds deterministic likelihood calculators. It is a hybrid model-plus-LLM pipeline rather than a multi-agent system.

## RAG
- **Central component.** Retrieval-augmented generation extracts relevant note chunks for each queried sign/symptom: notes segmented into 1000-token chunks (300 overlap), embedded via HuggingFace Instructor, stored in Chroma, top-K=5 retrieved and appended to the prompt — grounding the LLM in the **patient's own clinical notes** rather than external literature.

## Healthcare Contribution
- A prospectively validated, real-time LLM-augmented sepsis early-warning system integrated into live ED workflows via FHIR/HL7v2.
- Large PPV/false-alarm improvement over standalone COMPOSER and commercial baselines (Epic Sepsis Score, TREWS) while maintaining sensitivity.
- As a "digital sepsis biomarker" for patients with suspected infection, COMPOSER-LLM(DDx) reached PPV ~80% and F1 ~77%.
- Demonstrates safe on-premise, open-source LLM deployment inside a HIPAA-compliant firewall.

## Trustworthy AI
- **Uncertainty-aware by design:** LLM invoked only in the high-uncertainty band; conformal prediction rejects out-of-distribution inputs; the parent COMPOSER model was built to "say I don't know."
- **Explainability:** the extractor outputs a concise justification for each sign/symptom, unlike opaque NLP embeddings; DDx ranking mitigates anchoring/automation bias.
- **Human-in-the-loop and rigorous validation:** nurse-facing BPA, clinician chart review of false positives (62% had bacterial infection), silent-mode prospective deployment, hallucination control via low temperature and majority voting.

## Evaluation
- **Retrospective (2500 encounters):** COMPOSER-LLM(DDx) sensitivity 72.1%, PPV 52.9%, F1 61.0%, FAPH 0.0087 vs standalone COMPOSER PPV 22.6%, FAPH 0.037; COMPOSER-LLM(SLT) PPV 31.9%; standalone LLM baseline sensitivity 34.4%.
- **Prospective (754 encounters, two EDs):** sensitivity 70.8%, PPV 58.2%, F1 63.9%, FAPH 0.0086.
- **Suspected-infection sub-cohort:** COMPOSER-LLM(DDx) PPV 80.1%, F1 77.2% (retrospective).
- **Top-5 differential coverage:** actual diagnosis captured for 83.1% (retro) / 73.2% (prospective) of false positives.
- **Clinician chart review (50 FPs):** 62% agreed as suspicion of bacterial infection.

## Research Gap
- DDx tool triggers only after specific notes are available, potentially delaying alerts.
- Uses a pre-trained (not fine-tuned) LLM; generalizability across sites and to end-to-end LLM differential diagnosis is untested.
- Silver-standard Sepsis-3 labeling has limited sensitivity/specificity; impact on patient outcomes not yet measured.

## Key Contributions
- COMPOSER-LLM, a hybrid structured-model + LLM sepsis predictor with uncertainty-gated LLM invocation.
- A RAG + Bayesian differential-diagnosis tool over 19 conditions grounded in patient notes.
- Prospective real-world deployment with FHIR/HL7v2 and demonstrated PPV/FAPH gains.
- Evidence that LLMs work best as information extractors feeding probabilistic reasoning, not standalone diagnosticians.

## Limitations
- Alert generation depends on availability of certain note types; incomplete notes may delay/limit the tool.
- Single health system (UCSD, two EDs); no fine-tuning or domain-specific LLM tested.
- Outcome impact (does it change patient care/mortality) not evaluated; Sepsis-3 silver-standard labels are imperfect.
- Modest LLM throughput assumptions (~10 calls/day) reflect the narrow uncertainty band, not full-cohort continuous use.

## Important Quotes
- "integrating LLMs with traditional models can enhance predictive performance by leveraging unstructured data" (Abstract)
- "we examined the effectiveness of LLMs as information retrieval tools rather than diagnostic tools" (Discussion)

## Thesis Relevance
- The closest analog to the thesis's goal: a **prospectively deployed ICU/ED early-warning system** combining structured data, LLM note processing, RAG, and probabilistic reasoning — a template for the thesis's monitoring-plus-decision-support architecture.
- Its **uncertainty-gated LLM invocation** is a concrete instantiation of the thesis's verification gate: use cheap models by default and escalate to LLM reasoning only when confidence is low.
- **RAG grounded in the patient's own notes** (Chroma + Instructor) directly validates the thesis's differentiator — retrieval over the patient timeline rather than external guidelines/literature.
- The thesis differs by targeting **longitudinal, multi-condition monitoring on MIMIC-IV** rather than a single-condition ED sepsis alarm at one site, and by treating audit-trail faithfulness as a first-class evaluated component (here explainability is per-sign justification only).
- Trust mechanisms to borrow: conformal OOD rejection, majority-vote hallucination control, per-sign justifications, silent-mode prospective validation, and clinician chart review of false positives.
- The negative result that standalone LLM diagnosis fails (sensitivity 34.4%) reinforces the thesis's layered agentic design over end-to-end LLM diagnosis.

## References
- Boussina, A. et al. (2024). Impact of a deep learning sepsis prediction model on quality of care and survival. npj Digital Medicine. (COMPOSER deployment, 17% mortality reduction)
- Shashikumar, S. P. et al. (2021). Artificial intelligence sepsis prediction algorithm learns to say "I don't know". npj Digital Medicine. (COMPOSER + conformal prediction)
- Lewis, P. et al. (2020). Retrieval-augmented generation for knowledge-intensive NLP tasks. NeurIPS. (RAG foundation)
- Jiang, A. Q. et al. (2024). Mixtral of experts. (the deployed open-source LLM)
- Hager, P. et al. (2024). Evaluation and mitigation of the limitations of large language models in clinical decision-making. Nature Medicine. (limits of standalone LLM diagnosis)
