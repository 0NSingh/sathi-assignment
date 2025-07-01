import os

def load_prompt(filename: str) -> str:
    """
    Load the contents of a text file from the prompts directory.
    
    Args:
        file_name (str): Name of the text file to load
        
    Returns:
        str: Contents of the text file
        
    Raises:
        FileNotFoundError: If the file doesn't exist
    """
    # Get the directory where this file is located
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Go up one level to the app directory    # Full path to the requested file
    file_path = os.path.join(current_dir, filename)
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"Prompt file not found: {filename}") 