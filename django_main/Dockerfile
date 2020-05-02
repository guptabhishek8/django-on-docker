FROM python:3.7.1
WORKDIR /usr/src/app/django_main


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


RUN pip install --upgrade pip

COPY ./requirements.txt /usr/src/app/django_main/requirements.txt

RUN pip3 install --upgrade setuptools
RUN pip3 install --upgrade gcloud

RUN pip3 install -r requirements.txt


COPY . /usr/src/app/django_main


