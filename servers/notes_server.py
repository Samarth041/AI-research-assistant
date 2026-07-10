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
def delete_note(title:str)->str:
    """Delete a saved note by its title"""
    if title not in _NOTES:
        raise ValueError(f"Note '{title}' does not exist")
    del _NOTES[title]
    return f"Deleted note '{title}' "

@mcp.resource("notes://{title}")
def get_note(title:str)->str:
    """Read a single note's content by title"""
    return _NOTES.get(title,"")

@mcp.prompt()
def summarize_notes_prompt()->str:
    """Prompt template asking the model to summarize all saved notes."""
    titles=", ".join(_NOTES.keys()) or "(no notes yet)"
    return f"Summarise the key themes across these research notes: {titles}"

if __name__=="__main__":
    mcp.run(transport="stdio")