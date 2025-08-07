from datetime import datetime
from pydantic import BaseModel, Field


class User(BaseModel):
    id: int
    name: str
    age: int
    created_at: datetime = Field(default_factory=datetime.utcnow)


USER_TABLE_SQL = (
    """
    CREATE TABLE IF NOT EXISTS users (
        id Int32,
        name String,
        age Int32,
        created_at DateTime
    )
    ENGINE = MergeTree()
    ORDER BY id
    """
)
