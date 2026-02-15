FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application
COPY tools/curator-ai tools/curator-ai
COPY tools/dashboard/backend tools/dashboard/backend
COPY tools/integrations tools/integrations
COPY core core
COPY docs docs

# Expose port
EXPOSE 8000

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Run API
CMD ["uvicorn", "tools.dashboard.backend.api:app", "--host", "0.0.0.0", "--port", "8000"]
