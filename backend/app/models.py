from datetime import datetime
from pydantic import BaseModel
from typing import List


class AttackEvent(BaseModel):
    id: str
    source_ip: str
    source_lat: float
    source_lng: float
    target_lat: float
    target_lng: float
    ddos_score: float
    created_at: datetime


class GlobeArc(BaseModel):
    order: int
    startLat: float
    startLng: float
    endLat: float
    endLng: float
    arcAlt: float
    color: str
