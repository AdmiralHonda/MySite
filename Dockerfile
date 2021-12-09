FROM ubuntu

USER root
WORKDIR /src
ADD . /src/

RUN apt-get update
RUN apt-get install -y git \ hugo