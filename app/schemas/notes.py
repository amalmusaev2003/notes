from pydantic import BaseModel
from typing import List, Optional


class SNewNote(BaseModel):
    title: str
    content: str


class SNote(SNewNote):
    class Config:
        from_attributes = True
