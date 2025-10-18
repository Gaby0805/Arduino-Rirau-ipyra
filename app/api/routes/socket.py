from fastapi import  WebSocket,WebSocketDisconnect
from app.websocket.manager import WebSocketManager
from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter(prefix="/socket", tags=["socket"])
ws_manager = WebSocketManager()

async def activate_socket(recado):
    await ws_manager.send_to_device(recado)

@router.websocket("/")
async def websocket_endpoint(websocket: WebSocket):
    connected = await ws_manager.connect(websocket)
    if not connected:
        return
    try:
        while True:
            data = await websocket.receive_text()  
            print(f"Recebido do Arduino: {data}")
    except:
        await ws_manager.disconnect(websocket)

@router.post("/disparar-alarme")
async def disparar_alarme():
    await activate_socket("ALARME")
    return JSONResponse(content={"status": "ALARME enviado"})
