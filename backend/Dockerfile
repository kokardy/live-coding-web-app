FROM python:3.14-slim

WORKDIR /backend

COPY ./pyproject.toml /backend/pyproject.toml
COPY ./src /backend/src

RUN pip install uv && uv python pin 3.14 && uv sync
