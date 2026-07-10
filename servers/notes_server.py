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
    """List all saved note titles."""
    return list(_NOTES.keys())

@mcp.tool()
def delete_node(title:str)->str:
    """Delete a saved note by its title"""
    if title in _NOTES:
        del _NOTES[title]
        return f"Deleted node '{title}'"
    return f"Note '{title}' does  not exists. "

@mcp.resource("notes://{title}")
def get_note(title:str)->str:
    """Read a single note's content by title"""
    return _NOTES.get(title,"")

if __name__=="__main__":
    mcp.run(transport="stdio")