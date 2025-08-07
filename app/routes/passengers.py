from fastapi import APIRouter
from typing import List
from ..models import passenger
from ..db import client

router = APIRouter()

@router.post("/passengers", status_code=201)
def create_passenger(passenger: passenger.Passenger):
    client.execute(
        "INSERT INTO passengers (id, name, seat, created_at) VALUES",
        [(passenger.id, passenger.name, passenger.seat, passenger.created_at)],
    )
    return {"status": "passenger inserted"}

@router.get("/passengers", response_model=List[passenger.Passenger])
def list_passengers():
    rows = client.execute("SELECT id, name, seat, created_at FROM passengers ORDER BY id")
    return [passenger.Passenger(id=r[0], name=r[1], seat=r[2], created_at=r[3]) for r in rows]
