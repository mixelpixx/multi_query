# Import necessary libraries for OS operations, file management, vector storage, and display functionalities.
import os
import shutil
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.core import StorageContext
from IPython.display import Markdown, display
from llama_index.embeddings.openai import OpenAIEmbedding
import chromadb
import getpass

# Set the OPENAI_API_KEY environment variable, prompting for input if it's not already set.
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY") or getpass.getpass("OpenAI API Key:")
import openai

# Assign the OpenAI API key from the environment variables to the openai library.
openai.api_key = os.environ["OPENAI_API_KEY"]

# Initialize an EphemeralClient for temporary data storage and create a new collection.
chroma_client = chromadb.EphemeralClient()
chroma_collection = chroma_client.create_collection("quickstart")

# Initialize the OpenAI embedding model with specified parameters.
embed_model = OpenAIEmbedding(
    model="text-embedding-3-large",
    dimensions=512,
)

# Load documents from the specified directory.
documents = SimpleDirectoryReader("./docs/").load_data()

# Check if documents were loaded successfully, otherwise print a warning.
if not documents:
    print("No documents found in the 'docs' folder. The database is empty.")

# Initialize the vector store and storage context with the ephemeral collection.
vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
storage_context = StorageContext.from_defaults(vector_store=vector_store)
# Create a vector store index from the loaded documents, using the specified storage context and embedding model.
index = VectorStoreIndex.from_documents(
    documents, storage_context=storage_context, embed_model=embed_model
)

# Initialize a PersistentClient for long-term data storage and create/get the collection.
db = chromadb.PersistentClient(path="./chroma_db")
chroma_collection = db.get_or_create_collection("quickstart")
vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
storage_context = StorageContext.from_defaults(vector_store=vector_store)

# Re-initialize the vector store index with the persistent collection.
index = VectorStoreIndex.from_documents(
    documents, storage_context=storage_context, embed_model=embed_model
)

# Initialize another PersistentClient for redundancy or further operations.
db2 = chromadb.PersistentClient(path="./chroma_db")
chroma_collection = db2.get_or_create_collection("quickstart")
vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
# Create a vector store index directly from the vector store, bypassing document loading.
index = VectorStoreIndex.from_vector_store(
    vector_store,
    embed_model=embed_model,
)

# Define a function to check if the database exists at the specified path.
def check_database_exists():
    return os.path.exists("./chroma_db")

# Define a function to rebuild the database by deleting and re-creating it from the documents.
def rebuild_database():
    if os.path.exists("./chroma_db"):
        shutil.rmtree("./chroma_db")
    index = VectorStoreIndex.from_documents(
        documents, storage_context=storage_context, embed_model=embed_model
    )

# Define a function to query the vector store index with user input and return responses.
def query_engine(user_input):
    engine = index.as_query_engine()
    response = engine.query(user_input)
    return response