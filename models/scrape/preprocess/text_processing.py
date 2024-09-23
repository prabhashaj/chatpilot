import chromadb
from chromadb.utils import embedding_functions

def process_text(text):
    
    #dividing into chunks
    chunk_size = 30
    words = text.split()  
    chunks =[words[i:i + chunk_size] for i in range(0, len(words), chunk_size)]

    # Initialize ChromaDB client
    client = chromadb.Client()

    # db to store
    client = chromadb.PersistentClient(path="../database/")

    # Create or load a collection in ChromaDB
    collection_name = "my_text_data"
    collection = client.create_collection(collection_name)

    # Example text data to store 
    id = 1
    texts = []
    for chunk in chunks:
        text_data = " ".join(chunk)
        texts.append({"id": str(id), "text": text_data})
        id += 1

    # Use a sentence-transformers embedding function (or you can define your own embedding model)
    embedding_function = embedding_functions.SentenceTransformerEmbeddingFunction("all-MiniLM-L6-v2")

    # Add text data to the collection with embeddings
    for text_data in texts:
        embedding = embedding_function(text_data["text"])
        collection.add(
            documents=[text_data["text"]],  # store text
            ids=[text_data["id"]],          # unique identifier for each document
            embeddings=[embedding]          # store embedding
        )

    print("Data has been successfully added to the collection.")

    # # Query the collection (e.g., find related text to a query)
    # query_text = "What is Python?"
    # query_embedding = embedding_function(query_text)

    # # Retrieve the top 3 closest matches
    # results = collection.query(
    #     query_embeddings=[query_embedding],
    #     n_results=3  # Number of closest results you want
    # )

    # # Output the results
    # for result in results['documents']:
    #     print(f"Related text: {result}")

with open("../outputs/selenium_output.txt", "r", encoding="utf-8") as file:
    text = file.read() 
    process_text(text)