from sqlalchemy import Column, Integer, String, Float, DateTime, JSON
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime, timezone

# If you already have a Base defined in a database.py file, import it instead.
# Otherwise, declaring it here will work for the worker.
Base = declarative_base()

class WorkItem(Base):
    __tablename__ = "work_items"

    id = Column(Integer, primary_key=True, index=True)
    component_id = Column(String, index=True, nullable=False)
    status = Column(String, default="OPEN")  # OPEN, INVESTIGATING, RESOLVED, CLOSED
    severity = Column(String, default="P3")  # P0, P1, P2, P3
    
    # Timestamps & Metrics
    start_time = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    end_time = Column(DateTime(timezone=True), nullable=True)
    mttr = Column(Float, nullable=True)  # Mean Time To Repair (in seconds)
    
    # Mandatory for closing an incident
    rca_data = Column(JSON, nullable=True)
