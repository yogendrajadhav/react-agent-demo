from pydantic import BaseModel, Field

class ChatRequest(BaseModel):
    """
    Request model for chat interactions.
    """
    message: str = Field(..., example="Hello, how are you?")

class ChatResponse(BaseModel):
    """
    Response model for chat interactions.
    """
    response: str = Field(..., example="I am doing well, thank you!")
