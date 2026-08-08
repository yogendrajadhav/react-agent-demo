from fastapi import APIRouter, HTTPException
from app.schemas.chat import ChatRequest, ChatResponse
from app.services.agent_service import agent_service
import logging

logger = logging.getLogger(__name__)
router = APIRouter()

@router.post("/chat", response_model=ChatResponse, summary="Chat with AI Agent", description="Send a message to the AI agent and receive a response. The agent can use tools to answer your query.")
async def chat(request: ChatRequest):
    """
    API endpoint to interact with the AI agent.
    """
    try:
        response_text = await agent_service.get_response(request.message)
        return ChatResponse(response=response_text)
    except Exception as e:
        logger.exception("Error occurred during chat request")
        raise HTTPException(status_code=500, detail=str(e))
