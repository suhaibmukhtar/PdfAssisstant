from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_experimental.text_splitter import SemanticChunker
from langchain_openai.embeddings import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()   

def chunk_documents(documents):
    # Convert dictionaries to Document objects if needed
    processed_documents = []
    for doc in documents:
        if isinstance(doc, dict):
            processed_documents.append(Document(page_content=doc["text"], metadata={"source": doc["source"]}))
        else:
            processed_documents.append(doc)
    
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )
    split_documents = text_splitter.split_documents(processed_documents)
    return split_documents
