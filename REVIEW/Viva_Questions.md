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
