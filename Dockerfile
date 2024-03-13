FROM python:3.11-alpine

RUN apk update && \
    apk add --no-cache \
    ca-certificates \
    gcc \
    libffi-dev \
    build-base \
    curl \
    gnupg \
    lsb-release \
    libpq \
    libpq-dev \
    python3-dev

RUN pip install --upgrade pip poetry && \
    poetry config virtualenvs.in-project false && \
    pip install gunicorn


COPY  poetry.lock .
COPY  pyproject.toml .

RUN poetry config virtualenvs.create false && \
    poetry install --no-root
   

WORKDIR /app
COPY . .

EXPOSE 8000

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
# 
