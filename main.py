import asyncio
from mcp import StdioServerParameters
from mcp_client.client import MCPClient

async def main():
    params=StdioServerParameters(command='python',args=["servers/notes_server.py"])

    client=MCPClient(params)

    await client.connect()
    
    tools=await client.list_tools()
    for tool in tools:
        print("="*50)
        print("name : ",tool.name)
        print("Description", tool.description)
        print("Input schema",tool.inputSchema)


    await client.close()

if __name__=="__main__":
    asyncio.run(main())