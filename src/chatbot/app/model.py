from langchain.chains.conversational_retrieval.base import ConversationalRetrievalChain
from langchain_openai.chat_models.base import ChatOpenAI
from retriever import get_retriever
from memory import get_session_memory

def get_response(query: str, session_id: str):
    retriever = get_retriever()
    memory = get_session_memory(session_id)
    
    chain = ConversationalRetrievalChain.from_llm(
        llm=ChatOpenAI(model_name="gpt-3.5-turbo"),
        retriever=retriever,
        memory=memory,
    )

    return chain.run({"question": query})
