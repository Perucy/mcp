from fastmcp import FastMCP

mcp = FastMCP("Calculator", instructions="A simple calculator that can add and subtract numbers.")

@mcp.tool(
    name="add",
    description="Adds two numbers together",
)
def add(a: int, b: int) -> int:
    return a + b

@mcp.tool(
    name="subtract",
    description="Subtracts the second number from the first",
)
def subtract(a: int, b: int) -> int:
    return a - b

if __name__ == "__main__":
    mcp.run(transport="stdio")
    