# Plagiarism / Similarity Risk Report (Phase 3)

**No plagiarism is asserted.** This report flags passages *likely to score high similarity* in Turnitin/iThenticate because they (a) reproduce standard, widely‑copied descriptions of well‑known systems without citation, (b) repeat internally across files, or (c) contain near‑verbatim source‑abstract text. Each item gives file, heading, reason, risk, and a rewrite **strategy** (not a rewrite).

**Risk key:** HIGH = likely > 2 % single‑source or clearly matchable · MEDIUM = matchable phrasing, reducible by paraphrase+cite · LOW = original or already reworded.

---

## 1. The three structural drivers of your similarity score

Before the paragraph list, understand *where* the score will come from:

1. **Internal self‑similarity** — the repeated "this research proposes…" paragraph (×7) and the triplicated Taxonomy / Framework / Research‑Gap files. Turnitin counts repeated internal text. **This is your largest and most easily removed source.** (See Review Report §2.)
2. **Uncited canonical descriptions** — ReAct/AutoGen/CAMEL/MetaGPT/RAG/Med‑PaLM descriptions in the un‑revised files read like every other paper's description of them, so they match many sources at once (raises overall %, low per‑source).
3. **Copied abstract sentences in the notes** — the only place with genuine near‑verbatim single‑source text. **This is your largest single‑source (< 2 %) threat** if any of it migrates into the thesis body.

---

## 2. Risky passages — definitions & background

| File | Heading | Reason | Risk | Rewrite strategy |
|---|---|---|---|---|
| `Chapter_2/RAG…AI.md` (orig) | §2.6.1 Concept of RAG | "combines two components: Retriever… Generator…" is the textbook RAG definition, uncited. | MED | Use the Revised version (already cites `lewis2020rag; gao2023rag`); delete original. |
| `Chapter_2/Agentic_AI.md` (orig) | §2.X.1 Intro | Generic Agentic‑AI definition mirrors survey phrasing, uncited. | MED | Superseded by `_Revised` (cited). Delete original. |
| `Chapter_2/Clinical_Decision_Support.md` (orig) | §2.3 intro | Standard CDSS definition ("computer‑based systems designed to assist…"). | MED | Superseded by `_Revised`. Delete original. |
| `Chapter_2/Trustworthy_AI_in_Healthcare.md` | whole | Generic "Trustworthy AI = reliable, transparent, explainable, fair…" definitions, uncited, overlaps the two other 2.8 files. | MED | Merge into `Trustworthy…_Revised`; delete this file. |
| `04_Architecture/Proposed_Framework.md` | §"RAG layer" (L153) | "RAG reduces hallucinations and improves factual accuracy" — canonical claim stated as fact, uncited. | MED | Attribute + hedge (`lewis2020rag`), as the Revised RAG section does. |

---

## 3. Risky passages — literature review of named systems

These describe famous systems in the same terms the field always uses. Uncited, they match many prior sources.

| File | Heading | System(s) | Risk | Rewrite strategy |
|---|---|---|---|---|
| `Chapter_2/Agentic_AI_Frameworks.md` | §2.5.1–2.5.5 | ReAct, AutoGen, CAMEL, MetaGPT, Agent Hospital | **HIGH** | Cite each (`yao2023react`, `wu2024autogen`, `li2023camel`, `hong2024metagpt`, `li2024agenthospital`) and add a *critical* clause per system ("…but its evaluation centers on QA, not monitoring"). The Revised Agentic‑AI section models this. |
| `Chapter_2/LLM_Based_Agents.md` | whole | ReAct, Generative Agents, AutoGen/CAMEL/MetaGPT, RAG | **HIGH** | Rewrite per `_Rewrite_Notes.md`; add `yao2023react`, `park2023generative`, `wu2024autogen`, `li2023camel`, `hong2024metagpt`, `schick2023toolformer`, `wang2023voyager`. |
| `Chapter_2/Taxonomy_of_LLM_Based_Agents.md` | §2.X.2–2.X.7 | all of the above + MedAgents, MedRAG, Med‑PaLM, Clinical Camel | **HIGH** | Cite `xi2023rise`, `wang2024survey`, `sapkota2025agents`; convert per‑paper template into an argued taxonomy; reconcile with `04_Architecture/Taxonomy.md`. |
| `Chapter_2/Large_Language_Models_in_Healthcare.md` | §2.7.1–2.7.4 | Med‑PaLM, Med‑PaLM 2, Med‑PaLM M, Clinical Camel | **HIGH** | Cite `singhal2023clinical`, `singhal2025medpalm2`, `tu2024generalist`, `toma2023clinicalcamel`; the "Major contributions include:" bullet lists especially resemble the papers' own framing — convert to critical prose. |
| `04_Architecture/Taxonomy.md` | per‑paper rows | same set | **HIGH** | Same as above; this file duplicates the Chapter‑2 taxonomy and carries zero citations. |
| `Chapter_2/Agentic_AI.md` (orig) | §2.X.5 | MedAgents, MedRAG, Agent Hospital, Clinical Camel (parallel uncited bullets) | **HIGH** | Superseded — the `_Revised` version already cites and critiques all four. Delete original. |

**Note on the revised files:** `Agentic_AI_Revised`, `Clinical_Decision_Support_Revised`, `RAG…_Revised`, `Trustworthy…_Revised`, `Research_Gap_Analysis`, `02_Research/Research_Gap`, and Chapter 3 all describe the *same* systems but are **LOW risk** — they reword, cite, and add critical judgment. That proves the fix works; apply it to the HIGH rows above.

---

## 4. Risky passages — near‑verbatim source text (single‑source < 2 % threat)

These are in the **research notes**, not the thesis body. They are the most serious single‑source matches and must **not** be pasted forward without quotation + citation.

| File | Line | Near‑verbatim of | Risk | Strategy |
|---|---|---|---|---|
| `Notes/Paper_003.md` | 16 (& 217) | ReAct abstract: "reasoning traces help the model induce, track, and update action plans as well as handle exceptions" | **HIGH** | Paraphrase fully or quote with `[yao2023react]`. |
| `Notes/Paper_004.md` | 243 | Toolformer: "Language models can teach themselves to use external tools via simple APIs" | **HIGH** | Same, `[schick2023toolformer]`. |
| `Notes/Paper_005.md` | 14, 237 | VOYAGER: "the first LLM‑powered embodied lifelong learning agent… without human intervention" | **HIGH** | Same, `[wang2023voyager]`. |
| `Notes/Paper_016.md` & `Paper_017.md` | 16 / 14 | Med‑PaLM M: "in up to 40.50 % of cases, clinicians preferred Med‑PaLM M's outputs… 0.25 clinically significant errors per report" | **HIGH** | Paraphrase; report the statistic with `[tu2024generalist]`. Also de‑duplicate the two notes. |
| `Notes/Paper_011.md` | 200 | Agent Hospital: "simulates the whole closed cycle of treating a patient's illness" (quoted) | MED | Already quoted — ensure the quote marks + cite survive into any prose. |
| `Notes/Paper_019.md` | 12–14, 22, 28 | Clinical Camel abstract fragments — flagged by **orphaned commas** (",." ",,") where source citation superscripts were stripped | **HIGH** | Rewrite in your own words; the comma artifacts are a forensic copy‑paste signature. |
| `Notes/Paper_013.md`, `016`, `017` matrix rows | — | same citation‑strip artifacts | MED | Clean and reword. |

---

## 5. Definitions/explanations repeated internally (self‑similarity)

| Repeated content | Appears in | Risk | Strategy |
|---|---|---|---|
| "this research proposes an Agentic AI Framework… integrates MIMIC‑IV, memory, RAG, agents, trustworthy AI, human validation" | 7 Chapter‑2 files (see Review Report §2.3) | **HIGH** | Keep once in the chapter summary; delete the rest. |
| Evolution narrative rule‑based→ML→DL→LLM | 5 files | MED | State once (in the AI‑in‑Healthcare or Agentic‑AI section); cross‑reference elsewhere. |
| Agent‑role list (Monitoring/Diagnosis/Risk/Treatment/Explanation/Verification) | 5 files + Ch3 | MED | Define once in Chapter 3; in Chapter 2 forward‑reference it. |
| RAG two‑component definition | 4 files | MED | Define once; the Revised RAG section is canonical. |

---

## 6. Bottom line & how to hit the targets

- **Overall < 15 %:** primarily a *deletion* problem, not a rewriting problem. Removing superseded originals + de‑duplicating the boilerplate + citing the canonical descriptions gets you most of the way.
- **Single‑source < 2 %:** driven almost entirely by the copied note abstracts (§4). Keep them out of the body, or quote‑and‑cite. Nothing in the *revised thesis body* currently poses a single‑source threat.
- **Run Turnitin on the `Compiled/` output only**, after items 1–7 of the Review Report, so you are measuring the real submission and not the scaffold.

Feeds `TODO_Plagiarism.md`.
