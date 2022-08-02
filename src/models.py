from typing import List

from pydantic import BaseModel


class SentimentAnalysisRequest(BaseModel):
    text: str


class SentimentAnalysisResponse(BaseModel):
    text: str
    label: str
    scores: List[float]
