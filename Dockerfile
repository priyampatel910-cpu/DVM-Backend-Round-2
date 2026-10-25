FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    UV_LINK_MODE=copy

WORKDIR /app

RUN pip install --no-cache-dir uv

COPY pyproject.toml uv.lock README.md ./
COPY src/ ./src/

RUN uv sync --locked --no-dev

COPY . .

EXPOSE 8000

CMD ["uv", "run", "--no-sync", "python", "manage.py", "runserver", "0.0.0.0:8000"]
