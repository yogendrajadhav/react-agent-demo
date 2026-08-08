import logging
from langchain_ollama import ChatOllama
from langchain.agents import create_agent
from app.core.config import settings
from app.tools.custom import custom_tools

logger = logging.getLogger(__name__)

class AgentService:
    """
    Service for managing AI agent orchestration. Implemented as a singleton.
    """
    _instance = None

    def __new__(cls):
        """
        Ensures that only one instance of AgentService is created.
        """
        if cls._instance is None:
            cls._instance = super(AgentService, cls).__new__(cls)
            cls._instance._initialize()
        return cls._instance

    def _initialize(self):
        """
        Initializes the LLM and agent.
        """
        logger.info("Initializing AgentService...")
        try:
            self.llm = ChatOllama(model=settings.LLM_MODEL, base_url=settings.LLM_BASE_URL)
            self.agent = create_agent(self.llm,tools=custom_tools)
            logger.info("AgentService initialized successfully.")
        except Exception as e:
            logger.error(f"Failed to initialize AgentService: {e}")
            raise e

    async def get_response(self, message: str) -> str:
        """
        Invokes the agent to get a response for a given message.

        Args:
            message (str): The user message.

        Returns:
            str: The agent's response content.
        """
        try:
            response = self.agent.invoke({"messages": [{"role": "user", "content": message}]})
            last_message = response["messages"][-1]
            return last_message.content
        except Exception as e:
            logger.error(f"Error getting response from agent: {e}")
            raise e

# Global singleton instance
agent_service = AgentService()
