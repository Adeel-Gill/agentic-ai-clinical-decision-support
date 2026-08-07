# 6. Conclusion

The 2025–2026 literature settled the question of whether LLM agents can act in clinical
settings; it left open whether their actions can be trusted for a specific patient over
time. This paper's answer is architectural and methodological rather than model-centric: a
layered multi-agent framework whose distinguishing commitments — the patient timeline as a
retrieval corpus, a verification gate that checks recommendations against retrieved patient
evidence, an audit trail whose faithfulness is measured, and structured rather than advisory
clinician oversight — target exactly the properties the field's own benchmarks and
regulatory analyses identify as absent. A pilot on the open MIMIC-IV demo demonstrates that
the non-LLM substrate of these commitments is implementable at interactive latency and that
evidence-gating discriminates in the intended direction, blocking unsupported alerts at a
substantially higher rate than supported ones while exposing an honest sensitivity floor that
exam-style evaluation cannot reveal. The full evaluation on credentialed MIMIC-IV, with the
LLM agent loop in place, is designed and pending; it, not the pilot, will test the clinical
substance of the claims. If the framework's components fail to improve grounded decision
quality there, the design permits that failure to be located precisely — which is, in a
domain where unverifiable success is indistinguishable from plausible error, the property we
argue clinical agentic AI needs most.
