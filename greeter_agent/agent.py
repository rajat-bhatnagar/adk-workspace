from google.adk.agents import LlmAgent
from google.adk.agents.callback_context import CallbackContext

def initialize_greeting_state(context: CallbackContext) -> None:
    """Supply defaults in the session ADK is actually running."""
    context.state.setdefault("user_name", "Alex")
    context.state.setdefault("user_language", "Spanish")


root_agent = LlmAgent(
    name="localized_greeter",
    model='gemini-3.5-flash',
    instruction="Hello {user_name}. Please respond in {user_language}.",
    before_agent_callback=initialize_greeting_state,
)
