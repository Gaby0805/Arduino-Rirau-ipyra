# app/controllers/ws_controller.py
from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from app.core.database import websocket_manager

router = APIRouter()

@router.websocket("/ws")
# essa bomba serve pq o servidor de ws não fecha ent precisa disso aqui
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        print(f"📩 Mensagem recebida: {data}")