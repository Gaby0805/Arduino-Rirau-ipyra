# app/controllers/ws_controller.py
from fastapi import APIRouter, WebSocket
from app.core.manager import websocket_manager

router = APIRouter()

@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()  
    websocket_manager.connection = websocket 

    try:
        while True:
            data = await websocket.receive_text()
            print(f" Mensagem recebida: {data}")
    except Exception:
        websocket_manager.disconnect()
