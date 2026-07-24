# AI‑Generated Writing Detection Report (Phase 2)

**Scale:** LOW = reads as human‑authored / already de‑AI'd · MEDIUM = mixed, needs a pass · HIGH = strong AI‑generation signature.
**Method:** manual read of every section for the tells the project's own `REVIEW/Style_And_Citation_Keys.md` bans — banned openers, uniform sentence length, bullet dumps, uncited name‑drops, formulaic per‑item scaffolds, absence of a critical sentence.

> Important context: the connective‑word abuse people usually screen for ("Moreover/Furthermore/It is important to note") is **only mildly present here** (grep: 35 hits across all 12 Chapter‑2 files). The dominant AI signature in this repository is **structural** — uniform paragraph blocks, bold‑header‑then‑bullet‑list scaffolding, generic openers, and identical closing paragraphs — not connective spam. Do not be reassured by a low "Furthermore" count.

---

## 1. Rating table (every substantive section)

| File / Section | AI Risk | Primary tells |
|---|---|---|
| `07_Thesis/Chapter_1/Chapter_1_Revised.md` | **LOW** | Varied rhythm, actor‑driven sentences, inline citations, honest scope. Model of the target style. |
| `07_Thesis/Compiled/Chapter_1.md` | **LOW** | Same content, assembled. |
| `07_Thesis/Compiled/Chapter_2.md` | **LOW** | De‑AI'd, cited, renumbered. |
| `07_Thesis/Chapter_3/Chapter_3.md` | **LOW** | First‑person design‑science voice, per‑agent contracts, worked trace, hedged bets. Clearly hand‑written. |
| `07_Thesis/Chapter_4/Chapter_4.md` | **LOW** | Reasoned metric rationales, "why this baseline" prose, explicit falsifiability. |
| `07_Thesis/Chapter_2/Agentic_AI_Revised.md` | **LOW** | Critical caveats per subsection, cited. |
| `…/Clinical_Decision_Support_Revised.md` | **LOW** | Argued prose, limitations named. |
| `…/Retrieval_Augmented_Generation_in_Healthcare_AI_Revised.md` | **LOW** | Hedged claims ("lowers hallucination without driving it to zero"). |
| `…/Trustworthy_AI_in_Clinical_Decision_Support_Revised.md` | **LOW** | Each mechanism paired with its limitation. |
| `07_Thesis/Chapter_2/Research_Gap_Analysis.md` | **LOW** | Genuinely critical; refuses the weak "no unified framework" claim. |
| `02_Research/Research_Gap.md` | **LOW** | Three concrete, testable questions; strong. |
| `06_Experiments/Experimental_Design.md`, `Evaluation_Metrics.md` | **LOW** | Reproducible, reasoned. |
| `03_Dataset/Cohort_Definition.md`, `Preprocessing_Pipeline.md` | **LOW** | Concrete, dataset‑specific. |
| `04_Architecture/System_Design.md`, `Technical_Feasibility.md` | **LOW** | Hedged engineering trade‑offs. |
| `07_Thesis/Chapter_2/Chapter_2.md` (§2.1 intro) | **MEDIUM** | Some "comprehensive review" throat‑clearing; otherwise fine (Compiled version already fixes it). |
| `07_Thesis/Chapter_5/Chapter_5.md` | **MEDIUM** | Explicitly a stub outline — not AI‑generated, but bullet‑stub form + "*(pending)*" markers cannot be submitted as prose. |
| **`07_Thesis/Chapter_1/Chapter_1.md`** | **HIGH** | `*See Problem_Statement.md*` placeholders; banned opener "Agentic AI represents the next evolution…" (L11 original). Superseded. |
| **`07_Thesis/Chapter_2/Agentic_AI.md`** | **HIGH** | Bullet dump of 7 capabilities (L23‑31); five same‑shaped "challenge" blocks; uncited. |
| **`07_Thesis/Chapter_2/AI_in_Healthcare.md`** | **HIGH** | "has emerged as a transformative technology" (L3); bold‑header + 3‑sentence block template ×12; zero citations. |
| **`…/Large_Language_Models_in_Healthcare.md`** | **HIGH** | Per‑model template (Med‑PaLM / 2 / M / Clinical Camel) each "Major contributions include:" + bullets; 10‑item application bullet list (L86‑97); zero citations. |
| **`…/LLM_Based_Agents.md`** | **HIGH** | Eight uniform ~5‑sentence paragraphs; "brain, perception, action" definition uncited; name‑drops ReAct/Generative Agents/AutoGen/CAMEL/MetaGPT/RAG with no keys. |
| **`…/Agentic_AI_Frameworks.md`** | **HIGH** | Per‑framework template (intro → bullets → ASCII diagram → "However, challenges remain"); "rapid development of LLMs has transformed…" (L3); zero citations. |
| **`…/Taxonomy_of_LLM_Based_Agents.md`** | **HIGH** | Unresolved `2.X` headers; per‑paper "X introduced… This concept is valuable for healthcare because…" scaffold; zero citations. |
| **`…/Trustworthy_AI_in_Healthcare.md`** | **HIGH** | Eight near‑equal paragraphs, one per virtue; generic "high‑risk domain" framing; uncited. |
| **`…/Trustworthy_AI_in_Clinical_Decision_Support.md`** (original) | **HIGH** | Bold‑header + bullet template; superseded by Revised. |
| **`…/Clinical_Decision_Support.md`** (original) | **HIGH** | Component list template; superseded by Revised. |
| **`…/Retrieval_Augmented_Generation_in_Healthcare_AI.md`** (original) | **HIGH** | Overclaim "RAG reduces the probability of unsupported recommendations" stated as solved; superseded. |
| **`07_Thesis/Chapter_2/Chapter_Summary.md`** | **HIGH** | Pure name‑drop recap ("ReAct, AutoGen, CAMEL, MetaGPT, Toolformer… were analyzed"); no critical content; uncited. |
| **`04_Architecture/Proposed_Framework.md`** | **HIGH** | One‑line‑intro + bullet per section; literal `![alt text](image.png)` placeholder (L384); uncited overclaims. |
| **`04_Architecture/Taxonomy.md`** | **HIGH** | `Figure 2.X` placeholder, `![alt text](image-1.png)`; per‑paper template; uncited. |
| **`02_Research/Notes/Paper_001–020`** | **HIGH** | Formulaic "This paper/survey provides a comprehensive and systematic…" openers; promo phrasing ("landmark", "state‑of‑the‑art"); emoji star‑ratings; orphaned‑comma copy‑paste artifacts (see Plagiarism report). |

**Tally:** LOW ≈ 20 files/sections · MEDIUM ≈ 2 · HIGH ≈ 15 (11 thesis‑body drafts + 2 architecture + notes as a block).

---

## 2. Why the HIGH files read as AI‑generated (evidence)

1. **Banned opener boilerplate.** "has emerged as a transformative technology in healthcare" (`AI_in_Healthcare.md:3`), "The rapid development of Large Language Models has transformed…" (`Agentic_AI_Frameworks.md:3`), "Agentic AI represents a shift from passive AI assistants toward proactive intelligent systems" (`Agentic_AI.md:9`). These are exactly the openers the project's own style guide bans.
2. **Bullet dumps replacing argument.** `Agentic_AI.md:23‑31` lists seven capabilities as bullets instead of explaining why they compose; `Large_Language_Models_in_Healthcare.md:86‑97` is a 10‑item application list. Style rule: bullets < 20 % of a section.
3. **Uniform paragraph geometry.** `Trustworthy_AI_in_Healthcare.md` is eight paragraphs of near‑identical length, one per virtue — the signature "even block" rhythm of generated prose.
4. **Per‑item templates.** Every framework in `Agentic_AI_Frameworks.md` follows intro → bullet list → ASCII diagram → "However, challenges remain regarding…". Every paper note follows the same heading skeleton verbatim.
5. **No critical sentence.** The HIGH files describe and praise; they never say what a system *fails* to do. The LOW files always land a critical/limiting sentence per subsection — the clearest human‑vs‑generated discriminator in this repository.
6. **Uncited claims.** Zero inline citations in any HIGH thesis‑body file, including specific empirical claims ("RAG reduces hallucinations and improves factual accuracy", `Proposed_Framework.md:153`).
7. **Placeholder residue.** `*See X.md*` (`Chapter_1.md`), `2.X` headers, `![alt text](image.png)`, "**Figure 2.X**" — machine scaffolding never cleaned up.

---

## 3. What "good" looks like here (use as your rewrite target)

The `_Revised` files already demonstrate the fix. Compare, on the same topic:

- **Before (HIGH):** "Agentic AI represents a shift from passive AI assistants toward proactive intelligent systems capable of continuous interaction and decision‑making." (`Agentic_AI.md:9`)
- **After (LOW):** "Large Language Models made text generation cheap and fluent, and in doing so they exposed how little fluency alone accomplishes when a task requires acting over time. Out of that gap grew Agentic AI: systems that do not merely produce text but analyze a situation, form a plan, take actions, and adjust when the environment answers back [xi2023rise; wang2024survey]." (`Agentic_AI_Revised.md:5`)

The `_Rewrite_Notes.md` file already records five such before/after fixes and the rule set. **Apply that same pass to the six remaining HIGH sections and the AI‑detection risk collapses.**

---

## 4. Priority (feeds `TODO_AI.md`)

1. **Delete the superseded originals** (they cannot be "fixed" — they are replaced).
2. **De‑AI the six un‑revised sections** listed HIGH above, using `_Rewrite_Notes.md` (b) as the work order.
3. **Rewrite the paper notes** in your own words or mark direct quotes (they are internal, but their text has leaked patterns and would fail if pasted forward).
4. **Convert Chapter 5** from outline to prose.
5. **Strip placeholder residue** repo‑wide (`2.X`, `alt text`, `*See …*`).
