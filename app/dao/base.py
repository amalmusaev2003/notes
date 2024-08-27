from fastapi import status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, insert
from typing import Optional


class BaseDAO:
    model = None

    @classmethod
    async def find_all(cls, db: AsyncSession, **filter_by):
        query = select(cls.model.__table__.columns).filter_by(**filter_by)
        result = await db.execute(query)
        return result.mappings().all()

    @classmethod
    async def create(cls, db: AsyncSession, **data) -> Optional[dict]:
        await db.execute(insert(cls.model).values(**data))
        await db.commit()

        return {
            "status_code": status.HTTP_201_CREATED,
            "detail": "created successfully",
        }

    @classmethod
    async def find_one_or_none(cls, db: AsyncSession, **filter_by):
        query = select(cls.model).filter_by(**filter_by)
        result = await db.execute(query)
        return result.scalar_one_or_none()
