from fastapi import APIRouter, Query

from .server_handlers import fetch_weather_from_server

router = APIRouter()


@router.get("/context/weather")
async def get_weather_context(city: str = Query(..., description="US city name")):
    """
    Endpoint exposed to MCP Host
    """
    return await fetch_weather_from_server(city)
