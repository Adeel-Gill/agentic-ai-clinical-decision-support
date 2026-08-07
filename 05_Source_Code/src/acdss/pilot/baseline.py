"""Early-warning baseline: in-hospital mortality from first-24h ICU features.

A deliberately simple, fully classical model (standardized logistic
regression, stratified cross-validation) whose only purpose is to provide a
real alert stream for the verification-gate experiment and an honest
small-sample baseline for the pilot. The demo cohort is 100 patients, so all
results are reported with bootstrap confidence intervals and framed as
feasibility evidence, not performance claims.
"""
from __future__ import annotations

import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import StratifiedKFold, cross_val_predict
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer

from .timeline import Timeline

FEATURE_LABELS = ["heart_rate", "sbp_ni", "resp_rate", "spo2", "temp_c",
                  "wbc", "lactate", "creatinine", "bilirubin_total", "platelets"]


def first24h_features(tl: Timeline) -> dict:
    qt = tl.intime + pd.Timedelta(hours=24)
    ev = tl.events
    win = ev[(ev.t >= tl.intime) & (ev.t <= qt) & ev.label.isin(FEATURE_LABELS)]
    feats: dict = {
        "age": tl.anchor_age,
        "male": 1 if tl.gender == "M" else 0,
        "prior_admissions": int((ev.etype == "prior_admission").sum()),
    }
    for lab in FEATURE_LABELS:
        vals = pd.to_numeric(win[win.label == lab].value, errors="coerce").dropna()
        feats[f"{lab}_min"] = vals.min() if len(vals) else np.nan
        feats[f"{lab}_max"] = vals.max() if len(vals) else np.nan
    return feats


def run_baseline(timelines: dict[int, Timeline], alert_top_fraction: float = 0.2,
                 seed: int = 42) -> tuple[pd.DataFrame, dict]:
    """Cross-validated risk scores. Returns (per-stay frame, metrics)."""
    rows, ys, sids = [], [], []
    for sid, tl in timelines.items():
        rows.append(first24h_features(tl))
        ys.append(tl.hospital_expire_flag)
        sids.append(sid)
    X = pd.DataFrame(rows, index=sids)
    y = np.array(ys)

    model = make_pipeline(SimpleImputer(strategy="median"), StandardScaler(),
                          LogisticRegression(max_iter=2000, class_weight="balanced"))
    cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=seed)
    risk = cross_val_predict(model, X, y, cv=cv, method="predict_proba")[:, 1]

    auroc = roc_auc_score(y, risk)
    rng = np.random.default_rng(seed)
    boots = []
    for _ in range(2000):
        ix = rng.integers(0, len(y), len(y))
        if len(set(y[ix])) < 2:
            continue
        boots.append(roc_auc_score(y[ix], risk[ix]))
    lo, hi = np.percentile(boots, [2.5, 97.5])

    thr = np.quantile(risk, 1 - alert_top_fraction)
    out = pd.DataFrame({"stay_id": sids, "y": y, "risk": risk, "alert": risk >= thr})
    metrics = {
        "n_stays": int(len(y)),
        "n_deaths": int(y.sum()),
        "death_rate": round(float(y.mean()), 4),
        "features": int(X.shape[1]),
        "feature_missingness_mean": round(float(X.isna().mean().mean()), 4),
        "auroc_cv": round(float(auroc), 3),
        "auroc_ci95": [round(float(lo), 3), round(float(hi), 3)],
        "alert_threshold_quantile": 1 - alert_top_fraction,
        "n_alerts": int(out.alert.sum()),
        "alerts_true_positive": int(((out.alert) & (out.y == 1)).sum()),
        "alerts_false_positive": int(((out.alert) & (out.y == 0)).sum()),
    }
    return out, metrics
