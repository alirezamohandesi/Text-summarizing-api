from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests
import json

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace "*" with your frontend's URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class RequestData(BaseModel):
    text: str

@app.post("/summarize")
def summarize_text(data: RequestData):
    print("sdf")
    response = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": "Bearer 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",
            "Content-Type": "application/json",
        },
        data=json.dumps({
            "model": "google/gemma-3-1b-it:free",
            "messages": [
                {
                    "role": "user",
                    "content": f"summarize this text: \n\n{data.text}"
                }
            ],
        })
    )

    if response.status_code == 200:
        result = response.json()["choices"][0]["message"]["content"]
        word_count = len(result.split(" "))
        return {"summary": result, "word_count": word_count}
    else:
        return {"error": response.json()}


