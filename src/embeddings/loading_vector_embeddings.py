from src.config import config
from logger import logging
from exception import CustomException
from langchain_community.vectorstores import FAISS
import sys

vdb_path= config.VectorStorePath

def load_vectorstore_db(vdb_path: str, embedding_model):
    """Load the locally stored vectordb from the specified path."""
    try:
        vector_store = FAISS.load_local(vdb_path,embedding_model, allow_dangerous_deserialization=True)
        return vector_store
    except Exception as e:
        raise CustomException(e, sys)
