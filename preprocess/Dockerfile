FROM python:3.10-slim

WORKDIR /app

# Install pandas
RUN pip install pandas

# Copy the script
COPY preprocess.py .

# Mount /data folder at runtime
CMD ["python", "preprocess.py"]
