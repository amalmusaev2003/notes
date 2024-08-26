import uuid
from sqlalchemy import Column, String, TIMESTAMP, func, ForeignKey
from sqlalchemy.dialects.postgresql import UUID as SQLAlchemyUUID
from sqlalchemy.orm import relationship

from app.database.db import Base
from app.models import *


class Notes(Base):
    __tablename__ = "notes"

    id = Column(SQLAlchemyUUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(SQLAlchemyUUID(as_uuid=True), ForeignKey("users.id"))
    title = Column(String, default="Пустой заголовок")
    content = Column(String)
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())
    updated_at = Column(
        TIMESTAMP(timezone=True), server_default=func.now(), onupdate=func.now()
    )

    def __str__(self):
        return f"Заметка {self.title}"

    user = relationship("Users", back_populates="notes")
