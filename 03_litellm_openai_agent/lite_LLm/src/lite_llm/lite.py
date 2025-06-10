from litellm import completion
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Retrieve the API keys from environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Set them as environment variables for LiteLLM to use internally
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
os.environ["GEMINI_API_KEY"] = GEMINI_API_KEY

def openai():
    response = completion(
        model="openai/gpt-4o",
        messages=[{"role": "user", "content": "Hello, how are you?"}]
    )
    print(response)

def gemini():
    response = completion(
        model="gemini/gemini-1.5-flash",
        messages=[{"role": "user", "content": "Hello, how are you?"}]
    )
    print(response)

def gemini2():
    response = completion(
        model="gemini/gemini-2.0-flash-exp",
        messages=[{"role": "user", "content": "Hello, how are you?"}]
    )
    print(response)

# Optional: Call functions for testing
# openai()
# gemini()
# gemini2()
