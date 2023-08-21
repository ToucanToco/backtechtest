from fastapi import FastAPI
from pydantic import BaseModel
import psycopg
from psycopg.rows import dict_row
from psycopg import sql

app = FastAPI()

class QueryInput(BaseModel):
    table: str


@app.post("/query")
async def run_query(query: QueryInput):
    with psycopg.connect("postgresql://postgres:postgres@localhost:5438", row_factory=dict_row) as conn:
        with conn.cursor() as cur:
            data = cur.execute(sql.SQL(
                "SELECT * FROM {table}"
                ).format(
                    table=sql.Identifier(query.table),
                )
            ).fetchall()
            return data
