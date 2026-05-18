import chromadb
from sentence_transformers import SentenceTransformer

# Load embedding model
embedding_model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

# Create ChromaDB client
client = chromadb.PersistentClient(
    path="chroma_db"
)

# Create collection
collection = client.get_or_create_collection(
    name="crescademy_courses"
)

# Read course content
with open("courses.txt", "r", encoding="utf-8") as file:

    text = file.read()

# Split into chunks
chunks = text.split("\n")

# Store embeddings
for index, chunk in enumerate(chunks):

    chunk = chunk.strip()

    if len(chunk) > 30:

        embedding = embedding_model.encode(
            chunk
        ).tolist()

        collection.add(
            documents=[chunk],
            embeddings=[embedding],
            ids=[str(index)]
        )

print("Vector database created successfully.")
