from datetime import datetime


def normalize_weather_data(raw: dict) -> dict:
    """
    Converts raw server data into Host-ready MCP context
    """

    return {
        "type": "weather_context",
        "city": raw.get("city"),
        "temperature": raw.get("temperature"),
        "condition": raw.get("condition"),
        "wind": raw.get("wind"),
        "alerts": raw.get("alerts"),
        "source": raw.get("source"),
        "timestamp": datetime.utcnow().isoformat(),
    }
