from fastapi import APIRouter, WebSocket, WebSocketDisconnect
import asyncio
import random
from app.services.connection_manager import manager

router = APIRouter()

@router.websocket("/stocks")
async def stock_stream(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            await asyncio.sleep(1000)
            
    except WebSocketDisconnect:
        manager.disconnect(websocket)        