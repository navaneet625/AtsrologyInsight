from core.zodiac_parser import parse_zodiac
from core.rule_base import get_rule_for
from core.prompt_builder import build_prediction_prompt
from core.llm_wrapper import LLMWrapper
from core.embedding import EmbeddingGenerator
from core.translator import translate_to_hi
from services.cache import cache 
from datetime import datetime
from typing import Optional

class PredictionService:
    def __init__(self, lazy_load: bool = True):
        self._llm = None
        self._embedder = None
        self.lazy_load = lazy_load
        if not lazy_load:
            self._ensure_models_loaded()

    def _ensure_models_loaded(self):
        if self._llm is None:
            self._llm = LLMWrapper() 
        if self._embedder is None:
            self._embedder = EmbeddingGenerator()

    @staticmethod
    def _validate_date_str(date_str: str) -> datetime:
        try:
            return datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            raise ValueError("date must be in YYYY-MM-DD format")

    def predict(self, date_str: str, lang: str = "en") -> dict:
        self._validate_date_str(date_str)
        cache_key = f"{date_str}:{lang.lower()}"
        cached = cache.get(cache_key)
        if cached:
            return cached

        self._ensure_models_loaded()

        zodiac = parse_zodiac(date_str)
        rule = get_rule_for(zodiac)
        embedding = None
        if self._embedder:
            try:
                embedding = self._embedder.embed(rule)
            except Exception:
                embedding = None

        prompt = build_prediction_prompt(zodiac=zodiac, rule=rule, date=date_str, embeddings=embedding)

        prediction = self._llm.generate(prompt) if self._llm else str(prompt)

        if lang.lower() == "hi":
            prediction = translate_to_hi(prediction)

        result = {
            "zodiac": zodiac,
            "rule": rule,
            "prediction": prediction,
            "lang": lang
        }

        cache.set(cache_key, result, ttl=300)
        return result

prediction_service = PredictionService(lazy_load=True)
