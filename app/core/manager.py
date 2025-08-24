from fastapi import WebSocket

# manager
class WebSocketManager:
    def __init__(self):
        self.connection: WebSocket | None = None  

    def disconnect(self):
        self.connection = None

    async def send_to_arduino(self, message: str):
        if self.connection:
            await self.connection.send_text(message)


websocket_manager = WebSocketManager()