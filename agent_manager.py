## agent_manager.py
import os
import streamlit as st
from langchain_core.prompts import PromptTemplate
from langchain_ollama.llms import OllamaLLM
from langchain.tools import Tool
from langchain import hub
from react_prompt import get_react_prompt_template
from langchain.agents import create_react_agent, AgentExecutor
from langchain_community.utilities import GoogleSerperAPIWrapper
from dotenv import load_dotenv
load_dotenv()

serper_api_key = os.getenv('serper_apikey')
search = GoogleSerperAPIWrapper(serper_api_key=serper_api_key)


# Wrap the string in a PromptTemplate object
prompt_template = get_react_prompt_template()

def get_price_for_ingredient(ingredient: str):
    """Fetch price link for a specific ingredient."""
    search_results = search.results(f"Amazon price of {ingredient} in India")
    #print(f"Search Results for {ingredient}: {search_results}")  # Debugging line
    if "organic" in search_results and search_results["organic"]:
        return search_results["organic"][0]["link"]  # Return first organic result's link
    return "Price not found"

def initialize_price_finder_agent():
    """Initialize agent for finding price links."""
    ollama_llm = OllamaLLM(model="llama3.1")
    price_tool = Tool(
        name="Price Finder Tool",
        func=get_price_for_ingredient,
        description="Fetches the price link for ingredients."
    )
    
    tools = [price_tool]
    
    # Create the agent using the new LLMChain
    agent = create_react_agent(
    ollama_llm,
    tools,
    prompt_template
)
    agent_executor = AgentExecutor(agent=agent,tools =tools,max_iterations=3,verbose=True)
    return agent_executor

def fetch_ingredient_prices(agent_executor, ingredients):
    """Fetch price links for each ingredient using the agent."""
    st.write("**Price Links for Ingredients:**")
    for ingredient in ingredients[:2]:  # Limit to first 2 ingredients
        try:
            result = agent_executor.invoke({"input":ingredient})
            st.write(f"- {ingredient}: [Check Price]({result['output']})")
        except Exception as e:
            st.write(f"- {ingredient}: Failed to fetch price link.")
        
