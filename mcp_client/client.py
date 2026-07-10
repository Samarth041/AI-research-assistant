from contextlib import AsyncExitStack
from mcp import ClientSession , StdioServerParameters
from mcp.client.stdio import stdio_client

class MCPClient:
    def __init__(self,server_params:StdioServerParameters):
        self.server_params=server_params
        self.session:ClientSession | None=None
        self._stack=AsyncExitStack()

    async def connect(self)->None:
        stdio_transport=await self._stack.enter_async_context(stdio_client(self.server_params))

        stdio,write=stdio_transport

        self.session=await self._stack.enter_async_context(ClientSession(stdio,write))

        result=await self.session.initialize()
        print(result.capabilities)

    async def list_tools(self):
        response=await self.session.list_tools()
        return response.tools

    async def call_tool(self,name:str,arguments:dict):
        result=await self.session.call_tool(name,arguments)
        return result

    async def read_resource(self,uri:str):
        result=await self.session.read_resource(uri)
        return result.contents

    async def get_prompt(self,name:str,arguments:dict | None=None):
        result=await self.session.get_prompt(name,arguments or {})
        return result.messages

    async def close(self)->None:
        await self._stack.aclose()

