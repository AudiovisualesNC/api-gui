from classes.User import User


class UserInDB(User):
    hashed_password: str
