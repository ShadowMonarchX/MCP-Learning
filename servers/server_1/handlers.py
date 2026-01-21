from typing import Dict
from datetime import datetime
from fastapi import HTTPException

from .config import settings


def get_weather_for_city(city: str) -> Dict:
    """
    Core weather logic for Server-1

    This function:
    - Receives a city name from a client
    - Validates it
    - Returns structured weather context
    """
    city = city.strip().title()

    if not city:
        raise HTTPException(status_code=400, detail="City name is required")


    if city not in settings.SUPPORTED_CITIES:
        raise HTTPException(status_code=404, detail=f"City '{city}' is not supported")
    
    mock_weather_data = {
        "New York": {
            "temperature": 72,
            "condition": "Clear",
            "wind": 10,
            "alerts": None,
        },
        "Los Angeles": {
            "temperature": 78,
            "condition": "Sunny",
            "wind": 6,
            "alerts": None,
        },
        "Chicago": {
            "temperature": 65,
            "condition": "Cloudy",
            "wind": 14,
            "alerts": "Strong wind advisory",
        },
    }

    # Default fallback weather
    weather = mock_weather_data.get(
        city,
        {"temperature": 70, "condition": "Partly Cloudy", "wind": 8, "alerts": None},
    )

    return {
        "city": city,
        "timestamp": datetime.utcnow().isoformat(),
        "temperature": f"{weather['temperature']}°{settings.TEMPERATURE_UNIT}",
        "condition": weather["condition"],
        "wind": f"{weather['wind']} {settings.WIND_SPEED_UNIT}",
        "alerts": weather["alerts"],
        "source": settings.SERVER_NAME,
    }
