# 30 Viva / Defense Questions

Derived only from this thesis's own claims and artifacts. Prepare a crisp, evidence-backed answer to each; several are deliberately adversarial.

## Novelty & positioning
1. Your comparative table showed Agent Hospital satisfying all six capability columns. What, precisely, is left for you to contribute?
2. Define "integration novelty" and defend why it is a research contribution rather than engineering.
3. Why was *"On Internal Categories and Crossed Objects in the Category of Monoids"* ever in your literature matrix, and how did that happen?
4. Your title says "patient monitoring," but MIMIC-IV is retrospective. Justify the word "monitoring."
5. What is the single most novel, testable claim in this thesis?

## Architecture
6. How does the Coordinator decide which agents to invoke? Give the exact mechanism, not a description.
7. What happens when the Diagnosis and Risk agents produce contradictory outputs? Walk through your arbitration protocol.
8. A single ICU stay's `chartevents` can exceed any context window. How does your framework ingest it?
9. Distinguish the Planner from the Coordinator. Are both necessary, or is that redundancy?
10. Why did you add a Data/Retrieval Agent and Memory Manager that were absent from your first design?
11. Is the Verification agent a peer or a hard gate? What is its false-negative risk on unsafe recommendations?

## RAG & memory
12. Which embedding model and vector database, and why? What is your chunking strategy for clinical notes?
13. How does your RAG differ from MedRAG's knowledge-graph approach [zhao2025medrag]?
14. You claim RAG reduces hallucinations. How exactly will you *measure* that on MIMIC-IV?
15. What is stored in "Clinical Context Memory," and what is the write/eviction/reflection policy?
16. How does patient-timeline (EHR-grounded) retrieval differ from guideline-only RAG, and why should it matter?

## Methodology & evaluation
17. What are your baselines and what does each one isolate?
18. Which ablation would most convincingly show the Verification agent earns its latency cost?
19. For risk prediction, what beats a SOFA score or logistic-regression baseline, and by how much would be meaningful?
20. Without ground-truth "correct recommendations," how do you evaluate the framework end-to-end?
21. Estimate end-to-end latency and cost for a 7-agent pipeline. Is that compatible with "monitoring"?
22. How large is your prototype cohort and how did you choose the size? What are the inclusion/exclusion criteria?
23. What statistical tests will you use, and how do you handle multiple comparisons?

## Trustworthy AI & clinical safety
24. How is the Explanation agent's output guaranteed *faithful* to the actual reasoning rather than a post-hoc rationalization?
25. How do you measure bias on MIMIC-IV? Which subgroups, which metric?
26. What are the regulatory implications (FDA SaMD / CE marking) of an autonomous treatment-recommendation agent, and how does HITL change them?
27. What is your confidence-calibration method, and why does calibration matter clinically?

## Data & integrity
28. Do you have credentialed access to MIMIC-IV-Note? Your notes-RAG depends on it — confirm.
29. Several passages paraphrase source papers without citation. How is that not an academic-integrity concern, and what have you changed?
30. If you had three months and could run exactly one experiment, which result would most validate the thesis, and why that one?

## Paper viva questions (from final examiner-style review, 2026-08-08)

These 15 target the W-category paper specifically; several will recur in the thesis defense.
Q1-Q4 and Q6 are answered in the manuscript itself after the final revision (Table I scaffold
status, "no statistically significant discrimination" statement, the rule-based-to-entailment
bridge in Section V, the sensitivity-floor limitation, and the deterministic-pilot caveat).

1. What constitutes the seven-agent "scaffold", and how much pilot reasoning was LLM-based? (Answer: none — stated in III-C and Table I.)
2. Given AUROC CI crosses chance, how can the gate be said to behave "as designed"? (Answer: gate claims concern alert-stream filtering behavior, not baseline skill — stated in V-C.)
3. How do you guarantee the LLM verification agent shows the same preferential suppression as the rule-based gate? (Answer: we don't — explicit hypothesis for the full evaluation, stated in V-D.)
4. Is a gate that blocks 57% of true alerts clinically viable? (Answer: no — treated as a governance-set safety parameter, Limitations item 2.)
5. How does reversing grounding direction improve diagnosis accuracy? (To argue: patient-specific evidence entailment vs population priors; ablation will quantify.)
6. Why expect 100% trail resolvability to hold with a non-deterministic LLM? (Answer: we don't — that is why it is a measured target, stated in V-C.)
7. Does structured review invite automation bias (clinicians clicking approve)? (Prepare: mandatory reasons, rejection-rate monitoring, audit sampling.)
8. How do MCP/A2A specifically satisfy UNDCS inspectability? (Prepare: standardized message logs at the coordinator hub; needs a concrete mapping table in the thesis.)
9. Is a notes-free pilot a valid test of the retrieval thesis? (Answer in V-D: structured-data only; notes in full evaluation.)
10. How are revised/retracted lab values handled? (Answer: supersede-not-erase memory management, III-B; demonstrate in full evaluation.)
11. Is retrospective MIMIC-IV a valid substrate for "revision and contradiction"? (Prepare: revisions exist in the record; prospectivity acknowledged as next rung.)
12. Estimated daily LLM cost per monitored bed? (OPEN — needs measurement before the viva; flagged INSUFFICIENT EVIDENCE by the reviewer.)
13. Why not compare against Sepsis-3-specific predictors? (Prepare: they are among planned baselines via Sepsis-3 labels; make explicit in Chapter 4.)
14. How is bias measured in the orchestration layer? (OPEN — thesis Chapter 4 must specify subgroup metrics; currently only named in the trustworthy panel.)
15. What metric triggers silent-mode to active decision support? (Prepare: pre-registered sensitivity/PPV thresholds + governance sign-off; add to future work.)
