FROM python:3.9.7-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /app
COPY requirements.txt /app/
COPY . /app
RUN pip install -r requirements.txt
