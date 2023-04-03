FROM debian:bookworm
RUN apt-get -y update && apt-get -y upgrade
RUN apt-get -y install nodejs npm --no-install-recommends
WORKDIR /root/src
VOLUME /root/src/code
ADD package.json /root/src
RUN npm install
