FROM alpine:latest
RUN apk update && apk upgrade && apk add nodejs npm wget unzip
WORKDIR /home/src
VOLUME /home/src/code
ADD package.json /home/src
RUN npm install
