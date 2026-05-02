from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes import signals, health

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(signals.router)
app.include_router(health.router)
