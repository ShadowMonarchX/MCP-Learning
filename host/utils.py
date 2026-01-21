import httpx
from fastapi import HTTPException

from .config import settings


async def call_weather_client(city: str) -> dict:
    """
    Calls Client-A to retrieve weather context
    """

    url = f"{settings.WEATHER_CLIENT_URL}{settings.WEATHER_CLIENT_ENDPOINT}"
    params = {"city": city}

    try:
        async with httpx.AsyncClient(
            timeout=settings.REQUEST_TIMEOUT_SECONDS
        ) as client:
            response = await client.get(url, params=params)
            response.raise_for_status()

    except httpx.TimeoutException:
        raise HTTPException(status_code=504, detail="Weather client timeout")

    except httpx.HTTPStatusError as exc:
        raise HTTPException(
            status_code=exc.response.status_code,
            detail=exc.response.json().get("detail", "Weather client error"),
        )

    except Exception:
        raise HTTPException(
            status_code=502, detail="Failed to connect to weather client"
        )

    return response.json()
