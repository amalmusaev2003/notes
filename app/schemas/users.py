from pydantic import BaseModel, EmailStr, UUID4
from datetime import datetime


class SUserAuth(BaseModel):
    username: str
    email: EmailStr
    password: str


class SUser(BaseModel):
    id: UUID4
    username: str
    email: EmailStr
    password_hash: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
