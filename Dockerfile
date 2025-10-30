FROM python:3.13-slim@sha256:8b0b5bd0c6b4e0a0688b9e0521c83325eaeb5d7f3dd5f8e5b3c2b3c1c5e5e5e5e

WORKDIR /app


COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
