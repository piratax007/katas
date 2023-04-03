
FROM alpine:latest
RUN apk update && apk upgrade && apk add nodejs npm
WORKDIR /root/src
VOLUME /root/src/code
ADD package.json /root/src
RUN npm install
