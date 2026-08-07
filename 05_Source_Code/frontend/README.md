# ACDSS Frontend (React + Vite)

React implementation of the clinician platform — the six screens designed in
`04_Architecture/UI_Prototype/` — served by the FastAPI dashboard API.

**Research prototype. All data is synthetic; not for clinical use.**

## Run (two terminals)

Backend (FastAPI, port 8000 — only needs `fastapi` + `uvicorn`):

```bash
cd 05_Source_Code/src
python -m uvicorn acdss.api.app_dashboard:app --reload --port 8000
```

Frontend (Vite dev server, port 5173, proxies `/api` → 8000):

```bash
cd 05_Source_Code/frontend
npm install
npm run dev
```

Open http://localhost:5173.

## Structure

```
src/
  api.js                    fetch client + useApi hook
  App.jsx                   shell: nav, header, view switching
  styles.css                ported from the HTML prototype (single source of design truth)
  components/shared.jsx     Chip, StatusChip, Sparkline, RiskBar
  views/
    UnitOverview.jsx        bed grid + review queue        GET /beds, /queue
    PatientTimeline.jsx     lanes + replay cursor          GET /patients/{id}/timeline
    RecommendationReview.jsx claims→evidence, HITL actions GET /patients/{id}/recommendation, POST /review/{id}
    AlertsGate.jsx          verified/blocked + gate curve  GET /alerts (curve = real pilot data)
    AuditTrail.jsx          append-only log                GET /audit
    AgentMonitor.jsx        hub-and-spoke + health strip   GET /agents (health = real pilot metrics)
```

## Wiring notes

- The Agent Monitor health strip and the gate operating curve read **real pilot numbers**
  from `06_Experiments/results/pilot/pilot_metrics.json` via the backend; everything
  patient-shaped is synthetic fixture data in `acdss/api/demo_data.py`.
- Clinician decisions POST to `/api/dashboard/review/{rec_id}`; the backend enforces a
  reason for modify/reject and appends the event to the (in-memory) audit trail —
  refresh the Audit Trail screen to see it.
- Replacing fixtures with live data means implementing the same response shapes in
  `acdss/api/dashboard.py` on top of the real memory/retrieval layers (`acdss.pilot`
  already computes several of them from the MIMIC-IV demo).
