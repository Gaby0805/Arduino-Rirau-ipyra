from fastapi import FastAPI
from app.api.routes import auth 
from app.infra import jwt 
from app.core.database import Base,engine
from dotenv import load_dotenv

Base.metadata.create_all(bind=engine) # obrigado para criar as tabelas antes de usar o banco de dados
load_dotenv()

app = FastAPI()

app.include_router(auth.router)
app.include_router(jwt.router)

