from fastapi import FastAPI
from fastapi.responses import JSONResponse

from app.routes.notes import router as notes_router
from app.routes.users import router_auth as auth_router
from app.routes.users import router_users as users_router
from app.exceptions import NoteValidationException

app = FastAPI()


@app.exception_handler(NoteValidationException)
async def note_validation_exception_handler(request, exc: NoteValidationException):
    return JSONResponse(
        status_code=400,
        content={"status": "error", "errors": exc.errors},
    )


app.include_router(auth_router)
app.include_router(users_router)
app.include_router(notes_router)
