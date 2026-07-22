# ACDSS application image (research prototype).
FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

# System deps for psycopg / sentence-transformers build steps.
RUN apt-get update \
    && apt-get install -y --no-install-recommends build-essential libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install dependencies first (better layer caching).
COPY pyproject.toml README.md ./
COPY src ./src
RUN pip install --upgrade pip && pip install -e .

# Non-root user.
RUN useradd --create-home --uid 1000 acdss
USER acdss

EXPOSE 8000

# TODO: for production, drop --reload and set worker count via gunicorn/uvicorn.
CMD ["uvicorn", "acdss.api.main:app", "--host", "0.0.0.0", "--port", "8000"]
