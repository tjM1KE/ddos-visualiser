import asyncio
import uuid
from datetime import datetime
from typing import List
from random import uniform

from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware

from pydantic_settings import BaseSettings, SettingsConfigDict

from .models import AttackEvent, GlobeArc
from .geo import geoip_lookup
from .ml import score_ddos
from .abuseipdb import get_abuse_confidence
from .ingest import get_suspicious_ips


class Settings(BaseSettings):
    # Defaults if you don't have a .env file yet
    target_lat: float = 51.5074
    target_lng: float = -0.1278
    ddos_threshold: float = 0.7

    # Tell it to read from ../.env if present
    model_config = SettingsConfigDict(
        env_file="../.env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


settings = Settings()

app = FastAPI(title="DDoS Visualizer API")

# Allow the Next.js frontend to call this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

ATTACK_EVENTS: List[AttackEvent] = []
MAX_EVENTS = 5000


async def poll_and_update():
    """
    Background job: pull suspicious IPs, score, geolocate and store events.
    """
    global ATTACK_EVENTS

    while True:
        try:
            candidates = await get_suspicious_ips()
            new_events: List[AttackEvent] = []

            for c in candidates:
                ip = c["ip"]
                abuse_conf = await get_abuse_confidence(ip)

                features = {
                    "req_rate": c.get("req_rate", 0),
                    "unique_ports": c.get("unique_ports", 1),
                    "abuse_confidence": abuse_conf,
                }
                score = score_ddos(features)
                if score < settings.ddos_threshold:
                    continue

                src_lat, src_lng = geoip_lookup(ip)
                if src_lat is None:
                    continue

                evt = AttackEvent(
                    id=str(uuid.uuid4()),
                    source_ip=ip,
                    source_lat=src_lat,
                    source_lng=src_lng,
                    target_lat=settings.target_lat,
                    target_lng=settings.target_lng,
                    ddos_score=score,
                    created_at=datetime.utcnow(),
                )
                new_events.append(evt)

            if new_events:
                ATTACK_EVENTS.extend(new_events)
                if len(ATTACK_EVENTS) > MAX_EVENTS:
                    ATTACK_EVENTS = ATTACK_EVENTS[-MAX_EVENTS:]
        except Exception as e:
            print("Ingest error:", e)

        await asyncio.sleep(10)  # run every 10 seconds


@app.on_event("startup")
async def startup_event():
    # Start the real background polling (even if it's still a stub)
    asyncio.create_task(poll_and_update())

    # --- FAKE DATA FOR TESTING ---
    # Seed some fake attack events so /arcs returns data
    for i in range(20):
        ATTACK_EVENTS.append(
            AttackEvent(
                id=str(uuid.uuid4()),
                source_ip=f"198.51.100.{i}",
                # random point somewhere on Earth
                source_lat=uniform(-60, 60),
                source_lng=uniform(-180, 180),
                # all attacks target your main data center coordinates
                target_lat=settings.target_lat,
                target_lng=settings.target_lng,
                ddos_score=0.5,
                created_at=datetime.utcnow(),
            )
        )
    # --- END FAKE DATA ---



@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/arcs", response_model=List[GlobeArc])
async def get_arcs(limit: int = Query(200, le=1000)):
    """
    Provide data to the Aceternity GitHub Globe in Position[] format.
    """
    events = sorted(ATTACK_EVENTS, key=lambda e: e.created_at, reverse=True)[:limit]
    arcs: List[GlobeArc] = []

    for order, evt in enumerate(events):
        arcs.append(
            GlobeArc(
                order=order,
                startLat=evt.source_lat,
                startLng=evt.source_lng,
                endLat=evt.target_lat,
                endLng=evt.target_lng,
                arcAlt=0.3 + evt.ddos_score * 0.4,
                color="#ff0000" if evt.ddos_score > 0.9 else "#fb923c",
            )
        )
    return arcs
