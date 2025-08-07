from fastapi import FastAPI
from .models import passenger
from .services.clickhouse import client
from .routes import ping, passengers

app = FastAPI()

@app.on_event("startup")
def startup() -> None:
    """Create the ClickHouse table on application startup."""
    client.execute(passenger.PASSENGER_TABLE_SQL)

app.include_router(ping.router)
app.include_router(passengers.router)
