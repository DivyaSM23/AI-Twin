from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from ingest import load_and_prepare_documents
from vector_store import create_vector_store
from summarize import generate_summary
from qa import answer_query
import uvicorn
import json

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

# Load and prepare data
documents = load_and_prepare_documents()
vectordb = create_vector_store(documents)

class QueryRequest(BaseModel):
    question: str

@app.get("/", response_class=HTMLResponse)
def serve_ui():
    return open("static/index.html").read()

@app.get("/summarize")
def get_summary():
    context = "\n".join(documents)
    summary = generate_summary(context)
    calendar_events = []
    notes = []

    with open("data/calendar.json") as f:
            calendar_raw = json.load(f)
            calendar_dict = {
                (event["title"], ", ".join(event["participants"])): event for event in calendar_raw
            }
    for d in documents:
            if "Meeting:" in d:
                try:
                    title = d.split("Meeting: ")[1].split(" with ")[0]
                    participants = d.split("with ")[1].split("\n")[0]
                    notes_text = d.split("Notes: ")[1] if "Notes: " in d else ""

                    key = (title, participants)
                    if key in calendar_dict:
                        event = calendar_dict[key]
                        start_time = event["start"]
                        end_time = event["end"]
                    else:
                        start_time = ""
                        end_time = ""

                    calendar_events.append({
                        "title": title,
                        "participants": participants,
                        "notes": notes_text,
                        "start": start_time,
                        "end": end_time
                    })
                except:
                    calendar_events.append({"raw": d})
            elif d.startswith("Notes:\n"):
                notes_text = d.replace("Notes:\n", "").strip()
                notes.extend([line.strip() for line in notes_text.split("\n") if line.strip()])

    return {
            "summary": summary,
            "calendar": calendar_events,
            "notes": notes
    }

@app.post("/ask")
def ask_question(request: QueryRequest):
    response = answer_query(request.question, vectordb)
    return {"answer": response}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
