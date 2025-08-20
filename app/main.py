from fastapi import FastAPI
from app.api.routes import auth, alarms_days, alarms, websocket
from app.infra import jwt
from app.core.database import Base, engine
from dotenv import load_dotenv
from contextlib import asynccontextmanager
from app.scheduler import scheduler, load_alarms
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)  # Cria tabelas no banco

from contextlib import asynccontextmanager
from fastapi import FastAPI

from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.scheduler import scheduler, load_alarms

origins = [
    "*"
]


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Inicia o scheduler antes de adicionar jobs
    scheduler.start()
    print("🚀 Scheduler iniciado.")

    # Carrega e agenda alarmes
    load_alarms()
    print("🎯 Alarmes carregados e agendados.")

    yield  # Aqui a API começa a aceitar requisições

    # Quando a API está desligando
    scheduler.shutdown()
    print("🛑 Scheduler finalizado.")

app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(auth.router)
app.include_router(alarms.router)
app.include_router(alarms_days.router)
app.include_router(websocket.router)
