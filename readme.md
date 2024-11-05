# FastAPI Docker Quickstart

This guide will help you get started with a FastAPI application using Docker.

## Prerequisites

- Docker installed on your machine
- Basic knowledge of FastAPI and Docker

## Dockerfile

Here is the `Dockerfile` used to build the FastAPI application:

```Dockerfile
# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the FastAPI application code into the container
COPY . .

# Expose the port the app runs on
EXPOSE 8000

# Command to run the application
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
```

## app.py

Here is a simple example of `app.py` for the FastAPI application:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
```

## Building and Running the Docker Container

1. **Build the Docker image:**

    ```sh
    docker build -t fastapi-app .
    ```

2. **Run the Docker container:**

    ```sh
    docker run -d -p 8000:8000 fastapi-app
    ```

3. **Access the application:**

    Open your browser and navigate to `http://localhost:8000` to see the FastAPI application in action.

## Conclusion

You have successfully set up a FastAPI application with Docker. You can now extend the application and customize it as per your requirements.