# summarize.py
from transformers import pipeline

summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

def generate_summary(text):
    chunks = [text[i:i+1024] for i in range(0, len(text), 1024)]
    summaries = summarizer(chunks, max_length=150, min_length=30, do_sample=False)
    return "\n".join([s['summary_text'] for s in summaries])
