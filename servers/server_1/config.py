from pydantic import BaseSettings
from typing import List


class ServerConfig(BaseSettings):
    SERVER_NAME: str = "weather-server-1"
    SERVER_HOST: str = "127.0.0.1"
    SERVER_PORT: int = 8001

    SUPPORTED_CITIES: List[str] = [
        "New York",
        "Los Angeles",
        "Chicago",
        "Houston",
        "Phoenix",
        "San Francisco",
        "Seattle",
        "Boston",
        "Miami",
        "Denver",
    ]

    TEMPERATURE_UNIT: str = "F"  # Fahrenheit
    WIND_SPEED_UNIT: str = "mph"  # Miles per hour
    WEATHER_API_KEY: str | None = None
    WEATHER_API_BASE_URL: str = "https://api.openweathermap.org/data/2.5"
    ENVIRONMENT: str = "development"  # development | staging | production
    DEBUG: bool = True

    class Config:
        env_file = ".env"
        case_sensitive = True


# Singleton config object (import this everywhere)
settings = ServerConfig()
