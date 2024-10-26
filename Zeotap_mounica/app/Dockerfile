# Use Python 3.9-slim as the base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file from the current directory
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all files from the app directory into the container
COPY . .

# Set the default command to run rule_engine.py
CMD ["python", "rule_engine.py"]
