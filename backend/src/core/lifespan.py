from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager
from typing import Any

from core.database import database


@asynccontextmanager
async def database_init(_: Any) -> AsyncGenerator:
    await database.connect()
    yield
    await database.disconnect()
