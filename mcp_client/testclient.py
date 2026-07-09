import asyncio

from mcp import StdioServerParameters
from client import MCPClient

async def main():

    #give erver params
    server_params=StdioServerParameters(
        command="python",
        args=["servers/notes_server.py"]
    )
    #make client
    client=MCPClient(server_params)

    await client.connect()
    print("Connected Successfully")

    await client.close()
    print("Closed successfully")

if __name__=="__main__":
    asyncio.run(main())