from google.adk.agents.llm_agent import LlmAgent

# Step 1: Write a Python function
def calculate_shipping_cost(weight_kg: float, country: str) -> dict:
    """Calculates shipping cost based on package weight and destination."""
    rates = {"usa": 10, "canada": 12, "uk": 15}

    if country.lower() not in rates:
        return {"status": "error", "error_message": f"We don't ship to {country}"}

    cost = weight_kg * rates[country.lower()]
    return {"status": "success", "cost_usd": cost}

# Step 2: Add function to agent's tools list
root_agent = LlmAgent(
    model='gemini-3.5-flash',        # Model : The reasoning engine
    name="shipping_agent",
    instruction="You help customers with shipping cost estimates.",
    tools=[calculate_shipping_cost]  # ADK automatically wraps as FunctionTool
)
