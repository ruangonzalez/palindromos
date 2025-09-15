FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
COPY palindrome.py .
COPY test_palindrome.py .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "palindrome.py"]
