# clients/client_a/client.py
import asyncio
import sys
from contextlib import AsyncExitStack
from typing import Optional
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()


class MCPClient:
    def __init__(self):
        self.session: Optional[ClientSession] = None
        self.exit_stack = AsyncExitStack()
        self.anthropic = Anthropic()

    async def connect_to_server(self, server_script_path: str):
        """Connect to MCP server"""
        command = "python" if server_script_path.endswith(".py") else "node"
        params = StdioServerParameters(command=command, args=[server_script_path])
        stdio_transport = await self.exit_stack.enter_async_context(
            stdio_client(params)
        )
        self.stdio, self.write = stdio_transport
        self.session = await self.exit_stack.enter_async_context(
            ClientSession(self.stdio, self.write)
        )
        await self.session.initialize()
        tools = await self.session.list_tools()
        print("Connected to server with tools:", [t.name for t in tools.tools])

    async def process_query(self, query: str) -> str:
        """Send query to server and handle tool calls"""
        if not self.session:
            raise RuntimeError("Client not connected")
        response = await self.session.list_tools()
        # For simplicity, call first tool
        if response.tools:
            tool_name = response.tools[0].name
            result = await self.session.call_tool(tool_name, {"state": query})
            return result.content
        return "No tools available"

    async def chat_loop(self):
        """Interactive chat with server"""
        print("MCP Client started! Type 'quit' to exit.")
        while True:
            query = input("Query: ").strip()
            if query.lower() == "quit":
                break
            response = await self.process_query(query)
            print("Response:", response)

    async def cleanup(self):
        await self.exit_stack.aclose()


# Main entry
async def main():
    if len(sys.argv) < 2:
        print("Usage: python client.py <path_to_server_script>")
        sys.exit(1)
    client = MCPClient()
    try:
        await client.connect_to_server(sys.argv[1])
        await client.chat_loop()
    finally:
        await client.cleanup()


if __name__ == "__main__":
    asyncio.run(main())
