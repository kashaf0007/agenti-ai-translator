from dotenv import load_dotenv
import os
from agents import Agent, AsyncOpenAI,Runner, OpenAIChatCompletionsModel
from agents.run import RunConfig


load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")


if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set. Please ensure it is defined in your .env file.")

external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)          

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)
     

aiagent = Agent(
    name = "AI Translation",
    instructions = "you are a helpfull tanslator always translate  a sentence into urdu"
) 
result = Runner.run_sync(
    aiagent,
    input = "  Hello, my name is Kashaf. How are you? ",
    run_config= config

)
print(result)