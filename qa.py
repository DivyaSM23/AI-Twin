# qa.py
from transformers import pipeline

qa_pipeline = pipeline("question-answering", model="deepset/roberta-base-squad2")

def answer_query(query, vectordb):
    # Use Chroma to find relevant chunks
    results = vectordb.query(query_texts=[query], n_results=3)
    context = " ".join(results['documents'][0])
    result = qa_pipeline(question=query, context=context)
    return result['answer']
