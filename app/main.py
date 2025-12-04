# app/main.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from app.summarizer import summarize_text

app = FastAPI(
    title="AI Text Summarizer API",
    description="FastAPI backend using a BART-based model for text summarization.",
    version="1.0.0",
)

class SummaryRequest(BaseModel):
    text: str = Field(..., description="The input text to summarize")
    max_length: int = Field(130, description="Maximum summary length (tokens)")
    min_length: int = Field(30, description="Minimum summary length (tokens)")

class SummaryResponse(BaseModel):
    summary: str
    original_length: int
    summary_length: int

@app.get("/")
def root():
    return {"message": "AI Text Summarizer API is running."}

@app.post("/summarize", response_model=SummaryResponse)
def summarize(request: SummaryRequest):
    """
    Summarize the input text using the underlying summarization function.
    """

    try:
        summary_text = summarize_text(
            request.text,
            max_length=request.max_length,
            min_length=request.min_length,
        )
    except ValueError as e:
        # from our safety check
        raise HTTPException(status_code=400, detail=str(e))
    except Exception:
        # catch-all in case model fails
        raise HTTPException(status_code=500, detail="Error while summarizing text.")

    return SummaryResponse(
        summary=summary_text,
        original_length=len(request.text),
        summary_length=len(summary_text),
    )
