FROM alpine:latest
RUN apk update && apk upgrade && apk add nodejs npm wget unzip
WORKDIR /root/src
VOLUME /root/src/code
ADD package.json /root/src
RUN wget https://github.com/processing/p5.js/releases/download/v1.6.0/p5.zip
RUN unzip p5.zip
RUN npm install
