"""Pilot feasibility study on the openly licensed MIMIC-IV Clinical Database Demo (v2.2).

This package implements the non-LLM slice of the proposed framework so that the
memory (timeline construction), retrieval, early-warning baseline, and
verification-gate mechanisms can be exercised on real (demo) ICU data without
credentialed access or an LLM API key.

Run:  python -m acdss.pilot.run_pilot --data <demo_root> --out <results_dir>
where <demo_root> is the extracted `mimic-iv-clinical-database-demo-2.2` folder.

No patient-level data is written to the repository: outputs are aggregate
metrics only (see repo policy in 03_Dataset/README.md).
"""
