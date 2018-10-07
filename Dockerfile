# Based on:
# - https://github.com/ageitgey/face_recognition/blob/master/Dockerfile
# - https://hub.docker.com/r/library/python/
#
FROM python:3.6-slim-stretch
LABEL name=goldenprofile \
      version=0.0.1 \
      maintainer="dev@florianrusch.de"

EXPOSE 3000

RUN apt-get -y update \
    && apt-get install -y --fix-missing \
        build-essential \
        cmake \
        gfortran \
        git \
        wget \
        curl \
        graphicsmagick \
        libgraphicsmagick1-dev \
        libatlas-dev \
        libavcodec-dev \
        libavformat-dev \
        libgtk2.0-dev \
        libjpeg-dev \
        liblapack-dev \
        libswscale-dev \
        pkg-config \
        python3-dev \
        python3-numpy \
        software-properties-common \
        zip \
    && apt-get clean \
    && rm -rf /tmp/* /var/tmp/*

# RUN cd ~ \
#     && git clone -b 'v19.9' --single-branch https://github.com/davisking/dlib.git dlib/ \
#     && cd dlib/ \
#     && python3 setup.py install

WORKDIR /app
ADD ./server/ /app

# Using pip:
RUN pip3 install -r requirements.txt \
    && apt-get remove build-essential cmake
CMD ["python3", "-m", "run"]
