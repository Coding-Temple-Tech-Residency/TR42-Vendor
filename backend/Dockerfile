FROM python:3.11

WORKDIR /app

# Prevent Python from buffering logs (important for Docker logs)
ENV PYTHONUNBUFFERED=1

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5001

CMD ["python", "run.py"]