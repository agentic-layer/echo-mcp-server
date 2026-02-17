FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

WORKDIR /app

# Copy project files
COPY pyproject.toml .
COPY src ./src

# Install dependencies
RUN uv sync --frozen

# Run the server
CMD ["uv", "run", "echo-mcp-server"]
