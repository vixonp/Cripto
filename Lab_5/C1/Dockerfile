# C1/Dockerfile - Ubuntu 16.10 con SSH Client
FROM ubuntu:16.10

ENV DEBIAN_FRONTEND=noninteractive

# Instalar OpenSSH Client y herramientas de red
RUN apt-get update && \
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