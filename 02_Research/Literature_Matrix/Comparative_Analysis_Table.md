# Comparative Analysis Table

The first block of columns records the general agent capabilities commonly claimed in the
literature. The second block adds the capabilities that actually distinguish the proposed
framework from prior work; these are the dimensions on which the research gap is defensible.

## General capabilities

| Paper | Memory | Planning | Reasoning | Multi-Agent | Healthcare | Trustworthy |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| ReAct [yao2023react] | ❌ | ✅ | ✅ | ❌ | ❌ | ✅ |
| AutoGen [wu2024autogen] | ❌ | ✅ | ✅ | ✅ | ❌ | ✅ |
| MetaGPT [hong2024metagpt] | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ |
| MedAgents [tang2024medagents] | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Agent Hospital [li2024agenthospital] | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| MedRAG [zhao2025medrag] | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ |
| **Proposed Framework** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

## Differentiating capabilities

| Paper | Patient-timeline RAG (EHR-grounded) | Dedicated Verification Gate | Longitudinal Memory | Real ICU data (MIMIC-IV) | Faithful Audit Trail |
| :--- | :--- | :--- | :--- | :--- | :--- |
| ReAct [yao2023react] | ❌ | ❌ | ❌ | ❌ | ❌ |
| AutoGen [wu2024autogen] | ❌ | ❌ | ❌ | ❌ | ❌ |
| MetaGPT [hong2024metagpt] | ❌ | ❌ | ❌ | ❌ | ❌ |
| MedAgents [tang2024medagents] | ❌ | ❌ | ❌ | ❌ | ❌ |
| Agent Hospital [li2024agenthospital] | ❌ | ❌ | ❌ | ❌ | ❌ |
| MedRAG [zhao2025medrag] | ❌ | ❌ | ❌ | ❌ | ❌ |
| **Proposed Framework** | ✅ | ✅ | ✅ | ✅ | ✅ |

Notes on the honest ❌ ratings, so the table is not read as a strawman. MetaGPT keeps a shared
message pool and Agent Hospital keeps a case/experience base, so both have *some* persistent
memory — but neither maintains a single patient's longitudinal clinical timeline, which is the
sense meant by "Longitudinal Memory" here. MedRAG is the strongest prior competitor: it does
retrieve from EHR databases and a diagnostic knowledge graph, but its retrieval is oriented to
snapshot differential diagnosis rather than a patient's admission-to-discharge timeline, and it
is evaluated on DDXPlus and a chronic-pain dataset rather than real ICU records. AutoGen and
MetaGPT include safeguard/code-review agents, but these verify code safety, not clinical claims,
so they are not a dedicated clinical verification gate. Agent Hospital and MedAgents are
evaluated on exam-style benchmarks (MedQA, MedMCQA, PubMedQA) or simulated patients, not on
MIMIC-IV.

## What the new columns reveal

The general-capability block collapses almost every system into an identical row of check marks,
which is exactly why "our framework integrates memory, planning, reasoning, and multi-agent
collaboration" is a weak claim to novelty: prior work integrates those too. The differentiating
block tells a different story. Every prior system misses at least one — in practice most or all —
of the five dimensions that matter for real clinical decision support: retrieval grounded in a
patient's own longitudinal EHR timeline rather than in guidelines or exam corpora; a verification
step that checks generated recommendations against retrieved evidence as a first-class, evaluated
component rather than an incidental safeguard; memory that persists a single patient's history
across time; evaluation on real ICU data (MIMIC-IV) rather than static examination QA; and an
audit trail whose entries are faithful to the evidence the agents actually used. No prior row in
the differentiating table carries more than a single check, and most carry none. The contribution
of the proposed framework is therefore not "integration for its own sake" but the combination of
these specific, individually under-served capabilities, evaluated together on real ICU records.
