# 6. Conclusion

Medical LLM agents can now act inside clinical workflows; whether their actions can be
trusted for a specific patient over time is a question the systems reviewed in Section 2
neither answer nor measure. This paper's response is architectural and methodological rather
than model-centric. The framework's distinguishing commitments (the patient timeline as a
retrieval corpus, a verification gate that checks recommendations against retrieved patient
evidence, an audit trail whose faithfulness is measured, and structured rather than advisory
clinician oversight) each correspond to a specific absence documented in the benchmark,
safety, and regulatory literature cited throughout. The pilot on the open MIMIC-IV demo
establishes a bounded but concrete result: the non-LLM substrate of these commitments runs
on real ICU records at interactive latency, and requiring recent, concordant, multi-signal
evidence blocks unsupported alerts at a substantially higher rate than supported ones, while
also exposing a sensitivity floor that examination-style evaluation cannot reveal. What the
pilot does not do is equally definite. It says nothing about the LLM agent loop, whose test
is the full MIMIC-IV evaluation specified in Section 3.6, and nothing about clinical
utility, which only prospective study can establish. If the full evaluation shows these
components fail to improve grounded decision quality, the design permits that failure to be
located exactly. In a domain where unverifiable success is indistinguishable from plausible
error, we argue that this is the property clinical agentic AI needs most.
