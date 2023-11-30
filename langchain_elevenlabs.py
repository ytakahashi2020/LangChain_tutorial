import os
from langchain.agents import AgentType, initialize_agent, load_tools, get_all_tool_names
from langchain.llms import OpenAI
from langchain.tools import ElevenLabsText2SpeechTool
from elevenlabs import generate, play, set_api_key, voices

set_api_key(os.environ.get("ELEVENLABS_API_KEY"))
# Initialize ElevenLabsText2SpeechTool
tts = ElevenLabsText2SpeechTool()


# Initialize LLM and agent
llm = OpenAI(temperature=0)

tools = load_tools(["eleven_labs_text2speech"])

# all_tools = get_all_tool_names();
# print(all_tools)


agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

# Request a joke and get the path to the audio file
response = agent.run("Please provide me with an audio file containing a joke about a tiger")
print("response: ", response)


tts.play(response)