# AI-Agents-and-Agentic-AI-with-Python-Generative-AI
AI Agents and Agentic AI with Python & Generative AI

## Agent Simulation Example

I'd like to simulate an AI agent that I'm designing. The agent will be built using these components:

**Goals:**
- Find potential code enhancements
- Ensure changes are small and self-contained
- Get user approval before making changes
- Maintain existing interfaces

**Actions available:**
- `list_project_files()`
- `read_project_file(filename)`
- `ask_user_approval(proposal)`
- `edit_project_file(filename, changes)`

At each step, your output must be an action to take.

Stop and wait and I will type in the result of the action as my next message.

Ask me for the first task to perform.

---

# README for the Project

## Overview
This project implements a simple agent-based framework for achieving goals in an environment simulated through code. The central components of this implementation revolve around the concepts of Agents, Actions, Goals, Memories, and Environments. The environment is designed to process various actions executed by the agent.

## Structure

- **Action.py:** Defines the `Action` class, which models executable functions with specific parameters that the agent can invoke.
- **ActionRegistry.py:** Manages an `ActionRegistry` class to register and retrieve available agent actions.
- **Agent.py:** Develops the `Agent` class, which can perform actions based on goals and interact with the environment using defined strategies and memory.
- **AgentFunctionCallingActionLanguage.py:** Implements `AgentLanguage`, specializing in formatting agent goals, memory, and actions into structured prompts and parsing the agent's responses.
- **AgentLanguage.py:** Provides a base class for defining how the agent will construct prompts and parse responses. It sets the foundation for how the agent will understand and execute its tasks.
- **Environment.py:** Models the `Environment` class where agent actions occur, and results are returned, formatted with metadata.
- **Example.py:** Contains an example setup for a `Goal`, demonstrating the use of the framework.
- **Goal.py:** Defines the `Goal` class, used to specify objectives that the agent strives to achieve.
- **Main.py:** The main entry point that initializes goals, the agent language, environment, and actions. It runs the agent with user input and processes tasks iteratively.
- **Memory.py:** Provides a `Memory` class, enabling the agent to store and recall past interactions to inform future decisions.
- **Prompt.py:** Defines a `Prompt` data structure used to format messages and tools that guide agent interactions.
- **ToolRegistration.py:** Registers actions using the `ActionRegistry`, wiring them up with their functionalities such as listing and reading project files.
- **Tools.py:** Implements functions for listing and reading files in the project, enabling file management tasks for the agent.

## Usage
To execute this project, run the `Main.py` script, which initializes the agent, defines its goals, sets up the environment and actions, and initiates the agent loop with the task to write a README using the project files as a resource.

This implementation demonstrates fundamental principles of agent-based systems, emphasizing modularity and abstraction to flexibly define objectives and interactions. By iterating over tasks and employing memory, the agent simulates decision-making in a controlled environment.