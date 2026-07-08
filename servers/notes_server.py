# a toy server

from mcp.server.fastmcp import FastMCP

mcp=FastMCP("notes-server")

_NOTES: dict[str,str]={}

@mcp.tool()
def save_note(title:str,content:str)->str:
    """Save a research note under a title"""
    _NOTES[title]=content
    return f"Saved note '{title}'"

@mcp.tool()
def list_notes()->list[str]:
    """ List all saved notes"""
    return list(_NOTES.keys())

if __name__=="__main__":
    mcp.run(transport="stdio")