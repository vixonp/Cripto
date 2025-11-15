# C4-S1/Dockerfile - Ubuntu 22.10 con SSH Client y Server
FROM ubuntu:22.10

ENV DEBIAN_FRONTEND=noninteractive

# Instalar OpenSSH Client, Server y herramientas
RUN apt-get update && \
    apt-get install -y \
    openssh-client \
    openssh-server \
    sudo \
    tcpdump \
    net-tools \
    iputils-ping && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Crear directorio SSH
RUN mkdir -p /var/run/sshd

# Crear usuario 'prueba' con contraseña 'prueba'
RUN useradd -m -s /bin/bash prueba && \
    echo 'prueba:prueba' | chpasswd && \
    usermod -aG sudo prueba

# Configurar SSH para permitir autenticación por contraseña
RUN sed -i 's/#PasswordAuthentication yes/PasswordAuthentication yes/' /etc/ssh/sshd_config && \
    sed -i 's/PasswordAuthentication no/PasswordAuthentication yes/' /etc/ssh/sshd_config && \
    sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

# Crear directorio para capturas
RUN mkdir -p /capturas

WORKDIR /root

EXPOSE 22

# Iniciar SSH y mantener contenedor activo
CMD service ssh start && tail -f /dev/null