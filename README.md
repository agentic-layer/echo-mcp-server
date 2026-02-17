# echo-mcp-server

A simple MCP (Model Context Protocol) server that echoes messages. Built with [FastMCP](https://github.com/jlowin/fastmcp) and [uv](https://github.com/astral-sh/uv).

## Features

- **Echo Tool**: A single tool that echoes back any message you send it
- **FastMCP**: Built on the FastMCP framework for easy MCP server development
- **Modern Python**: Uses uv for fast, reliable dependency management

## Installation

### Using uv (recommended)

```bash
# Install uv if you haven't already
pip install uv

# Clone the repository
git clone https://github.com/agentic-layer/echo-mcp-server.git
cd echo-mcp-server

# Install dependencies
uv sync

# Run the server
uv run echo-mcp-server
```

### Using pip

```bash
pip install -e .
echo-mcp-server
```

## Usage

The server exposes a single tool:

### `echo`

Echoes back the provided message.

**Parameters:**
- `message` (string): The message to echo back

**Returns:**
- The same message that was provided

## Docker

Build and run the server using Docker:

```bash
docker build -t echo-mcp-server .
docker run echo-mcp-server
```

## Development

```bash
# Install dependencies
uv sync

# Run the server
uv run echo-mcp-server

# Run tests (if available)
uv run pytest
```

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

