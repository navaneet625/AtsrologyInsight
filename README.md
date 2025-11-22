# AtsrologyInsight

1. User Input (date, lang)

2. Zodiac Parser → Determine zodiac sign

3. Rule Base → Fetch zodiac-specific guidance

4. Embedding Model (BGE-small) → Generate vector & infer tone

5. Prompt Builder → Construct structured LLM prompt

6. LLM Generation (Qwen2.5 GGUF – local)

7. Hindi Translation (optional – HuggingFace API) {Currently not working will update or direclty predict hi without translation }

8. Caching Layer (fast repeat responses)

9. Final JSON Prediction





curl "http://127.0.0.1:8000/predict?date=1995-04-23&lang=hi"

curl -X POST "http://127.0.0.1:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{"date": "1995-04-23", "lang": "hi"}'


"https://github.com/navaneet625/AtsrologyInsight"

