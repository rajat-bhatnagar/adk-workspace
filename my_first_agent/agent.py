from google.adk.agents.llm_agent import Agent

first_agent = Agent(
    model='gemini-3.5-flash',        # Model : The reasoning engine
    name='root_agent',               # Identity : Required Identifier
    description='A helpful Agent.',  # Purpose : What this Agent does
    instruction='You are helpful',   # Behavior : How to Act
    # Tools: You'll add these in the "Other ways to run your agent" module
    # Orchestration: Handled automatically by Agent class
)

root_agent = first_agent
