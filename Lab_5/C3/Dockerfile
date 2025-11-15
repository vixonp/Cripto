# C3/Dockerfile - Ubuntu 20.10 con SSH Client
FROM ubuntu:20.10

ENV DEBIAN_FRONTEND=noninteractive

# Instalar OpenSSH Client y herramientas de red
RUN sed -i -re 's/([a-z]{2}\.)?archive.ubuntu.com|security.ubuntu.com/old-releases.ubuntu.com/g' /etc/apt/sources.list && \
    apt-get update && \
    apt-get install -y \
    openssh-client \
    tcpdump \
    net-tools \
    iputils-ping && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Crear directorio para capturas
RUN mkdir -p /capturas

WORKDIR /root

CMD ["tail", "-f", "/dev/null"]