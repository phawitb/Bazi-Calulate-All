# Use official Python image
FROM python:3.10

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8003
EXPOSE 8003

# Start FastAPI on port 8003
CMD ["uvicorn", "main_api:app", "--host", "0.0.0.0", "--port", "8003"]
