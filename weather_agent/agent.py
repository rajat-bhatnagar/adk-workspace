from google.adk.agents.llm_agent import LlmAgent


def get_weather(city: str) -> dict:
    """Retrieves the current weather for a specified city."""
    # In a real implementation, this would call a weather API
    return {
        "status": "success",
        "report": f"Weather in {city} is sunny, 25°C"
    }

weather_agent = LlmAgent(
    model='gemini-3.5-flash',
    name='root_agent',
    description='Answer questions about the weather in the city.',
    instruction='You are an agent that provides the weather in the city.',
    tools=[get_weather]
)

root_agent = weather_agent