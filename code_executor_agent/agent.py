from google.adk.agents.llm_agent import LlmAgent
from google.adk.code_executors import BuiltInCodeExecutor

root_agent = LlmAgent(
    model='gemini-3.5-flash',  # Must use gemini 2.0 or later
    name='code_agent',
    description='Calculation Execution Agent',
    instruction='Your help users with calculations and data processing',
    code_executor=BuiltInCodeExecutor()  # Enables code executions
)
