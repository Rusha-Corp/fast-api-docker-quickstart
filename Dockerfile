FROM python:3.13-slim

RUN pip install --upgrade pip poetry && \
    poetry config virtualenvs.in-project true

WORKDIR /app
COPY . .
RUN poetry install --no-root

CMD ["poetry", "run", "python", "-m", "uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
#