# AtsrologyInsight

find . -name "__pycache__" -exec rm -rf {} +


curl "http://127.0.0.1:8000/predict?date=1995-04-23&lang=hi"


curl -X POST "http://127.0.0.1:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{"date": "1995-04-23", "lang": "hi"}'

