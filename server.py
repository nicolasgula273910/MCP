from fastmcp import FastMCP

mcp = FastMCP("HelloServer")

@mcp.tool
def say_hello(nombre: str) -> str:
    """Multiplies two numbers together."""
    return f"Hi {nombre} how are you AI engineer?"

if __name__ == "__main__":
    mcp.run()