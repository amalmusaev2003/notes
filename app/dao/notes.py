from app.models import Notes
from .base import BaseDAO


class NoteDAO(BaseDAO):
    model = Notes
