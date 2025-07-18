class Action:
    def __init__(self, 
                 name: str,
                 function: callable,
                 description: str,
                 parameters: dict,
                 terminal: bool = False):
        self.name = name
        self.function = function
        self.description = description
        self.terminal = terminal
        self.parameters = parameters

    def execute(self, **args) -> any:
        """Execute the action's function"""
        return self.function(**args)