import paramiko
import socket

HOST_IP = "c4-s1"  # Dirección del servidor (nombre del contenedor Docker)
PUERTO = 22
VERSION_A_FALSIFICAR = "SSH-2.0-OpenSSH_?"  # Versión personalizada
USUARIO = "prueba"
PASSWORD = "prueba"

# Crear socket y conectar
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST_IP, PUERTO))

# Crear transporte SSH
transport = paramiko.Transport(sock)

# CLAVE: Modificar la versión local que anuncia el cliente
transport.local_version = VERSION_A_FALSIFICAR

# Iniciar conexión SSH
transport.start_client()

# Autenticar con usuario y contraseña
transport.auth_password(username=USUARIO, password=PASSWORD)