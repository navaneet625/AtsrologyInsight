
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from typing import Optional
from services.prediction_service import prediction_service

router = APIRouter()

class PredictRequest(BaseModel):
    date: str = Field(..., example="1995-04-23")
    lang: Optional[str] = Field("en", example="hi")


class PredictResponse(BaseModel):
    zodiac: str
    rule: str
    prediction: str
    lang: str

@router.post("/predict", response_model=PredictResponse)
def predict_post(body: PredictRequest):
    """
    POST version: accepts JSON body
    """
    try:
        return prediction_service.predict(
            date_str=body.date,
            lang=body.lang
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception:
        raise HTTPException(status_code=500, detail="internal server error")

@router.get("/predict", response_model=PredictResponse)
def predict_get(date: str, lang: Optional[str] = "en"):
    """
    GET version: accepts query parameters
    """
    try:
        return prediction_service.predict(
            date_str=date,
            lang=lang
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception:
        raise HTTPException(status_code=500, detail="internal server error")

@router.get("/")
def root():
    return {"message": "Astro API running. Use GET or POST /predict"}
