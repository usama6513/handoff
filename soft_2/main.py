from agents import Agent, Runner, OpenAIChatCompletionsModel, RunConfig 
from openai import AsyncOpenAI

gemini_api_key = "AIzaSyBWGYNREjwmSgTsJXeEB_Cucs28CGb1gUc"

#Reference: https://ai.google.dev/gemini-api/docs/openai
client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)
model = OpenAIChatCompletionsModel(
    model="gemini-2.5-pro",
    openai_client=client
)

config = RunConfig(
    model=model,
    model_provider=client,
    tracing_disabled=True
)

maths_assistant = Agent(name ="maths Assistant")
python_assitant = Agent(name = "python Assistant")
Lead_agent = Agent(
    name="Lead Agent",
    instructions="you are a helpful triage agent you are knowing very well everything and  you have to handoff the specific tasks to the special agents ",
    handoffs=[maths_assistant, python_assitant])

result = Runner.run_sync(starting_agent=Lead_agent,input="I am having some issues about maths problem in parabola , explain it with the an example also", run_config=config)

print("Last agent>>>>>",result.last_agent)
print("result>>>>>", result.final_output)


