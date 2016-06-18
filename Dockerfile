FROM jfloff/alpine-python:3.4-onbuild

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY server.py /usr/src/app/
COPY emitter.py /usr/src/app/
