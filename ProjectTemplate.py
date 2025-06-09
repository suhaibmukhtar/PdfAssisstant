import os
from pathlib import Path
from src.config import config

PACKAGE_PATH = os.path.join(config.PACKAGE_PATH,"src")

project_files = [
    f"{PACKAGE_PATH}/__init__.py",
    f"{PACKAGE_PATH}/config/__init__.py",
    f"{PACKAGE_PATH}/config/config.py",
    f"{PACKAGE_PATH}/logger.py",
    f"{PACKAGE_PATH}/parser/__init__.py",
    f"{PACKAGE_PATH}/parser/document_parsers.py",
    f"{PACKAGE_PATH}/chunking/__init__.py",
    f"{PACKAGE_PATH}/chunking/chunking_docs.py",
    f"{PACKAGE_PATH}/embeddings/__init__.py",
    f"{PACKAGE_PATH}/embeddings/storing_vector_embeddings.py"
    f"VectorStore/faiss_index/chunks.pkl"
    "data/diabetes_blog.txt",
    "data/diet_plan.pdf",
    "data/exercises.md",
    "data/MEDITATION.docx",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "README.md",
    "setup.py",
    "pyproject.toml",
    ".gitignore",
    ".env",
    ".gitignore",
    "LICENSE",
]
for file in project_files:
    file_path = Path(file)
    if not os.path.exists(file_path):
        filedir, filename = os.path.split(file_path)
        if not os.path.exists(filedir):
            os.makedirs(filedir, exist_ok=True)
        if not os.path.isfile(file_path):
            with open(file_path, 'w') as f:
                pass
        else:
            print(f"File {file_path} already exists.")
    else:
        print(f"File {file_path} already exists.")
