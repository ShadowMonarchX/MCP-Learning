from fastapi import FastAPI

from .routes import router
from .config import settings

app = FastAPI(
    title="MCP Client-A",
    description="Weather context client",
    version="1.0.0",
)

app.include_router(router)


@app.get("/health")
def health_check():
    return {"client": settings.CLIENT_NAME, "status": "running"}
