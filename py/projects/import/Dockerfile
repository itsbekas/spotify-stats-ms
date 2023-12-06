FROM python:3.11-alpine

WORKDIR /app

COPY pyproject.toml /app
COPY src /app/src

RUN pip install .

EXPOSE 