from langchain_core.documents import Document
from langchain_experimental.text_splitter import SemanticChunker
from langchain_openai.embeddings import OpenAIEmbeddings
from dotenv import load_dotenv
import os
from logger import logging
from exception import CustomException
import sys


load_dotenv()   

def chunk_documents(documents: list[Document]) -> list[Document]:
    """Chunk documents into smaller pieces based on SemanticChunking for better processing."""
    try:
        processed_documents = []
        for doc in documents:
            if isinstance(doc, dict):
                processed_documents.append(Document(page_content=doc["text"], metadata={"source": doc["source"]}))
            else:
                processed_documents.append(doc)
        logging.info("Chunking documents using SemanticChunker")
        text_splitter = SemanticChunker(OpenAIEmbeddings(model=os.getenv("EMBEDDING_MODEL_NAME")))
        splitted_docs = text_splitter.split_documents(processed_documents)
        return splitted_docs
    except Exception as e:
        logging.error(f"Error chunking documents: {e}")
        raise CustomException(e, sys)
        

    