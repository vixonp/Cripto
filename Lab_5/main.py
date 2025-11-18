import paramiko
import socket
import time
import sys

# Configuración
HOST_IP = "172.19.0.5"
PUERTO = 22
VERSION_A_FALSIFICAR = "SSH-2.0-OpenSSH_?"
USUARIO = "prueba"
PASSWORD = "prueba"

def conectar_ssh_falsificado():
    sock = None
    transport = None
    
    try:
        print("="*60)
        print("  REPLICACIÓN SSH CON VERSIÓN FALSIFICADA")
        print("="*60)
        print(f"[*] Servidor: {HOST_IP}:{PUERTO}")
        print(f"[*] Usuario: {USUARIO}")
        print(f"[*] Versión a falsificar: {VERSION_A_FALSIFICAR}")
        print()
        
        # Paso 1: Crear socket
        print("[1/5] Creando socket TCP...")
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)  # ← IMPORTANTE: timeout de 5 segundos
        print("      ✓ Socket creado")
        
        # Paso 2: Conectar
        print(f"[2/5] Conectando a {HOST_IP}:{PUERTO}...")
        sock.connect((HOST_IP, PUERTO))
        print("      ✓ Conexión TCP establecida")
        
        # Paso 3: Crear transporte SSH y falsificar versión
        print("[3/5] Creando transporte SSH...")
        transport = paramiko.Transport(sock)
        transport.local_version = VERSION_A_FALSIFICAR
        print(f"      ✓ Versión falsificada: {VERSION_A_FALSIFICAR}")
        
        # Paso 4: Iniciar handshake
        print("[4/5] Realizando handshake SSH...")
        transport.start_client(timeout=10)
        print("      ✓ Handshake completado")
        
        # Paso 5: Autenticar
        print(f"[5/5] Autenticando como '{USUARIO}'...")
        transport.auth_password(username=USUARIO, password=PASSWORD, fallback=False)
        print("      ✓ Autenticación exitosa")
        
        print()
        print("[SUCCESS] Conexión establecida correctamente")
        print("[*] Manteniendo conexión por 5 segundos...")
        time.sleep(5)
        
        return True
        
    except socket.timeout:
        print("\n[ERROR] Timeout - El servidor no responde")
        print("Verifica que el contenedor esté accesible desde el host")
        return False
        
    except ConnectionRefusedError:
        print(f"\n[ERROR] Conexión rechazada a {HOST_IP}:{PUERTO}")
        return False
        
    except paramiko.AuthenticationException:
        print("\n[ERROR] Autenticación fallida")
        return False
        
    except Exception as e:
        print(f"\n[ERROR] {type(e).__name__}: {e}")
        return False
        
    finally:
        if transport:
            transport.close()
            print("[*] Transporte cerrado")
        if sock:
            sock.close()
            print("[*] Socket cerrado")

if __name__ == "__main__":
    resultado = conectar_ssh_falsificado()
    sys.exit(0 if resultado else 1)