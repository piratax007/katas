FROM jupyter/minimal-notebook:latest
WORKDIR /home/jovyan
VOLUME /home/jovyan/src
ADD requirements.txt /home/jovyan
RUN pip3 install -r requirements.txt
