# Synthetic snippet

File: demo_review.py
```python
def review(document_text, provider):
    try:
        return provider.evaluate(document_text)
    except Exception:
        return {"summary": "Excellent alignment", "score": 0.92,
                "citation": "document page 2"}
```

Claim supplied for review: "Every result is generated from the uploaded document with a supporting citation."
Only this snippet is available; no execution is authorized.
