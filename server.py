from mcp.server.fastmcp import FastMCP
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create an MCP server with explicit port - default is 6277
PORT = 8080
mcp = FastMCP("Weather Service", port=PORT, host="0.0.0.0")  # Bind to all interfaces


@mcp.tool()
def get_weather(location: str) -> str:
    """Get the current weather for a specified location."""
    logger.info(f"Getting weather for {location}")
    return f"Weather in {location}: Sunny, 72°F"


@mcp.resource("weather://{location}")
def weather_resource(location: str) -> str:
    """Provide weather data as a resource."""
    logger.info(f"Accessing weather resource for {location}")
    return f"Weather data for {location}: Sunny, 72°F"


@mcp.prompt()
def weather_report(location: str) -> str:
    """Create a weather report prompt."""
    logger.info(f"Creating weather report prompt for {location}")
    return f"""You are a weather reporter. Weather report for {location}?"""


# Run the server
if __name__ == "__main__":
    logger.info(f"Starting Weather Service MCP server on port {PORT}...")
    mcp.run()
