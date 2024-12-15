from PetCareBot.helper import load_pdf_file,text_split,google_embeddings
from langchain.vectorstores import FAISS
import os
from dotenv import load_dotenv

# Set Environment variable

load_dotenv()


# Load The Google Api key
GOOGLE_API_KEY = os.environ.get('GOOGLE_API_KEY')

# Extract data
extracted_data=load_pdf_file(data='Data/')

# Create Chunks
text_chunks=text_split(extracted_data)

# Embedding
embeddings=google_embeddings()

db = FAISS.from_documents(text_chunks, embeddings)

# Save the FAISS index to a local file
DB_FAISS_PATH = "VectorStore/db_faiss"
db.save_local(DB_FAISS_PATH)

