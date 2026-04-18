FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y postgresql-client && rm -rf /var/lib/apt/lists/*

COPY sample_requirements.txt .
RUN pip install --no-cache-dir -r sample_requirements.txt

COPY . .