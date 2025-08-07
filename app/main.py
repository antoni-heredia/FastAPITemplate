from fastapi import FastAPI
from . import models
from .db import client
from .routes import ping, passengers

app = FastAPI()

@app.on_event("startup")
def startup() -> None:
    """Create the ClickHouse table on application startup."""
    client.execute(models.PASSENGER_TABLE_SQL)

app.include_router(ping.router)
app.include_router(passengers.router)
