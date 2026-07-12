import asyncio
from mcp_client.manager import MCPServerManager
from mcp_client.exceptions import ToolCallError
from agent.graph import build_tools
from agent.graph import build_agent

from dotenv import load_dotenv
load_dotenv()


async def main():
    manager=MCPServerManager()

    #register servers
    manager.register(
        "notes",
        "python",
        ["servers/notes_server.py"]
    )

    #connect to every registered server
    await manager.connect_all()

    #tools=await build_tools(manager)

    # print("Number of tools",len(tools))

    # for tool in tools:
    #     print(tool.name)
    #     print(tool.description)
    #     print("-"*40)

    model=await build_agent(manager)

    response = await model.ainvoke(
        "Save a note titled Python with content Async programming"
    )

    print(response)


    await manager.close_all()




if __name__=="__main__":
    asyncio.run(main())
