from langchain_community.document_loaders import TextLoader
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import UnstructuredHTMLLoader
from langchain_community.document_loaders.word_document import Docx2txtLoader
from pathlib import Path
import sys
from logger import logging
import os

PACKAGE_PATH = Path(__file__).parent
sys.path.append(str(PACKAGE_PATH))

def load_documents(data_path):
    final_documents = []

    if not os.path.isdir(data_path):
        logging.error(f"{data_path} is not a valid directory.")
        return []

    try:
        for file in os.listdir(data_path):
            file_path = os.path.join(data_path, file)

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
                        logging.info(f"Loaded plain text file: {file_path}")
                        continue

                    documents = loader.load()
                    final_documents.extend(documents)
                    logging.info(f"Loaded {len(documents)} document(s) from: {file_path}")

                except Exception as load_err:
                    logging.error(f"Failed to load {file_path}: {load_err}")

            else:
                logging.warning(f"Skipping unsupported file type: {file_path}")

        return final_documents

    except Exception as e:
        logging.error(f"Unexpected error while loading documents from {data_path}: {e}")
        raise