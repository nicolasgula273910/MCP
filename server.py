from fastmcp import FastMCP

mcp = FastMCP("HelloServer")

@mcp.tool
def say_hello(nombre: str) -> str:
    """Multiplies two numbers together."""
    return "Hi, how are you AI engineer?"