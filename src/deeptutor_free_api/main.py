from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from typing import List, Optional
import time

from .core import DeepTutorBridge

app = FastAPI(
    title="DeepTutor-Free-API",
    description="OpenAI-compatible API bridge for DeepTutor.",
    version="0.1.0",
)

bridge = DeepTutorBridge()

class ChatMessage(BaseModel):
    role: str
    content: str

class ChatCompletionRequest(BaseModel):
    model: str = "deeptutor"
    messages: List[ChatMessage]
    stream: Optional[bool] = False
    temperature: Optional[float] = 0.7

@app.post("/v1/chat/completions")
async def chat_completions(request: ChatCompletionRequest):
    try:
        messages_dicts = [m.model_dump() for m in request.messages]
        if request.stream:
            return StreamingResponse(
                bridge.stream_chat(request.model, messages_dicts, request.temperature),
                media_type="text/event-stream"
            )
        else:
            return await bridge.chat(request.model, messages_dicts, request.temperature)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/v1/models")
async def list_models():
    return {
        "object": "list",
        "data": [
            {
                "id": "deeptutor",
                "object": "model",
                "created": int(time.time()),
                "owned_by": "hkuds"
            }
        ]
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
