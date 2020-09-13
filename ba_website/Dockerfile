FROM python:3.7-buster
ENV PYTHONUNBUFFERED 1
RUN apt update && apt upgrade -y
RUN pip install poetry
RUN mkdir /backend
WORKDIR /backend
COPY ./ba_website/pyproject.toml /backend/
COPY ./ba_website/poetry.lock /backend/
COPY ./ba_website/run_docker.sh /backend/
RUN poetry config virtualenvs.create false && poetry install --no-dev
COPY ./ba_website /backend/
