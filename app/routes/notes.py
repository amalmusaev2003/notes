import httpx
from fastapi import APIRouter, Depends
from typing import Annotated, List
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.notes import SNewNote, SNote
from app.models import Users
from app.dao.notes import NoteDAO
from app.database.db_depends import get_db
from app.dependencies import get_current_user
from app.exceptions import NoteValidationException

router = APIRouter(prefix="/notes", tags=["Заметки"])


async def check_spelling(text: str):
    url = "https://speller.yandex.net/services/spellservice.json/checkText"
    params = {"text": text}
    async with httpx.AsyncClient() as client:
        response = await client.get(url, params=params)
        response.raise_for_status()
        return response.json()


@router.get("")
async def get_notes(
    db: Annotated[AsyncSession, Depends(get_db)],
    user: Users = Depends(get_current_user),
) -> List[SNote]:
    return await NoteDAO.find_all(db, user_id=user.id)


@router.post("")
async def create_note(
    db: Annotated[AsyncSession, Depends(get_db)],
    note: SNewNote,
    user: Users = Depends(get_current_user),
) -> dict:
    spelling_errors = await check_spelling(note.content)
    if spelling_errors:
        raise NoteValidationException(errors=spelling_errors)

    await NoteDAO.create(db, user_id=user.id, title=note.title, content=note.content)
    return {"status": "success", "message": "Заметка успешно добавлена!"}
