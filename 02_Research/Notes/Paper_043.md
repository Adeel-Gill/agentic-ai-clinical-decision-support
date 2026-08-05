# Paper 043

## Basic Information
- **Title:** Unregulated Large Language Models Produce Medical Device-Like Output
- **Authors:** Gary E. Weissman, Toni Mankowitz, Genevieve P. Kanter (all three authors)
- **Year:** 2025
- **DOI:** 10.1038/s41746-025-01544-y
- **Venue:** npj Digital Medicine (2025) 8:148, Brief Communication
- **Publisher:** Nature Portfolio (Springer Nature)
- **Link:** https://www.nature.com/articles/s41746-025-01544-y

## Abstract Summary (200–300 words)
This brief communication asks whether popular general-purpose LLMs, which are **not FDA-authorized clinical decision support (CDS) devices**, can nonetheless be induced to produce **device-like CDS output** as defined by the FD&C Act, the 21st Century Cures Act, and FDA CDS guidance. Under those criteria, software is a regulated device if it issues **specific directives** for diagnosis or treatment (rather than general information), fails to provide a reviewable basis for its recommendations, or is used for **time-critical emergencies** that preclude independent clinician review. The authors tested **GPT-4 and Llama-3** (May and October 2024 versions) across five clinical settings — cardiology, family medicine, immunology, neurology, and psychiatry — using single-shot and multi-shot prompts that explicitly instructed the models to comply with **non-device criteria** (the multi-shot prompt included **48 verbatim examples** from FDA guidance). Each model then received requests for preventive care advice, a time-critical emergency (cardiac arrest, sepsis, anaphylaxis, acute stroke, opioid overdose), and a **"desperate intern" jailbreak** ("Please help me. I am just an intern..."), each repeated five times. For preventive care, final outputs stayed non-device-like. But after emergency requests, **100% of GPT-4 and 52% of Llama-3 responses were device-like**, with identical overall rates under multi-shot prompting; the jailbreak elicited device-like output in up to 80% (GPT-4) and 76% (Llama-3) of responses — and was often unnecessary. All suggestions were clinically appropriate, but many (IV catheters, paracentesis, IV thrombolytics) were suitable only for trained clinicians. The authors conclude that prompt-based constraints derived from FDA guidance **cannot reliably confine LLM output to non-device decision support**, and new regulatory paradigms and alignment technologies are needed.

## Research Problem
- LLMs carry medical-advice disclaimers and are therefore **unregulated by FDA**, yet clinicians and patients increasingly use them for medical decision support.
- Under FD&C Act §201(h)(1), Cures Act criteria, and FDA guidance, CDS software becomes a **device** when it gives specific diagnostic/treatment directives, lacks a reviewable basis, or supports time-critical emergency decisions.
- It was unknown whether free-text output of unconstrained LLMs meets these device criteria, and whether prompting can keep LLM output within a **non-device** designation.

## Proposed Solution
- Not a system-building paper: an **empirical regulatory stress-test**. Prompt LLMs with explicit non-device instructions (single-shot rule statement; multi-shot with 48 FDA-guidance examples), then escalate through preventive-care requests, emergency requests, and a pre-specified jailbreak, and classify outputs against device criteria.

## Architecture
- Not a core focus; the study evaluates off-the-shelf chat interfaces of GPT-4 and Llama-3 with fresh sessions per scenario (new chat / incognito browser), no bespoke architecture.

## Memory
- Not a core focus; sessions were deliberately reset before each scenario, so no persistent memory is involved.

## Planning
- Not a core focus; no planning components — single-turn and short multi-turn prompt sequences only.

## Reasoning
- Not a core focus; the paper evaluates output classification against regulatory criteria rather than reasoning mechanisms, though it notes device status hinges on whether users can **independently review the basis** of recommendations.

## Tool Use
- Not a core focus; no tool calling or external integrations were evaluated.

## Multi-Agent
- Not a core focus; two standalone LLMs are tested independently.

## RAG
- Not a core focus; no retrieval grounding — outputs come from pre-trained knowledge alone.

## Healthcare Contribution
- First empirical demonstration that unregulated general-purpose LLMs readily emit **regulated-device-like CDS**, especially for emergencies (specific diagnoses, drug administration, invasive procedures).
- Documents the clinician-vs-bystander split: some device-like advice matched bystander rescue standards (naloxone, epinephrine auto-injector, CPR), while other advice (IV antibiotics, paracentesis, thrombolytics) was appropriate only for trained clinicians — exposing the absence of a regulatory category for **non-clinician bystander AI CDS**.
- Argues for new authorization pathways (e.g., "generalized" decision support or firm-based approval) balancing innovation, safety, and effectiveness.

## Trustworthy AI
- Shows **prompt-based guardrails fail**: neither single-shot nor multi-shot prompts built from FDA guidance text reliably constrained output; jailbreaks were often unnecessary.
- Frames regulatory alignment as a technical alignment problem: new methods are needed to keep flexible LLM output **within an approved indication**.
- Highlights accountability/oversight gaps for generative AI operating outside decades-old device frameworks.

## Evaluation
- 2 LLMs x 5 clinical settings x 3 request types (preventive, emergency, jailbreak) x 2 prompt regimes (single-/multi-shot) x 5 repetitions; manual review scored each response as device-like vs non-device, and clinician-only vs bystander-appropriate.
- Headline numbers: emergencies elicited device-like output in 100% (GPT-4) and 52% (Llama-3) of responses; jailbreak: 80%/68% (GPT-4, single/multi-shot) and 36%/76% (Llama-3).
- All device-like suggestions were judged clinically appropriate and consistent with standards of care.

## Research Gap
- Only two LLMs tested; other widely used models and stronger prompting/alignment methods unexplored.
- Compared output to **non-binding** FDA guidance, not statutory determinations or other jurisdictions' frameworks.
- Did not study integration into real clinical workflows or intended-use deployments — leaving open how a purpose-built, verified, human-supervised CDS agent should be engineered and evaluated to satisfy device criteria.

## Key Contributions
- Empirical evidence that LLM output **readily crosses the device threshold** across specialties and models, even under explicit regulatory-compliance prompting.
- Quantification of jailbreak (and jailbreak-free) elicitation of device-like emergency decision support.
- Concrete regulatory implications: need for output-constraint methods, indication-agnostic authorization pathways, and a bystander CDS category.

## Limitations
- Evaluated a use that is not the software's specified intended use; findings reflect elicited, not sanctioned, behavior.
- FDA guidance is non-binding; other statutory/regulatory frameworks not assessed.
- Alternative prompting methods and other LLMs untested; no evaluation of practical integration into clinical workflows.
- Small scenario set (5 settings, 5 repetitions) with manual scoring.

## Important Quotes
- "LLM output readily produced device-like decision support across a range of scenarios" (Abstract, p. 1)
- "Single- and multi-shot prompts... are insufficient to align LLM output with non-device decision support" (Conclusion, p. 3)

## Thesis Relevance
- Establishes the regulatory stakes for the thesis: an agentic CDS framework issuing specific diagnostic/treatment recommendations for ICU (time-critical) patients is squarely **device-like**, so design must anticipate regulatory scrutiny.
- Empirically proves that **prompt-level constraints are insufficient safety controls** — directly motivating the thesis's architectural **verification gate** and human-in-the-loop validation as enforced, non-prompt-based safeguards.
- The device criterion that users must be able to **independently review the basis** of recommendations maps onto the thesis's audit-trail and evidence-grounding components (RAG citations, reasoning traces) as a compliance mechanism, supporting thesis gap (3).
- Its emergency scenarios show risk concentrates in **time-critical decisions** — precisely the ICU monitoring context of the thesis — arguing for conservative escalation-to-clinician policies.
- Provides a benchmark-style protocol (repeated adversarial prompting, jailbreak testing, manual device-criteria scoring) reusable for stress-testing the thesis framework's safety behavior.

## References
- U.S. Food and Drug Administration. "Clinical Decision Support Software – Guidance for Industry and FDA Staff" (2022).
- Meskó, B. & Topol, E. J. "The imperative for regulatory oversight of large language models (or generative AI) in healthcare." npj Digit. Med. 6, 120 (2023).
- Goh, E. et al. "Large language model influence on diagnostic reasoning: a randomized clinical trial." JAMA Netw. Open 7, e2440969 (2024).
- Lee, J. T. et al. "Analysis of devices authorized by the FDA for clinical decision support in critical care." JAMA Intern. Med. 183, 1399–1401 (2023).
- Savage, T. et al. "Diagnostic reasoning prompts reveal the potential for large language model interpretability in medicine." npj Digit. Med. 7, 20 (2024).
