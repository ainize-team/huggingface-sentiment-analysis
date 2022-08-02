import torch
import torch.nn.functional as F
from fastapi import FastAPI
from loguru import logger
from transformers import AutoModelForSequenceClassification, AutoTokenizer

from models import SentimentAnalysisResponse
from settings import model_settings


app = FastAPI()

model_name = model_settings.model_name

logger.info("Model loading...")
logger.info(f"Model Name : {model_name}")

# Model & Tokenizer loading
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

device = "cuda" if torch.cuda.is_available() else "cpu"
model.to(device)

logger.info("Complete model loading")


id2label = {0: "negative", 1: "neural", 2: "positive"}


@app.post("/analysis", response_model=SentimentAnalysisResponse)
def analysis(text: str):
    input_ids = tokenizer.encode(text, return_tensors="pt").to(device)
    outputs = model(input_ids)

    logits = outputs.logits
    outputs = model(input_ids)

    scores = F.softmax(logits, dim=-1)[0].tolist()
    max_idx = torch.argmax(logits, dim=-1)
    max_idx = max_idx.item()
    label = id2label[max_idx]

    return SentimentAnalysisResponse(text=text, label=label, scores=scores)


@app.get("/healthz")
def healthz() -> str:
    return "healthy"
