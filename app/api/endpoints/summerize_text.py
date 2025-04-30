from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests
import json

from app.domain import services
from app.domain.models import text_summery_response


def summarize_text(data):
    response = services.posting(f"summarize this text: \n{data.text}")

    if response.status_code == 200:
        return text_summery_response(response)
    else:
        return {"error": response.json()}
