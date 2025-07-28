FROM python:3.11-slim

WORKDIR /app

# Install Firefox dependencies
RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    curl \
    firefox-esr \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Install Geckodriver manually
ENV GECKODRIVER_VERSION=v0.34.0

RUN wget -q "https://github.com/mozilla/geckodriver/releases/download/${GECKODRIVER_VERSION}/geckodriver-${GECKODRIVER_VERSION}-linux64.tar.gz" \
    && tar -xzf "geckodriver-${GECKODRIVER_VERSION}-linux64.tar.gz" \
    && mv geckodriver /usr/local/bin/ \
    && chmod +x /usr/local/bin/geckodriver \
    && rm "geckodriver-${GECKODRIVER_VERSION}-linux64.tar.gz"

# Copy project files
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set environment variable for unbuffered logs
ENV PYTHONUNBUFFERED=1

# Default command
CMD ["python", "main.py"]
