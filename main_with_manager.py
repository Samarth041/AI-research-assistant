import asyncio
from mcp_client.manager import MCPServerManager
from mcp_client.exceptions import ToolCallError

async def main():
    manager=MCPServerManager()

    #register servers
    manager.register(
        "notes",
        "python",
        ["servers/notes_server.py"]
    )

    manager.register(
        "notes2",
        "python",
        ["servers/notes_server.py"]
    )
    #connect to every registered server
    await manager.connect_all()

    all_tools=await manager.list_all_tools()
    

    for server_name,tools in all_tools.items():
        print(f"\n Server:{server_name}")

        for tool in tools:
            print(f"{tool.name}")

    await manager.close_all()




if __name__=="__main__":
    asyncio.run(main())
