class MCPClientError(Exception):
    """Base Error for our client wrapper"""

class ToolCallError(MCPClientError):
    """Raised when a tool call return isError=True"""

    