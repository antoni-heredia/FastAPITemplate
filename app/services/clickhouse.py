import os
from clickhouse_driver import Client

clickhouse_host = os.getenv("CLICKHOUSE_HOST", "localhost")
client = Client(host=clickhouse_host)


def execute_query(query: str, params=None):
    """Execute a ClickHouse query."""
    return client.execute(query, params) if params else client.execute(query)