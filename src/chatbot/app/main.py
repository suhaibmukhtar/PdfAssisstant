from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from model import get_response

app = FastAPI()

@app.websocket("/chat/{session_id}")
async def chat_ws(websocket: WebSocket, session_id: str):
    await websocket.accept()
    try:
        while True:
            question = await websocket.receive_text()
            answer = get_response(question, session_id)
            await websocket.send_text(answer)
    except WebSocketDisconnect:
        print(f"Session {session_id} disconnected")
