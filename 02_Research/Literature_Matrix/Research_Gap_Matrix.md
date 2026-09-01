# Research Gap Matrix

This table renders into the thesis as Table 2.2 via `build_thesis_docx.py`, so the Papers
column uses citation keys (which compile to reference numbers), not internal paper IDs.
The key↔ID mapping (from the Notes titles, 2026-08-13): P001=xi2023rise ·
P002=park2023generative · P003=yao2023react · P004=schick2023toolformer · P006=wu2024autogen ·
P007=li2023camel · P008=hong2024metagpt · P009=wang2024survey · P010=tang2024medagents ·
P011=li2024agenthospital · P012=zhao2025medrag · P013=singhal2023clinical · P014=zhou2024survey.

| Theme | Papers | Current State | Limitation | Gap | Thesis Contribution |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Memory | [xi2023rise; park2023generative; wang2024survey; li2024agenthospital] | Episodic and semantic memories | Little support for continuous patient monitoring | Need patient-centric long-term memory | Longitudinal patient memory |
| Planning | [xi2023rise; yao2023react; wu2024autogen] | Task decomposition | No clinical workflow planning | Clinical care planning | Intelligent treatment planning |
| Multi-Agent | [park2023generative; wu2024autogen; li2023camel; hong2024metagpt; tang2024medagents] | Agent collaboration | Limited healthcare orchestration | Specialized clinical agents | Clinical multi-agent architecture |
| RAG | [schick2023toolformer; wang2024survey; zhao2025medrag] | External knowledge retrieval | Limited EHR integration | Healthcare-specific RAG | EHR + Guidelines + Medical Literature |
| Trustworthy AI | [xi2023rise; li2024agenthospital; singhal2023clinical; zhou2024survey] | Hallucination reduction | Lack of explainability | Explainable decisions | Explainable clinical reasoning |

