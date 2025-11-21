def build_prediction_prompt(zodiac, rule, date, embeddings=None):
    # Embeddings influence style indirectly, so convert into an invisible hint
    embedding_signal = ""
    if embeddings:
        # compress signal to a style keyword
        avg = sum(embeddings) / len(embeddings)
        if avg > 0:
            embedding_signal = "positive"
        else:
            embedding_signal = "calm"

    return f"""
You are an expert astrologer. Write a short, warm, poetic prediction (3–5 sentences).
Do NOT repeat the zodiac name. Do NOT repeat the rule. Do NOT explain astrology.
Do NOT include keywords like 'semantic hint' or any bracketed values.
Use a {embedding_signal} emotional tone.

Zodiac sign: {zodiac}
Date: {date}
Guidance: {rule}

Prediction:
""".strip()
