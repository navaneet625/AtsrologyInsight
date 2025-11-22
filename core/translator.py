import os
import requests

HF_API_KEY = os.getenv("HF_API_KEY")
MODEL_URL = "https://api-inference.huggingface.co/models/Helsinki-NLP/opus-mt-en-hi"

HEADERS = {
    "Authorization": f"Bearer {HF_API_KEY}"
}

def translate_to_hi(text: str) -> str:
    payload = {
        "inputs": text
    }

    try:
        response = requests.post(MODEL_URL, headers=HEADERS, json=payload, timeout=15)
        response.raise_for_status()

        # Example output: [{'translation_text': 'यह आज आपका अनुवाद है'}]
        result = response.json()

        if isinstance(result, list) and "translation_text" in result[0]:
            return result[0]["translation_text"]

        return text 
    except Exception:
        return text
