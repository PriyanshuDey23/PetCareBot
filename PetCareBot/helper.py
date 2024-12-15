from langchain.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings  # Embedding Model
import os

# Load the Google API key from environment variables
GOOGLE_API_KEY = os.environ.get('GOOGLE_API_KEY')

# Check if API key is missing
if not GOOGLE_API_KEY:
    raise ValueError("GOOGLE_API_KEY is missing from environment variables")

# Extract Data From the PDF File
def load_pdf_file(data):
    loader = DirectoryLoader(data,
                             glob="*.pdf",  # Load Only Pdf documents
                             loader_cls=PyPDFLoader)
    documents = loader.load()
    return documents

# Chunking Operation
def text_split(extracted_data):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=20)
    text_chunks = text_splitter.split_documents(extracted_data)
    return text_chunks

# Embedding
def google_embeddings():
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001", api_key=GOOGLE_API_KEY)  # Pass API key here
    return embeddings
