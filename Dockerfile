FROM python:3.10.12-bookworm

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
RUN pip3 install pylint
COPY . .



CMD pylint *.py
