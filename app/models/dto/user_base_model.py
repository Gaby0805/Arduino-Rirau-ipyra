from pydantic import BaseModel

class User(BaseModel):
    name: str

class UserInDB(User):
    password: str