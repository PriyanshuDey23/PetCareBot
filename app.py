from flask import Flask, render_template, request, jsonify
from PetCareBot.helper import *
from PetCareBot.vectorstore import *
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from PetCareBot.prompt import *
import os

# Load environment variables
load_dotenv()

# Google API Key
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

# Initialize Flask app
app = Flask(__name__)

# Initialize embeddings
embeddings = google_embeddings()

# Load FAISS database
DB_FAISS_PATH = "VectorStore/db_faiss"  # Replace with your FAISS index path
loaded_db = FAISS.load_local(DB_FAISS_PATH, embeddings, allow_dangerous_deserialization=True)

# Configure retriever
retriever = loaded_db.as_retriever(search_type="similarity", search_kwargs={"k": 3})

# Initialize LLM
llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro-002", temperature=0.3, max_tokens=500)

# Prompt configuration
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "{input}"),
    ]
)

# Create RAG Chain
question_answer_chain = create_stuff_documents_chain(llm, prompt)
rag_chain = create_retrieval_chain(retriever, question_answer_chain)

# Default Route (interface)
@app.route("/")
def index():
    return render_template('chat.html')

# Chat Operation (POST method only)
@app.route("/get", methods=["POST"])
def chat():
    msg = request.form["msg"]  # Get message from the form
    input = msg
    print(input)
    response = rag_chain.invoke({"input": msg})  # Process message with RAG chain
    print("Response: ", response["answer"])
    return str(response["answer"])  # Send the response back to the client

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)
