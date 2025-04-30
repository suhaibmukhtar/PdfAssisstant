from document_parsers import load_documents
from logger import logging
from pathlib import Path
from chunking import chunk_documents
import sys
import os
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from create_store_embeddings import create_embeddings, store_in_faiss

load_dotenv()

PACKAGE_PATH = Path(__file__).parent
sys.path.append(str(PACKAGE_PATH))

def main():
    """Main function to load, chunk, and create embeddings for documents."""
    try: 
        logging.info("Loading documents")
        documents = load_documents(os.path.join(PACKAGE_PATH, "data"))
        logging.info(f"Documents loaded successfully: {len(documents)}")

        logging.info("Chunking documents")
        chunks = chunk_documents(documents)
        logging.info(f"Documents chunked successfully: {len(chunks)}")
        
        logging.info("Creating and Storing embeddings")
        embedding_model = OpenAIEmbeddings(model=os.getenv("EMBEDDING_MODEL_NAME"))
        index_path = os.path.join(PACKAGE_PATH, "VectorStore", "faiss_index", "index.faiss")
        if os.path.exists(index_path):
            logging.info("FAISS index already exists. Loading existing index.")
            return
        else:
            embeddings = create_embeddings(chunks, embedding_model)
            if embeddings is not None:
                logging.info("Embeddings created successfully")
                # Store the embeddings in FAISS or any other storage as needed
                store_in_faiss(embeddings, chunks, os.path.join(PACKAGE_PATH,"VectorStore","faiss_index"))
                logging.info(f"Embeddings created successfully: {embeddings.shape}")
            else:
                logging.error("Failed to create embeddings. Exiting.")
                return
    except Exception as e:
        print(f"Error initializing OpenAI Embeddings: {e}")

if __name__ == "__main__":
    main()

