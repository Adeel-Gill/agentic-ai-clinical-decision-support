# Recommended Additional Papers

Influential works that are cited in the thesis prose or that materially strengthen the argument,
but are not yet represented as rows in the Literature Matrix. Keys are the canonical citation keys
from `REVIEW/Style_And_Citation_Keys.md`. These should be added to the matrix (or at minimum kept
consistent in the References) so the review's foundations are complete.

| Key | Paper | Why it matters | Where to cite |
| :--- | :--- | :--- | :--- |
| lewis2020rag | Retrieval-Augmented Generation (original) | Foundational RAG method; the basis for every grounding argument in the thesis. | Ch. 2 RAG background; Ch. 3 where patient-timeline retrieval is introduced. |
| gao2023rag | RAG survey | Situates RAG variants and their failure modes; supports the claim that most medical RAG is guideline/literature-grounded. | Ch. 2 RAG section; Research Gap (grounding argument). |
| asai2024selfrag | Self-RAG | Learns when to retrieve and to critique its own outputs; direct precedent for the verification gate. | Ch. 2 RAG/verification; Ch. 3 verification gate design. |
| wei2022chain | Chain-of-Thought | The step-by-step reasoning primitive underlying ReAct and medical reasoning agents. | Ch. 2 reasoning section; wherever CoT is invoked. |
| wang2023selfconsistency | Self-Consistency | Sampling-and-voting reliability technique; relevant to reducing reasoning variance in clinical decisions. | Ch. 2 reasoning reliability; Ch. 3 reasoning module. |
| yao2023tree | Tree of Thoughts | Deliberate multi-path reasoning/search; contrasts with linear CoT for complex planning. | Ch. 2 reasoning/planning taxonomy. |
| shinn2023reflexion | Reflexion | Verbal self-reflection and memory of past failures; precedent for longitudinal/experiential memory and self-correction. | Ch. 2 memory/reflection; Ch. 3 memory + verification loop. |
| thirunavukarasu2023llms | LLMs in Medicine (Nat Med) | Authoritative overview of clinical LLM promise and risk; frames healthcare motivation. | Ch. 1 motivation; Ch. 2 healthcare LLM background. |
| singhal2025medpalm2 | Med-PaLM 2 | Expert-level medical QA via ensemble refinement; a key parametric-only baseline for the exam-QA critique. | Ch. 2 medical LLMs; Research Gap (exam QA critique). |
| jin2021medqa | MedQA benchmark | The USMLE-style benchmark that most clinical agents are evaluated on; central to the "static exam QA" gap. | Ch. 2 evaluation; Research Gap (evaluation-data argument). |
| shi2024ehragent | EHRAgent | Agent that grounds in structured EHR via code execution; nearest precedent to patient-timeline grounding. | Ch. 2 clinical agents; Research Gap (EHR grounding); Ch. 3 RAG design. |
| schmidgall2024agentclinic | AgentClinic | Simulated interactive clinical environment; shows the move beyond static QA is still on simulated data. | Ch. 2 clinical agents/evaluation; Research Gap (evaluation-data argument). |
| tu2025amie | AMIE | Conversational diagnostic agent evaluated in dialogue; relevant to multi-turn clinical interaction and evaluation. | Ch. 2 clinical agents; comparison of interaction paradigms. |
| johnson2023mimic | MIMIC-IV dataset | The real ICU dataset underpinning the thesis; the basis of the "real data, not exam QA" contribution. | Ch. 1 and Ch. 2 (dataset); Ch. 3/Ch. 4 methodology and evaluation. |
