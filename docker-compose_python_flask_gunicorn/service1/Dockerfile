FROM ubuntu:focal-20211006
RUN apt-get -y update
RUN apt-get -y install python3
RUN apt-get -y install python3-pip
ADD . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
EXPOSE 80