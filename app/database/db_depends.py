from typing import AsyncIterator
from sqlalchemy.ext.asyncio import AsyncSession
from app.database.db import async_session_maker


async def get_db() -> AsyncIterator[AsyncSession]:
    async with async_session_maker() as session:
        yield session
