from pydantic import BaseModel

class User(BaseModel):
    name: str

class UserInDB(User):
    password: str
    
class UserCreate(BaseModel):
    name: str
    password: str