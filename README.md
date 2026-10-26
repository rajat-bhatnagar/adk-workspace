# Google Agent Development Kit (ADK) Workspace

This repository contains hands-on implementations, prototypes, and study experiments built with **Google Agent Development Kit (ADK)** (`google-adk`). It covers essential agent patterns ranging from minimal code-based and YAML-declarative agents to session state management, lifecycle callbacks, tool integration, and programmatic execution runners.

---

## Workspace Overview

The workspace demonstrates two primary styles of agent authoring in Google ADK:
1. **Programmatic Python Agents (`agent.py`)**: Authoring agents via `google.adk.agents.LlmAgent` / `Agent`, utilizing lifecycle callbacks (`before_agent_callback`), dynamic template interpolation, and programmatic execution via `google.adk.runners.Runner`.
2. **Declarative Config Agents (`root_agent.yaml`)**: Defining agents, system instructions, and tool integrations purely through YAML configuration matching the ADK `AgentConfig` schema.

---

## Agent Implementations

| Agent Directory | Format | Primary Model | Key Concept & Purpose |
|---|---|---|---|
| [`my_first_agent`](file:///Users/rajatbhatnagar/repos/adk-workspace/my_first_agent/agent.py) | Python | `gemini-3.5-flash` | **Baseline Agent**: Foundational `Agent` instance with identity, description, and instructions. |
| [`config_agent`](file:///Users/rajatbhatnagar/repos/adk-workspace/config_agent/root_agent.yaml) | YAML | `gemini-flash-latest` | **Declarative Agent**: Complete YAML configuration for an algebra tutor with structured pedagogical guidelines. |
| [`maths_agent`](file:///Users/rajatbhatnagar/repos/adk-workspace/maths_agent/root_agent.yaml) | YAML | `gemini-3.5-flash` | **Minimal Declarative Agent**: Lightweight YAML-based maths tutor configuration. |
| [`search_agent`](file:///Users/rajatbhatnagar/repos/adk-workspace/search_agent/root_agent.yaml) | YAML | `gemini-3.5-flash` | **Tool Integration**: Demonstrates binding built-in tools (`google_search`) directly in YAML. |
| [`greeter_agent`](file:///Users/rajatbhatnagar/repos/adk-workspace/greeter_agent/agent.py) | Python | `gemini-3.5-flash` | **Lifecycle Callbacks & Templating**: Uses `before_agent_callback` (`CallbackContext`) to initialize session state and inject dynamic variables (`{user_name}`, `{user_language}`) into prompt instructions. |
| [`name_extractor`](file:///Users/rajatbhatnagar/repos/adk-workspace/name_extractor/agent.py) | Python | `gemini-3.5-flash` | **State Extraction & Multi-Turn Testing**: Uses `output_key="user_name"` to persist agent outputs to `session.state`, accompanied by a multi-turn programmatic runner test (`test_state.py`). |
| [`name_extractor_agent`](file:///Users/rajatbhatnagar/repos/adk-workspace/name_extractor_agent/agent.py) | Python | `gemini-3.5-flash` | **Self-Contained Runner**: Single-file demonstration combining `LlmAgent`, `InMemorySessionService`, and `Runner`. |

---

## Detailed Agent Breakdown

### 1. `my_first_agent`
* **Path**: [`my_first_agent/agent.py`](file:///Users/rajatbhatnagar/repos/adk-workspace/my_first_agent/agent.py)
* **Description**: A minimal "Hello World" agent in Python using `google.adk.agents.llm_agent.Agent`.
* **Key Components**:
  - `model`: Reasoning model (`gemini-3.5-flash`).
  - `name`: Identifier used by the ADK framework (`root_agent`).
  - `description`: Agent purpose.
  - `instruction`: Core behavior instruction.

### 2. `config_agent`
* **Path**: [`config_agent/root_agent.yaml`](file:///Users/rajatbhatnagar/repos/adk-workspace/config_agent/root_agent.yaml)
* **Description**: A declarative agent created via `adk create --type=config config_agent`.
* **Key Components**:
  - Adheres to the official ADK `AgentConfig.json` schema (`yaml-language-server`).
  - Implements an algebra tutor persona (`math_tutor_agent`) using `gemini-flash-latest`.
  - Encapsulates multi-step teaching instructions directly in YAML without writing Python code.

### 3. `maths_agent`
* **Path**: [`maths_agent/root_agent.yaml`](file:///Users/rajatbhatnagar/repos/adk-workspace/maths_agent/root_agent.yaml)
* **Description**: A streamlined declarative YAML agent.
* **Key Components**:
  - Configures a maths tutor agent targeting `gemini-3.5-flash`.
  - Minimalist specification showing the core required YAML fields: `name`, `model`, `description`, `instruction`.

### 4. `search_agent`
* **Path**: [`search_agent/root_agent.yaml`](file:///Users/rajatbhatnagar/repos/adk-workspace/search_agent/root_agent.yaml)
* **Description**: Demonstrates tool attachment in declarative YAML.
* **Key Components**:
  - Configured with `tools: - name: google_search`.
  - Enables the agent to execute Google searches and answer questions based on retrieved web results.

### 5. `greeter_agent`
* **Path**: [`greeter_agent/agent.py`](file:///Users/rajatbhatnagar/repos/adk-workspace/greeter_agent/agent.py)
* **Description**: Demonstrates dynamic prompt templating and session state initialization via lifecycle callbacks.
* **Key Components**:
  - **`initialize_greeting_state(context: CallbackContext)`**: Intercepts the execution lifecycle to set default state values (`user_name`, `user_language`) using `context.state.setdefault()`.
  - **`before_agent_callback`**: Hook executed prior to agent reasoning.
  - **Templated Instructions**: Prompt instruction `Hello {user_name}. Please respond in {user_language}.` dynamically interpolates values populated from `session.state`.

### 6. `name_extractor`
* **Path**: [`name_extractor/agent.py`](file:///Users/rajatbhatnagar/repos/adk-workspace/name_extractor/agent.py) & [`name_extractor/test_state.py`](file:///Users/rajatbhatnagar/repos/adk-workspace/name_extractor/test_state.py)
* **Description**: Demonstrates state output persistence and multi-turn state verification.
* **Key Components**:
  - **`output_key="user_name"`**: Instructs the agent to automatically write its final output directly into `session.state["user_name"]`.
  - **`test_state.py`**: A programmatic verification script using `Runner` and `InMemorySessionService`:
    1. Initializes an in-memory session.
    2. Sends a first turn ("*Hi, my name is Alex Johnson*") and streams response events via `runner.run_async()`.
    3. Asserts and prints the session state to confirm extraction.
    4. Executes a second turn ("*What's my name?*") to prove state persistence across turns.

### 7. `name_extractor_agent`
* **Path**: [`name_extractor_agent/agent.py`](file:///Users/rajatbhatnagar/repos/adk-workspace/name_extractor_agent/agent.py)
* **Description**: A self-contained script that unifies the agent definition and execution runner into one file.
* **Key Components**:
  - Defines `root_agent` with `output_key="user_name"`.
  - Contains an executable `main()` block running `InMemorySessionService` and `Runner` for rapid CLI experimentation.

---

## Getting Started

### Prerequisites
- Python 3.10+ (tested with Python 3.15)
- Active Google Gemini API key or Google Cloud credentials

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

Detailed reference study guides and codelab tracking worksheets are located in [`docs/`](file:///Users/rajatbhatnagar/repos/adk-workspace/docs):
- [`docs/a-week-study-plan_23rd-to-30th-Oct-26.MD`](file:///Users/rajatbhatnagar/repos/adk-workspace/docs/a-week-study-plan_23rd-to-30th-Oct-26.MD): 1-week master curriculum for Google ADK, Model Context Protocol (MCP), and Agent2Agent (A2A) protocol.
- [`docs/agentic_ai_mastery_worksheet_v7.xlsx`](file:///Users/rajatbhatnagar/repos/adk-workspace/docs/agentic_ai_mastery_worksheet_v7.xlsx): Progress tracking worksheet for skills, badges, and codelabs.
- [`docs/Anthropic_Architect_Study_Plan.xlsx`](file:///Users/rajatbhatnagar/repos/adk-workspace/docs/Anthropic_Architect_Study_Plan.xlsx): Architecture learning reference.
