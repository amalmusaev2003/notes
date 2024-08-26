from fastapi import APIRouter, Depends, Response
from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.users import SUserAuth, SUser
from app.dao.users import UserDAO
from app.models.users import Users
from app.exceptions import UserAlreadyExistsException, UserIsNotPresentException
from app.auth import get_password_hash, authenticate_user, create_access_token
from app.dependencies import get_current_user
from app.database.db_depends import get_db

router_auth = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)

router_users = APIRouter(
    prefix="/users",
    tags=["Пользователи"],
)

@router_auth.post("/register")
async def register_user(db: Annotated[AsyncSession, Depends(get_db)], user_data: SUserAuth):
    existing_user = await UserDAO.find_one_or_none(db, email=user_data.email)
    if existing_user:
        raise UserAlreadyExistsException
    hashed_password = get_password_hash(user_data.password)
    await UserDAO.create(db, username=user_data.username, email=user_data.email, password_hash=hashed_password)
    return {"message": "Пользователь успешно зарегестирован!"}

@router_auth.post("/login")
async def login_user(db: Annotated[AsyncSession, Depends(get_db)], response: Response, user_data: SUserAuth):
    user = await authenticate_user(db, user_data.email, user_data.password)
    if not user:
        raise UserIsNotPresentException
    access_token = create_access_token({"sub": str(user.id)})
    response.set_cookie("notes_access_token", access_token, httponly=True)
    return access_token

@router_auth.post("/logout")
async def logout_user(response: Response):
    response.delete_cookie("notes_access_token")

@router_users.get("/me")
async def read_users_me(current_user: Users = Depends(get_current_user)) -> SUser:
    return current_user
