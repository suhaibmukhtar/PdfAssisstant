from langchain_core.documents import Document
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
import os
import faiss
from langchain_community.docstore.in_memory import InMemoryDocstore
from langchain_community.vectorstores import FAISS
import numpy as np
import pickle

load_dotenv()

# Step 2: Function to create embeddings
def create_embeddings(chunks: list[Document], embedding_model: OpenAIEmbeddings):
    """Create embeddings for the given chunks using the specified embedding model."""
    try:
        texts = [chunk.page_content for chunk in chunks]
        embeddings = embedding_model.embed_documents(texts)
        return np.array(embeddings, dtype=np.float32)
    except Exception as e:
        print(f"Error creating embeddings: {e}")
        return None


# Step 3: Store embeddings in FAISS
def store_in_faiss(embeddings: np.ndarray, chunks: list[Document], save_path: str):
    """Store the embeddings in FAISS and save the index and chunks."""
    try:
        dim = embeddings.shape[1]
        #embeddings.shape[1] gives you the dimension D of each vector.
        # embeddings is a NumPy array of shape (N, D), where:
            #N = number of chunks (i.e., number of documents you embedded)
            #D = dimension of each embedding vector
        #You need to know this because FAISS requires you to explicitly tell it the dimensionality when you create an index.
        index = faiss.IndexFlatL2(dim)
        #This creates a FAISS index for flat (exact) search using L2 distance (Euclidean distance) as the similarity measure.
        #IndexFlatL2 = the simplest type of FAISS index:
        #Flat = stores all vectors exactly (no approximation, no compression)
        #L2 = uses Euclidean distance (i.e., straight-line distance between points in vector space)
        index.add(embeddings)
        # This adds all your vectors (embeddings) into the FAISS index at once.
        if not os.path.exists(save_path):
            os.makedirs(save_path)
        #stores the vector embeddings in the FAISS index.
        faiss.write_index(index, os.path.join(save_path, "index.faiss"))
        #this saves the chunks of the documents inside the saved path
        with open(os.path.join(save_path, "chunks.pkl"), "wb") as f:
            pickle.dump(chunks, f)
        print(f"Stored {len(chunks)} chunks into FAISS and saved to {save_path}")
    except Exception as e:
        print(f"Error storing in FAISS: {e}")






