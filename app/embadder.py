from dotenv import load_dotenv
import os
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_pinecone import PineconeVectorStore
from langchain_docling.loader import DoclingLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.vectorstores.utils import filter_complex_metadata
from langchain_ollama import OllamaEmbeddings

load_dotenv()

# embadder = OllamaEmbeddings(
#     model="qwen3-embedding"
# )
embadder = GoogleGenerativeAIEmbeddings(model="gemini-embedding-001")
text_splitter = CharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

def initiate_loader(file_path: str):
    return DoclingLoader(file_path=[file_path])

def delete_all():
    print("Initiating complete delete...")
    pinecone_vector = PineconeVectorStore(
        index_name=os.environ["INDEX_NAME"],
        embedding=embadder,
    )
    pinecone_vector.delete(delete_all=True)
    print("deletion process completed!")

def embedding(file_path: str):
    print("Initiating Process....")
    print('Loading the document...')
    loader = initiate_loader(file_path)
    document = loader.load()
    
    print('Splitting smartlly....')
    texts = text_splitter.split_documents(document)

    print('Formating the trims....')
    formated_texts = filter_complex_metadata(texts)

    print('Initiating embbade....')
    PineconeVectorStore.from_documents(formated_texts, embadder, index_name=os.environ["INDEX_NAME"])
    print('Vectore process completed!')

embedding("/media/rohan/D-Drive/Agentic development/teamupdates-agent/data/Jira_Tickets_Export.txt")
# delete_all()
