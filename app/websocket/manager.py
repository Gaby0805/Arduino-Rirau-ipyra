from fastapi import WebSocket, WebSocketDisconnect

class WebSocketManager:
    def __init__(self):
        self.connected_device: WebSocket | None = None

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        if self.connected_device:
            await websocket.send_text("Tem outro ja usando pae")
            await websocket.close()
            return False
        self.connected_device = websocket
        return True

    async def disconnect(self, websocket: WebSocket):
        if self.connected_device == websocket:
            self.connected_device = None

    async def send_to_device(self, message: str):
        if self.connected_device:
            await self.connected_device.send_text(message)
        else:
            print("Nenhum dispositivo conectado para enviar sinal")