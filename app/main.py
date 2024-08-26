from fastapi import FastAPI

from app.routes.notes import router as notes_router
from app.routes.users import router_auth as auth_router
from app.routes.users import router_users as users_router

app = FastAPI()

app.include_router(auth_router)
app.include_router(users_router)
app.include_router(notes_router)