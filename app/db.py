import os
from clickhouse_driver import Client

clickhouse_host = os.getenv("CLICKHOUSE_HOST", "localhost")
client = Client(host=clickhouse_host)
