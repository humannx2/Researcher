from langchain_anthropic import ChatAnthropic
from browser_use import Agent
import asyncio
import os

# # Initialize the model
# llm = ChatAnthropic(
#     model_name="claude-3-sonnet-20240229",
#     temperature=0.0,
#     timeout=100, # Increase for complex tasks
# )

# # Create agent with the model
# agent = Agent(
#     task="Your task here",
#     llm=llm
# )

api_key = os.getenv("ANTHROPIC_API_KEY")
# print(api_key)

async def main():
    agent=Agent(
        task="Give me a summary of the top trending news in AI",
        llm=ChatAnthropic(
        # model_name="Claude 3.5 Sonnet 2024-06-20",
        model_name="Claude 3.5 Haiku",
        temperature=0.5,
        timeout=100, # Increase for complex tasks
        api_key=api_key
        )
    )
    result= await agent.run()
    print(result)

asyncio.run(main())