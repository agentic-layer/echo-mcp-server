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
    tools = await mcp.list_tools()
    tool_names = [tool.name for tool in tools]
    assert "echo" in tool_names


@pytest.mark.asyncio
async def test_echo_tool_description():
    """Test that the echo tool has a description."""
    tools = await mcp.list_tools()
    echo_tool = next((tool for tool in tools if tool.name == "echo"), None)
    assert echo_tool is not None
    assert "Echo back the provided message" in echo_tool.description
