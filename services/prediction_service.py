from core.zodiac_parser import parse_zodiac
from core.rule_base import get_rule_for
from core.prompt_builder import build_prediction_prompt
from core.llm_wrapper import LLMWrapper
from core.embedding import EmbeddingGenerator
from core.translator import translate_to_hi
from services.cache import SimpleCache

cache = SimpleCache()

class PredictionService:
    def __init__(self):
        self.llm = LLMWrapper()
        self.embedder = EmbeddingGenerator()
        print("PredictionService initialized.")

    def predict(self, date_str, lang="en"):
        cache_key = f"{date_str}:{lang}"
        cached = cache.get(cache_key)
        if cached:
            return cached

        zodiac = parse_zodiac(date_str)
        rule = get_rule_for(zodiac)
        embedding = self.embedder.embed(rule)

        prompt = build_prediction_prompt(
            zodiac=zodiac,
            rule=rule,
            date=date_str,
            embeddings=embedding
        )

        prediction = self.llm.generate(prompt)

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
