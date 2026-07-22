"""Bias / fairness monitoring (trustworthy AI).

Tracks outcome and confidence distributions across protected subgroups (e.g. sex,
age band) to surface disparate performance. Offline/aggregate — never alters an
individual decision.
"""

from __future__ import annotations

from pydantic import BaseModel, Field


class FairnessReport(BaseModel):
    """Aggregate fairness metrics by subgroup."""

    metric: str
    by_group: dict[str, float] = Field(default_factory=dict)
    max_disparity: float = 0.0


class BiasMonitor:
    """Computes subgroup fairness metrics over a batch of decisions."""

    def evaluate(self, records: list[dict], group_key: str) -> FairnessReport:
        """Return a :class:`FairnessReport` for ``group_key``.

        TODO: compute per-group rates (e.g. positive rate, mean confidence,
        abstention rate) and the max pairwise disparity; consider standard
        fairness metrics (demographic parity, equalized odds) where labels exist.
        """
        raise NotImplementedError
