"""Run the name extractor and inspect its session state.

Run with: python test_state.py
"""

import asyncio
from pathlib import Path

from dotenv import load_dotenv
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai.types import Content, Part

from agent import root_agent


async def main() -> None:
    load_dotenv(Path(__file__).with_name(".env"))

    session_service = InMemorySessionService()
    session = await session_service.create_session(
        app_name="name_extractor_app",
        user_id="test_user",
        session_id="test_session",
    )

    async with Runner(
        agent=root_agent,
        app_name="name_extractor_app",
        session_service=session_service,
    ) as runner:
        print("=== Running agent ===")
        async for event in runner.run_async(
            user_id="test_user",
            session_id=session.id,
            new_message=Content(role="user", parts=[Part(text="Hi, my name is Alex Johnson")]),
        ):
            if event.is_final_response():
                print(f"\nAgent response: {event.content.parts[0].text}")

        session = await session_service.get_session(
            app_name="name_extractor_app",
            user_id="test_user",
            session_id=session.id,
        )
        if session is None:
            raise RuntimeError("Session was not found after the first turn")

        print("\n=== State after execution ===")
        print(f"Full state: {session.state}")
        print(f"Extracted name: {session.state.get('user_name')}")

        if session.state.get("user_name"):
            print("Name was successfully extracted and stored!")
        else:
            print("Name extraction failed")

        print("\n=== Simulating second turn ===")
        async for event in runner.run_async(
            user_id="test_user",
            session_id=session.id,
            new_message=Content(role="user", parts=[Part(text="What's my name?")]),
        ):
            if event.is_final_response():
                print(f"Agent response: {event.content.parts[0].text}")

        session = await session_service.get_session(
            app_name="name_extractor_app",
            user_id="test_user",
            session_id=session.id,
        )
        if session is None:
            raise RuntimeError("Session was not found after the second turn")
        print(f"\nState still contains: {session.state.get('user_name')}")
        print("State persists across turns!")


if __name__ == "__main__":
    asyncio.run(main())
