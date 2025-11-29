from typing import Any

from asyncpg import Record, create_pool

from core import config


class Database:
    def __init__(self) -> None:
        self.pool = None

    async def connect(self) -> None:
        self.pool = await create_pool(
            user=config.DB_USER,
            password=config.DB_PASSWORD,
            database=config.DB_DATABASE,
            host=config.DB_HOST,
            port=config.DB_PORT,
            min_size=3,
            max_size=10,
        )

    async def disconnect(self) -> None:
        await self.pool.close()

    async def execute(self, query: str, *args: Any) -> None:
        async with self.pool.acquire() as conn:
            await conn.execute(query, *args)

    async def fetch(self, query: str, *args: tuple[Any]) -> list[Record]:
        async with self.pool.acquire() as conn:
            return await conn.fetch(query, *args)

    async def fetchrow(self, query: str, *args: tuple[Any]) -> Record:
        async with self.pool.acquire() as conn:
            return await conn.fetchrow(query, *args)

    async def fetchval(self, query: str, *args: tuple[Any]) -> Any:
        async with self.pool.acquire() as conn:
            return await conn.fetchval(query, *args)


database = Database()
