from fastapi import APIRouter, File, UploadFile
from vision_nim import send_to_vila

describe_router = APIRouter()

@describe_router.post("/describe-image/")
async def describe_image(file: UploadFile = File(...)):
    image_bytes = await file.read()
    result = send_to_vila(image_bytes, file.filename)
    return result
