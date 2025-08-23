from fastapi import APIRouter
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi import APIRouter, Depends, status
from app.exceptions.incorrect_credentials_exception import IncorrectCredentialsException
from app.models.dto.token_base_model import Token
from app.models.dto.user_base_model import User,UserInDB
from typing import Annotated
from app.services.user_service import UserService
from app.infra.jwt import JWTService
from datetime import timedelta
from app.models.dto.user_base_model import UserCreate

router = APIRouter(prefix="/auth", tags=["auth"])
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

jwt_service = JWTService()
user_service = UserService()

@router.post("/login")
async def login_for_acess_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
) -> Token:
    user:User = jwt_service.authenticate_user(form_data.username, form_data.password)
    if not user:
        raise IncorrectCredentialsException
    access_token_expires = timedelta(minutes=jwt_service.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = jwt_service.create_access_token(
        data={"sub": user.name}, expires_delta=access_token_expires
    )
    return Token(access_token = access_token, token_type="bearer")


@router.post("/register", status_code=status.HTTP_201_CREATED)
async def creat_user_with_hashed_password(user: UserCreate) -> UserInDB:
    hashed_password = jwt_service.get_password_hash(user.password)
    created_user = user_service.create_user(user.name, hashed_password)
    return UserInDB(**jwt_service.orm_to_dict(created_user))


async def get_current_user(token: str = Depends(oauth2_scheme)):
    return await jwt_service.get_current_user(token)