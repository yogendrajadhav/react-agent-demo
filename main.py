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
    print("Chat bot started. Type 'exit' or 'quit' to stop.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        response = agent.invoke({"messages": [{"role": "user", "content": user_input}]})
        last_message = response["messages"][-1]
        print(f"AI: {last_message.content}")
    
def main():
    print("Hello from react-agent-demo!")
    run()

if __name__ == "__main__":
    main()
