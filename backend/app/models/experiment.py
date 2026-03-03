from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime

from app.db.session import Base


class Experiment(Base):
    __tablename__ = "experiments"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    strategy = Column(String, nullable=False)
    average_wait_time = Column(Float, nullable=False)
    throughput = Column(Float, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    