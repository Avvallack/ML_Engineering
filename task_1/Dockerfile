FROM ubuntu:18.04


WORKDIR /home/starspace_worker

RUN apt-get update && apt-get install -yq git automake autoconf libtool build-essential libboost-all-dev

RUN git clone https://github.com/facebookresearch/Starspace.git && \
    cd Starspace && \
    make && \
    cp -Rf starspace /usr/local/bin

ARG USER_ID
ARG GROUP_ID

RUN addgroup --gid $GROUP_ID user
RUN adduser --disabled-password --gecos '' --uid $USER_ID --gid $GROUP_ID user
USER user

WORKDIR /home/starspace_worker