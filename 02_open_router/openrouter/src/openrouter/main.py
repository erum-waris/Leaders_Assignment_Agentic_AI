import os
from agents import Agent, Runner, OpenAIChatCompletionsModel, AsyncOpenAI, set_tracing_disabled
from dotenv import load_dotenv

def agent():
    # Load environment variables from .env file
    load_dotenv()

    # Disable tracing logs (optional)
    set_tracing_disabled(True)

    # Create the OpenAI-compatible client with OpenRouter
    provider = AsyncOpenAI(
        api_key=os.getenv("OPENROUTER_API_KEY"),
        base_url=os.getenv("BASE_URL")  # Use BASE_URL from .env for flexibility
    )

    # Define the model to use (Gemini or any other OpenRouter-supported model)
    model = OpenAIChatCompletionsModel(
        model=os.getenv("MODEL"),  # Also pulled from .env for dynamic switching
        openai_client=provider,
    )

    # Define your AI agent
    Assistant = Agent(
        name="ChefBot",
        instructions="You are a master chef who explains recipes in a friendly tone.",
        model=model
    )

    # Ask the AI a cooking-related question
    user_input = """
    I want to impress my guests with a dessert. Can you give me a recipe for chocolate lava cake?
    """

    # Run the agent synchronously
    response = Runner.run_sync(
        starting_agent=Assistant,
        input=user_input,
    )

    # Print the result
    print("-" * 30)
    print("🍰 Response from ChefBot:")
    print(response.final_output)
    print("-" * 30)

if __name__ == "__main__":
    agent()
