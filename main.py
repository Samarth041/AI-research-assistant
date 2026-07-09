import asyncio
from mcp import StdioServerParameters
from mcp_client.client import MCPClient

async def main():
    params=StdioServerParameters(command='python',args=["servers/notes_server.py"])

    client=MCPClient(params)

    await client.connect()
    print("Connected: ",client.session is not None)
    await client.close()

if __name__=="__main__":
    asyncio.run(main())