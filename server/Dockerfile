#####################################################################
# GOLDENPROFILE PYTHONBASE IMAGE
#
# Based on:
# https://github.com/ageitgey/face_recognition/blob/master/Dockerfile
# https://hub.docker.com/r/library/python/
# https://goo.gl/Zj7Fx1
#####################################################################
FROM python:3.6-slim-stretch as goldenprofile_pythonbase
LABEL name=goldenprofile_pythonbase \
      version=0.0.1 \
      maintainer="dev@florianrusch.de"

RUN apt-get -y update --no-install-recommends \
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

RUN pip3 install face_recognition==1.2.1
RUN pip3 install Flask==0.12.2

COPY ./requirements.txt /

# Add still missing requirements
RUN pip3 install -r requirements.txt

# Remove build-dependencies
RUN apt-get remove -y build-essential cmake



#####################################################################
# GOLDENPROFILE SERVER IMAGE
#####################################################################
FROM goldenprofile_pythonbase
LABEL name=goldenprofile_backend \
      version=0.0.1 \
      maintainer="dev@florianrusch.de"

EXPOSE 8080

WORKDIR /app

CMD ["python3", "-m", "run"]
