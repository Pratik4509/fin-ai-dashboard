import asyncio
import random
from app.services.connection_manager import manager 

async def market_data_stream():
    price = 100
    
    while True:
        price += random.uniform(-1, 1)  # Simulate price changes
        data = {
            "symbol": "AAPL",
            "price": round(price, 2),
            "timestamp": asyncio.get_event_loop().time()
        }
        await manager.broadcast(data)
        
        await asyncio.sleep(1)  # Simulate real-time updates every second