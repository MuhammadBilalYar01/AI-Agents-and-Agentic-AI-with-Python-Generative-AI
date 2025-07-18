# from Tools import list_files, read_file, search_in_file
from Tools import read_project_file, list_project_files
from Action import Action
from ActionRegistry import ActionRegistry


# Define the action registry and register some actions
action_registry = ActionRegistry()

action_registry.register(Action(
        name="list_project_files",
        function=list_project_files,
        description="Lists all files in the project.",
        parameters={},
        terminal=False
    ))

action_registry.register(Action(
        name="read_project_file",
        function=read_project_file,
        description="Reads a file from the project.",
        parameters={
            "type": "object",
            "properties": {
                "name": {"type": "string"}
            },
            "required": ["name"]
        },
        terminal=False
    ))

action_registry.register(Action(
        name="terminate",
        function=lambda message: f"{message}\nTerminating...",
        description="Terminates the session and prints the message to the user.",
        parameters={
            "type": "object",
            "properties": {
                "message": {"type": "string"}
            },
            "required": []
        },
        terminal=True
    ))



# Create and populate the action registry
# registery = ActionRegistry()

# registery.register(Action(
#     name="list_files",
#     function=list_files,
#     description="List all files in the current directory.",
#     parameters={
#         "type": "object",
#         "properties": {},
#         "required": []
#     },
#     terminal=False
# ))

# registery.register(Action(
#     name="read_file",
#     function=read_file,
#     description="Read the contents of a specified file.",
#     parameters={
#         "type": "object",
#         "properties": {
#             "file_name": {
#                 "type": "string",
#                 "description": "The name of the file to read."
#             }
#         },
#         "required": ["file_name"]
#     },
#     terminal=False
# ))

# registery.register(Action(
#     name="search_in_file",
#     function=search_in_file,
#     description="Search for a term in a specified file and return matching lines.",
#     parameters={
#         "type": "object",
#         "properties": {
#             "file_name": {
#                 "type": "string",
#                 "description": "The name of the file to search in."
#             },
#             "search_term": {
#                 "type": "string",
#                 "description": "The term to search for in the file."
#             }
#         },
#         "required": ["file_name", "search_term"]
#     },
#     terminal=False
# ))
