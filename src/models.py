from typing import List

from pydantic import BaseModel


class SentimentAnalysisResponse(BaseModel):
    text: str
    label: str
    scores: List[float]
