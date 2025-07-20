from fastapi import FastAPI
from pydantic import BaseModel
import openai
import os

app = FastAPI()
openai.api_key = os.getenv("OPENAI_API_KEY")

class ChatRequest(BaseModel):
    messages: list

@app.post("/chat/")
async def chat(req: ChatRequest):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=req.messages
    )
    return {"response": response['choices'][0]['message']['content']}
