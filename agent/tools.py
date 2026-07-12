from langchain_core.tools import StructuredTool
from mcp_client.manager import MCPServerManager

def mcp_tool_to_langchain_tool(manager:MCPServerManager,server_name:str,mcp_tool):
    async def _call(**kwargs):
        result=await manager.call_tool(server_name,mcp_tool.name,kwargs)
        return result.content
    
    return StructuredTool.from_function(
        coroutine=_call,
        name=mcp_tool.name,
        description=mcp_tool.description or "",
        args_schema=mcp_tool.inputSchema
    )

async def build_tools(manager:MCPServerManager)->list:
    all_tools=await manager.list_all_tools()
    return [
        mcp_tool_to_langchain_tool(manager,server,t)
        for server, tools in all_tools.items()
        for t in tools
    ]