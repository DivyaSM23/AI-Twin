from ingest import load_and_prepare_documents
from vector_store import create_vector_store
from summarize import generate_summary
from qa import answer_query
import argparse

vectordb = None

def main():
    global vectordb

    parser = argparse.ArgumentParser(description="AI Twin Prototype")
    parser.add_argument("command", choices=["summarize", "ask"], help="What to do")
    parser.add_argument("--query", type=str, help="Question to ask your AI twin")
    args = parser.parse_args()

    documents = load_and_prepare_documents()
    vectordb = create_vector_store(documents)

    if args.command == "summarize":
        context = "\n".join(documents)
        summary = generate_summary(context)
        print("\n--- Daily Summary ---\n")
        print(summary)

    elif args.command == "ask" and args.query:
        response = answer_query(args.query, vectordb)
        print("\n--- Answer ---\n")
        print(response)

if __name__ == "__main__":
    main()