
from .password import *
from ..database import users


def authenticate_user(username: str, password: str):
    user = users.get_user(username)

    if not user:
        return False

    if not verify_password(password, user["password"]):
        return False
    return user
