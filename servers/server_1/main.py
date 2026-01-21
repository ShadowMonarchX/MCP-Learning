from fastapi import FastAPI, Query

from .config import settings
from .handlers import get_weather_for_city

app = FastAPI(
    title="Weather MCP Server",
    description="Provides weather context for supported US cities",
    version="1.0.0",
)

@app.get("/health")
def health_check():
    return {"server": settings.SERVER_NAME, "status": "running"}

@app.get("/weather")
def weather(city: str = Query(..., description="US city name")):
    """
    Entry-point API endpoint.

    - Receives city from client
    - Delegates logic to handlers
    - Returns weather context
    """
    return get_weather_for_city(city)
