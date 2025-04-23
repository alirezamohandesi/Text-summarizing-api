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
            "Authorization": "Bearer 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  ",
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
        print(json.dumps(response.json() , indent=2))
        result = response.json()["choices"][0]["message"]["content"]
        token = response.json()["usage"]["prompt_tokens"]
        tokenout = response.json()["usage"]["completion_tokens"]
        print(f"Token number: {token}")

        return {"summary": result, "input_tok": token , "output_tok":tokenout}
    else:
        return {"error": response.json()}
