from embadder import embedding
from rag import ask_jira

def embed_data(file_path: str):
    embedding(file_path)

def main():
    print("main")
    # embed_data("/media/rohan/D-Drive/Agentic development/teamupdates-agent/data/data.txt")
    result = ask_jira("Give me all ticket IDs")
    print(result)

if __name__ == "__main__":
    main()