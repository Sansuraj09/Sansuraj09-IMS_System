kfrom fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

# 🔥 THIS goes here (top-level)
signals_db = []

class Signal(BaseModel):
    service: str
    status: str

@router.post("/signals")
def create_signal(signal: Signal):
    signals_db.append(signal.dict())
    return signal

@router.get("/signals")
def get_signals():
    return signals_db
