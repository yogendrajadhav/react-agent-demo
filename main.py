from langchain_ollama import ChatOllama # pyright: ignore[reportMissingImports]
from langchain.tools import tool
from langchain.agents import create_agent
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn

# Configuration
llm = ChatOllama(model="gemma4:31b-cloud", base_url="http://localhost:11434")

@tool
def my_tool(query: str) -> str:
    """
    A simple tool that takes a query and returns a response."""
    return f"Tool response for query: {query}"

# Create the agent once for reuse
agent = create_agent(llm, tools=[my_tool])

app = FastAPI()

# Enable CORS for frontend consumption
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
async def chat(request: ChatRequest):
    response = agent.invoke({"messages": [{"role": "user", "content": request.message}]})
    last_message = response["messages"][-1]
    return {"response": last_message.content}

def main():
    print("Starting API server on http://localhost:8080")
    uvicorn.run(app, host="0.0.0.0", port=8080)

if __name__ == "__main__":
    main()
