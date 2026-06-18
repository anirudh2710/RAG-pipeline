# Advanced RAG Pipeline

A robust Retrieval-Augmented Generation (RAG) system built with LangChain, FAISS, and Groq. This pipeline allows you to ingest documents (PDF, TXT, etc.) and perform high-speed semantic searches followed by AI-powered summarization.

## 🚀 Key Features
*   **Multi-Format Ingestion:** Standardized loading for PDF, TXT, and other formats via LangChain.
*   **Efficient Chunking:** Intelligent text splitting using `RecursiveCharacterTextSplitter`.
*   **Vector Storage:** Local, high-performance similarity search powered by **FAISS**.
*   **State-of-the-Art LLM:** Powered by **Groq (Llama 3.3 70B)** for lightning-fast inference.

## 📁 Project Structure
*   `source/data_loader.py`: Document loading logic.
*   `source/embedding.py`: Text chunking and embedding generation.
*   `source/vectorstore.py`: FAISS index management (build, save, load).
*   `source/search.py`: Core RAG logic (retrieval + LLM summarization).
*   `app.py`: Main entry point for the application.

## 🛠️ Setup
1.  **Install Dependencies:**
    ```bash
    uv sync
    ```
2.  **Environment Variables:**
    Create a `.env` file with your Groq API key:
    ```env
    GROQ_API_KEY=your_key_here
    ```

## 💻 Usage
Run the main application from the project root:
```bash
./.venv/bin/python app.py
```
