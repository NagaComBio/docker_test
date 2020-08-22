FROM ubuntu:18.04

RUN apt-get update \
    && apt-get install -y python3-dev wget


RUN wget -nv https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh \
    && mkdir /home/app \
    && mkdir /home/app/data \
    && mkdir /home/app/src \
    && mv Miniconda3-latest-Linux-x86_64.sh /home/app \
    && cd /home/app \
    && sh Miniconda3-latest-Linux-x86_64.sh -b \
    && rm Miniconda3-latest-Linux-x86_64.sh

COPY requirements.txt /home/app/src
COPY nltk_setup.py /home/app/src

ENV PATH="/root/miniconda3/bin:${PATH}"

RUN cd /home/app/src \
    && conda env create -f requirements.txt -n ml_env

RUN /bin/bash -c "source activate ml_env && python /home/app/src/nltk_setup.py"