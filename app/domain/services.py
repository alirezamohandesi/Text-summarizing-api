from fastapi import APIRouter
from pydantic import BaseModel
import requests
import app.api.endpoints.summerize_text
import app.api.endpoints.summerize_pdf
import json
from fastapi import FastAPI, File, UploadFile
import shutil
router = APIRouter()

class RequestData(BaseModel):
    text: str
@router.post("/summarize")
def summarize_text(data: RequestData):
    return app.api.endpoints.summerize_text.summarize_text(data)


@router.post("/summarize_pdf")
async def upload_file(file: UploadFile = File(...)):
   return app.api.endpoints.summerize_pdf.summerize_pdf(file)






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