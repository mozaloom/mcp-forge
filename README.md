# MCP Forge

A collection of Model Control Protocol (MCP) servers and tools for building AI-powered applications.

## Features

- **Weather Service**: A simple MCP server providing weather tools, resources, and prompts
- **Sentiment Analysis**: MCP tools for text sentiment analysis
- **HTTP Tools**: MCP client demonstrations and utilities

## Quick Start

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Weather Service**:
   ```bash
   uv run --with mcp server.py
   ```

3. **Access the service**:
   - Server runs on port 8080 by default
   - View logs in terminal for activity

## Project Structure

```
├── server.py           # Main MCP Weather Service
├── mcp-sentiment/      # Sentiment analysis MCP tools
├── mcp-tool-http/      # HTTP client demonstrations
├── my-agent/          # Agent configuration
└── requirements.txt   # Python dependencies
```

## Usage

The Weather Service provides three main MCP capabilities:
- **Tool**: `get_weather(location)` - Get weather for any location
- **Resource**: `weather://{location}` - Weather data as a resource
- **Prompt**: Weather reporting prompt template

## Requirements

- Python 3.8+
- UV package manager
- MCP framework

## License

MIT License


