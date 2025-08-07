from fastapi import APIRouter
from ..db import client

router = APIRouter()

@router.get("/")
def read_root():
    return {"status": "ok"}

@router.get("/ping")
def ping():
    version = client.execute("SELECT version()")[0][0]
    return {"clickhouse_version": version}
