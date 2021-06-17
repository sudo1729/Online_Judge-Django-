
FROM ubuntu:latest
RUN mkdir /app
RUN apt update && apt -y upgrade
RUN apt install -y g++
RUN apt install -y python3

WORKDIR /app
COPY . /app
RUN apt update
RUN apt install -y python3-pip
RUN pip3 install -r requirements.txt
CMD python3 manage.py runserver 0.0.0.0:$PORT

