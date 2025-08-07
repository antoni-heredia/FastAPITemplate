from datetime import datetime
from pydantic import BaseModel, Field


class Passenger(BaseModel):
    id: int
    name: str
    seat: str
    created_at: datetime = Field(default_factory=datetime.utcnow)


PASSENGER_TABLE_SQL = (
    """
    CREATE TABLE IF NOT EXISTS passengers (
        id Int32,
        name String,
        seat String,
        created_at DateTime
    )
    ENGINE = MergeTree()
    ORDER BY id
    """
)
