# Dockerfile for FastAPI AI Text Summarizer

# 1. Base image
FROM python:3.11-slim

# 2. Set working directory inside the container
WORKDIR /app

# 3. Environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    HF_HOME=/hf-cache \
    TRANSFORMERS_CACHE=/hf-cache \
    HUGGINGFACE_HUB_CACHE=/hf-cache

# 4. Install system dependencies (needed for some Python packages)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# 5. Copy requirements and install Python dependencies
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# 6. Copy application code (only backend)
COPY app ./app

# 7. Expose FastAPI port
EXPOSE 8000

# 8. Start FastAPI using Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
