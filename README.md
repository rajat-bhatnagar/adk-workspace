# Google Agent Development Kit (ADK) Workspace

This repository contains hands-on implementations, prototypes, and study experiments built with **Google Agent Development Kit (ADK)** (`google-adk`). It covers agent patterns ranging from minimal code-based and YAML-declarative agents to session state management, lifecycle callbacks, function tools, code execution, MCP tools, and programmatic execution runners.

---

## Workspace Overview

The workspace demonstrates two primary styles of agent authoring in Google ADK:
1. **Programmatic Python Agents (`agent.py`)**: Authoring agents via `google.adk.agents.LlmAgent` / `Agent`, using lifecycle callbacks (`before_agent_callback`), dynamic template interpolation, Python function tools, `BuiltInCodeExecutor`, MCP tools, and programmatic execution via `google.adk.runners.Runner`.
2. **Declarative Config Agents (`root_agent.yaml`)**: Defining agents, system instructions, and tool integrations purely through YAML configuration matching the ADK `AgentConfig` schema.

---

## Agent Implementations

| Agent Directory | Format | Primary Model | Key Concept & Purpose |
|---|---|---|---|
| [`my_first_agent`](my_first_agent/agent.py) | Python | `gemini-3.5-flash` | **Baseline Agent**: Foundational `Agent` instance with identity, description, and instructions. |
| [`config_agent`](config_agent/root_agent.yaml) | YAML | `gemini-flash-latest` | **Declarative Agent**: Complete YAML configuration for an algebra tutor with structured pedagogical guidelines. |
| [`maths_agent`](maths_agent/root_agent.yaml) | YAML | `gemini-3.5-flash` | **Minimal Declarative Agent**: Lightweight YAML-based maths tutor configuration. |
| [`search_agent`](search_agent/root_agent.yaml) | YAML | `gemini-3.5-flash` | **Tool Integration**: Demonstrates binding built-in tools (`google_search`) directly in YAML. |
| [`greeter_agent`](greeter_agent/agent.py) | Python | `gemini-3.5-flash` | **Lifecycle Callbacks & Templating**: Uses `before_agent_callback` (`CallbackContext`) to initialize session state and inject dynamic variables (`{user_name}`, `{user_language}`) into prompt instructions. |
| [`name_extractor`](name_extractor/agent.py) | Python | `gemini-3.5-flash` | **State Extraction & Multi-Turn Testing**: Uses `output_key="user_name"` to persist agent outputs to `session.state`, accompanied by a multi-turn programmatic runner test (`test_state.py`). |
| [`name_extractor_agent`](name_extractor_agent/agent.py) | Python | `gemini-3.5-flash` | **Self-Contained Runner**: Single-file demonstration combining `LlmAgent`, `InMemorySessionService`, and `Runner`. |
| [`weather_agent`](weather_agent/agent.py) | Python | `gemini-3.5-flash` | **Function Tool**: Returns a fixed sample weather report through `get_weather`. |
| [`geography_assistant`](geography_assistant/agent.py) | Python | `gemini-3.5-flash` | **Function Tool**: Looks up capital cities from an in-memory dictionary through `get_capital_city`. |
| [`code_executor_agent`](code_executor_agent/agent.py) | Python | `gemini-3.5-flash` | **Code Execution**: Uses ADK's `BuiltInCodeExecutor` for calculations and data processing. |
| [`file_reader_assistant`](file_reader_assistant/agent.py) | Python | `gemini-3.5-flash` | **MCP Toolset**: Uses the filesystem MCP server to list directories and read files. |

---

## Detailed Agent Breakdown

### 1. `my_first_agent`
* **Path**: [`my_first_agent/agent.py`](my_first_agent/agent.py)
* **Description**: A minimal "Hello World" agent in Python using `google.adk.agents.llm_agent.Agent`.
* **Key Components**:
  - `model`: Reasoning model (`gemini-3.5-flash`).
  - `name`: Identifier used by the ADK framework (`root_agent`).
  - `description`: Agent purpose.
  - `instruction`: Core behavior instruction.

### 2. `config_agent`
* **Path**: [`config_agent/root_agent.yaml`](config_agent/root_agent.yaml)
* **Description**: A declarative agent created via `adk create --type=config config_agent`.
* **Key Components**:
  - Adheres to the official ADK `AgentConfig.json` schema (`yaml-language-server`).
  - Implements an algebra tutor persona (`math_tutor_agent`) using `gemini-flash-latest`.
  - Encapsulates multi-step teaching instructions directly in YAML without writing Python code.

### 3. `maths_agent`
* **Path**: [`maths_agent/root_agent.yaml`](maths_agent/root_agent.yaml)
* **Description**: A streamlined declarative YAML agent.
* **Key Components**:
  - Configures a maths tutor agent targeting `gemini-3.5-flash`.
  - Minimalist specification showing the core required YAML fields: `name`, `model`, `description`, `instruction`.

### 4. `search_agent`
* **Path**: [`search_agent/root_agent.yaml`](search_agent/root_agent.yaml)
* **Description**: Demonstrates tool attachment in declarative YAML.
* **Key Components**:
  - Configured with `tools: - name: google_search`.
  - Enables the agent to execute Google searches and answer questions based on retrieved web results.

### 5. `greeter_agent`
* **Path**: [`greeter_agent/agent.py`](greeter_agent/agent.py)
* **Description**: Demonstrates dynamic prompt templating and session state initialization via lifecycle callbacks.
* **Key Components**:
  - **`initialize_greeting_state(context: CallbackContext)`**: Intercepts the execution lifecycle to set default state values (`user_name`, `user_language`) using `context.state.setdefault()`.
  - **`before_agent_callback`**: Hook executed prior to agent reasoning.
  - **Templated Instructions**: Prompt instruction `Hello {user_name}. Please respond in {user_language}.` dynamically interpolates values populated from `session.state`.

### 6. `name_extractor`
* **Path**: [`name_extractor/agent.py`](name_extractor/agent.py) & [`name_extractor/test_state.py`](name_extractor/test_state.py)
* **Description**: Demonstrates state output persistence and multi-turn state verification.
* **Key Components**:
  - **`output_key="user_name"`**: Instructs the agent to automatically write its final output directly into `session.state["user_name"]`.
  - **`test_state.py`**: A programmatic verification script using `Runner` and `InMemorySessionService`:
    1. Initializes an in-memory session.
    2. Sends a first turn ("*Hi, my name is Alex Johnson*") and streams response events via `runner.run_async()`.
    3. Asserts and prints the session state to confirm extraction.
    4. Executes a second turn ("*What's my name?*") to prove state persistence across turns.

### 7. `name_extractor_agent`
* **Path**: [`name_extractor_agent/agent.py`](name_extractor_agent/agent.py)
* **Description**: A self-contained script that unifies the agent definition and execution runner into one file.
* **Key Components**:
  - Defines `root_agent` with `output_key="user_name"`.
  - Contains an executable `main()` block running `InMemorySessionService` and `Runner` for rapid CLI experimentation.

### 8. `weather_agent`
* **Path**: [`weather_agent/agent.py`](weather_agent/agent.py)
* **Description**: Demonstrates a Python function passed to `LlmAgent` as a tool.
* **Key Components**:
  - `get_weather(city)` returns a sample sunny, 25°C report for any city. It does not query a live weather service.
  - `tools=[get_weather]` makes the function available to the agent.

### 9. `geography_assistant`
* **Path**: [`geography_assistant/agent.py`](geography_assistant/agent.py)
* **Description**: Demonstrates tool calling with a local capital-city lookup.
* **Key Components**:
  - `get_capital_city(country)` searches an in-memory dictionary of eight countries and returns a fallback message for others.
  - `tools=[get_capital_city]` makes the function available to the agent.

### 10. `code_executor_agent`
* **Path**: [`code_executor_agent/agent.py`](code_executor_agent/agent.py)
* **Description**: Demonstrates ADK's built-in code execution for calculations and data processing.
* **Key Components**:
  - `code_executor=BuiltInCodeExecutor()` enables code execution by the agent.
  - The configured model is `gemini-3.5-flash`; the example notes that code execution requires Gemini 2.0 or later.

### 11. `file_reader_assistant`
* **Path**: [`file_reader_assistant/agent.py`](file_reader_assistant/agent.py)
* **Description**: Demonstrates MCP integration with the filesystem server.
* **Key Components**:
  - `McpToolset` launches `@modelcontextprotocol/server-filesystem` through `npx` using a stdio connection.
  - `tool_filter` exposes only `list_directory` and `read_file` to the agent.
  - The allowed folder is resolved from `./my_files` relative to the process's current working directory. The repository includes sample files in [`file_reader_assistant/my_files/`](file_reader_assistant/my_files/).

---

## Getting Started

### Prerequisites
- Python 3.10+ (tested with Python 3.15)
- Active Google Gemini API key or Google Cloud credentials
- Node.js and `npx` to run the filesystem MCP server used by `file_reader_assistant`

### Setup Environment

1. Clone repository and navigate to root:
   ```bash
   cd adk-workspace
   ```

2. Activate virtual environment (or create one):
   ```bash
   source .venv/bin/activate
   ```

3. Ensure dependencies are installed:
   ```bash
   pip install google-adk google-genai python-dotenv
   ```

4. Configure environment variables:
   Create a `.env` file in the root or target agent directory with your API credentials:
   ```env
   GEMINI_API_KEY="your-gemini-api-key"
   # Or for Vertex AI / GCP:
   # GOOGLE_GENAI_USE_VERTEXAI=true
   # GOOGLE_CLOUD_PROJECT="your-project-id"
   # GOOGLE_CLOUD_LOCATION="us-central1"
   ```

---

## Running the Agents

### Option 1: Using the ADK CLI

The `google-adk` CLI provides several ways to interact with agents:

* **Interactive CLI Session**:
  ```bash
  adk run my_first_agent
  # or
  adk run config_agent
  # or
  adk run greeter_agent
  # Other Python examples:
  adk run weather_agent
  adk run geography_assistant
  adk run code_executor_agent
  ```

  To use the included MCP sample files, run the file reader from its directory so `./my_files` resolves to `file_reader_assistant/my_files`:
  ```bash
  cd file_reader_assistant
  adk run .
  ```

* **Web UI (FastAPI + Browser Interface)**:
  ```bash
  adk web greeter_agent
  ```

* **API Server (FastAPI Endpoint)**:
  ```bash
  adk api_server config_agent
  ```

### Option 2: Programmatic Execution Scripts

Run Python scripts directly to test session state and event streaming:

```bash
# Test name extraction and session state persistence across turns
python name_extractor/test_state.py

# Run standalone name extractor runner
python name_extractor_agent/agent.py
```

---

## Study Plans and Documentation

Detailed reference study guides and codelab tracking worksheets are located in [`docs/`](a docs):
- [`docs/a-week-study-plan_23rd-to-30th-Oct-26.MD`](a docs/a-week-study-plan_23rd-to-30th-Oct-26.MD): 1-week master curriculum for Google ADK, Model Context Protocol (MCP), and Agent2Agent (A2A) protocol.
- [`docs/agentic_ai_mastery_worksheet_v7.xlsx`](a docs/agentic_ai_mastery_worksheet_v7.xlsx): Progress tracking worksheet for skills, badges, and codelabs.
- [`docs/Anthropic_Architect_Study_Plan.xlsx`](a docs/Anthropic_Architect_Study_Plan.xlsx): Architecture learning reference.
