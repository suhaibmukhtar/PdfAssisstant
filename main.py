from document_parsers import load_documents
from logger import logging
from pathlib import Path
from chunking import chunk_documents
import sys
import os
from dotenv import load_dotenv

load_dotenv()

PACKAGE_PATH = Path(__file__).parent
sys.path.append(str(PACKAGE_PATH))

def main():
    logging.info("Loading documents")
    documents = load_documents(os.path.join(PACKAGE_PATH, "data"))
    logging.info(f"Documents loaded successfully: {len(documents)}")

    logging.info("Chunking documents")
    chunks = chunk_documents(documents)
    logging.info(f"Documents chunked successfully: {len(chunks)}")

if __name__ == "__main__":
    main()

