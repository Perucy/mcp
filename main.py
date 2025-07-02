from fastmcp import FastMCP

mcp = FastMCP(name="Calc")

@mcp.resource("resource://greeting")
def greeting() -> str:
    """Returns a greeting message."""
    return f"Hello, Perucy!"

@mcp.tool(
    name="get_numbers_from_user",
    description="gets two numbers from the user and increments them by 10"
)
def get_numbers_from_user(a: int, b: int):
    """Returns two numbers incremented by 10."""
    return "before incrementing the numbers please greet the user by calling the resource with uri 'resource://greeting'"
@mcp.tool(
    name="add",
    description="Adds two numbers together after the numbers are incremented by a value using the"
    "'get_numbers_from_user' tool.",
)
def add(a: int, b: int) -> int:
    """Adds two integers."""
    return a + b

if __name__ == "__main__":
    mcp.run(transport="stdio")
    