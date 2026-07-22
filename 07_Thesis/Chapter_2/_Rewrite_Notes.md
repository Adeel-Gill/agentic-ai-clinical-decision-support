# Chapter 2 — Rewrite Notes

These notes track the de-AI'ing / citation pass on Chapter 2. Revised files are created as
`*_Revised.md` siblings so the originals stay intact for comparison. Style rules come from
`REVIEW/Style_And_Citation_Keys.md` (vary sentence length, <20% bullets, kill banned openers,
one critical sentence per subsection, active voice, US spelling, cite only canonical keys).

## (a) Files rewritten in this pass

- `Agentic_AI.md` → `Agentic_AI_Revised.md`
- `Trustworthy_AI_in_Clinical_Decision_Support.md` → `Trustworthy_AI_in_Clinical_Decision_Support_Revised.md`
- `Clinical_Decision_Support.md` → `Clinical_Decision_Support_Revised.md`
- `Retrieval_Augmented_Generation_in_Healthcare_AI.md` → `Retrieval_Augmented_Generation_in_Healthcare_AI_Revised.md`

## (b) Files that still need the same treatment

The following Chapter 2 section files remain in their original list-heavy, uncited draft form
and should get a `_Revised.md` sibling with the same rules applied. Ordered by priority.

| File | Why it needs work | Suggested citations to add |
|---|---|---|
| `AI_in_Healthcare.md` | Broad, list-heavy overview; almost no inline citations. | `thirunavukarasu2023llms`, `zhou2024survey`, `singhal2023clinical`, `tu2024generalist` |
| `Large_Language_Models_in_Healthcare.md` | Describes Med-PaLM / clinical LLMs without keys; needs critical read. | `singhal2023clinical`, `singhal2025medpalm2`, `tu2024generalist`, `thirunavukarasu2023llms`, `jin2021medqa` |
| `LLM_Based_Agents.md` | Core agent concepts uncited (ReAct, Reflexion, Toolformer, Voyager). | `yao2023react`, `shinn2023reflexion`, `schick2023toolformer`, `wang2023voyager`, `wei2022chain` |
| `Agentic_AI_Frameworks.md` | Lists AutoGen/CAMEL/MetaGPT/Generative Agents as bullets; no keys, no critique. | `wu2024autogen`, `li2023camel`, `hong2024metagpt`, `park2023generative`, `sapkota2025agents` |
| `Taxonomy_of_LLM_Based_Agents.md` | Taxonomy prose is descriptive, not critical; reconcile with taxonomy figure. | `xi2023rise`, `wang2024survey`, `sapkota2025agents` |
| `Large_Language_Models_in_Healthcare.md` benchmark refs | Add MedQA / AMIE / AgentClinic / EHRAgent where evaluation is discussed. | `jin2021medqa`, `tu2025amie`, `schmidgall2024agentclinic`, `shi2024ehragent` |
| `Chapter_Summary.md` | Should be rewritten last, once all sections are final, to reflect the critical framing. | (synthesis; cite sparingly) |

Do NOT touch `Research_Gap.md` or `Research_Gap_Analysis.md` — another agent owns those.
`Chapter_2.md` (the 2.1 intro) reads reasonably well already; a light pass to add one critical
sentence and trim the "comprehensive review" throat-clearing would be enough.

Reconciliation still pending (from the style guide, for whoever finishes the matrix):
P016/P017 are the same paper (keep P016); P018 row must be remapped to `jimenez2023trustworthy`
(the stored PDF), not the "monoids" text; MedAgents year = 2024 everywhere.

## (c) Five before/after AI-tell fixes

1. **Banned opener → concrete claim.**
   - Before: "Agentic AI represents the next evolution of intelligent systems by enabling
     autonomous agents to reason, plan, collaborate..." (Chapter_1, and echoed in Agentic_AI.md)
   - After: "Agentic AI reframes the model as one component inside a larger loop rather than the
     whole system. An agent perceives its environment, reasons about a goal, plans a sequence of
     steps, calls external tools... [xi2023rise; wang2024survey]."
   - Why: "represents the next evolution" is an explicitly banned filler opener and reads as
     generated boilerplate; replaced with an actor-driven, cited claim.

2. **Uncited name-drop list → cited, critical prose.**
   - Before: "MedAgents introduced collaborative medical reasoning... MedRAG combined retrieval...
     Agent Hospital explored... Clinical Camel investigated..." (four parallel bullets, no sources).
   - After: Each is cited and assessed for what it does *not* do — e.g., "MedAgents ... though its
     evaluation centers on question answering rather than on monitoring a patient over time
     [tang2024medagents]." Adds `[zhao2025medrag]`, `[li2024agenthospital]`, `[toma2023clinicalcamel]`.
   - Why: parallel uncited bullets are a strong AI tell and violate the citation + critique rules.

3. **Uniform hedge cadence → varied sentence rhythm.**
   - Before: repeated "Although X, Y remain..." / "However, Z..." sentences of near-identical length
     (e.g., the Agentic_AI.md challenges section, five same-shaped paragraphs).
   - After: mixed short and long sentences — "Reliability is the first: agents can generate
     unsupported recommendations, and in medicine such errors reach the patient." followed by longer
     analytical sentences, closing on a blunt short one.
   - Why: uniform paragraph length and repeated connectives are classic detector signals.

4. **Bullet dump → argued prose.**
   - Before: "Agentic AI extends LLM capabilities by integrating additional components such as:"
     followed by a 7-item bullet list (memory, planning, reasoning, tools, RAG, collaboration, reflection).
   - After: folded into a sentence that also makes the point *why* — "these components are not merely
     accumulated; they are what convert a response generator into a system that can pursue a goal
     [yao2023react; shinn2023reflexion; lewis2020rag]" with a critical follow-up on added failure modes.
   - Why: keeps bullets under ~20% of the section and replaces a list with an argument.

5. **Empty summary claim → honest limitation.**
   - Before: "By retrieving verified clinical evidence before generating a response, RAG reduces the
     probability of unsupported recommendations." (stated as if the problem is solved).
   - After: "It does not eliminate it: a model can still misread, over-generalize, or selectively use
     a correctly retrieved passage, so retrieval lowers the hallucination rate without driving it to
     zero, and clinical use has to be designed around the residue."
   - Why: adds the required critical sentence and removes the overclaiming tone that reads as generated.
