# TODO — AI‑Writing Remediation

Priority: **Critical / High / Medium / Low.** Source: `AI_Content_Report.md`. Goal: no submitted file carries an AI‑generation signature.

## Critical
- [x] **Delete/archive the superseded AI‑draft originals** — they cannot be fixed, only replaced: `Chapter_1/Chapter_1.md`; `Chapter_2/{Agentic_AI, Clinical_Decision_Support, Retrieval_Augmented_Generation_in_Healthcare_AI, Trustworthy_AI_in_Clinical_Decision_Support}.md`; the stubs `Chapter_2/{Literature_Review, Research_Gap, Taxonomy, Proposed_Framework}.md`. *(2026-08-13: bannered. 2026-08-14: **deleted with author approval** — all 17 bannered files (16 in Chapter_2 plus Chapter_1/Chapter_1.md), each banner verified before removal; recoverable from git history. See `.ai/THESIS_STRUCTURE.md` §7 deletion record.)*
- [ ] **Commit to `Compiled/` as the submission surface** so no HIGH‑AI section file can be graded by mistake.

## High
- [ ] **Apply the `_Rewrite_Notes.md` de‑AI pass** to the six remaining HIGH files: `AI_in_Healthcare.md`, `Large_Language_Models_in_Healthcare.md`, `LLM_Based_Agents.md`, `Agentic_AI_Frameworks.md`, `Taxonomy_of_LLM_Based_Agents.md`, `Chapter_Summary.md`.
- [ ] For each: kill banned openers ("has emerged as", "rapid development of", "represents a shift"); cut bullet lists below 20 % of the section; add one **critical** sentence per subsection; add inline citations.
- [ ] **Rewrite the 20 research notes** in your own words; remove copy‑paste artifacts (orphaned commas in `Paper_019.md`; verbatim abstract lines in `Paper_003/004/005/016/017`).
- [ ] **De‑duplicate the repeated closing paragraph** ("this research proposes…") across the 7 Chapter‑2 files — keep once.

## Medium
- [ ] **Convert Chapter 5 from outline to prose** (remove `*Stub:*` and bullet‑stub form).
- [x] **Update `04_Architecture/Proposed_Framework.md` and `Taxonomy.md`** to de‑AI'd, cited prose, or delete in favor of Chapter 3 / the Chapter‑2 taxonomy. *(Done 2026-08-13: `Proposed_Framework.md` aligned to Chapter 3 with citations at the audit-flagged claims (D4 fix); `Taxonomy.md` bannered as superseded by Compiled §2.5, its figure block given a real caption with an explicit unassigned-number marker.)*
- [ ] **Break over‑long paragraphs** (Chapter_4 §4.2; RAG_Revised §2.6.6; Chapter_3 §3.4.3, §3.5) into 2–3 units.
- [ ] **Decide first‑person vs impersonal voice** and apply consistently (see Writing report §8).

## Low
- [ ] Strip placeholder residue repo‑wide: `2.X` headers, `![alt text](image.png)`, `*See X.md*`, `**Figure 2.X**`.
- [ ] Replace promo adjectives in notes/summaries ("landmark", "seminal", "state‑of‑the‑art", "transformative").
- [ ] Reduce lexical repetition of "comprehensive/intelligent/continuous".
