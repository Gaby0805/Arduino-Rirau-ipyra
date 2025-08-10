from fastapi import FastAPI
from app.api.routes import auth 
from app.infra import jwt 
app = FastAPI()

app.include_router(auth.router)
app.include_router(jwt.router)