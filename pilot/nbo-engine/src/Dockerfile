FROM python:3.11-slim

WORKDIR /app

COPY src/ /app/

RUN pip install --no-cache-dir pydantic numpy

CMD ["python", "main.py"]
