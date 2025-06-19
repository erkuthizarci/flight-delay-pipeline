FROM python:3.10-slim

WORKDIR /app

# Install pandas
RUN pip install pandas

# Copy the script
COPY aggregate.py .

# Run the aggregation
CMD ["python", "aggregate.py"]
