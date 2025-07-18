import os
def list_files():
    """List all files in the current directory."""
    return os.listdir('.')

def read_file(file_name) -> str:
    """Read and return the contents of a file."""
    with open(file_name, 'r') as file:
        return file.read()
    
def search_in_file(file_name, search_term) -> list[str]:
    """Search for a term in a file and return matching lines."""
    matches = []
    with open(file_name, 'r') as file:
        for i, line in enumerate(file.readlines()):
            if search_term in line:
                matches.append((i+1, line.strip()))
    return matches