# Base Python image
FROM python:3.12.11-slim-bullseye

# Set work directory
WORKDIR /app

# Copy project files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set environment variables (optional, use .env in production)
ENV PYTHONUNBUFFERED=1

# Entrypoint
CMD ["python", "main.py"]
