from pydantic import BaseSettings


class ClientConfig(BaseSettings):

    CLIENT_NAME: str = "client-a"
    CLIENT_ROLE: str = "weather-context-client"

    WEATHER_SERVER_URL: str = "http://127.0.0.1:8001"
    WEATHER_ENDPOINT: str = "/weather"

    REQUEST_TIMEOUT_SECONDS: int = 5
    MAX_RETRIES: int = 2
    RETRY_BACKOFF_SECONDS: float = 0.5

    SUPPORTED_COUNTRY: str = "US"

    ENVIRONMENT: str = "development"
    DEBUG: bool = True

    class Config:
        env_file = ".env"
        case_sensitive = True


# Singleton config object
settings = ClientConfig()
