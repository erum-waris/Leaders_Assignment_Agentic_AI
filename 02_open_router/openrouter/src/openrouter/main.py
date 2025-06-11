# import os
# from dotenv import load_dotenv
# import asyncio
# import openai

# # Load the environment variables from the .env file
# load_dotenv()

# # --- Your provided OpenRouter details ---
# openrouter_api_key = os.getenv("OPENROUTER_API_KEY")
# openrouter_base_url = "https://openrouter.ai/api/v1/"
# openrouter_model_name = "deepseek/deepseek-r1-distill-qwen-7b"

# # Check if the API key is present; if not, raise an error
# if not openrouter_api_key:
#     raise ValueError("OPENROUTER_API_KEY is not set. Please ensure it is defined in your .env file.")

# # Configure the OpenAI client to use OpenRouter's API endpoint
# client = openai.OpenAI(
#     api_key=openrouter_api_key,
#     base_url=openrouter_base_url,
# )

# async def main():
#     print("AI Assistant started. Type 'exit' to end the conversation.")

#     # Define the initial system instruction for the AI
#     messages = [
#         {"role": "system", "content": "You are a helpful assistant."},
#     ]

#     while True:
#         # Get user input
#         user_input = input("You: ")

#         if user_input.lower() == 'exit':
#             print("Assistant: Goodbye!")
#             break

#         # Add user's message to the history
#         messages.append({"role": "user", "content": user_input})

#         try:
#             # print("\n--- Sending request to OpenRouter ---") # Debug print
#             # print(f"Model: {openrouter_model_name}") # Debug print
#             # print(f"Messages being sent: {messages}") # Debug print

#             response = client.chat.completions.create(
#                 model=openrouter_model_name,
#                 messages=messages,
#                 max_tokens=200 # Optional: Limit the response length
#             )

#             # print("\n--- Raw API Response ---") # Debug print
#             # print(response) # Print the entire raw response object

#             if response.choices:
#                 assistant_response = response.choices[0].message.content
#                 if assistant_response:
#                     print(f"\nAssistant: {assistant_response}")
#                     # Add assistant's response to the history for future turns
#                     messages.append({"role": "assistant", "content": assistant_response})
#                 else:
#                     print("\nAssistant: (Received empty response content from model)")
#                     messages.append({"role": "assistant", "content": "Empty response"}) # Add to history
#             else:
#                 print("\nAssistant: (No choices found in API response)")
#                 messages.append({"role": "assistant", "content": "No response choices"}) # Add to history

#         except openai.APIStatusError as e:
#             error_message = e.response.json().get('error', {}).get('message', 'Unknown error from API')
#             print(f"\nOpenRouter API Error: {e.status_code} - {error_message}")
#             print("Please check your OPENROUTER_API_KEY, base_url, and model name on OpenRouter's documentation.")
#             break
#         except Exception as e:
#             print(f"\nAn unexpected error occurred: {e}")
#             break


# if __name__ == "__main__":
#     asyncio.run(main())

# 1. Using the OpenRouter API directly but hidden in .env file

# from dotenv import load_dotenv
# import requests
# import json
# import os

# load_dotenv()

# BASE_URL = "https://openrouter.ai/api/v1"
# OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
# MODEL = "deepseek/deepseek-r1-distill-qwen-7b"

# response = requests.post(
#   url=f"{BASE_URL}/chat/completions",
#   headers={
#     "Authorization": f"Bearer {OPENROUTER_API_KEY}",
#   },
#   data=json.dumps({
#     "model": MODEL,
#     "messages": [
#       {
#         "role": "user",
#         "content": "What is the meaning of Agentic AI How to implement?"
#       }
#     ]
#   })
# )

# print(response.json())


#  2. Using OpenAI Agents SDK
import os
from dotenv import load_dotenv
import asyncio
from openai import AsyncOpenAI
from agents import Agent, OpenAIChatCompletionsModel, Runner, set_tracing_disabled

load_dotenv()

BASE_URL = "https://openrouter.ai/api/v1"
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
MODEL = "deepseek/deepseek-r1-distill-qwen-7b"

client = AsyncOpenAI(
    api_key=OPENROUTER_API_KEY,
    base_url=BASE_URL
)

set_tracing_disabled(disabled=True)

async def main():
    # This agent will use the custom LLM provider
    agent = Agent(
        name="Assistant",
        instructions="You only respond in haikus.",
        model=OpenAIChatCompletionsModel(model=MODEL, openai_client=client),
    )

    result = await Runner.run(
        agent,
        "Tell me about programming how many programming languages are there?",
    )
    print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())    