from app.models.users import Users
from .base import BaseDAO


class UserDAO(BaseDAO):
    model = Users
