import uuid
from sqlalchemy import Column, String, TIMESTAMP, func
from sqlalchemy.dialects.postgresql import UUID as SQLAlchemyUUID
from sqlalchemy.orm import relationship

from app.database.db import Base
from app.models import *


class Users(Base):
    __tablename__ = "users"

    id = Column(SQLAlchemyUUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())
    updated_at = Column(
        TIMESTAMP(timezone=True), server_default=func.now(), onupdate=func.now()
    )

    def __self__(self):
        return f"Пользователь {self.username}"

    notes = relationship("Notes", back_populates="user")
