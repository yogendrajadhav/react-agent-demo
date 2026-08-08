from langchain.tools import tool

@tool
def my_tool(query: str) -> str:
    """
    A simple tool that takes a query and returns a response."""
    return f"Tool response for query: {query}"

@tool
def multiply(a: int, b: int) -> int:
    """Multiply two numbers."""
    return a * b

# List of all tools available for the agent
custom_tools = [my_tool, multiply]
