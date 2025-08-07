from fastapi import FastAPI
from clickhouse_driver import Client
import os
from typing import List

from . import models

app = FastAPI()

# Host provided via environment variable or defaults to localhost
clickhouse_host = os.getenv("CLICKHOUSE_HOST", "localhost")
client = Client(host=clickhouse_host)


@app.on_event("startup")
def startup() -> None:
    """Create the ClickHouse table on application startup."""
    client.execute(models.PASSENGER_TABLE_SQL)

@app.get("/")
def read_root():
    return {"status": "ok"}

@app.get("/ping")
def ping():
    version = client.execute("SELECT version()")[0][0]
    return {"clickhouse_version": version}


@app.post("/passengers", status_code=201)
def create_passenger(passenger: models.Passenger):
    client.execute(
        "INSERT INTO passengers (id, name, seat, created_at) VALUES",
        [(passenger.id, passenger.name, passenger.seat, passenger.created_at)],
    )
    return {"status": "passenger inserted"}


@app.get("/passengers", response_model=List[models.Passenger])
def list_passengers():
    rows = client.execute("SELECT id, name, seat, created_at FROM passengers ORDER BY id")
    return [models.Passenger(id=r[0], name=r[1], seat=r[2], created_at=r[3]) for r in rows]
