import chromadb

client = chromadb.PersistentClient(path="app/vector_db")

collection = client.get_or_create_collection(
    name="shl_assessments"
)