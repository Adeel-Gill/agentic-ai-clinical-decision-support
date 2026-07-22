"""Confidence calibration (trustworthy AI).

Maps raw model/agent confidence to calibrated probabilities so the aggregate
confidence reported by the decision engine is trustworthy (e.g. temperature or
isotonic/Platt scaling), and reports reliability metrics (ECE, Brier).
"""

from __future__ import annotations

from pydantic import BaseModel


class CalibrationReport(BaseModel):
    """Reliability metrics for a set of (confidence, outcome) pairs."""

    expected_calibration_error: float = 0.0
    brier_score: float = 0.0


class Calibrator:
    """Fits and applies a confidence-calibration mapping."""

    def __init__(self, method: str = "isotonic") -> None:
        self.method = method
        self._model = None  # TODO: fitted calibration transform.

    def fit(self, confidences: list[float], outcomes: list[int]) -> CalibrationReport:
        """Fit the calibration map and return reliability metrics. TODO."""
        raise NotImplementedError

    def apply(self, confidence: float) -> float:
        """Map a raw confidence to a calibrated probability.

        TODO: apply the fitted transform; identity until fitted.
        """
        raise NotImplementedError
