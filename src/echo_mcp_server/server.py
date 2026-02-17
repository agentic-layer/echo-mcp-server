"""Echo MCP Server implementation using FastMCP."""

from fastmcp import FastMCP

# Create the FastMCP server
mcp = FastMCP("Echo Server")


@mcp.tool()
def echo(message: str) -> str:
    """
    Echo back the provided message.
    
    Args:
        message: The message to echo back
        
    Returns:
        The same message that was provided
    """
    return message
