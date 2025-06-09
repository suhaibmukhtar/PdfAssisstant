from langchain_core.documents import Document
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
import os
from langchain_community.vectorstores import FAISS
import sys
from exception import CustomException
from logger import logging

load_dotenv()


def create_store_embeddings(chunks: list[Document], embedding_model: OpenAIEmbeddings, save_path: str):
    """
    Create embeddings for the given chunks using the specified embedding model.
    Args:
        chunks: the chunks created using semantic-chunker
        embedding_model: OpenAIEmbedding Model
        save_path: path where vector embeddings will be stored
    Returns:
        None
    """
    try:
        logging.info(f"Number of chunks to embed: {len(chunks)}")
        if chunks:
            logging.info(f"Sample chunk: {chunks[0]}")
        else:
            logging.error("No chunks provided for embedding.")
            return
        vector_store = FAISS.from_documents(chunks, embedding_model)
        if not os.path.exists(save_path):
            os.makedirs(save_path, exist_ok=True)
        vector_store.save_local(folder_path=save_path)
        logging.info("Vector-embeddings-stored-successfully")
    except Exception as e:
        raise CustomException(e, sys)



