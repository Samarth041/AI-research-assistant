from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from mcp_client.manager import MCPServerManager
from agent.tools import build_tools

async def build_agent(manager):
    endpoint = HuggingFaceEndpoint(
        repo_id="Qwen/Qwen2.5-7B-Instruct",
        task="text-generation",
        provider="auto",
        temperature=0.3,
        max_new_tokens=512,
    )

    llm = ChatHuggingFace(llm=endpoint)

    tools = await build_tools(manager)

    return llm.bind_tools(tools)