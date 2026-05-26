import asyncio
from fastmcp import Client

async def main():
    client = Client("server.py")

    async with client:
        result = await client.call_tool("say_hello", {"nombre":"Esto funciona?"})
        print(result)

asyncio.run(main())