from langchain.agents import create_agent
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

products = {
    "headphones":{
        "title":"Soundcore Headphones",
        "description":"These are soundcore wireless headphones",
        "price":"12000/-"
    },
    "earbuds":{
        "title":"Soundcore Earbuds",
        "description":"These are soundcore wireless earbuds",
        "price":"5000/-"
    },
    "phone":{
        "title":"Samsung S30",
        "description":"This is Samsung new launched smartphone",
        "price":"120000/-"
    }
}

def get_product(name:str)->str:
    """lookup the product by its name and return its title, description and price"""

    product = products.get(name.lower())

    if not product:
        return "No product found"

    return str(product)

llm = ChatGroq(model="llama-3.1-8b-instant",api_key=api_key)

agent = create_agent(
    llm,
    tools=[get_product],
    system_prompt="You are an helpful shopping assistant that use the tools to answer the questions"
)

result = agent.invoke({"messages":[{"role":"user","content":"Give me the product earbuds"}]})

print(result["messages"][-1].content)