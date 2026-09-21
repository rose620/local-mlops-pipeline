# 1. Use clean, official, lightweight Python base image
FROM python:3.11-slim


# 2. Set working directory inside container
WORKDIR /app

# 3. Copy over python package list and install them
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copy live API code and trained model weights into container
COPY app.py .
COPY wine_model.pkl .

# 5. Tell Docker that this container will listen on port 8000
EXPOSE 8000

# 6. This is command to launch the FastAPI server automatically when container wakes up
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
