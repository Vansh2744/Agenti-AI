from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain.agents import create_agent

load_dotenv()

llm = ChatGroq(model="llama-3.1-8b-instant")

agent = create_agent(
    model=llm,
    tools=[],
    system_prompt="You are an therapy assistant"
)