"""Tests for the echo MCP server."""

import asyncio
import pytest
from echo_mcp_server.server import mcp


@pytest.mark.asyncio
async def test_server_name():
    """Test that the server has the correct name."""
    assert mcp.name == "Echo Server"


@pytest.mark.asyncio
async def test_echo_tool_exists():
    """Test that the echo tool is registered."""
    tools = await mcp.get_tools()
    assert "echo" in tools
    assert tools["echo"].name == "echo"


@pytest.mark.asyncio
async def test_echo_tool_description():
    """Test that the echo tool has a description."""
    tools = await mcp.get_tools()
    echo_tool = tools["echo"]
    assert "Echo back the provided message" in echo_tool.description
