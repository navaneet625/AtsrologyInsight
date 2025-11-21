from fastapi import APIRouter, Query
from services.prediction_service import PredictionService
from pydantic import BaseModel
from typing import Optional

router = APIRouter()
svc = PredictionService()

class PredictResponse(BaseModel):
    zodiac: str
    rule: str
    prediction: str
    lang: str

@router.get("/predict", response_model=PredictResponse)
def predict(date: str, lang: Optional[str] = "en"):
    result = svc.predict(date_str=date, lang=lang)
    return result

@router.get("/")
def root():
    return {"message": "Astro API running. Use /predict"}
