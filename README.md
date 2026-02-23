# echo-mcp-server

A simple MCP (Model Context Protocol) server that echoes messages. Built with [FastMCP](https://github.com/jlowin/fastmcp) and [uv](https://github.com/astral-sh/uv).

## Features

- **Echo Tool**: A single tool that echoes back any message you send it
- **FastMCP**: Built on the FastMCP framework for easy MCP server development
- **Modern Python**: Uses uv for fast, reliable dependency management
- **Configurable**: Customize server name and add a second tool via environment variables

## Installation

Requires [uv](https://github.com/astral-sh/uv).

```bash
# Install dependencies
uv sync

# Run the server
uv run echo-mcp-server
```

## Configuration

The server can be configured using environment variables:

### Server Name

- `ECHO_SERVER_NAME`: Customize the MCP server name (default: "Echo Server")

```bash
ECHO_SERVER_NAME="My Custom Server" uv run echo-mcp-server
```

### Second Tool (Optional)

You can add a second tool with a static response by setting both environment variables:

- `ECHO_TOOL_NAME`: Name for the second tool
- `ECHO_TOOL_RESPONSE`: Static response value for the second tool

**Note:** Both variables must be set for the second tool to be registered.

```bash
ECHO_TOOL_NAME="get_status" ECHO_TOOL_RESPONSE="All systems operational" uv run echo-mcp-server
```

## Usage

The server exposes tools based on configuration:

### `echo`

Echoes back the provided message.

**Parameters:**
- `message` (string): The message to echo back

**Returns:**
- The same message that was provided

### Custom Tool (when configured)

When `ECHO_TOOL_NAME` and `ECHO_TOOL_RESPONSE` are set, a second tool is registered with:

**Parameters:**
- None

**Returns:**
- The static response configured via `ECHO_TOOL_RESPONSE`

## Docker

Build and run the server using Docker:

```bash
docker build -t echo-mcp-server .
docker run echo-mcp-server
```

With custom configuration:

```bash
docker run -e ECHO_SERVER_NAME="Custom Server" \
           -e ECHO_TOOL_NAME="get_status" \
           -e ECHO_TOOL_RESPONSE="OK" \
           echo-mcp-server
```

## Development

Run tests:
```bash
uv run pytest tests/ -v
```

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

