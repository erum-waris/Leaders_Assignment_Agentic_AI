from litellm import completion
import os

os.environ["OPENAI_API_KEY"] = "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"
os.environ["GEMINI_API_KEY"] = "AIzaSyAe9AP_dxas9OPIJkLEdkCpZKgRL_fn4sA"

def openai():
    response = completion(
        model="openai/gpt-4o",
        messages=[{ "content": "Hello, how are you?","role": "user"}]
    )
 
    print(response)

def gemini():
    response = completion(
        model="gemini/gemini-1.5-flash",
        messages=[{ "content": "Hello, how are you?","role": "user"}]
    )

    print(response)

def gemini2():
    response = completion(
        model="gemini/gemini-2.0-flash-exp",
        messages=[{ "content": "Hello, how are you?","role": "user"}]
    )

    print(response)