# vector_store.py
from sentence_transformers import SentenceTransformer
import chromadb
from chromadb.config import Settings

def create_vector_store(docs):
    model = SentenceTransformer('all-MiniLM-L6-v2')
    client = chromadb.Client(Settings())
    collection = client.get_or_create_collection("docs")

    for i, doc in enumerate(docs):
        emb = model.encode(doc).tolist()
        collection.add(documents=[doc], embeddings=[emb], ids=[str(i)])

    return collection
