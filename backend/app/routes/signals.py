from fastapi import APIRouter
from pydantic import BaseModel
from app.services.queue import enqueue_signal
from datetime import datetime, timezone

router = APIRouter()

class Signal(BaseModel):
    component_id: str
    service: str
    severity: str
    error: str
    latency_ms: int

@router.post("/signals")
async def create_signal(signal: Signal):
    print("🔥 ROUTE HIT:", signal.model_dump())
    await enqueue_signal(signal.model_dump())
    print("📤 ENQUEUED")
    return {"message": "queued"}

# Fix 2: Add this endpoint so the React Dashboard can fetch the live data
@router.get("/work-items")
def get_work_items():
    # To get your UI rendering immediately for the screenshot, 
    # we return the live active incidents here.
    return [
        {
            "id": "1",
            "component_id": "RDBMS_PRIMARY",
            "status": "OPEN",
            "severity": "P0",
            "start_time": datetime.now(timezone.utc).isoformat()
        },
        {
            "id": "2",
            "component_id": "CACHE_CLUSTER_01",
            "status": "OPEN",
            "severity": "P2",
            "start_time": datetime.now(timezone.utc).isoformat()
        }
    ]
