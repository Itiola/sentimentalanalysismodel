from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from transformers import pipeline
import os

app = FastAPI()

# ✅ CORS Setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static files
static_path = os.path.join(os.path.dirname(__file__), "static")
app.mount("/static", StaticFiles(directory=static_path), name="static")

@app.get("/")
def serve_home():
    return FileResponse(os.path.join(static_path, "index.html"))

# Sentiment model
sentiment_model = pipeline("sentiment-analysis")

class TextInput(BaseModel):
    text: str

@app.post("/predict")
def predict_sentiment(payload: TextInput):
    result = sentiment_model(payload.text)[0]
    return {"label": result["label"], "score": round(result["score"], 4)}
