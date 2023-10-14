FROM python:3.10.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /backend

WORKDIR /backend

COPY requirements.txt /backend/

RUN pip install --upgrade pip && pip install -r requirements.txt

ADD . /backend/