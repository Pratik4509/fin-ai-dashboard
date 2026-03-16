from fastapi import APIRouter, WebSocket
import asyncio
import random

router = APIRouter()

@router.websocket("/stocks")
async def stock_stream(websocket: WebSocket):
    await websocket.accept()
    
    price = 100
    
    while True:
        price += random.uniform(-1, 1)
        
        data= {
            "symbol": "AAPL",
            "price": round(price, 2)
        }
        await websocket.send_json(data)
        
        await asyncio.sleep(1)