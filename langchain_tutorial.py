from langchain.agents import AgentType, initialize_agent, load_tools, get_all_tool_names
from langchain.llms import OpenAI

llm = OpenAI(temperature=0)

# print("model_name: ", llm.model_name)


# all_tool_names = get_all_tool_names()

# print(all_tool_names)

tools = load_tools(["serpapi", "llm-math"], llm=llm)


agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,verbose=True)
output = agent.run("今日の新宿区の最高気温の摂氏温度の平方根はいくつ？")

print(output)
