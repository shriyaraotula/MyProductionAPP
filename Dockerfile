# Dockerfile
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install curl (required for healthcheck)
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY MyProductionAPP/ ./MyProductionAPP

# Expose port
EXPOSE 8000

# Command to run the app
CMD ["uvicorn", "MyProductionAPP.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
