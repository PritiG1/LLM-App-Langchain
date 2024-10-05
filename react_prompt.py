from langchain_core.prompts import PromptTemplate

def get_react_prompt_template():
    return PromptTemplate.from_template("""Answer the following questions as best you can. You have access to the following tools:

{tools}

Use the following format:

Question: the input question you must answer
Thought: You should always think about what to do next.
Action: The action to take, should be one of [{tool_names}]
Action Input: The input to the action
Observation: The result of the action

Once you receive the first relevant web link (starting with https:) from the tool, stop all further thoughts and provide the final answer immediately. Do not care about the quantity or measurement or type of the ingridient.

Thought: I now know the final answer
Final Answer: The final answer to the original input question

Begin!

Question: {input}
Thought: {agent_scratchpad}
""")