# ==============================================================================
# Bilota (بيلوتا / قطوة) - Production Container for Google Cloud Run (GCP)
# ==============================================================================
FROM python:3.11-slim

# Prevent Python from writing .pyc files and enable unbuffered logging
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app \
    PORT=8080

WORKDIR /app

# Install minimal system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application source code and runtime assets
COPY src/ ./src/
COPY domain-packs/ ./domain-packs/
COPY docs/ ./docs/
COPY eval/ ./eval/

# Ensure non-root execution for container security
RUN useradd -m -u 1000 appuser && chown -R appuser:appuser /app
USER appuser

# Health check to ensure service readiness
HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:${PORT}/api/health || exit 1

# Cloud Run injects $PORT environment variable dynamically (defaults to 8080)
EXPOSE 8080

# Launch FastAPI via uvicorn
CMD ["sh", "-c", "uvicorn src.app:app --host 0.0.0.0 --port ${PORT:-8080}"]
