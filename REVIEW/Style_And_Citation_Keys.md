# Style Guide & Canonical Citation Keys

This file governs all thesis prose so chapters stay consistent. Every generated/rewritten
chapter cites using ONLY the BibTeX keys below (defined in `02_Research/References.bib`).
If a claim needs a source not listed here, write `[CITATION NEEDED]` — never invent one.

## Writing rules (to pass AI-detection and read as human academic prose)
1. Vary sentence length; avoid uniform 3–5 sentence paragraphs.
2. No more than ~20% of any section as bullet lists; argue in prose.
3. Every non-trivial claim gets an inline citation `[key]` or is hedged honestly.
4. Ban the following filler openers: "represents the next evolution", "plays a crucial role",
   "In today's world", "It is worth noting", "Furthermore, current research rarely",
   "One major limitation", "Another significant gap".
5. Include at least one *critical* sentence per subsection (what a cited work fails to do).
6. Prefer active voice; name the actor.
7. UK/US spelling: pick US (analyze, behavior) and keep consistent.
8. Terminology (use exactly): "the proposed framework" (not system/architecture interchangeably);
   "agent" for an LLM-driven role; "module" for a non-agent component; "layer" for the six tiers.

## Chapter numbering (AUTHORITATIVE — fix all cross-refs to this)
- Chapter 1: Introduction
- Chapter 2: Literature Review (incl. taxonomy + research gap)
- Chapter 3: Proposed Framework & Methodology  ← the architecture lives HERE (Figure 3.x)
- Chapter 4: Experimental Design & Evaluation
- Chapter 5: Conclusion & Future Work
(The old "Figure 4.1 / Chapter 4" labels on the framework are WRONG → they are Chapter 3.)

## Canonical citation keys
| Key | Short name |
|---|---|
| johnson2023mimic | MIMIC-IV dataset |
| goldberger2000physiobank | PhysioNet |
| yao2023react | ReAct |
| park2023generative | Generative Agents |
| xi2023rise | Rise of LLM Agents (survey) |
| schick2023toolformer | Toolformer |
| wang2023voyager | Voyager |
| wu2024autogen | AutoGen |
| li2023camel | CAMEL |
| hong2024metagpt | MetaGPT |
| wang2024survey | Survey of LLM Autonomous Agents |
| wei2022chain | Chain-of-Thought |
| wang2023selfconsistency | Self-Consistency |
| yao2023tree | Tree of Thoughts |
| shinn2023reflexion | Reflexion |
| sapkota2025agents | AI Agents vs Agentic AI |
| lewis2020rag | RAG (original) |
| gao2023rag | RAG survey |
| asai2024selfrag | Self-RAG |
| zhao2025medrag | MedRAG |
| singhal2023clinical | Med-PaLM (Nature) |
| singhal2025medpalm2 | Med-PaLM 2 |
| tu2024generalist | Med-PaLM M / Generalist Biomedical AI |
| thirunavukarasu2023llms | LLMs in Medicine (Nat Med) |
| zhou2024survey | Survey of LLMs in Medicine |
| tang2024medagents | MedAgents |
| li2024agenthospital | Agent Hospital |
| toma2023clinicalcamel | Clinical Camel |
| jin2021medqa | MedQA benchmark |
| shi2024ehragent | EHRAgent |
| schmidgall2024agentclinic | AgentClinic |
| tu2025amie | AMIE |
| rasheed2022explainable | Explainable/Trustworthy ML for Healthcare |
| jimenez2023trustworthy | Toward Trustworthy AI in Healthcare (verify) |

### 2025–2026 literature update keys (P021–P045, added 2026-08-05)
| Key | Short name |
|---|---|
| wang2025baymax | Survey of LLM Agents in Medicine (Baymax) |
| jiang2025medagentbench | MedAgentBench (virtual EHR benchmark) |
| gao2025txagent | TxAgent (therapeutic reasoning) |
| feng2025doctoragent | DoctorAgent-RL |
| palepu2025disease | AMIE disease management |
| saab2025multimodal | AMIE multimodal diagnosis |
| liu2025riskagent | RiskAgent (risk prediction tools) |
| arora2025healthbench | HealthBench (OpenAI) |
| wu2025memory | Survey of LLM memory mechanisms |
| ehtesham2025protocols | Agent interoperability protocols (MCP/A2A/ACP/ANP) |
| singh2025agenticrag | Agentic RAG survey |
| tran2025collaboration | Multi-agent collaboration mechanisms survey |
| liu2025foundationagents | Foundation agents survey |
| yehudai2025evaluation | Survey on evaluation of LLM agents |
| yu2025trustagent | Trustworthy LLM agents survey (TrustAgent) |
| fallahpour2025medrax | MedRAX (chest X-ray agent) |
| kim2025hallucinations | Medical hallucinations study |
| atf2025uncertainty | Uncertainty quantification in medical LLMs |
| lovon2025mimic | MIMIC-IV LLM benchmark revisit |
| shashikumar2025sepsis | COMPOSER-LLM prospective sepsis prediction |
| ke2025ragfitness | Guideline RAG across 10 LLMs (npj) |
| chen2025medsentry | MedSentry (multi-agent safety) |
| weissman2025unregulated | Unregulated LLM device-like output |
| tan2026undcs | UNDCS regulation of agentic clinical AI |
| wang2026collaboration | Human–LLM collaboration meta-analysis |

### Longitudinal-EHR systems (P046–P050, added 2026-08-08)
| Key | Short name |
|---|---|
| li2026clicare | CliCARE (guideline-grounded longitudinal cancer EHR, AAAI-26) |
| zeng2025trajcoa | Traj-CoA (chain-of-agents trajectory modeling) |
| zeng2026trajonco | TrajOnco (multi-agent temporal EHR reasoning) |
| cui2025timer | TIMER (temporal instruction modeling, npj Digit Med) |
| liang2025rgar | RGAR (recurrence generation-augmented retrieval, EMNLP-25 Findings) |

## Paper-ID reconciliation (fix in Literature_Matrix + Notes)
- Use `Pnn` consistently (P001–P020); drop the stray `P003s`.
- **P016 and P017 are the SAME paper** ("Towards Generalist Biomedical AI") → keep one (P016), delete/repurpose the other.
- **P018 matrix row is WRONG**: it describes a category-theory "monoids" paper, but the stored
  PDF is "Toward Trustworthy AI in Healthcare". Rewrite the P018 row to match the stored PDF
  (map to `jimenez2023trustworthy`) OR remove it. Do NOT keep the monoids text.
- Reconcile years: MedAgents = 2024 (ACL Findings) everywhere.
