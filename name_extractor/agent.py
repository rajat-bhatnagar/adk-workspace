"""
Name Extractor - Demonstrates Session State Basics
Shows how to use output_key to save data and access it via session.state.

Reference: https://adk.dev/sessions/state/
"""

from google.adk.agents import LlmAgent

# Single agent that extracts and saves name
root_agent = LlmAgent(
    model='gemini-3.5-flash',
    name="name_extractor",
    instruction="Extract the person's name from the message. Return ONLY the name, nothing else.",
    output_key="user_name"  # Saves response to state["user_name"]
)