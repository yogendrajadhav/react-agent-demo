import logging
import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import router as api_router
from app.core.config import settings

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="React Agent API",
    description="A simple API to interact with a LangChain agent powered by Ollama.",
    version="1.0.0"
)

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Global Exception Handler
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    """
    Global exception handler to catch and log any unhandled exceptions.
    """
    logger.error(f"Unhandled exception occurred: {exc}", exc_info=True)
    return JSONResponse(
        status_code=500,
        content={"detail": "An internal server error occurred. Please try again later."},
    )

# Include API routes
app.include_router(api_router)

def main():
    """
    Main entry point to start the FastAPI server.
    """
    logger.info(f"Starting API server on http://{settings.APP_HOST}:{settings.APP_PORT}")
    uvicorn.run(app, host=settings.APP_HOST, port=settings.APP_PORT)

if __name__ == "__main__":
    main()
