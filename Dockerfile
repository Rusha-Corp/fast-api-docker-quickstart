FROM python:3.13-bookworm

RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y

# add cargo to PATH
ENV PATH="/root/.cargo/bin:${PATH}"

RUN pip install --upgrade pip poetry && \
    poetry config virtualenvs.in-project true

COPY pyproject.toml poetry.lock ./
RUN poetry install

COPY . /app

WORKDIR /app

CMD ["poetry", "run", "uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
#