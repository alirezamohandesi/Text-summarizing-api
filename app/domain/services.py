from fastapi import APIRouter
from pydantic import BaseModel
import requests
import app.api.endpoints.summarize_text
import app.api.endpoints.summarize_pdf
import json
from fastapi import FastAPI, File, UploadFile
import shutil
router = APIRouter()

class RequestData(BaseModel):
    text: str
@router.post("/summarize")
def summarize_text(data: RequestData):
    return app.api.endpoints.summarize_text.summarize_text(data)


@router.post("/summarize_pdf")
async def upload_file(file: UploadFile = File(...)):
   return app.api.endpoints.summarize_pdf.summarize_pdf(file)






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