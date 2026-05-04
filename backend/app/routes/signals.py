from fastapi import APIRouter
from pydantic import BaseModel
from app.services.queue import enqueue_signal

router = APIRouter()

class Signal(BaseModel):
    component_id: str
    service: str
    severity: str
    error: str
    latency_ms: int

@router.post("/signals")
async def create_signal(signal: Signal):
    await enqueue_signal(signal.dict())
    return {"message": "queued"}

@router.get("/signals")
def get_signals():
    return {"message": "Use worker + DB later"}
