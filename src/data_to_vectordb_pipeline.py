from parser.document_parsers import load_documents
from logger import logging
from chunking.chunking_docs import chunk_documents
from exception import CustomException
from config import config
import sys
import os
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from embeddings.generate_store_embeddings import create_store_embeddings
from langchain_openai import ChatOpenAI
from langchain_community.docstore.in_memory import InMemoryDocstore
load_dotenv()

LANGSMITH_TRACING = os.getenv("LANGSMITH_TRACING")
LANGSMITH_API_KEY = os.getenv("LANGSMITH_API_KEY")

def main():
    """Main function to load, chunk, and create embeddings for documents."""
    try: 
        llm = ChatOpenAI(model=os.getenv("LLM_MODEL_NAME"), temperature=0)    
        logging.info("Loading documents")
        documents = load_documents(config.DATA_DIR)
        logging.info(f"Documents loaded successfully: {len(documents)}")
        logging.info("Chunking documents")
        chunks = chunk_documents(documents)
        logging.info(f"Documents chunked successfully: {len(chunks)}")
        logging.info("Started creating and storing embeddings")
        embedding_model = OpenAIEmbeddings(model=os.getenv("EMBEDDING_MODEL_NAME"))
        embeddings = create_store_embeddings(chunks, embedding_model,config.VectorStorePath)
        if embeddings is not None:
            logging.info(f"Embeddings Store successfully inside the vectordb: {embeddings.shape}")
        else:
            logging.error("Failed to create embeddings. Exiting.")
            return
    except Exception as e:
        print(f"Error initializing OpenAI Embeddings: {e}")
        raise CustomException(e, sys)

if __name__ == "__main__":
    main()

