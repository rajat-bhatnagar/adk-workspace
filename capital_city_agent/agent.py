from google.adk.agents import LlmAgent


# Step 1: Define a tool function
def get_capital_city(country: str) -> str:
    """Retrieves the capital city for a given country."""
    capitals = {"france": "Paris", "japan": "Tokyo", "canada": "Ottawa"}
    return capitals.get(country.lower(), f"Sorry, I don't know the capital of {country}.")


# Step 2: Add the tool to the agent
capital_agent = LlmAgent(
    model='gemini-3.5-flash',
    name="capital_agent",
    description="Answers questions about capital cities.",
    instruction="You are an agent that provides the capital city of a country.",
    tools=[get_capital_city]  # ✨ NEW: tools parameter
)

root_agent = capital_agent
