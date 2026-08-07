"""Standalone FastAPI app serving the React clinician dashboard (research prototype).

Run (only needs fastapi + uvicorn, no scaffold dependencies):
    cd 05_Source_Code/src
    uvicorn acdss.api.app_dashboard:app --reload --port 8000

The React dev server (05_Source_Code/frontend, `npm run dev`) proxies /api to this app.
"""
from __future__ import annotations

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .dashboard import router

DISCLAIMER = (
    "Research prototype, not a medical device. Synthetic data only. "
    "Decision support requires review by a qualified licensed clinician."
)

app = FastAPI(
    title="ACDSS Dashboard API (research prototype)",
    description=DISCLAIMER,
    version="0.1.0",
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(router)


@app.get("/health")
def health() -> dict:
    return {"status": "ok", "disclaimer": DISCLAIMER}
