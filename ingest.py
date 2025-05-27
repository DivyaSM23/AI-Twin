import json

def load_and_prepare_documents():
    documents = []

    with open("data/email.json") as f:
        emails = json.load(f)
        for e in emails:
            documents.append(f"Email: {e['subject']}\n{e['body']}")

    with open("data/calendar.json") as f:
        meetings = json.load(f)
        for m in meetings:
            documents.append(f"Meeting: {m['title']} with {', '.join(m['participants'])}\nNotes: {m['notes']}")

    with open("data/notes.md") as f:
        notes = f.read()
        documents.append(f"Notes:\n{notes}")

    return documents