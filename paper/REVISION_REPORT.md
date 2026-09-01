# Plagiarism-Risk & AI-Style Revision Report

**Date:** 2026-08-08 · **Scope:** full manuscript revision per the plagiarism-risk review and
AI-content risk review briefs. Objective was genuine academic originality and author-driven
prose — not detector evasion. No numbers, findings, architecture, or citations were changed.

---

## A. What was revised (change log)

### Related Work — rewritten in full (highest priority)
| Location | Change | Type | Citations |
|---|---|---|---|
| Section intro (new) | Added a framing paragraph organizing the review around four research questions (how agents are built / what medical agents do / what retrieval is grounded in / how trust is established) instead of a system-by-system tour | Structural synthesis | n/a |
| 2.1 (now "How Agents Are Built") | "X introduced, Y developed" catalog replaced by a three-wave narrative (single-agent competencies → coordination-logic placement → consolidation into taxonomies/protocols); added author-voice closing on why infrastructure maturity cuts both ways | Synthesis + author reasoning | all 12 retained, same order |
| 2.2 (now "What Medical Agents Do") | Paper-per-clause list replaced by a comparison of *what each system externalizes* (deliberation, record access, computation, interaction policy); the shared unstated assumption ("the patient exists only for the duration of a prompt") is now the analytical spine | Critical comparison | all 15 retained, same order |
| 2.3 (now "What Retrieval Is Grounded In") | Reframed as a single trajectory (increasing model control over evidence) with an explicit grounding-direction argument (corpus vs. query) | Synthesis | all 6 retained |
| 2.4 (now "How Trust Would Be Established") | Reorganized as three literatures (evaluation, safety, regulation) "that do not yet meet"; closing paragraph states the requirement-vs-measurement gap as the author's conclusion | Synthesis + author reasoning | all 12 retained, same order |

### Introduction — rewritten in full
| Location | Change | Type |
|---|---|---|
| Opening | Generic "LLMs have moved quickly…" replaced with a concrete scene: how an ICU clinician actually reasons (lactate overnight, stopped medications, prior admission) vs. how prompt-scoped systems reason | Specificity |
| Gap paragraph | The three shortfalls are now derived from the clinician/system mismatch, with explicit hedges ("no published system we identified", "we found none that measures") replacing flat absolutes | Calibrated certainty |
| Framework paragraph | Spatial description (beneath/above the agents) replaces list-like recitation; the structured-oversight design choice is tied to its evidential motivation | Author reasoning |
| Contributions | Kept as an explicit numbered list intentionally — venues expect it; content unchanged | none |

### Discussion — two subsections rewritten
| Location | Change | Type |
|---|---|---|
| 4.2 | Published findings ("~70% task success", rubric grading) now explicitly separated from our interpretation ("Our reading of those results, which the benchmark authors do not themselves draw…") | Attribution boundary |
| 4.3 | "List of failure modes" recast as failure-mode → design-response pairs, making the author's design rationale visible for gate, confidence, topology, and regulatory alignment; the stronger-than-authors'-claim reading of the meta-analysis is flagged as ours | Author reasoning |
| 4.5 | Fixed a thesis artifact ("the Chapter 4 evaluation" → "the evaluation of Section 3.6"); "COMPOSER-LLM-style" name-drop softened | Consistency |

### Abstract — moderately revised
Opening now states the paper's specific tension (trajectory vs. prompt) instead of a generic
field summary; passive claim-of-absence rewritten as an author claim ("we identify three
properties… that no published system measures"). All numbers untouched.

### Conclusion — moderately revised
"The 2025–2026 literature settled…" (broad, unsupported) replaced with a claim scoped to
Section 2; pilot result restated concretely; the feasibility / retrospective / clinical-utility
/ prospective distinctions are now stated in one explicit passage.

### Methodology — light touch only (as instructed)
Already concrete; earlier pass had removed generic phrasing. No structural changes; scanned
clean for all flagged patterns ("aims to provide", "highlights", "Taken together", etc. — zero
occurrences). Architecture, metrics, statistics untouched.

### Pilot Study — untouched this round
Numbers and findings preserved exactly (140 stays, 2.9 s, 11.7 ms, AUROC 0.641 CI 0.478–0.792,
28 alerts, 86%/43% at m=4, 183/183, 1.00).

---

## B. Citation integrity check — PASS

Verified mechanically against a pre-revision baseline (`tools/citation_order_baseline.txt`):

- **54 keys before, 54 after; none removed, none added.**
- **First-appearance order byte-identical**, so IEEE numbering [1]–[54] is unchanged in both
  the PDF and the DOCX.
- Every literature-derived claim retains its citation attached to the sentence making the
  claim (spot-checked per rewritten paragraph during editing).
- No new citations introduced; no claims left citation-less that previously had one.
- The trimmed `references.bib` regenerates identically (54/54 resolved).

---

## C. Originality review — residual similarity surface

These passages will always share vocabulary with source material because they describe named
systems and standard terminology; this is normal and should not be paraphrased away:

1. System names and their one-phrase functions (MedAgentBench, HealthBench, TxAgent, AMIE,
   COMPOSER-LLM) — Related Work 2.2/2.4, Discussion 4.2.
2. Standard definitions: retrieval-augmented generation, hub-and-spoke topology, Sepsis-3
   labels, AUROC/CI terminology — Methodology 3.3/3.6.
3. The MIMIC-IV dataset description (100 patients, module names) — Pilot 5.1/5.2.
4. Regulatory terms of art: "unconfined non-deterministic clinical software", "medical-device
   criteria" — these are the cited papers' own coinages and must appear verbatim.
   *(Author decision 2026-08-14, superseding the bare-verbatim ruling above: the UNDCS coinage
   is now quote-marked at all three occurrences — still verbatim, but typographically
   attributed — after a similarity scan matched it against the source's PMC page. No other
   wording or any number changed; `_body_generated.tex` regenerated via `tools/md2tex.py`.)*

An 8-gram overlap scan against all 45 paper notes and collection summaries found **zero
overlap beyond the thesis title**; overlap with the author's own unpublished thesis text is
expected and acceptable for a thesis-derived paper (disclose to the venue if asked).

---

## D. AI-writing risk classification (post-revision)

| Section | Risk | Main reason |
|---|---|---|
| Abstract | LOW | Opens on a paper-specific tension; every claim tied to a concrete mechanism or number |
| Introduction | LOW | Concrete clinician scenario; hedged absence-claims; remaining list is the conventional contributions list |
| Related Work | LOW–MEDIUM | Now question-driven synthesis with author-voice conclusions; residual risk is inherent to describing many named systems densely |
| Methodology | LOW | Concrete technical description of a specific system; design-science framing is cited convention |
| Discussion | LOW | Author interpretation explicitly separated from published findings; uncertainty stated |
| Pilot Study | LOW | Specific numbers, honest caveats, non-generic findings (sensitivity floor) |
| Conclusion | LOW | Scoped claims; explicit statement of what the pilot does not show |

**Overall AI-writing risk: LOW–MODERATE** (down from moderate/high in Introduction and
Related Work pre-revision). Residual risk ranking: Related Work > Introduction > Discussion >
others.

The ten paragraphs identified as highest-risk pre-revision were: Related Work 2.1–2.4 (all
paragraphs — formulaic "System X does Y" catalogs), Introduction ¶1–¶3 (generic field-summary
opening, flat absolutes, uniform sentence rhythm), Discussion 4.2 ¶1 and 4.3 ¶1
(literature-summary passages without attribution boundaries), and the Abstract opening. All
ten were rewritten as described in section A; the revised text is in the manuscript itself.

---

## E. Warnings and honest limits

- **No AI-detection or Turnitin percentage is claimed.** No external detector or similarity
  database was run. Detectors are probabilistic and false-positive on formal academic prose;
  run the university's Turnitin/iThenticate before submission and treat its report as the
  authority.
- No "humanizer" tricks were used: no inserted errors, no artificial informality, no synonym
  swapping. Every change is a genuine restructuring toward synthesis, specificity, calibrated
  certainty, or explicit author reasoning.
- Most journals require disclosure of AI writing assistance — check the venue's policy and
  disclose accordingly. The strongest authenticity step remaining is the author's own
  revision pass, so the final phrasing carries the author's voice.
