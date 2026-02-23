"""Echo MCP Server implementation using FastMCP."""

import os
from fastmcp import FastMCP

# Get server name from environment variable, default to "Echo Server"
server_name = os.getenv("ECHO_SERVER_NAME", "Echo Server")

# Create the FastMCP server
mcp = FastMCP(server_name)


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


# Get optional second tool configuration from environment variables
second_tool_name = os.getenv("ECHO_TOOL_NAME")
second_tool_response = os.getenv("ECHO_TOOL_RESPONSE")

# Register the second tool if both name and response are configured
if second_tool_name and second_tool_response:
    @mcp.tool(name=second_tool_name)
    def custom_tool() -> str:
        """
        Returns a static configured response.

        Returns:
            A static configured response
        """
        return second_tool_response


def main():
    """Run the MCP server."""
    mcp.run(transport="streamable-http", host="0.0.0.0")


if __name__ == "__main__":
    main()
