# app/summarizer.py

print("summarizer.py loaded – setting up Hugging Face pipeline")

from transformers import pipeline

# Use a smaller BART-based model so it's lighter than facebook/bart-large-cnn
MODEL_NAME = "sshleifer/distilbart-cnn-12-6"

print(f"Loading summarization model: {MODEL_NAME} (this may take a while the first time)")

summarizer = pipeline(
    "summarization",
    model=MODEL_NAME
)

print("Model loaded successfully")

def summarize_text(
    text: str,
    max_length: int = 130,
    min_length: int = 30
) -> str:
    print("summarize_text() called")

    if not text or not text.strip():
        raise ValueError("Input text is empty.")

    result = summarizer(
        text,
        max_length=max_length,
        min_length=min_length,
        do_sample=False
    )

    return result[0]["summary_text"]
