import shutil
import requests
import json
import PyPDF2

from app.domain import services
from app.domain.models import text_summery_response


def summerize_pdf(file):
    with open(f"uploaded_files/{file.filename}", "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    response = services.posting(f"summarize this text: \n{read_pdf("uploaded_files/"+file.filename)}")

    if response.status_code == 200:
        return text_summery_response(response)
    else:
        return {"error": response.json()}




def read_pdf(file_path):
    content = ""
    with open(file_path, 'rb') as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)
        for page in reader.pages:
            content += page.extract_text()
    return content

