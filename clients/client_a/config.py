# from pydantic_settings import BaseSettings


# class ClientConfig(BaseSettings):

#     CLIENT_NAME: str = "client-a"
#     CLIENT_ROLE: str = "weather-context-client"

#     WEATHER_SERVER_URL: str = "http://127.0.0.1:8001"
#     WEATHER_ENDPOINT: str = "/weather"

#     REQUEST_TIMEOUT_SECONDS: int = 5
#     MAX_RETRIES: int = 2
#     RETRY_BACKOFF_SECONDS: float = 0.5

#     SUPPORTED_COUNTRY: str = "US"

#     ENVIRONMENT: str = "development"
#     DEBUG: bool = True

#     class Config:
#         env_file = ".env"
#         case_sensitive = True


# # Singleton config object
# settings = ClientConfig()

# clients/client_a/config.py
import os


class ClientConfig:
    CLIENT_NAME = "client_a"
    # MCP server reference (could be IP:PORT or local module later)
    SERVER_1_HOST = os.getenv("SERVER_1_HOST", "127.0.0.1")
    SERVER_1_PORT = int(os.getenv("SERVER_1_PORT", 8001))

    # Timeouts / retry settings for calling the server
    REQUEST_TIMEOUT = int(os.getenv("REQUEST_TIMEOUT", 5))  # seconds
    MAX_RETRIES = int(os.getenv("MAX_RETRIES", 3))


config = ClientConfig()
