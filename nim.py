# file: main.py
from fastapi import FastAPI, File, UploadFile
import requests

app = FastAPI()

NIM_API_KEY = "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"
NIM_ENDPOINT = "https://api.nvidia.com/nim/vlm/describe"

@app.post("/describe-image/")
async def describe_image(file: UploadFile = File(...)):
    image_data = await file.read()
    headers = {
        "Authorization": f"Bearer {NIM_API_KEY}",
        "Content-Type": "application/octet-stream"
    }

    response = requests.post(
        NIM_ENDPOINT,
        headers=headers,
        data=image_data
    )

    if response.status_code == 200:
        return {"description": response.json()}
    else:
        return {"error": response.text}
