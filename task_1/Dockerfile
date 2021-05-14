FROM ubuntu:20.04

ARG PROJECT_NAME="task_1"

RUN useradd -ms /bin/bash starspace_worker
RUN su - starspace_worker

WORKDIR /home/starspace_worker

RUN apt-get update && apt-get install -yq git wget unzip make g++ build-essential

RUN wget https://sourceforge.net/projects/boost/files/boost/1.63.0/boost_1_63_0.tar.gz/download
RUN tar -xf boost_1_63_0.tar.gz
RUN mv boost_1_63_0 /usr/local/bin

RUN git clone https://github.com/facebookresearch/Starspace.git && \
    cd Starspace && \
    make && \
    cp -Rf starspace /usr/local/bin

RUN ./starspace train -trainFile data.txt -model modelSaveFile
