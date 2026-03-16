from fastapi import FastAPI
from app.api import ws

app = FastAPI(title="Fin AI Dashboard API")

app.include_router(ws.router, prefix="/ws")

@app.get("/")
async def root():
    return {"message": "Fin AI Dashboard API running"}