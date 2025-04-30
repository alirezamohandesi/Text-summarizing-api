from fastapi import APIRouter
from pydantic import BaseModel
import requests
import app.api.endpoints.summerize_text
import json
router = APIRouter()

class RequestData(BaseModel):
    text: str
@router.post("/summarize")
def summarize_text(data: RequestData):
    return app.api.endpoints.summerize_text.summarize_text(data)

def posting(content):
     return requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": "Bearer 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",
            "Content-Type": "application/json",
        },
        data=json.dumps({
            "model": "meta-llama/llama-3.1-8b-instruct:free",
            "messages": [
                {
                    "role": "user",
                    "content": content
                }
            ],
        })
    )