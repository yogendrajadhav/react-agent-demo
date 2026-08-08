from langchain_ollama import ChatOllama # pyright: ignore[reportMissingImports]
from langchain.tools import tool
from langchain.agents import create_agent
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
import uvicorn

# Configuration
llm = ChatOllama(model="gemma4:31b-cloud", base_url="http://localhost:11434")

@tool
def my_tool(query: str) -> str:
    """
    A simple tool that takes a query and returns a response."""
    return f"Tool response for query: {query}"

@tool
def multiply(a: int, b: int) -> int:
    """Multiply two numbers."""
    return a * b

# Create the agent once for reuse
agent = create_agent(llm, tools=[my_tool])

app = FastAPI(
    title="React Agent API",
    description="A simple API to interact with a LangChain agent powered by Ollama.",
    version="1.0.0"
)

# Enable CORS for frontend consumption
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str = Field(..., example="Hello, how are you?")

class ChatResponse(BaseModel):
    response: str = Field(..., example="I am doing well, thank you!")

@app.post("/chat", response_model=ChatResponse, summary="Chat with AI Agent", description="Send a message to the AI agent and receive a response. The agent can use tools to answer your query.")
async def chat(request: ChatRequest):
    response = agent.invoke({"messages": [{"role": "user", "content": request.message}]})
    last_message = response["messages"][-1]
    print(last_message)
    return {"response": last_message.content}

def main():
    print("Starting API server on http://localhost:8010")
    uvicorn.run(app, host="0.0.0.0", port=8010)

if __name__ == "__main__":
    main()
