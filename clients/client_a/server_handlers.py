import httpx
from fastapi import HTTPException

from .config import settings
from .utils import normalize_weather_data


async def fetch_weather_from_server(city: str) -> dict:
    """
    Calls Server-1 and returns cleaned weather context
    """

    url = f"{settings.WEATHER_SERVER_URL}{settings.WEATHER_ENDPOINT}"
    params = {"city": city}

    try:
        async with httpx.AsyncClient(
            timeout=settings.REQUEST_TIMEOUT_SECONDS
        ) as client:
            response = await client.get(url, params=params)
            response.raise_for_status()

    except httpx.TimeoutException:
        raise HTTPException(status_code=504, detail="Weather server timeout")

    except httpx.HTTPStatusError as exc:
        raise HTTPException(
            status_code=exc.response.status_code,
            detail=exc.response.json().get("detail", "Weather server error"),
        )

    except Exception:
        raise HTTPException(
            status_code=502, detail="Failed to connect to weather server"
        )

    raw_data = response.json()

    if not raw_data:
        raise HTTPException(status_code=500, detail="Weather data missing from server")

    return normalize_weather_data(raw_data)
