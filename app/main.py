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
    client.execute(models.USER_TABLE_SQL)

@app.get("/")
def read_root():
    return {"status": "ok"}

@app.get("/ping")
def ping():
    version = client.execute("SELECT version()")[0][0]
    return {"clickhouse_version": version}


@app.post("/users", status_code=201)
def create_user(user: models.User):
    client.execute(
        "INSERT INTO users (id, name, age, created_at) VALUES",
        [(user.id, user.name, user.age, user.created_at)],
    )
    return {"status": "user inserted"}


@app.get("/users", response_model=List[models.User])
def list_users():
    rows = client.execute("SELECT id, name, age, created_at FROM users ORDER BY id")
    return [models.User(id=r[0], name=r[1], age=r[2], created_at=r[3]) for r in rows]
