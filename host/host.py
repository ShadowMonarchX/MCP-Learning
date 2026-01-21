# host/host.py
import asyncio
from clients.client_a.client import MCPClient


async def main():
    print("=== MCP Host (Weather) ===")
    server_script = "servers/server_1/server.py"
    client = MCPClient()
    await client.connect_to_server(server_script)

    while True:
        user_input = input("Enter US state code (e.g., NY) or 'quit': ").strip()
        if user_input.lower() == "quit":
            break
        response = await client.process_query(user_input)
        print("\nWeather Alerts:\n", response)

    await client.cleanup()


if __name__ == "__main__":
    asyncio.run(main())
