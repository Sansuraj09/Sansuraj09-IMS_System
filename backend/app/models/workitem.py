# models/workitem.py

from sqlalchemy import Column, Integer, String
from app.core.db import Base

class WorkItem(Base):
    __tablename__ = "work_items"

    id = Column(Integer, primary_key=True)
    status = Column(String)
    component_id = Column(String)
