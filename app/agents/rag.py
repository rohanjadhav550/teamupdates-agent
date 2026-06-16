from dotenv import load_dotenv
import os
from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_ollama import OllamaLLM, OllamaEmbeddings
from langchain_pinecone import PineconeVectorStore
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from operator import itemgetter
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

print("Initiating Jira agent....")

embedder = OllamaEmbeddings(model="qwen3-embedding")
llm = OllamaLLM(
    model="gemma4",
    temperature=0
)
# embedder = GoogleGenerativeAIEmbeddings(model="gemini-embedding-001")
# llm = ChatGoogleGenerativeAI(
#     model="gemma-4-26b-a4b-it",
#     temperature=0,
# )  
vectores = PineconeVectorStore(
    index_name=os.environ["INDEX_NAME"],
    embedding=embedder
)

print("Retriving Vectors...")
retriver = vectores.as_retriever()

prompt_template = ChatPromptTemplate.from_template(
    """
    You are a expert Scrum master and know how to operate with Jira.

    You must always check the knowldge base only and never do any search or any operation outside the knowldgebase
    Answer the Questions based on the following context:
    {context}
    Question: {question}
    Provide detailed answer.
    """
)
print("chain initiation....")

def format_doc(docs):
    print("Doc formatiing....")
    return "\n\n".join(doc.page_content for doc in docs)

def chain_fun():
    """
    simple retrival chain
    """
    print("Chain initiated....")
    return (
        RunnablePassthrough.assign(
            context=itemgetter("question") | retriver | format_doc
        )
        | prompt_template
        | llm
        | StrOutputParser()
    )

def ask_jira(question: str):
    print("Welcome to my Jira Chat")

    chain = chain_fun()

    result = chain.invoke({"question":question})

    return result
