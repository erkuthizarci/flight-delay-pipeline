FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install required packages
RUN pip install kaggle

# Copy script into container
COPY ingest.py .

# Make sure /data directory exists
RUN mkdir -p /data

# Set command to run
CMD ["python", "ingest.py"]
