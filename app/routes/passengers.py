from typing import List

from fastapi import APIRouter

from ..models import passenger
from ..services.clickhouse import execute_query

router = APIRouter()

@router.post("/passengers", status_code=201)
def create_passenger(passenger: passenger.Passenger):
    execute_query("INSERT INTO passengers (id, name, seat, created_at) VALUES", [(passenger.id, passenger.name, passenger.seat, passenger.created_at)])

    return {"status": "passenger inserted"}

@router.get("/passengers", response_model=List[passenger.Passenger])
def list_passengers():
    rows = execute_query("SELECT id, name, seat, created_at FROM passengers ORDER BY id")
    return [passenger.Passenger(id=r[0], name=r[1], seat=r[2], created_at=r[3]) for r in rows]
