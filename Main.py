import os
import json
from Action import Action
from litellm import completion
from AgentFunctionCallingActionLanguage import AgentFunctionCallingActionLanguage
from Agent import Agent
from Environment import Environment
from Goal import Goal
from Prompt import Prompt
from ToolRegistration import action_registry
from dotenv import load_dotenv

load_dotenv()
os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')

# Define the agent's goals
goals = [
        Goal(priority=1, name="Gather Information", description="Read each file in the project"),
        Goal(priority=1, name="Terminate", description="Call the terminate call when you have read all the files "
                                                       "and provide the content of the README in the terminate message")
    ]

def generate_response(prompt: Prompt) -> str:
    """Call LLM to get response"""

    messages = prompt.messages
    tools = prompt.tools

    result = None

    if not tools:
        response = completion(
            model="openai/gpt-4o",
            messages=messages,
            max_tokens=1024
        )
        result = response.choices[0].message.content
    else:
        response = completion(
            model="openai/gpt-4o",
            messages=messages,
            tools=tools,
            max_tokens=1024
        )

        if response.choices[0].message.tool_calls:
            tool = response.choices[0].message.tool_calls[0]
            result = {
                "tool": tool.function.name,
                "args": json.loads(tool.function.arguments),
            }
            result = json.dumps(result)
        else:
            result = response.choices[0].message.content


    return result
# Define the agent's language
agent_language = AgentFunctionCallingActionLanguage()

# Define the environment
environment = Environment()

# Create an agent instance
agent = Agent(goals, agent_language, action_registry, generate_response, environment)

# Run the agent with user input
user_input = "Write a README for this project."
final_memory = agent.run(user_input)

# Print the final memory
print(final_memory.get_memories())