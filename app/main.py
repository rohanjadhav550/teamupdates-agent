from embadder import embedding
from agents.rag import ask_jira

def ask(question: str):
    return ask_jira("Give me all ticket IDs")

def main():
    print("main")
    result = ask("Brief me what all works done and there details by Gaurav.""")
    print(result)

if __name__ == "__main__":
    main()