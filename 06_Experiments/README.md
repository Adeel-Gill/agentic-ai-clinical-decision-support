# Experiments

This directory holds the evaluation protocol for the thesis *An Agentic AI Framework for Intelligent Patient Monitoring and Clinical Decision Support*. It is the operational companion to Chapter 4 (`07_Thesis/Chapter_4/Chapter_4.md`).

**Status: planned, not yet run.** These documents specify how experiments are organized and how they will be reproduced. The `results/` directory is an empty placeholder; no results have been produced. Nothing here should be read as reported findings.

## What lives here

| File | Purpose |
|---|---|
| `README.md` | This file: layout, reproduction workflow, config-driven runs. |
| `Experimental_Design.md` | Condensed protocol: baseline ladder, ablations, metric grid, and pre-registered hypotheses (H1..Hn) tied to RQ1–RQ5. |
| `Evaluation_Metrics.md` | Precise definition, formula, and tooling for every metric. |
| `results/` | Output artifacts (placeholder; `.gitkeep` only). |

## Design principles

Runs are **config-driven**. A configuration is a single declarative file that names the model, the retrieval sources, which agents are active, whether the Coordinator orchestrates dynamically or runs flat, and which cohort split to use. The four baselines (B0–B3) and the four ablations are each expressed as one such config; no code changes are needed to switch between them, which is what makes the baseline ladder in Chapter 4 a fair comparison rather than eight separately hand-tuned systems.

Every run is **reproducible from a fixed cohort manifest**. The cohort is sampled once from MIMIC-IV, written to a manifest of stay identifiers and split assignments, and reused verbatim by every configuration. This guarantees that B0 through B3 and all ablations see the identical set of cases, which is the precondition for the paired statistical tests in Chapter 4.

Every run emits a **complete audit trace**. For each case the framework records retrieved evidence, agent actions, verification outcomes, the final decision, and per-case latency and cost. Audit-log completeness is itself a reported metric, so the tracing is not optional instrumentation but part of what is being evaluated.

## Directory layout (intended)

```
06_Experiments/
  README.md
  Experimental_Design.md
  Evaluation_Metrics.md
  configs/            # one file per baseline / ablation (to be added)
  cohort/             # cohort manifest + split assignments (to be added)
  results/            # run outputs, one subdirectory per config (placeholder)
```

## Reproduction workflow

The intended end-to-end procedure is the following ordered steps.

1. **Obtain access.** MIMIC-IV [johnson2023mimic] requires credentialed PhysioNet access and a signed data use agreement. Raw data are never committed to this repository.
2. **Build the cohort.** Run the cohort-sampling step once to draw the bounded cohort (~100–500 adult ICU stays), apply the task label definitions, and write the manifest and patient-level split assignments to `cohort/`. This step is seeded so the draw is reproducible.
3. **Select a configuration.** Choose one config from `configs/` (a baseline B0–B3, or an ablation). The config fixes the model, retrieval sources, active agents, and orchestration mode.
4. **Run.** Execute the pipeline over the cohort manifest under the chosen config. Outputs, including the audit trace, per-case predictions, and latency/cost, are written to `results/<config-name>/`.
5. **Score.** Apply the metrics in `Evaluation_Metrics.md` to the run outputs. Automated metrics (task accuracy, faithfulness, AUROC/AUPRC, ECE, audit-log completeness, runtime) are computed directly; the clinician Likert study and safety adjudication require the human review step.
6. **Analyze.** Compute bootstrap confidence intervals and the paired significance tests, applying the false-discovery-rate correction to the pre-registered confirmatory hypotheses only.

## Reproducibility notes

- **Seeds** are fixed for cohort sampling, bootstrap resampling, and any stochastic decoding, and recorded alongside each result.
- **Model and prompt versions** are pinned per run; a change to either invalidates comparison across runs and starts a new result set.
- **Determinism is imperfect.** LLM outputs may vary run to run even at low temperature, so headline configurations are run multiple times and variability is reported, not hidden.
- **PHI never enters the repository.** Only derived, non-identifying artifacts (metrics, aggregate traces with content redacted where required by the data use agreement) belong under `results/`.
