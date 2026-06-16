from embadder import embedding
from agents.rag import ask_jira
def embed_data(file_path: str):
    embedding(file_path)

def ask(question: str):
    return ask_jira("Give me all ticket IDs")

def main():
    print("main")
    # embed_data("/media/rohan/D-Drive/Agentic development/teamupdates-agent/data/Jira_Tickets_Export.txt")
    result = ask("Brief me what all works done and there details by Gaurav.""")
    print(result)

if __name__ == "__main__":
    main()