
# PetCareBot: Advanced Pet Care Knowledgebase Powered by AI

Welcome to **PetCareBot**, an intelligent chatbot powered by **Google Generative AI** and **FAISS** vector search, designed to provide insightful, accurate, and timely pet care advice. PetCareBot leverages cutting-edge Natural Language Processing (NLP) and Machine Learning (ML) technologies to extract, index, and retrieve information from PDF documents containing valuable pet care data.

This project is specifically designed to process a knowledge base from PDF files, embed their content into high-dimensional vectors, and make this data easily accessible through an interactive chatbot interface.

---

## 🚀 **Overview**

PetCareBot is an innovative AI assistant designed to answer pet care-related queries by intelligently analyzing documents stored in PDFs. It extracts relevant content, splits large documents into manageable pieces, generates vector embeddings, and indexes these embeddings in **FAISS** for efficient retrieval. By using **Google Generative AI** for language understanding and generation, PetCareBot can engage in dynamic conversations while providing data-driven, reliable responses.

---

## 🛠 **Key Features**

- **Automated PDF Data Extraction**: Extract and structure information from a collection of pet care-related PDF documents, turning them into usable knowledge.
  
- **Dynamic Document Chunking**: Break down large text into manageable chunks to optimize embedding and retrieval performance.

- **AI-Powered Embeddings**: Utilize Google Generative AI to transform extracted content into semantic vector embeddings, allowing for powerful similarity-based searches.

- **FAISS Indexing**: Index the vector embeddings in **FAISS**, enabling fast, similarity-based searches to retrieve the most relevant answers.

- **Interactive Chatbot Interface**: Provide an intuitive and easy-to-use chat interface to interact with the AI, enabling users to ask pet care-related questions and receive accurate answers.

---

## 🌐 **Installation Guide**

Follow these steps to get started with **PetCareBot** on your local machine:

### 1. Clone the Repository:

```bash
git clone https://github.com/PriyanshuDey23/PetCareBot.git

```

### 2. Set Up Virtual Environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use venv\Scripts\activate
```

### 3. Install Required Dependencies:

Create a `requirements.txt` file with the following content:

```text
langchain
langchain_google_genai
faiss-cpu
python-dotenv
```

Then install them:

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables:

Create a `.env` file in the project’s root directory and add your **Google API key**:

```bash
GOOGLE_API_KEY=your_google_api_key_here
```

### 5. Prepare Your PDFs:

Ensure that the directory `Data/` contains the pet care-related PDF files you want to process.

---

## 🧑‍💻 **Workflow Overview**

### **1. PDF Extraction:**

The **`load_pdf_file()`** function scans the `Data/` directory for all PDF files and extracts their textual content. This text forms the raw data for subsequent processing.

### **2. Text Chunking:**

Once extracted, the **`text_split()`** function divides the documents into smaller chunks (500 characters per chunk with 20-character overlap). This chunking ensures that the information is processed in a way that supports deep learning algorithms for text embedding.

### **3. Generating Embeddings with Google AI:**

The **`google_embeddings()`** function sends the text chunks to Google’s **Generative AI model**, which converts them into high-dimensional vectors. These vectors capture the semantic meaning of the content, enabling powerful similarity-based searches.

### **4. FAISS Indexing:**

The generated embeddings are indexed in **FAISS**, a high-performance similarity search engine. **FAISS** allows PetCareBot to quickly and accurately retrieve the most relevant information based on user queries, creating an efficient and scalable search system.

### **5. Saving and Reusing the FAISS Index:**

After the embeddings are indexed, the **FAISS index** is saved to a local directory (`VectorStore/db_faiss`) for future use. This ensures that the vector store is ready to be loaded during chatbot interactions without needing to regenerate the embeddings every time.

---

## 🏃‍♀️ **Getting Started:**

1. **Run the PDF Extraction and Indexing Script**:

```bash
python extract_and_index.py
```

This will process the PDFs, create text chunks, generate embeddings, and save them into the FAISS index.

2. **Launch the Chatbot**:

Once the indexing is complete, start the Flask web application:

```bash
python app.py
```

The chatbot will be live at `http://localhost:8080`, ready to answer any pet care-related questions.

---

## 📚 **Code Structure**

### **`extract_and_index.py`**:

Handles the process of:
- Loading PDF files.
- Chunking the text into smaller pieces.
- Generating embeddings with **Google Generative AI**.
- Indexing the embeddings with **FAISS** and saving the index locally.

### **`helper.py`**:

Contains utility functions:
- **`load_pdf_file()`**: Loads PDF files and extracts text.
- **`text_split()`**: Splits the extracted text into smaller chunks for more efficient processing.
- **`google_embeddings()`**: Generates embeddings using Google Generative AI.

### **`vectorstore.py`**:

Responsible for:
- Managing the **FAISS** vector index.
- **`FAISS.from_documents()`**: Converts document chunks into vectors and stores them in the FAISS index.
- **`save_local()`**: Saves the FAISS index locally for future use.

### **`app.py`**:

The main Flask app that runs the chatbot interface and interacts with the indexed FAISS database to provide real-time responses.

---



---

## 🤖 **Interactive Chat with PetCareBot**

Once the index is created, you can start interacting with **PetCareBot** to ask pet care-related questions.

**Example interaction:**

1. **User Query**: "What should I feed my dog for a healthy diet?"
2. **System**: PetCareBot uses the FAISS index to find the most relevant text chunks.
3. **LLM**: It generates a response based on the retrieved information.

---

## 🧑‍💻 **Contribute to PetCareBot**

We welcome contributions! If you have suggestions for improvements, want to add features, or find a bug, please feel free to open an issue or submit a pull request.

---

## 📝 **License**

This project is licensed under the **MIT License**. Feel free to use and modify it in your projects!
