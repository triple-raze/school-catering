from core import config
from typing import Any
from asyncpg import create_pool, Record

class Database:
    def __init__(self):
        self.pool = None

    async def connect(self) -> None:
        self.pool = await create_pool(
            user = config.DB_USER,
            password = config.DB_PASSWORD,
            database = config.DB_DATABASE,
            host = config.DB_HOST,
            port = config.DB_PORT,
            min_size = 3,
            max_size = 10
        )

    async def execute(self, query, *args) -> None:
        async with self.pool.acquire() as conn:
            await conn.execute(query, *args)
        
    async def fetch(self, query, *args) -> list[Record]:
        async with self.pool.acquire() as conn:
            return await conn.fetch(query, *args)
        
    async def fetchrow(self, query, *args) -> Record:
        async with self.pool.acquire() as conn:
            return await conn.fetchrow(query, *args)
        
    async def fetchval(self, query, *args) -> Any:
        async with self.pool.acquire() as conn:
            return await conn.fetchval(query, *args)
        
database = Database()
