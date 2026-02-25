FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

WORKDIR /app

# Copy project files
COPY pyproject.toml uv.lock ./

# Install dependencies
RUN uv sync --frozen

# Copy source code
COPY src ./src

# Run the server
ENTRYPOINT ["uv", "run", "fastmcp", "run", "src/echo_mcp_server/server.py"]
CMD ["--host", "0.0.0.0", "--transport", "http"]
