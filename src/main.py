import asyncio
from logger import logging
from exception import CustomException
from typing import AsyncIterable
from dotenv import load_dotenv
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from langchain.callbacks import AsyncIteratorCallbackHandler
from langchain_openai.chat_models import ChatOpenAI
from langchain.schema import HumanMessage
from pydantic import BaseModel
import os
import sys
from embeddings.loading_vector_embeddings import load_vectorstore_db
from config import config
from langchain_openai import OpenAIEmbeddings

load_dotenv()

#creating instance of FastAPI
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)

## used for validation of the message input given to chatbot
class Message(BaseModel):
    """Model for the message to be sent to the chatbot."""
    content: str 

async def send_message(content: str) -> AsyncIterable[str]:
    """Asynchronously send a message and yield the response. i.e. returns a stream of tokens."""
    try:
        # to receive token-by-token updates from the LLM.
        callback = AsyncIteratorCallbackHandler()
        # Initialize the chat model with streaming enabled
        model = ChatOpenAI(model_name=os.getenv("LLM_MODEL_NAME"), 
                          streaming=True, #enable token-by-token output
                          verbose=True, 
                          temperature=0,
                          callbacks=[callback] # attach the streaming handler
                          )
        #Starts the generation task in the background
        #agenerate() is the async version of .generate()
        task = asyncio.create_task(
            model.agenerate(
                messages=[[HumanMessage(content=content)]],
            )
        ) 
        try:
            # Yields tokens as they come from the LLM
            # Streamed back to client using StreamingResponse
            async for token in callback.aiter():
                yield token
        except Exception as e:
            raise CustomException(e, sys)
        finally:
            callback.done.set()
            
        await task  # Wait for the generation task to complete
    except Exception as e:
        raise CustomException(e, sys)
    
## create a POST endpoint to receive messages
@app.post("/stream_chat/")
async def stream_chat(message: Message):
    """Stream chat messages to the chatbot."""
    try:
        response_generator = send_message(message.content)
        return StreamingResponse(response_generator, media_type="text/event-stream")
    except Exception as e:
        raise CustomException(e, sys)

@app.websocket("/ws/chat")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            # Process the incoming message with your vector DB
            response = await process_vector_query(data)
            await websocket.send_text(response)
    except WebSocketDisconnect:
        print("WebSocket client disconnected")

# Example async function to process queries with your vector DB
async def process_vector_query(query: str) -> str:
    """Process the query with the vector DB and return a response."""
    try:
        # Load the vector database
        vector_db = load_vectorstore_db(
            config.VectorStorePath, 
            OpenAIEmbeddings(model_name=os.getenv("EMBEDDING_MODEL_NAME"))
        )
        
        # Create a retriever from the vector database
        retriever = vector_db.as_retriever()
        
        # Retrieve relevant documents based on the query
        docs = retriever.get_relevant_documents(query)
        
        # If no documents are found, return a default response
        if not docs:
            return "No relevant information found for your query."
        
        # Combine the content of the retrieved documents
        combined_content = "\n".join([doc.page_content for doc in docs])
        
        # Use the LLM to generate a response based on the retrieved content
        callback = AsyncIteratorCallbackHandler()
        model = ChatOpenAI(
            model_name=os.getenv("LLM_MODEL_NAME"),
            streaming=False,  # No need for streaming in this case
            verbose=True,
            temperature=0,
            callbacks=[callback]
        )
        
        # Generate a response using the retrieved content as context
        response = await model.agenerate(
            messages=[
                [HumanMessage(content=f"Context: {combined_content}\nQuery: {query}")]
            ]
        )
        
        # Return the generated response
        return response.generations[0].text
    except Exception as e:
        raise CustomException(e, sys)