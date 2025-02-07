# Use official Python image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy files
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Expose port
EXPOSE 8000
# Run the server
CMD ["uvicorn", "app.server:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
