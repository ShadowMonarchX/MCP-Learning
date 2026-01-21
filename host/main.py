from fastapi import FastAPI, Query

from .config import settings
from .utils import call_weather_client

app = FastAPI(
    title="MCP Host",
    description="AI Host orchestrating multiple MCP clients",
    version="1.0.0",
)


@app.get("/health")
def health_check():
    return {"host": settings.HOST_NAME, "status": "running"}


@app.get("/ask/weather")
async def ask_weather(city: str = Query(..., description="US city name")):
    """
    Entry point for user requests.

    - Accepts user input
    - Decides which client to call
    - Returns final context
    """

    # Decision logic (simple for now)
    weather_context = await call_weather_client(city)

    return {"query": f"Weather in {city}", "context": weather_context}
