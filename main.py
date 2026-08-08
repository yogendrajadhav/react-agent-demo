from langchain_ollama import ChatOllama # pyright: ignore[reportMissingImports]
from langchain.tools import tool
from langchain.agents import create_agent

#llm=ChatOllama(model="qwen2.5:3b", base_url="http://localhost:11434") # this is working
llm=ChatOllama(model="gemma4:31b-cloud", base_url="http://localhost:11434") # this is also working
@tool
def my_tool(query: str) -> str:
    """
    A simple tool that takes a query and returns a response."""
    return f"Tool response for query: {query}"

def run():
    agent = create_agent(llm, tools=[my_tool])
    response = agent.invoke({"messages": [{"role": "user", "content": "Hello, how are you?"}]})
    print(response)
    
def main():
    print("Hello from react-agent-demo!")
    run()


if __name__ == "__main__":
    main()
