# Paper 044

## Basic Information
- **Title:** Regulation of clinical Artificial Intelligence (AI) in the Age of Agents: Unconfined Non-Deterministic Clinical Software (UNDCS) systems for healthcare
- **Authors:** Caitlyn Tan, Dinesh Visva Gunasekeran, Cheng Ooi Low, Gabrielle Sze Yee Sim, Danella Yaoxin Foo, Robert J. T. Morris, et al.
- **Year:** 2026
- **DOI:** 10.1038/s41746-026-02420-z
- **Venue:** npj Digital Medicine (2026) 9:186, Matters Arising
- **Publisher:** Nature Portfolio (Springer Nature)
- **Link:** https://www.nature.com/articles/s41746-026-02420-z

## Abstract Summary (200–300 words)
This **Matters Arising** responds to Weissman et al.'s demonstration (Paper 043) that unregulated LLMs produce medical device-like clinical decision support (CDS) output, and to their call for new LLM-CDS regulations. The authors argue that some proposed considerations are **already covered by existing frameworks**: the latest FDA Software as a Medical Device (SaMD) guidelines — consistent with EU, Australian, and Singaporean frameworks — already calibrate compliance requirements to intended use and end-users (clinicians vs non-clinicians), and all CDS systems fall under SaMD regardless of underlying technology, so LLM-specific guidelines may be unnecessary. However, they agree that **"generalized" CDS not anchored to specific clinical indications** exposes a genuine regulatory gap. To contextualize it, they introduce a taxonomy of clinical software: **deterministic clinical software (DCS)** with fixed input data-output label (IDOL) relationships; **confined clinical software (CCS)** (e.g., deep learning classifiers) with predictable variability over bounded output labels; and **unconfined non-deterministic clinical software (UNDCS)** — general-purpose transformer LLMs operating over an open-ended semantic space with stochastic sampling (temperature, floating-point effects), whose output spectrum cannot be exhaustively tested with datasets. They propose UNDCS as a **new regulatory category** spanning all health applications, with standards mandating safeguards: **red teaming** (jailbreaks, prompt injection, adversarial attacks with clinician involvement), **guardrails** (Llama Guard-style filters, acknowledged as jailbreak-susceptible), **confined RAG** grounding in validated sources, and **agent-agent moderation** via multi-agent consensus, LLM-as-a-Judge adjudication loops, and neuro-symbolic reasoning over validated guidelines. Finally, they argue that label-driven, manufacturer-registration regulation fails for direct-to-consumer LLMs whose developers control the whole AI supply chain, so a forward-looking, agile paradigm is needed to protect consumers, ensure accountability, and avoid stifling innovation.

## Research Problem
- Weissman et al. showed LLMs readily emit **device-like CDS output**, but which of their proposed regulatory responses are actually needed remained unresolved.
- Existing **label-driven regulation** (device classification by manufacturer-designated intended use) fails for direct-to-consumer LLMs (ChatGPT, Grok, Claude) distributed with blanket disclaimers that "are unlikely to deter real-world use".
- Traditional **dataset-driven evaluation by exhaustive testing** is infeasible for non-deterministic, open-ended LLM output, leaving no accepted evaluation paradigm for generalized CDS.
- End-users of consumer LLMs lack the protections of SaMD distribution pathways (user selection, right-siting of emergency care, adverse-event monitoring).

## Proposed Solution
- A **new regulatory category — UNDCS** (Unconfined Non-Deterministic Clinical Software) — for general-purpose GenAI health software not anchored to specific clinical indications, spanning CDS, administration, and health promotion.
- Regulations should set standards for **built-in safeguards**: red teaming, guardrails, confined RAG, and agent-agent moderation (multi-agent consensus, LLM-as-a-Judge loops with repeated sampling, neuro-symbolic reasoning from validated guidelines).
- Direct-to-consumer UNDCS should demonstrably **restrict outputs to non-medical-device use cases** unless formally evaluated in clinical trials with ongoing quality controls.
- A conceptual **DCS / CCS / UNDCS taxonomy** distinguishing confined vs unconfined and deterministic vs non-deterministic systems to calibrate regulatory treatment.

## Architecture
- Not a system paper; conceptually distinguishes confined (bounded IDOL outputs) from **unconfined** architectures (open-ended semantic space), and notes non-determinism arises from temperature sampling and floating-point inaccuracies atop inherently deterministic transformers.

## Memory
- Not a core focus; no memory mechanisms are discussed.

## Planning
- Not a core focus; no planning components are discussed.

## Reasoning
- Not a core focus as a mechanism; it does advocate **neuro-symbolic models that reason deterministically from validated guidelines** as a reliability safeguard, and repeated-sampling adjudication to score aggregate output validity.

## Tool Use
- Not a core focus; agents performing digital functions are noted as an emerging risk surface, but tool-calling mechanics are not analyzed.

## Multi-Agent
- **Agent-agent moderation** via multi-agent system (MAS) architectures is proposed as a first-class safeguard: consensus lowers error frequency, mitigates single-agent weaknesses (specialized domains, self-reference bias), and can be augmented with RAG at multiple checkpoints.

## RAG
- **Confined RAG** is one of the four recommended safeguards: grounding responses in validated trusted sources reduces risk but trades versatility for specialization, and RAG materials can **overpower the local context of a query**, causing omissions and incorrect responses.

## Healthcare Contribution
- Clarifies for the digital-health community which of Weissman et al.'s regulatory calls are already handled by **FDA/IMDRF SaMD frameworks** (2025 update) versus genuinely new territory.
- Introduces the **UNDCS category and DCS/CCS/UNDCS taxonomy** as shared vocabulary for regulating generative and agentic clinical AI.
- Flags that even non-clinical administrative tools (e.g., AI scribes) can compound into downstream clinical errors, flawed claims, and higher insurance premiums, arguing risk-mitigation standards should cover **all** health-related UNDCS.

## Trustworthy AI
- The paper is entirely a **trustworthy-AI governance** contribution: hallucinations are framed as inherent semantic errors of compressed models, motivating layered defenses (red teaming, guardrails, confined RAG, MAS moderation).
- Acknowledges each safeguard's weaknesses: guardrails cannot consistently check the full non-deterministic output spectrum and are jailbreak-susceptible; LLM-as-a-Judge carries known biases; RAG can override query context.
- Calls for **manufacturer accountability** for monetized software and consumer protections as UNDCS blurs intended uses and users.

## Evaluation
- Not a core focus; a commentary with no experiments or datasets ("No datasets were generated or analysed"). Argues traditional exhaustive dataset-driven evaluation is infeasible for UNDCS and suggests repeated sampling with LLM-as-a-Judge adjudication instead.

## Research Gap
- Proposes but does not operationalize the UNDCS category: no concrete evaluation protocol, metrics, thresholds, or reference implementation of the recommended safeguards is provided.
- The four safeguards are surveyed at concept level; their combined effectiveness on real clinical workloads (e.g., longitudinal ICU records) is untested.
- Verification/moderation agents are recommended, but how to audit the moderators themselves (audit-trail faithfulness) is left open.

## Key Contributions
- The **UNDCS concept** and DCS/CCS/UNDCS taxonomy separating confined-deterministic, confined-variable, and unconfined non-deterministic clinical software.
- A structured rebuttal-and-extension of Weissman et al.: existing SaMD guidance suffices for end-user calibration and technology-agnostic coverage, but generalized CDS needs a **new, non-label-driven regulatory paradigm**.
- A safeguard portfolio (red teaming, guardrails, confined RAG, agent-agent moderation) with explicit strengths/weaknesses analysis (Fig. 1).
- Argument that regulations must target **direct-to-consumer distribution** where technology providers control the entire AI supply chain.

## Limitations
- A 4-page opinion/Matters Arising piece: no empirical evidence, benchmark, or quantitative comparison of the proposed safeguards.
- Recommendations remain jurisdiction-general; no concrete statutory pathway or enforcement mechanism is drafted.
- The confined/unconfined boundary for hybrid systems (e.g., RAG-constrained agents with structured outputs) is not sharply defined.
- Does not address data-privacy, liability apportionment, or reimbursement dimensions of agentic clinical AI.

## Important Quotes
- "a new category of regulations may be required" (Section: UNDCS regulations, p. 2)
- "static regulations focused on present-day norms risk rapidly becoming outdated" (Section: New Regulatory Paradigm, p. 3)

## Thesis Relevance
- Provides the **regulatory framing** for the thesis framework: an agentic ICU CDS system is UNDCS by this taxonomy, and the thesis's safeguards should map onto the paper's recommended portfolio.
- The thesis's **verification gate with audit trail** directly instantiates the paper's "agent-agent moderation" and LLM-as-a-Judge adjudication safeguards — and goes further by evaluating verification faithfulness as a first-class component (thesis gap 3), which this paper only prescribes.
- **Confined RAG** is endorsed as a safeguard but only guideline/source-grounded; the thesis's patient-timeline-grounded RAG addresses the noted weakness that RAG materials can overpower the local (patient-specific) context of a query (thesis gap 2).
- The taxonomy gives the thesis vocabulary to position its layered design as deliberately **re-confining** an unconfined system: structured outputs, guideline grounding, and human-in-the-loop validation narrow the open-ended semantic space.
- Warning that multi-agent consensus and judge loops have their own biases justifies the thesis's **human-in-the-loop validation layer** above automated verification.
- Directly chains with Paper 043 (the article it arises from), letting the thesis cite an evidence-plus-response pair on why prompt-level and label-driven controls fail.

## References
- Weissman, G. E., Mankowitz, T. & Kanter, G. P. "Unregulated large language models produce medical device-like output." npj Digital Medicine 8, 148 (2025).
- Xu, Z., Jain, S. & Kankanhalli, M. "Hallucination is inevitable: An innate limitation of large language models." arXiv:2401.11817 (2024).
- Chang, C. T. et al. "Red teaming ChatGPT in medicine to yield real-world insights on model behavior." npj Digital Medicine 8, 149 (2025).
- Hakim, J. B. et al. "The need for guardrails with large language models in pharmacovigilance and other medical safety critical settings." Sci. Rep. 15, 27886 (2025).
- Meskó, B. & Topol, E. J. "The imperative for regulatory oversight of large language models (or generative AI) in healthcare." npj Digital Medicine 6, 120 (2023).
