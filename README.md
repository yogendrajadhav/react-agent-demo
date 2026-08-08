# React Agent API

A production-grade FastAPI implementation for interacting with an AI agent powered by LangChain and Ollama. This project demonstrates a modular software architecture designed for scalability, maintainability, and professional deployment.

## 🚀 Features

- **Modular Architecture**: Separated concerns across core configuration, API routing, business logic (services), data schemas, and custom tools.
- **Production-Ready Patterns**:
  - **Pydantic Settings**: Environment-based configuration management.
  - **Singleton Pattern**: Efficient Agent service initialization to prevent redundant LLM loading.
  - **Structured Logging**: Comprehensive logging for better observability.
  - **Global Error Handling**: Consistent API error responses using a global exception handler.
- **Tool Integration**: Extensible tool system allowing the agent to perform specific tasks (e.g., mathematical operations).
- **Auto-Generated Docs**: Fully documented API via Swagger UI.

## 📂 Project Structure

```text
react-agent-demo/
├── .env                    # Environment variables
├── pyproject.toml           # Project dependencies
└── app/
    ├── main.py              # App initialization and entry point
    ├── api/
    │   └── routes.py        # API endpoints
    ├── core/
    │   └── config.py        # Configuration management (Pydantic Settings)
    ├── schemas/
    │   └── chat.py          # Pydantic request/response models
    ├── services/
    │   └── agent_service.py # Agent orchestration logic
    └── tools/
        └── custom.py         # Tool definitions
```

## 🛠️ Getting Started

### Prerequisites
- Python 3.12+
- [Ollama](https://ollama.com/) installed and running locally.
- The required model pulled (default: `gemma4:31b-cloud`):
  ```bash
  ollama pull gemma4:31b-cloud
  ```

### Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd react-agent-demo
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   # OR if using a package manager as per pyproject.toml
   pip install .
   ```

### Configuration

Create a `.env` file in the root directory:

```env
LLM_MODEL=gemma4:31b-cloud
LLM_BASE_URL=http://localhost:11434
APP_HOST=0.0.0.0
APP_PORT=8010
```

### Running the Application

Start the server using the module path:

```bash
python -m app.main
```

The server will be available at `http://localhost:8010`.

## 🔌 API Reference

### Chat Endpoint
**POST** `/chat`

Sends a message to the AI agent.

**Request Body:**
```json
{
  "message": "What is 2 multiplied by 3?"
}
```

**Response Body:**
```json
{
  "response": "2 multiplied by 3 is 6."
}
```

### Documentation
Once the server is running, you can access the interactive API documentation at:
- Swagger UI: `http://localhost:8010/docs`
- Redoc: `http://localhost:8010/redoc`

## 🧰 Custom Tools
The agent is equipped with custom tools defined in `app/tools/custom.py`. You can easily add more tools by defining a function with the `@tool` decorator and adding it to the `custom_tools` list.
