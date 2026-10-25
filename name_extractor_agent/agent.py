import asyncio

from google.adk import Runner
from google.adk.agents.llm_agent import LlmAgent
from google.adk.sessions import InMemorySessionService
from google.genai import types

# Create agent with output_key to save response
root_agent = LlmAgent(
    model='gemini-3.5-flash',
    name='root_agent',
    description='User Name Extractor.',
    instruction="Extract the user's name. Return only the name",
    output_key="user_name",  # Saves response to state["user_name"]
)
async def main() -> None:
    """Run the example directly without executing it during ADK imports."""
    session_service = InMemorySessionService()
    session = await session_service.create_session(app_name="my_app", user_id="user1")
    runner = Runner(agent=root_agent, app_name="my_app", session_service=session_service)
    async for _ in runner.run_async(
        user_id="user1",
        session_id=session.id,
        new_message=types.Content(
            role="user", parts=[types.Part(text="My name is Alex")]
        ),
    ):
        pass

    updated_session = await session_service.get_session(
        app_name="my_app", user_id="user1", session_id=session.id
    )
    if updated_session is None:
        raise RuntimeError("Session was not found after the agent run")
    print(updated_session.state)
    print(updated_session.state.get("user_name"))
    if updated_session.state.get("user_name"):
        print("User has provided their name!")

if __name__ == "__main__":
    asyncio.run(main())
