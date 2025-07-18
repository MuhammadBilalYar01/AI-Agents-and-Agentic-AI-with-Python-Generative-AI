class Memory:
    def __init__(self):
        self.items = []  # Basic conversation histor
        
    def add_memory(self, memory:dict):
        """Add memory to working memory"""
        self.items.append(memory)
        
    def get_memories(self, limit:int = None) ->list[dict]:
        """Get formatted conversation history for prompt"""
        return self.items[:limit]