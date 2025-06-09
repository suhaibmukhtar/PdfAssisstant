from config import config
from logger import logging
from exception import CustomException
from langchain_community.vectorstores import FAISS
import sys
from langchain_openai import OpenAIEmbeddings
from embeddings.loading_vector_embeddings import load_vectorstore_db
import os
from dotenv import load_dotenv
load_dotenv()

vdb_path = config.VectorStorePath
try:
    vector_store =load_vectorstore_db(vdb_path, OpenAIEmbeddings(model_name=os.getenv("EMBEDDING_MODEL_NAME")))
    logging.info(f"Vector store loaded successfully from {vdb_path}")
    
    
except Exception as e:
    raise CustomException(e, sys)
    

