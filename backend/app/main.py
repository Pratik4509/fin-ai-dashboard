from fastapi import FastAPI

app = FastAPI(title="Fin AI Dashboard API")

@app.get("/")
async def root():
    return {"message": "Fin AI Dashboard API running"}