from google.genai import types
from google import genai
from dotenv import load_dotenv
from genai.utils import load_prompt
import os
load_dotenv()
client=genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
def parse_query(query):
    '''
    This function takes a query as input and returns a json object
    Args:
        query (str): The query to parse
    Returns:
        json object: The parsed query
    '''
    prompt=load_prompt(filename="prompt.txt")
    response = client.models.generate_content(
    model="gemini-2.0-flash-001",
    contents="high",
    config=types.GenerateContentConfig(
        system_instruction=f'''
        {prompt}

        {query}
        '''
    )
    )
    return response.text
