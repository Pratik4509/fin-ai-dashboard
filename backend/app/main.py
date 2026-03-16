from fastapi import FastAPI
import asyncio
from app.services.market_stream import market_data_stream
from app.api import ws
from contextlib import asynccontextmanager

app = FastAPI(title="Fin AI Dashboard API")
    
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup code
    task = asyncio.create_task(market_data_stream())
    
    yield
    
    # Shutdown code (if needed)
    task.cancel()
    

app = FastAPI(
    title="Fin AI Dashboard API",
    lifespan=lifespan
)

app.include_router(ws.router, prefix="/ws")

@app.get("/")
async def root():
    return {"message": "Fin AI Dashboard API running"}