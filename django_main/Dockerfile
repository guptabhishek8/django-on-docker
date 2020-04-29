FROM python:3.8.0-alpine

WORKDIR /usr/src/app/django_main


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


RUN pip install --upgrade pip

COPY ./requirements.txt /usr/src/app/django_main/requirements.txt

RUN pip install -r requirements.txt


COPY . /usr/src/app/django_main
