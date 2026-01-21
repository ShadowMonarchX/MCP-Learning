# from pydantic_settings import BaseSettings


# class HostConfig(BaseSettings):

#     HOST_NAME: str = "mcp-host"
#     HOST_ROLE: str = "ai-orchestrator"

#     WEATHER_CLIENT_NAME: str = "client-a"
#     WEATHER_CLIENT_URL: str = "http://127.0.0.1:8002"
#     WEATHER_CLIENT_ENDPOINT: str = "/context/weather"

#     REQUEST_TIMEOUT_SECONDS: int = 5

#     ENVIRONMENT: str = "development"
#     DEBUG: bool = True

#     class Config:
#         env_file = ".env"
#         case_sensitive = True


# # Singleton
# settings = HostConfig()


# host/config.py
import os


class HostConfig:
    HOST_NAME = "mcp_host"

    # MCP client references
    CLIENTS = {
        "client_a": {
            "module": "clients.client_a",  # Python module reference
            "timeout": int(os.getenv("CLIENT_A_TIMEOUT", 10)),
        },
        # Future clients can be added here
        # "client_b": { "module": "clients.client_b", "timeout": 10 },
    }


config = HostConfig()
