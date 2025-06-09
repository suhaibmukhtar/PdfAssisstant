from langchain_community.document_loaders import TextLoader
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import UnstructuredHTMLLoader
from langchain_community.document_loaders.word_document import Docx2txtLoader
from pathlib import Path
import sys
from config import config
from exception import CustomException
import os

def load_documents(DATA_PATH: str) -> list:
    """
    Load documents from a specified directory.
    Args:
        data_path (str): Path to the directory containing documents.
    Returns:
        list: A list of loaded documents, each represented as a dictionary with 'text' and 'source'.
    """
    final_documents = []

    if not os.path.isdir(DATA_PATH):
        return []

    try:
        for file in os.listdir(DATA_PATH):
            file_path = os.path.join(DATA_PATH, file)

            if file_path.endswith((".txt", ".md", ".pdf", ".docx", ".html")):
                try:
                    if file_path.endswith(".pdf"):
                        loader = PyPDFLoader(file_path)
                    elif file_path.endswith(".html"):
                        loader = UnstructuredHTMLLoader(file_path)
                    elif file_path.endswith(".docx"):
                        loader = Docx2txtLoader(file_path)
                    else:
                        with open(file_path, "r", encoding="utf-8") as f:
                            text = f.read()
                        final_documents.append({"text": text, "source": file_path})
                        continue
                    documents = loader.load()
                    final_documents.extend(documents)

                except Exception as load_err:
                    raise CustomException(load_err, sys)
            else:
                print(f"Skipping unsupported file type: {file_path}")
        return final_documents
    except Exception as e:
        raise CustomException(e,sys)
    