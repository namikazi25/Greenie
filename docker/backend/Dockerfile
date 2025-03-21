FROM python:3.9-slim

WORKDIR /app

# Install dependencies
COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy backend code
COPY backend/ .

# Create directories for logs and uploads
RUN mkdir -p logs uploads

# Expose port
EXPOSE 8000

# Start the FastAPI server
CMD ["uvicorn", "api.chat:app", "--host", "0.0.0.0", "--port", "8000"]