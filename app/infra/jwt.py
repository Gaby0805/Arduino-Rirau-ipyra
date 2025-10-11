import os
from passlib.context import CryptContext
from datetime import timedelta, datetime, timezone
import jwt
from jwt.exceptions import InvalidTokenError
from app.exceptions.credentials_exception import CredentialsException
from app.services.user_service import UserService
from app.models.dto.token_base_model import TokenData
from app.models.dto.user_base_model import UserInDB
from dotenv import load_dotenv

class JWTService:
    def __init__(self):
        load_dotenv()
        self.user_service = UserService()
        self.SECRET_KEY = os.getenv("SECRET_KEY")
        self.ALGORITHM = os.getenv("ALGORITHM")
        self.ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto" )

    def verify_password(self,plain_password, hashed_password):
        return self.pwd_context.verify(plain_password, hashed_password)

    def get_password_hash(self, password):    
        return self.pwd_context.hash(password)
    
    def orm_to_dict(self, obj):
        return {c.key: getattr(obj, c.key) for c in obj.__table__.columns}
    
    def get_user(self,name: str):
        db_user = self.user_service.get_user_by_name(name)
        return UserInDB(**self.orm_to_dict(db_user)) #cria e retorna uma instancia de UserInDb
    
    def authenticate_user(self, name:str, password:str):
        user = self.get_user(name)
        if not self.verify_password(password, user.password):
            return False
        return user
    
    def create_access_token(self, data: dict, expires_delta:timedelta | None = None):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.now(timezone.utc) + expires_delta
        else:
            expire = datetime.now(timezone.utc) + timedelta(minutes=15)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, self.SECRET_KEY, algorithm=self.ALGORITHM)
        return encoded_jwt
    
    async def get_current_user(self,token: str):
        try: 
            payload = jwt.decode(token, self.SECRET_KEY, algorithms=[self.ALGORITHM])
            name = payload.get("sub")
            if name is None:
                raise CredentialsException()
            token_data = TokenData(name=name)
        except InvalidTokenError:
            raise  CredentialsException()
        user = self.get_user(name=token_data.name)
        if user is None:
            raise  CredentialsException()
        return user