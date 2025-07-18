from Tools import list_files, read_file, search_in_file
from Action import Action
from ActionRegistry import ActionRegistry


# Create and populate the action registry
registery = ActionRegistry()

registery.register(Action(
    name="list_files",
    function=list_files,
    description="List all files in the current directory.",
    parameters={
        "type": "object",
        "properties": {},
        "required": []
    },
    terminal=False
))

registery.register(Action(
    name="read_file",
    function=read_file,
    description="Read the contents of a specified file.",
    parameters={
        "type": "object",
        "properties": {
            "file_name": {
                "type": "string",
                "description": "The name of the file to read."
            }
        },
        "required": ["file_name"]
    },
    terminal=False
))

registery.register(Action(
    name="search_in_file",
    function=search_in_file,
    description="Search for a term in a specified file and return matching lines.",
    parameters={
        "type": "object",
        "properties": {
            "file_name": {
                "type": "string",
                "description": "The name of the file to search in."
            },
            "search_term": {
                "type": "string",
                "description": "The term to search for in the file."
            }
        },
        "required": ["file_name", "search_term"]
    },
    terminal=False
))
