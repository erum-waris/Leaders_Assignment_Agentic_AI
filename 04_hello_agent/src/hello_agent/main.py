# import os
# from dotenv import load_dotenv
# import asyncio
# import openai # OpenAI's official Python library

# # Load the environment variables from the .env file
# load_dotenv()

# gemini_api_key = os.getenv("GEMINI_API_KEY")

# # Check if the API key is present; if not, raise an error
# if not gemini_api_key:
#     raise ValueError("GEMINI_API_KEY is not set. Please ensure it is defined in your .env file.")

# # Configure the OpenAI client to use Google Gemini's OpenAI-compatible endpoint
# # Reference: https://ai.google.dev/gemini-api/docs/openai
# client = openai.OpenAI(
#     api_key=gemini_api_key,
#     base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
# )

# async def main():
#     # Define the "agent" behavior using a system message for chat completions
#     # This replaces the 'Agent' class from the 'agents' library.
#     system_instruction = "You are a helpful assistant."

#     user_query = "what is AI?."

#     print(f"User: {user_query}")

#     try:
#         # Use OpenAI's chat completions to interact with the Gemini model
#         # This replaces the 'Runner.run' logic.
#         response = client.chat.completions.create(
#             model="gemini-1.5-flash", # Using gemini-1.5-flash as it's common, you can change to gemini-2.0-flash if available and preferred
#             messages=[
#                 {"role": "system", "content": system_instruction},
#                 {"role": "user", "content": user_query},
#             ],
#             max_tokens=200 # Optional: Limit the response length
#         )

#         # Access the content from the response
#         assistant_response = response.choices[0].message.content
#         print(f"Assistant: {assistant_response}")

#     except openai.APIStatusError as e:
#         print(f"OpenAI API Error: {e.status_code} - {e.response}")
#         print("Please check your API key, base_url, and model name.")
#     except Exception as e:
#         print(f"An unexpected error occurred: {e}")


# if __name__ == "__main__":
#     asyncio.run(main())


