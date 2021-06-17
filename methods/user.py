from classes.UserInDB import UserInDB
from methods.password import *
from database.users import *


def authenticate_user(username: str, password: str):
    user = get_user(username)

    if not user:
        return False

    if not verify_password(password, user["password"]):
        return False
    return user
