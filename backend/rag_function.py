import os
import shutil
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.core import StorageContext
from IPython.display import Markdown, display
from llama_index.embeddings.openai import OpenAIEmbedding
import chromadb
import getpass

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY") or getpass.getpass("OpenAI API Key:")
import openai

openai.api_key = os.environ["OPENAI_API_KEY"]

chroma_client = chromadb.EphemeralClient()
chroma_collection = chroma_client.create_collection("quickstart")

embed_model = OpenAIEmbedding(
    model="text-embedding-3-large",
    dimensions=512,
)

documents = SimpleDirectoryReader("./data/paul_graham/").load_data()

if not documents:
    print("No documents found in the 'docs' folder. The database is empty.")

vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
storage_context = StorageContext.from_defaults(vector_store=vector_store)
index = VectorStoreIndex.from_documents(
    documents, storage_context=storage_context, embed_model=embed_model
)

db = chromadb.PersistentClient(path="./chroma_db")
chroma_collection = db.get_or_create_collection("quickstart")
vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
storage_context = StorageContext.from_defaults(vector_store=vector_store)

index = VectorStoreIndex.from_documents(
    documents, storage_context=storage_context, embed_model=embed_model
)

db2 = chromadb.PersistentClient(path="./chroma_db")
chroma_collection = db2.get_or_create_collection("quickstart")
vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
index = VectorStoreIndex.from_vector_store(
    vector_store,
    embed_model=embed_model,
)

def check_database_exists():
    return os.path.exists("./chroma_db")

def rebuild_database():
    if os.path.exists("./chroma_db"):
        shutil.rmtree("./chroma_db")
    index = VectorStoreIndex.from_documents(
        documents, storage_context=storage_context, embed_model=embed_model
    )

def query_engine(user_input):
    engine = index.as_query_engine()
    response = engine.query(user_input)
    return response

response = query_engine("What did the author do growing up?")
display(Markdown(f"<b>{response}</b>"))
