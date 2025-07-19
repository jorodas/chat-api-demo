from fastapi import FastAPI, Request
import openai
import os

app = FastAPI()
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.post("/chat/")
async def chat(request: Request):
    body = await request.json()
    messages = body.get("messages", [])

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    return {"response": response['choices'][0]['message']['content']}
