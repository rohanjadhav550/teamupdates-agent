from app.tools.tickets import get_all_tickets
from langchain.messages import HumanMessage
from langchain_ollama import ChatOllama
from langchain.agents import create_agent

print("="*10)
print("Tickets Agent")
print("="*10)
llm = ChatOllama(
    model="gemma4",
    temperature=0
)

print("+"*5)
print("Agent initiation..")
print("+"*5)
agent = create_agent(
    model=llm,
    tools=[
        get_all_tickets
    ]
)


question = "List me all the tickets present in the system"
print("+"*5)
print("Agent invoked..")
print("+"*5)
result = agent.invoke({
    "messages":[
        HumanMessage(question)
    ]
})

print("#"*10)
print(result['messages'][-1].content)
print("#"*10)


