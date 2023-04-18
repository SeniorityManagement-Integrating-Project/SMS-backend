# Our base image
FROM python:3.10-alpine

# Create app directory
WORKDIR /app

# Copy the requirements
COPY ./requirements.txt /app/requirements.txt

# Copy the .env file
COPY ./.env /app/.env

# Install the requirements
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy the source code
COPY ./src /app/src

EXPOSE 8000

# Run the app
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]