"""Synthetic data provider for the dashboard API.

⚠️ RESEARCH PROTOTYPE — all patient-shaped data here is synthetic (modeled on
the open MIMIC-IV demo). Pilot metrics are read from
06_Experiments/results/pilot/pilot_metrics.json when available so the Agent
Monitor and gate operating curve show real pilot numbers.
"""
from __future__ import annotations

import json
from pathlib import Path

# ---- pilot metrics (real, aggregate-only) ---------------------------------
_PILOT = None
for _cand in [
    Path(__file__).resolve().parents[4] / "06_Experiments" / "results" / "pilot" / "pilot_metrics.json",
]:
    if _cand.exists():
        _PILOT = json.loads(_cand.read_text())
        break


def pilot_metrics() -> dict | None:
    return _PILOT


# ---- synthetic unit --------------------------------------------------------
BEDS = [
    {"bed": "04", "id": "P-1043", "meta": "M · 67 · 32 h", "risk": 0.72, "lo": 0.58, "hi": 0.83,
     "st": "crit", "label": "Verified alert — review", "hr": [88, 92, 95, 99, 104, 101, 106, 108]},
    {"bed": "09", "id": "P-1088", "meta": "F · 71 · 51 h", "risk": 0.61, "lo": 0.47, "hi": 0.74,
     "st": "crit", "label": "Verified alert — review", "hr": [78, 80, 84, 88, 92, 96, 99, 103]},
    {"bed": "02", "id": "P-1102", "meta": "M · 54 · 18 h", "risk": 0.57, "lo": 0.41, "hi": 0.70,
     "st": "warn", "label": "Watch — gate blocked", "hr": [84, 88, 86, 90, 95, 92, 97, 104]},
    {"bed": "11", "id": "P-1067", "meta": "F · 62 · 76 h", "risk": 0.55, "lo": 0.40, "hi": 0.69,
     "st": "warn", "label": "Watch", "hr": [90, 87, 85, 88, 86, 89, 91, 90]},
    {"bed": "07", "id": "P-1029", "meta": "M · 48 · 12 h", "risk": 0.54, "lo": 0.38, "hi": 0.68,
     "st": "warn", "label": "Watch", "hr": [72, 75, 78, 74, 79, 82, 80, 84]},
    {"bed": "01", "id": "P-1010", "meta": "F · 59 · 96 h", "risk": 0.31, "lo": 0.20, "hi": 0.44,
     "st": "good", "label": "Stable", "hr": [76, 74, 75, 73, 74, 72, 75, 74]},
    {"bed": "03", "id": "P-1051", "meta": "M · 44 · 40 h", "risk": 0.28, "lo": 0.18, "hi": 0.41,
     "st": "good", "label": "Stable", "hr": [68, 70, 69, 71, 70, 72, 69, 70]},
    {"bed": "05", "id": "P-1076", "meta": "F · 81 · 62 h", "risk": 0.42, "lo": 0.29, "hi": 0.56,
     "st": "warn", "label": "Watch", "hr": [82, 84, 81, 86, 84, 88, 85, 87]},
    {"bed": "06", "id": "P-1093", "meta": "M · 73 · 29 h", "risk": 0.26, "lo": 0.16, "hi": 0.39,
     "st": "good", "label": "Stable", "hr": [74, 73, 75, 72, 74, 73, 72, 74]},
    {"bed": "08", "id": "P-1015", "meta": "F · 66 · 84 h", "risk": 0.35, "lo": 0.23, "hi": 0.49,
     "st": "good", "label": "Stable", "hr": [70, 72, 71, 73, 72, 74, 73, 72]},
    {"bed": "10", "id": "P-1038", "meta": "M · 57 · 22 h", "risk": 0.24, "lo": 0.15, "hi": 0.36,
     "st": "good", "label": "Stable", "hr": [66, 68, 67, 69, 68, 70, 69, 68]},
    {"bed": "12", "id": "P-1120", "meta": "F · 52 · 8 h", "risk": 0.29, "lo": 0.18, "hi": 0.43,
     "st": "good", "label": "Stable", "hr": [72, 74, 73, 75, 74, 76, 75, 74]},
]

QUEUE = [
    {"severity": "crit", "bed": "04", "patient": "P-1043", "time": "12:42",
     "summary": "Rising lactate + hypotension + tachycardia (4 signals, 6 h). Sepsis risk ↑.",
     "verification": "PASSED"},
    {"severity": "warn", "bed": "09", "patient": "P-1088", "time": "12:17",
     "summary": "SpO2 trend ↓ with rising resp. rate (3 signals, 6 h).",
     "verification": "PASSED"},
]

# ---- synthetic patient timeline (P-1043) -----------------------------------
def _line(pts, abn):
    return [{"t": t, "v": v, "abn": bool(abn(v))} for t, v in pts]


TIMELINE = {
    "P-1043": {
        "header": {"patient": "P-1043", "bed": "MICU A-04",
                   "diagnosis": "Community-acquired pneumonia", "day": "2 (32 h)",
                   "prior_admissions": 2, "risk": 0.72, "lo": 0.58, "hi": 0.83,
                   "tmax": 32},
        "lanes": [
            {"name": "Heart rate", "type": "line", "unit": "bpm",
             "pts": _line([(0, 84), (4, 88), (8, 92), (12, 95), (16, 99), (20, 104), (24, 101), (28, 106), (32, 108)], lambda v: v > 100)},
            {"name": "MAP", "type": "line", "unit": "mmHg",
             "pts": _line([(0, 78), (4, 76), (8, 74), (12, 72), (16, 70), (20, 68), (24, 66), (28, 64), (32, 62)], lambda v: v < 65)},
            {"name": "SpO2", "type": "line", "unit": "%",
             "pts": _line([(0, 97), (4, 96), (8, 96), (12, 95), (16, 94), (20, 94), (24, 93), (28, 93), (32, 92)], lambda v: v < 92)},
            {"name": "Labs", "type": "dot", "unit": "",
             "pts": [{"t": 2, "label": "WBC 11.8", "abn": False}, {"t": 6, "label": "Lactate 1.4", "abn": False},
                      {"t": 10, "label": "Creatinine 1.1", "abn": False}, {"t": 18, "label": "WBC 14.2", "abn": True},
                      {"t": 26, "label": "Lactate 2.4", "abn": True}, {"t": 30, "label": "Lactate 3.1", "abn": True}]},
            {"name": "Medications", "type": "bar", "unit": "",
             "pts": [{"t0": 1, "t1": 14, "label": "Ceftriaxone"}, {"t0": 3, "t1": 32, "label": "IV fluids"},
                      {"t0": 20, "t1": 32, "label": "Norepinephrine (low)"}]},
            {"name": "Prior adm.", "type": "dot", "unit": "",
             "pts": [{"t": -6, "label": "2025-11 · COPD exac.", "abn": False},
                      {"t": -3, "label": "2026-03 · Pneumonia", "abn": False}]},
        ],
        "evidence": [
            {"t": "11:50", "label": "Lactate 3.1", "abn": True}, {"t": "12:30", "label": "MAP 62", "abn": True},
            {"t": "12:35", "label": "HR 108", "abn": True}, {"t": "10:15", "label": "WBC 14.2", "abn": True},
            {"t": "12:20", "label": "SpO2 93", "abn": False}, {"t": "09:40", "label": "Norepinephrine start", "abn": False},
            {"t": "2026-03", "label": "Prior adm.: pneumonia", "abn": False}, {"t": "08:05", "label": "Creatinine 1.1", "abn": False},
        ],
    }
}

RECOMMENDATION = {
    "P-1043": {
        "id": "rec-2026-08-07-1242",
        "patient": "P-1043", "bed": "04",
        "chain": ["Monitoring", "Risk Prediction", "Treatment Rec.", "Explanation", "Verification"],
        "claims": [
            {"text": "Early sepsis risk is elevated", "evidence": ["e1", "e2"]},
            {"text": "serum lactate has risen from 1.4 to 3.1 mmol/L over 8 h", "evidence": ["e1"]},
            {"text": "MAP trending below 65 mmHg", "evidence": ["e2"]},
            {"text": "heart rate persistently above 105 bpm", "evidence": ["e3"]},
            {"text": "blood cultures before antibiotic escalation", "evidence": ["e4"]},
        ],
        "narrative": "Recommend blood cultures before antibiotic escalation, fluid-status reassessment, and initiation of the sepsis bundle per unit protocol.",
        "confidence": {"point": 0.72, "lo": 0.58, "hi": 0.83},
        "verification": {"status": "PASSED", "signals": 4, "required": 3,
                          "detail": "Signals: elevated lactate · MAP < 65 · HR > 100 · WBC 14.2. Guideline conflicts: none. All quantitative claims entailed by retrieved evidence."},
        "patient_evidence": [
            {"id": "e1", "t": "11:50", "item": "Lactate", "value": "3.1 mmol/L", "severity": "crit"},
            {"id": "e2", "t": "12:30", "item": "MAP (arterial)", "value": "62 mmHg", "severity": "crit"},
            {"id": "e3", "t": "12:35", "item": "Heart rate", "value": "108 bpm", "severity": "warn"},
            {"id": "e4", "t": "10:15", "item": "WBC", "value": "14.2 ×10⁹/L", "severity": "warn"},
        ],
        "knowledge_evidence": [
            {"source": "Surviving Sepsis Campaign (2021), rec. 12",
             "excerpt": "obtain cultures before initiating antimicrobials where no substantial delay results."},
            {"source": "Unit protocol MICU-SEP-03",
             "excerpt": "lactate > 2 mmol/L with hypotension → bundle initiation + reassessment within 1 h."},
        ],
    }
}

ALERTS = {
    "verified": [
        {"time": "12:42", "patient": "P-1043", "bed": "04", "risk": 0.72, "type": "Sepsis risk ↑",
         "signals": 4, "required": 3},
        {"time": "12:17", "patient": "P-1088", "bed": "09", "risk": 0.61, "type": "Respiratory deterioration",
         "signals": 3, "required": 3},
    ],
    "blocked": [
        {"time": "11:58", "patient": "P-1102", "bed": "02", "risk": 0.57, "type": "Sepsis risk ↑",
         "reason": "1 signal in last 6 h (≥3 required)"},
        {"time": "10:31", "patient": "P-1067", "bed": "11", "risk": 0.55, "type": "Renal deterioration",
         "reason": "2 signals in last 6 h (≥3 required)"},
        {"time": "09:04", "patient": "P-1029", "bed": "07", "risk": 0.54, "type": "Sepsis risk ↑",
         "reason": "0 signals in last 6 h (≥3 required)"},
    ],
}

AUDIT = [
    {"ts": "12:42:07", "patient": "P-1043", "status": "verified-approved",
     "title": "Sepsis bundle recommendation — approved by Dr. A. Rehman",
     "recommendation": "Blood cultures, fluid reassessment, sepsis bundle initiation.",
     "verification": "PASSED — 4 distinct signals / ≥3 required · guideline conflicts: none · claims entailed: 5/5.",
     "references": ["hosp/labevents#48211 · 11:50 · lactate=3.1", "icu/chartevents#193307 · 12:30 · map=62",
                     "icu/chartevents#193341 · 12:35 · hr=108", "hosp/labevents#48160 · 10:15 · wbc=14.2"],
     "resolvability": True,
     "decision": "Approved, 12:47. Reason: “Consistent with bedside picture; cultures drawn.”"},
    {"ts": "11:58:22", "patient": "P-1102", "status": "blocked",
     "title": "Sepsis risk alert — insufficient recent evidence",
     "recommendation": "Model risk 0.57 (top-quintile).",
     "verification": "BLOCKED — 1 distinct signal in the last 6 h (≥3 required).",
     "references": ["icu/chartevents#188902 · 11:20 · hr=104"],
     "resolvability": True,
     "decision": "Visible under Alerts → Blocked; no notification sent."},
    {"ts": "12:17:41", "patient": "P-1088", "status": "verified-pending",
     "title": "Respiratory deterioration — awaiting clinician review",
     "recommendation": "Increase monitoring frequency; consider ABG and chest imaging review.",
     "verification": "PASSED — 3 distinct signals / ≥3 required (SpO2 89%, RR 26, temp 38.4 °C).",
     "references": ["icu/chartevents#201115 · 11:45 · spo2=89", "icu/chartevents#201162 · 12:00 · rr=26",
                     "icu/chartevents#201201 · 12:10 · temp_c=38.4"],
     "resolvability": True,
     "decision": "Pending."},
]

AGENTS = [
    {"name": "Monitoring", "status": "idle"}, {"name": "Planner", "status": "idle"},
    {"name": "Diagnosis", "status": "working"}, {"name": "Risk Prediction", "status": "working"},
    {"name": "Treatment Rec.", "status": "idle"}, {"name": "Explanation", "status": "idle"},
    {"name": "Verification", "status": "working"},
]

AGENT_LOG = [
    {"t": "12:42", "event": "P-1043 recommendation: PASS (4 signals, 0 conflicts)"},
    {"t": "12:17", "event": "P-1088 recommendation: PASS (3 signals)"},
    {"t": "11:58", "event": "P-1102 alert: BLOCK (1 signal < 3)"},
    {"t": "10:31", "event": "P-1067 alert: BLOCK (2 signals < 3)"},
]
