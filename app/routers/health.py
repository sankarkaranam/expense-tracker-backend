# app/routers/health.py
from fastapi import APIRouter
from datetime import datetime

router = APIRouter()


@router.get("/health", summary="Health Check")
def health_check():
    """
    Health check endpoint. Returns simple status and timestamp.
    Used by load balancers / monitoring to see if app is alive.
    """
    return {"status": "ok", "timestamp": datetime.utcnow().isoformat() + "Z"}
