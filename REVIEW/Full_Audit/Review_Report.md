# Master Review Report

**Thesis:** *An Agentic AI Framework for Intelligent Patient Monitoring and Clinical Decision Support*
**Author:** Adeel Gill · Roll SU92‑MSAIW‑S25‑011 · The Superior University, Lahore
**Audit date:** 2026‑07‑24
**Reviewer role:** Senior Academic Reviewer / Thesis Editor / Research‑Integrity Auditor
**Standard applied:** Turnitin reviewer + MS thesis examiner + IEEE reviewer + research supervisor
**Targets:** overall similarity < 15 %, single‑source similarity < 2 %, prose reads as naturally human‑written.

> This is a **review report only**. Nothing in the thesis was rewritten or modified. All eight report files plus four TODO lists live in `REVIEW/Full_Audit/`. This report is the umbrella; the per‑phase reports carry the detail.

---

## 0. Headline verdict (brutally honest)

The repository is **two theses wearing one coat**.

- A **strong, genuinely human‑sounding, well‑cited core** — Chapter 1 (Revised), Chapter 3, Chapter 4, the `Compiled/` build, the four `_Revised.md` Chapter 2 sections, `Research_Gap_Analysis.md`, `02_Research/Research_Gap.md`, and the `03_Dataset` / `06_Experiments` / `System_Design` / `Technical_Feasibility` documents. This material is examiner‑grade: varied sentence rhythm, critical framing, honest limitations, inline citations.
- A **weak, obviously AI‑generated, uncited scaffold** still sitting beside it — the *original* Chapter 2 section files, `04_Architecture/Proposed_Framework.md`, `04_Architecture/Taxonomy.md`, the one‑line stubs, and the 20 literature notes. This material is list‑dominant, formulaic, uncited, and in places copied near‑verbatim from source abstracts.

**The single biggest risk to your submission is not that the good writing is bad — it is that the bad drafts are still in the repository, un‑deleted, competing with the good ones for the same section numbers.** A Turnitin pass or an examiner who opens the wrong file will judge you on the scaffold, not the core.

This audit **confirms and extends** the prior `REVIEW/00_Examiner_Report.md` (score ≈ 46/100, "not approvable as a completed MS thesis; a strong design/proposal milestone"). Nothing here contradicts it. The empirical gap it flagged (no prototype, no results) remains the deepest problem, but that is out of scope for a plagiarism/AI/writing audit and is noted only for completeness.

---

## 1. What was scanned (Phase 1 coverage)

Every Markdown file under `07_Thesis/` and `02_Research/` was read in full, plus `04_Architecture/`, `06_Experiments/`, `03_Dataset/`, the prior `REVIEW/` folder, `References.bib`, and `07_Thesis/Compiled/build_thesis_docx.py`.

| Area | Files | State |
|---|---|---|
| Chapter 1 | `Chapter_1.md` (stub), `Chapter_1_Revised.md` (full), 4 sub‑files, `Compiled/Chapter_1.md` | Revised/Compiled are canonical; `Chapter_1.md` is superseded |
| Chapter 2 | 20 section files incl. 4 `_Revised` pairs + 3 stubs, `Compiled/Chapter_2.md` | Half revised, half AI‑draft; Compiled is canonical |
| Chapter 3 | `Chapter_3.md` | Strong, complete, cited |
| Chapter 4 | `Chapter_4.md` | Strong evaluation *design* (no results) |
| Chapter 5 | `Chapter_5.md` | Explicit stub/outline ("to be completed after Ch4 results") |
| Research | 20 notes, Literature Matrix (×4), `Research_Gap.md` | Matrix solid; notes AI‑generated with copy artifacts |
| Architecture | `Proposed_Framework.md`, `Taxonomy.md` (stale) + `System_Design.md`, `Technical_Feasibility.md` (revised) | Mixed |

---

## 2. Duplicated content — the master list (Phase 1)

This is the most consequential Phase‑1 finding. There are **five kinds of duplication**, and every one of them is fixable by deletion or consolidation, not rewriting.

### 2.1 Parallel "original vs `_Revised`" file pairs (superseded drafts still present)

| Canonical (keep) | Superseded (delete/archive) |
|---|---|
| `07_Thesis/Chapter_1/Chapter_1_Revised.md` | `07_Thesis/Chapter_1/Chapter_1.md` (still uses `*See X.md*` placeholders) |
| `07_Thesis/Chapter_2/Agentic_AI_Revised.md` | `07_Thesis/Chapter_2/Agentic_AI.md` |
| `07_Thesis/Chapter_2/Clinical_Decision_Support_Revised.md` | `07_Thesis/Chapter_2/Clinical_Decision_Support.md` |
| `07_Thesis/Chapter_2/Retrieval_Augmented_Generation_in_Healthcare_AI_Revised.md` | `…Retrieval_Augmented_Generation_in_Healthcare_AI.md` |
| `07_Thesis/Chapter_2/Trustworthy_AI_in_Clinical_Decision_Support_Revised.md` | `…Trustworthy_AI_in_Clinical_Decision_Support.md` |

### 2.2 Triplicated / duplicated section artifacts

- **Taxonomy — triplicated:** full copy in `04_Architecture/Taxonomy.md`, full copy in `07_Thesis/Chapter_2/Taxonomy_of_LLM_Based_Agents.md`, and a 1‑line stub `07_Thesis/Chapter_2/Taxonomy.md`. Same six dimensions, same example papers, near‑identical mapping table.
- **Proposed Framework — triplicated:** `04_Architecture/Proposed_Framework.md` (stale, 7 agents), `07_Thesis/Chapter_3/Chapter_3.md` (canonical, 8 agents), and a 1‑line stub `07_Thesis/Chapter_2/Proposed_Framework.md`.
- **Research Gap — triplicated:** `02_Research/Research_Gap.md` (full, three‑question framing), `07_Thesis/Chapter_2/Research_Gap_Analysis.md` (full, three‑gap framing, cited), 1‑line stub `07_Thesis/Chapter_2/Research_Gap.md`. The two full versions cover the **same three gaps** (exam‑QA evaluation; retrieval not patient‑grounded; verification/audit not first‑class) in different words.
- **Trustworthy AI — three overlapping files all numbered "2.8":** `Trustworthy_AI_in_Healthcare.md`, `Trustworthy_AI_in_Clinical_Decision_Support.md`, and its `_Revised` sibling.
- **Literature Review stub:** `07_Thesis/Chapter_2/Literature_Review.md` is a single sentence duplicating the intent of `Chapter_2.md` §2.1.
- **Med‑PaLM M written twice:** `02_Research/Notes/Paper_016.md` and `Paper_017.md` are the same paper ("Towards Generalist Biomedical AI"), with a shared verbatim result sentence ("in up to 40.50 % of cases … 0.25 clinically significant errors per report"). The Matrix itself logs this but the note files remain duplicated.

### 2.3 Repeated **paragraph / boilerplate** (near‑verbatim within Chapter 2)

The **closing "this research proposes…" paragraph** is repeated with only cosmetic changes at the end of at least seven Chapter‑2 section files: `Agentic_AI.md` §2.X.7, `Large_Language_Models_in_Healthcare.md` §2.7.7, `Agentic_AI_Frameworks.md` §2.5.7, `LLM_Based_Agents.md` (final para), `Taxonomy_of_LLM_Based_Agents.md` §2.X.8, `Trustworthy_AI_in_Clinical_Decision_Support.md` §2.8.7, `Retrieval_Augmented_Generation_in_Healthcare_AI.md` §2.6.7. Each lists the same six integrations (MIMIC‑IV, memory, RAG, agents, trustworthy AI, human validation). **When these sections are concatenated into one chapter, Turnitin will see the same paragraph ~7 times — internal self‑similarity that inflates the score.**

### 2.4 Repeated **ideas / explanations / definitions**

- **The "rule‑based → machine learning → deep learning → LLM → Agentic AI" evolution narrative** is retold in at least five places: `AI_in_Healthcare.md` §2.2.1, `Agentic_AI.md` §2.X.2 (and its Revised sibling), `Clinical_Decision_Support.md` §2.3.1, `LLM_Based_Agents.md`, `Large_Language_Models_in_Healthcare.md` intro.
- **The specialized‑agent role list** (Monitoring / Diagnosis / Risk / Treatment / Explanation / Verification) is defined in `Agentic_AI.md` §2.X.3, `Clinical_Decision_Support.md` §2.3.5, `Retrieval_Augmented_Generation_in_Healthcare_AI.md` §2.6.3 (table), `Agentic_AI_Frameworks.md`, and again in Chapter 3. In the literature‑review chapter this belongs **once**, forward‑referenced to Chapter 3.
- **The RAG definition** ("retriever + generator; grounds output in evidence; reduces hallucination") is given in full in `RAG.md` §2.6.1, `LLM_Based_Agents.md`, `Agentic_AI_Frameworks.md`, and `Taxonomy_of_LLM_Based_Agents.md`.

### 2.5 Section‑numbering collisions (a duplication symptom)

Unresolved `2.X` placeholders in `Agentic_AI.md`, `LLM_Based_Agents.md`, `Taxonomy_of_LLM_Based_Agents.md`; **two files numbered 2.8**; missing 2.4; the `Compiled/Chapter_2.md` uses a *different, correct* numbering. → See Consistency Report.

---

## 3. Phase summaries (detail in the linked reports)

| Phase | Report | One‑line verdict |
|---|---|---|
| 2 — AI writing | `AI_Content_Report.md` | ~13 files HIGH AI‑risk (all the un‑revised drafts + notes); the revised core is LOW. |
| 3 — Plagiarism risk | `Plagiarism_Risk_Report.md` | HIGH textual‑similarity risk in uncited framework/paper descriptions and in copied note abstracts; revised files LOW. |
| 4 — Writing quality | `Writing_Quality_Report.md` | Core is publishable; stubs and drafts drag the average; a few over‑long paragraphs in the good files. |
| 5 — Consistency | `Consistency_Report.md` | 5 real inconsistencies: agent count (7 vs 8), RQ schemes (5 vs 3, Ch1 vs Ch4), cohort labels vs tasks, stale architecture doc, "five/six" taxonomy. |
| 6 — Citations | `Citation_Audit.md` | `jimenez2023trustworthy` is an unverified placeholder cited 8×; whole `.bib` needs a verification pass; un‑revised files carry zero citations. |
| 7 — Originality | `Improvement_Checklist.md` | Integrative gap is defensible; boost originality via comparison tables, critical analysis, your own framework discussion. |
| Scores | `Repository_Scorecard.md` | Blended ≈ 5.6/10; core alone ≈ 7.5/10; scaffold ≈ 3/10. |

---

## 4. TOP 20 improvements before submission (ranked by impact)

Ranked by *impact on the stated targets* (similarity < 15 %, single‑source < 2 %, human‑sounding, examiner‑ready). **C = Critical, H = High, M = Medium.**

| # | Pri | Action | Why it matters | Effort |
|---|---|---|---|---|
| 1 | **C** | **Delete or move to an `_archive/` folder every superseded original** (§2.1): `Chapter_1.md`, `Agentic_AI.md`, `Clinical_Decision_Support.md`, `RAG…AI.md`, `Trustworthy…Support.md`, plus the three 1‑line stubs and `Literature_Review.md`. | Removes ~11 AI‑generated, uncited, high‑similarity files from the submission surface in one move. Biggest single risk reduction. | 30 min |
| 2 | **C** | **Verify `jimenez2023trustworthy` against the real P018 PDF** and replace the placeholder `.bib` entry (currently "Jimenez‑Luna, Jose and others / arXiv (TODO‑VERIFY)"). It is cited ~8× across Ch2–5. | An unverifiable reference on 8 claims reads as a fabricated citation to an examiner — the worst integrity finding. | 1 hr |
| 3 | **C** | **Run a full `.bib` verification pass** (every entry has a "verify before submission" note); confirm DOIs/venues, especially `tu2025amie` (venue TODO). | Fabricated/wrong citations are the fastest route to a viva failure. | 3–4 hr |
| 4 | **C** | **Choose ONE canonical Chapter 2** — the `Compiled/Chapter_2.md` path — and treat the section files as source only. | Prevents the same paragraph appearing 7× (self‑similarity) and fixes numbering. | 1 hr decision |
| 5 | **C** | **De‑duplicate the closing "this research proposes…" boilerplate** (§2.3): keep it once (chapter summary), delete the six repeats. | Directly attacks internal self‑similarity that inflates the Turnitin score. | 1 hr |
| 6 | **H** | **Finish the `_Revised` treatment for the still‑AI sections**: `AI_in_Healthcare`, `Large_Language_Models_in_Healthcare`, `LLM_Based_Agents`, `Agentic_AI_Frameworks`, `Taxonomy_of_LLM_Based_Agents`, `Chapter_Summary` (per `_Rewrite_Notes.md`). | These are the remaining HIGH AI‑risk + zero‑citation files. | 1–2 days |
| 7 | **H** | **Add inline citations to every framework/paper description** (ReAct, AutoGen, CAMEL, MetaGPT, MedAgents, MedRAG, Med‑PaLM, Clinical Camel, Agent Hospital). | Uncited canonical descriptions are the highest paraphrase‑plagiarism risk. | 1 day |
| 8 | **H** | **Reconcile the agent count**: replace every "seven‑agent" with "eight specialized agents" (Ch3 L41, L137; `System_Design` L143; `Technical_Feasibility` L7/§10) OR justify the count. | Internal contradiction an examiner will catch in 60 seconds. | 30 min |
| 9 | **H** | **Update `04_Architecture/Proposed_Framework.md`** to add the Data/Retrieval Agent + Memory‑Manager, or delete it and point to Chapter 3. | It is stale (7 agents) and contradicts the canonical Chapter 3. | 1 hr |
| 10 | **H** | **Reconcile the two RQ schemes**: Chapter 1's five RQs vs the research‑gap files' three questions; and fix the Ch4/experiments RQ numbering that reuses "RQ1–RQ5" with different meanings. | A thesis with two incompatible RQ sets fails the consistency bar. | 2–3 hr |
| 11 | **H** | **Align cohort labels with experiment tasks**: `Cohort_Definition.md` (prolonged‑LOS) vs `Experimental_Design.md` T2 (ICU transfer/escalation) do not match. | Reproducibility/validity red flag in the methodology chapters. | 1 hr |
| 12 | **H** | **Fix the Med‑PaLM M duplicate note** (Paper_016 = Paper_017) and the wrong Paper_018 (category‑theory maths paper). | Research‑record integrity; the notes underpin the matrix. | 1 hr |
| 13 | **M** | **Standardize citation format** to one style: source files use `[a; b]`, `Compiled/` uses `[a][b]`. Pick one. | Consistency; avoids the build script mis‑numbering. | 1 hr |
| 14 | **M** | **Sync the two reference stores**: `References.bib` (45 entries) and the IEEE dict in `build_thesis_docx.py` must match key‑for‑key. | The build silently prints "[MISSING REFERENCE]" for any key only in one store. | 1 hr |
| 15 | **M** | **Update `REVIEW/Style_And_Citation_Keys.md`** — its canonical key table is 11 keys behind `References.bib` (missing the stats/methodology keys). | Prevents future work wrongly flagging valid keys as invalid. | 30 min |
| 16 | **M** | **Break the over‑long paragraphs** in the good files (e.g., `RAG…_Revised` §2.6.6; `Chapter_4` §4.2; `Chapter_3` §3.4.3) into 2–3 units each. | Readability; single 200‑word paragraphs read as machine‑generated even when the prose is good. | 2 hr |
| 17 | **M** | **Add 2–3 original comparison tables** (see Improvement Checklist): capability matrix of prior systems vs your five differentiators; layer‑to‑RQ map. | Raises originality; tables are near‑zero similarity and show synthesis. | 3 hr |
| 18 | **M** | **Write Chapter 5 in full prose** (currently a stub outline) once Ch4 numbers exist; convert the bullet stubs to argued paragraphs. | An outline chapter cannot be submitted. | 1 day |
| 19 | **M** | **Resolve the P017 key collision** (Matrix reassigns it to `singhal2023clinical`, already P013's key) — either a new key or drop the row. | Duplicate keys corrupt the numbered reference list. | 30 min |
| 20 | **M** | **Decide first‑person vs impersonal voice** and apply uniformly (Ch3/Ch4 use "I adopt…"; Ch2 is impersonal). | Voice whiplash across chapters reads as different authors / different tools. | 2 hr |

**Do 1–5 first.** They are cheap, they are deletions and verifications rather than writing, and together they move the similarity and integrity risk more than anything else on the list.

---

## 5. How this maps to your numeric targets

- **Overall < 15 %:** achievable. Most similarity today is *internal self‑similarity* (repeated boilerplate, duplicate files) plus generic uncited descriptions. Items 1, 4, 5, 6, 7 remove the bulk of it.
- **Single‑source < 2 %:** the live threat is the **copied abstract sentences in the notes** (ReAct, Toolformer, VOYAGER, Med‑PaLM M) — keep them out of the thesis body, and quote‑and‑cite anything you do use. See Plagiarism Risk Report.
- **Human‑sounding:** the revised core already passes; finishing item 6 removes the detector‑bait scaffold.

See `Repository_Scorecard.md` for scores and `Improvement_Checklist.md` for the originality work.
