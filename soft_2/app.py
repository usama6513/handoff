from agents import (
    Agent,
    Runner,
    OpenAIChatCompletionsModel,
    RunConfig,
    handoff
)
from openai import AsyncOpenAI
gemini_api_key = ""

#Reference: https://ai.google.dev/gemini-api/docs/openai
client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)
model = OpenAIChatCompletionsModel(
    model="gemini-2.5-pro",
    openai_client=client,
)

config = RunConfig(
    model=model,
    model_provider=client,
    tracing_disabled=True
)

maths_assistant = Agent(name = "maths Assistant")
astronomy_assistant = Agent(name = "astronomy Assistant")
astronomy_handoff = handoff(
    agent = astronomy_assistant,
    tool_name_override = "specialized_astronomy_agent",
    tool_description_override = "You are specialized  astronomy agent")

Lead_agent = Agent(
    name = "Lead agent",
    instructions = "You are a Lead agent you will be given specified tasks and projects and you have to handoff to the specialized agents according to thier issues",
    handoffs = [
        maths_assistant,
        astronomy_assistant
    ]
)

result = Runner.run_sync(
    starting_agent = Lead_agent,
    input = "I am some issues about telescope and their parts",
    run_config = config
)


print("last agnet>>>>>>>", result.last_agent)
print("result>>>>>>>",result.final_output)
