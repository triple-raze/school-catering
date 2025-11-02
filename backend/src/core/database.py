from config import Config
import asyncpg

class Database:
    def __init__(self):
        self.pool = asyncpg.create_pool(
            user = Config.DB_USER,
            password = Config.DB_PASSWORD,
            database = Config.DB_DATABASE,
            host = Config.DB_HOST,
            port = Config.DB_PORT,
            min_size = 3,
            max_size = 10
        )

    async def execute(self, query, *args):
        async with self.pool.acquire() as conn:
            return await conn.execute(query, *args)
        
    async def fetch(self, query, *args):
        async with self.pool.acquire() as conn:
            return await conn.fetch(query, *args)
        
    async def fetchrow(self, query, *args):
        async with self.pool.acquire() as conn:
            return await conn.fetchrow(query, *args)
        
    async def fetchval(self, query, *args):
        async with self.pool.acquire() as conn:
            return await conn.fetchval(query, *args)
        
database = Database()

