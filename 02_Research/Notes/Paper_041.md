# Paper 041

## Basic Information
- **Title:** Retrieval Augmented Generation for 10 Large Language Models and its Generalizability in Assessing Medical Fitness
- **Authors:** Yu He Ke, Liyuan Jin, Kabilan Elangovan, Hairil Rizal Abdullah, Nan Liu, Alex Tiong Heng Sia, et al.
- **Year:** 2025
- **DOI:** 10.1038/s41746-025-01519-z
- **Venue:** npj Digital Medicine (2025) 8:187
- **Publisher:** Nature Portfolio (Springer Nature)
- **Link:** https://www.nature.com/articles/s41746-025-01519-z

## Abstract Summary (200–300 words)
This study develops and evaluates an **LLM-RAG pipeline** for preoperative medicine, testing whether retrieval-augmented LLMs can accurately, consistently, and safely determine **surgical fitness** and generate preoperative instructions. The authors built RAG systems over two knowledge corpora — **35 local guidelines** from a Singapore tertiary hospital and **23 international guidelines** (ASA, ESA, UpToDate) — and paired them with **ten LLMs**: GPT-3.5, GPT-4, GPT-4o, LLaMA2 (7B/13B/70B), LLaMA3 (8B/70B), Gemini-1.5-Pro, and Claude-3-Opus. Across **14 de-identified clinical scenarios** spanning ASA classes 1–3, the models generated **3234 responses**, which were compared with **448 human-generated answers** from four junior doctors and four attending anesthesiologists against expert-panel ground truth. The **GPT-4 model with international guidelines** achieved the highest accuracy in predicting fitness for surgery (**96.4% vs 86.6% for humans, p = 0.016; OR = 4.84**), outperformed its non-RAG counterpart (92.9%), generated answers within ~20 seconds versus ~10 minutes for humans, exhibited an **absence of hallucinations**, and produced more consistent output (IRR up to 0.96) than clinicians. The human **false negative rate** (unfit patients judged fit) was 62.5% versus 25% for the best model. Qualitative safety was assessed with the **S.C.O.R.E. framework** (Safety, Consensus, Objectivity, Reproducibility, Explainability), where the GPT-4 RAG model scored 4.93/5 for safety and 4.86/5 for reproducibility. Notably, RAG **worsened** LLaMA2-7b hallucination rates (48.6% vs 12.8% native), showing RAG benefits are model-dependent. The authors conclude that GPT-4-based LLM-RAG can serve as a consistent, efficient **human-in-the-loop support tool** for preoperative assessment, not an autonomous decision-maker.

## Research Problem
- Out-of-the-box LLMs answer complex clinical assessment questions from **pre-trained knowledge only**, ungrounded in institutional practice guidelines, and their **hallucinations** pose safety and ethical risks.
- **Surgery cancellations** from medical unfitness, incorrect physician instructions, and non-compliance carry large economic costs (OR time estimated at USD 1400–1700/hour), while traditional preoperative evaluation is labor-intensive.
- **Fine-tuning** is impractical for healthcare (extensive retraining data, GPU/compute demands), motivating RAG as a scalable, updatable alternative.
- It was unknown how well RAG **generalizes across many different LLMs** and across local vs international guideline corpora.

## Proposed Solution
- An **LLM-RAG pipeline** (Python 3.11, **LlamaIndex** with **Auto-Merging Retrieval**) that indexes preoperative guidelines and grounds LLM answers in retrieved guideline chunks.
- Hierarchical, tree-structured chunking where **parent chunks merge relevant sub-chunks** above a threshold to preserve contextual flow; `similarity_top_k` set to 30 to balance recall against noise and latency.
- Standardized inference parameters across all 10 models (**temperature 0.1**, max 2048 output tokens, top-p 0.90) plus role-playing **prompt engineering** ("You are the anesthesiologist seeing this patient in the preoperative clinic...").
- Three configurations per model: base LLM, **RAG-local** (35 guidelines), and **RAG-international** (23 guidelines), compared head-to-head with human clinicians.

## Architecture
- Pipeline stages: guideline PDF-to-text conversion, chunking, embedding and indexing (Pinecone/LangChain mentioned for vanilla RAG; LlamaIndex used for the advanced framework), retrieval, and grounded generation (Figs. 3–4).
- Not an agentic architecture — a single retrieval-then-generate pass; no orchestration, planning modules, or multi-agent layers.

## Memory
- Not a core focus; knowledge lives in a **static pre-indexed guideline corpus**, with no per-patient longitudinal or episodic memory across encounters.

## Planning
- Not a core focus; the system executes a fixed single-shot retrieval-generation workflow with no task decomposition or replanning.

## Reasoning
- Clinical reasoning is elicited by a structured **role-playing prompt** requiring 8 instruction components (doctor/nurse triage, fasting, carbohydrate loading, medications, team instructions, optimization, delay decision, protocols); no explicit CoT/ReAct mechanism is used.

## Tool Use
- The retriever functions as a single "search-engine-like" tool over the guideline index; no general tool-calling, API, or code-execution capabilities.

## Multi-Agent
- Not a core focus; the study compares single LLM-RAG systems, not agent teams.

## RAG
- **Central contribution**: benchmarks RAG generalizability across **10 LLMs and 2 guideline corpora**.
- Key findings: RAG improves GPT-4 accuracy (96.4% international vs 92.9% non-RAG); **international guidelines outperform local ones**, likely because they contain richer text explanations of diagrams/tables; RAG **increased hallucinations for LLaMA2-7b** (48.6% vs 12.8%), showing retrieval quality interacts with base-model capacity.
- Discusses computational overhead (embedding, indexing, retrieval latency), and proposes **adaptive/dynamic retrieval** depth as future work.

## Healthcare Contribution
- Demonstrates that guideline-grounded LLMs can **exceed clinician accuracy** in surgical fitness assessment while producing more consistent outputs (human IRR consistently lower than GPT-4-international's 0.92–0.96).
- Shows LLM-RAG adapts international recommendations to **local practice context** (e.g., converting generic referrals into the institution-specific "IMPT" pathway).
- Positions LLM-RAG for **preoperative triage** (nurse vs doctor, 93.0% accuracy with local guidelines) and drafting instructions to reduce clinician workload and burnout; reports a deployed **SecureGPT-enabled RAG** processing a patient chart in ~10 s.

## Trustworthy AI
- Explicit **hallucination accounting**: any critical medical error (e.g., wrong fasting/medication instruction) is classified as a hallucination and auto-fails, regardless of other correct content.
- Uses the **S.C.O.R.E. framework** (Safety, Consensus, Objectivity, Reproducibility, Explainability) scored by two attending anesthesiologists over 4 repeated generations.
- Advocates a **human-in-the-loop** deployment where a qualified clinician reviews all recommendations; discusses bias risks (race, gender, socioeconomic, regional practice) embedded in source material.

## Evaluation
- 14 de-identified scenarios (ASA 1–3); 3682 total evaluated components (3234 LLM, 448 human); expert panel of two board-certified perioperative anesthesiologists defined ground truth.
- Primary outcome: fitness-for-surgery accuracy; secondary: fasting, carbohydrate loading, medications, team instructions, optimization type (correct if ≥75% guideline-aligned, with 65%/85% sensitivity analyses).
- Statistics: Fisher's exact test; percentage-agreement IRR; **distinct n-gram** analysis for linguistic diversity; hallucination rates 0–2.9% for GPT/LLaMA3/Gemini/Claude vs much higher for LLaMA2.
- Humans were better only at medication instruction ordering (98.0% vs 91.0%, p = 0.035); combined secondary outcomes showed no significant difference (83.0% vs 81.0%, p = 0.710).

## Research Gap
- Evaluation is on **simulated, curated scenarios** engineered for clear-cut answers — not real, messy longitudinal patient records.
- Retrieval grounds only in **guidelines**, not in the individual patient's own history/timeline; the patient summary is pasted into the prompt.
- No agentic reasoning, memory, verification loop, or multi-step monitoring; a single-turn assessment task.
- Fine-tuning comparison absent; standardized healthcare-specific RAG evaluation metrics still lacking.

## Key Contributions
- First systematic assessment of **RAG generalizability across 10 LLMs** for a realistic clinical task with both local and international guideline corpora.
- Head-to-head **LLM-RAG vs clinician** comparison showing superhuman accuracy and consistency for GPT-4-international on surgical fitness.
- Evidence that RAG benefit is **model-dependent** and can amplify hallucinations in weaker models.
- Application of the **S.C.O.R.E.** qualitative safety framework and a strict hallucination-as-failure evaluation rule; public codebase on GitHub.

## Limitations
- Simulated scenarios limit real-world generalizability; hospital-specific protocols vary in fitness thresholds.
- Scenarios were structured toward unambiguous delay decisions, whereas real clinical decisions (e.g., cancer surgery timing) are ethically nuanced.
- Fine-tuning not evaluated (insufficient training examples); local-guideline corpora less machine-readable (diagrams/tables) than international ones.
- RAG adds latency, memory, and scalability costs; performance remains contingent on retrieval quality and ongoing expert oversight.

## Important Quotes
- "The model exhibited an absence of hallucinations and produced more consistent output than humans." (Abstract, p. 1)
- "Deployed as a support tool rather than an autonomous decision-maker" (Discussion, p. 5)

## Thesis Relevance
- Provides strong quantitative evidence for the thesis's **RAG grounding layer**: guideline-grounded generation improves accuracy and suppresses hallucinations — but only for capable base models, informing model selection for the framework.
- Directly exemplifies thesis gap (2): its RAG grounds in **guidelines only**, not the patient's own longitudinal timeline — the thesis's patient-memory-grounded RAG extends exactly this design.
- Exemplifies thesis gap (1): evaluation uses 14 curated simulated vignettes rather than real longitudinal ICU records like MIMIC-IV, motivating the thesis's evaluation setting.
- Its strict **hallucination-as-critical-error** rule and S.C.O.R.E. (Safety/Reproducibility/Explainability) scoring are reusable evaluation instruments for the thesis's verification gate and audit-trail faithfulness assessment.
- The explicit **human-in-the-loop support-tool** framing (clinician reviews all outputs) matches the thesis's human validation layer and supplies a deployment precedent.
- Practical RAG engineering details (LlamaIndex Auto-Merging Retrieval, similarity_top_k tuning, chunking of guideline PDFs) transfer directly to the thesis's retrieval implementation.

## References
- Zakka, C. et al. "Almanac: retrieval-augmented language models for clinical medicine." Res. Sq. (2023).
- Thirunavukarasu, A. J. et al. "Large language models in medicine." Nat. Med. 29, 1930–1940 (2023).
- Tan, T. F. et al. "A proposed S.C.O.R.E. evaluation framework for large language models: Safety, Consensus, Objectivity, Reproducibility and Explainability." arXiv (2024).
- Lim, D. Y. Z. et al. "Large language models in anaesthesiology: use of ChatGPT for ASA physical status classification." Br. J. Anaesth. (2023).
- Meskó, B. "Prompt engineering as an important emerging skill for medical professionals: tutorial." J. Med. Internet Res. 25, e50638 (2023).
