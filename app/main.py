from fastapi import FastAPI
from clickhouse_driver import Client
import os

app = FastAPI()

# Host provided via environment variable or defaults to localhost
clickhouse_host = os.getenv("CLICKHOUSE_HOST", "localhost")
client = Client(host=clickhouse_host)

@app.get("/")
def read_root():
    return {"status": "ok"}

@app.get("/ping")
def ping():
    version = client.execute("SELECT version()")[0][0]
    return {"clickhouse_version": version}
