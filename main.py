import asyncio
from mcp import StdioServerParameters
from mcp_client.client import MCPClient
from mcp_client.exceptions import ToolCallError

async def main():
    params=StdioServerParameters(command='python',args=["servers/notes_server.py"])

    client=MCPClient(params)

    async with MCPClient(params) as client:
        
        tools=await client.list_tools()
        # for tool in tools:
        #     print("="*50)
        #     print("name : ",tool.name)
        #     print("Description", tool.description)
        #     print("Input schema",tool.inputSchema)

        #print("-"*50)
        save_result=await client.call_tool("save_note",{"title":"test","content":"hello"})
        #print(save_result.content)

        #to see summarisation prompt
        

        await client.call_tool(
        "save_note",
            {
                "title": "AI",
                "content": "Artificial Intelligence"
            }
        )

        await client.call_tool(
            "save_note",
            {
                "title": "MCP",
                "content": "Model Context Protocol"
            }
        )

        await client.call_tool(
            "save_note",
            {
                "title": "LangGraph",
                "content": "Agent framework"
            }
        )

        messages=await client.get_prompt("summarize_notes_prompt")
        # for message in messages:
        #     print(message)

        #print("-"*50)
        list_result=await client.call_tool("list_notes",{})
        #print(list_result)

        resources=await client.session.list_resources()

        # print("-"*50)
        # for resource in resources.resources:
        #     print(resource.name)
        #     print(resource.uri)

        resource_result=await client.read_resource("notes://test")
        #print(resource_result)

        try:
            await client.call_tool("delete_note",{"title":"abc"})
        except ToolCallError as e:
            print(e)

        

        

if __name__=="__main__":
    asyncio.run(main())