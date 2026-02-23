"""Tests for the echo MCP server."""

import asyncio
import os
import pytest
import subprocess
import sys


@pytest.mark.asyncio
async def test_server_name():
    """Test that the server has the correct name."""
    from echo_mcp_server.server import mcp
    assert mcp.name == "Echo Server"


@pytest.mark.asyncio
async def test_echo_tool_exists():
    """Test that the echo tool is registered."""
    from echo_mcp_server.server import mcp
    tools = await mcp.list_tools()
    tool_names = [tool.name for tool in tools]
    assert "echo" in tool_names


@pytest.mark.asyncio
async def test_echo_tool_description():
    """Test that the echo tool has a description."""
    from echo_mcp_server.server import mcp
    tools = await mcp.list_tools()
    echo_tool = next((tool for tool in tools if tool.name == "echo"), None)
    assert echo_tool is not None
    assert "Echo back the provided message" in echo_tool.description


def test_custom_server_name():
    """Test that the server name can be customized via environment variable."""
    # Run a subprocess with the custom environment variable
    env = os.environ.copy()
    env["ECHO_SERVER_NAME"] = "Custom Test Server"
    
    result = subprocess.run(
        [sys.executable, "-c", 
         "from echo_mcp_server.server import mcp; print(mcp.name)"],
        capture_output=True,
        text=True,
        env=env
    )
    
    assert result.returncode == 0
    assert "Custom Test Server" in result.stdout.strip()


def test_second_tool_registration():
    """Test that a second tool can be registered via environment variables."""
    # Run a subprocess with the custom environment variables
    env = os.environ.copy()
    env["ECHO_TOOL_NAME"] = "test_tool"
    env["ECHO_TOOL_RESPONSE"] = "test response"
    
    result = subprocess.run(
        [sys.executable, "-c", 
         "import asyncio; "
         "from echo_mcp_server.server import mcp; "
         "tools = asyncio.run(mcp.list_tools()); "
         "print([t.name for t in tools])"],
        capture_output=True,
        text=True,
        env=env
    )
    
    assert result.returncode == 0
    assert "test_tool" in result.stdout
    assert "echo" in result.stdout


def test_second_tool_only_name_no_registration():
    """Test that second tool is not registered if only name is provided."""
    # Run a subprocess with only the name environment variable
    env = os.environ.copy()
    env["ECHO_TOOL_NAME"] = "test_tool"
    
    result = subprocess.run(
        [sys.executable, "-c", 
         "import asyncio; "
         "from echo_mcp_server.server import mcp; "
         "tools = asyncio.run(mcp.list_tools()); "
         "print([t.name for t in tools])"],
        capture_output=True,
        text=True,
        env=env
    )
    
    assert result.returncode == 0
    assert "test_tool" not in result.stdout
    assert "echo" in result.stdout


def test_second_tool_only_response_no_registration():
    """Test that second tool is not registered if only response is provided."""
    # Run a subprocess with only the response environment variable
    env = os.environ.copy()
    env["ECHO_TOOL_RESPONSE"] = "test response"
    
    result = subprocess.run(
        [sys.executable, "-c", 
         "import asyncio; "
         "from echo_mcp_server.server import mcp; "
         "tools = asyncio.run(mcp.list_tools()); "
         "print(len([t.name for t in tools]))"],
        capture_output=True,
        text=True,
        env=env
    )
    
    assert result.returncode == 0
    assert "1" in result.stdout.strip()
