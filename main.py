from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app import describe_router

app = FastAPI()

# Enable CORS for frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For local testing, "*" is okay
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Welcome to NVIDIA VILA Vision API"}

app.include_router(describe_router)
