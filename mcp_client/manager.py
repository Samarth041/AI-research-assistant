import asyncio
import logging
from mcp import StdioServerParameters
from mcp_client.client import MCPClient
from mcp.types import Tool

logger=logging.getLogger(__name__)

class MCPServerManager:
    def __init__(self):
        self.clients:dict[str,MCPClient]={}

    def register(self,name:str,command:str,args:list[str])->None:
        params=StdioServerParameters(command=command,args=args)
        self.clients[name]=MCPClient(params,name=name)

    async def connect_all(self) -> None:
        results=await asyncio.gather(
            *(c.connect() for c in self.clients.values()),
            
        )

        

    async def list_all_tools(self) -> dict[str, list[Tool]]:
        results={}
        for name,client in self.clients.items():
            results[name]=await client.list_tools()
        return results

    async def call_tool(self,server_name:str,tool_name:str,arguments:dict):
        client=self.clients[server_name]
        return await client.call_tool(tool_name,arguments)

    async def close_all(self) -> None:
        await asyncio.gather(*(c.close() for c in self.clients.values()))