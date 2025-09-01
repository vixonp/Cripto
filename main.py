from cesar import caesar_cipher
from pingp3 import send_icmp_message_48

if __name__ == "__main__":
    texto = input("Ingrese el texto a cifrar: ")
    corrimiento = int(input("Ingrese el corrimiento: "))
    destino = input("Ingrese la IP de destino: ")

    # 1) cifrado césar
    texto_cifrado = caesar_cipher(texto, corrimiento)
    print(f"\nTexto cifrado: {texto_cifrado}")

    # 2) envío en payloads ICMP de 48 bytes (8 bytes de mensaje por paquete)
    send_icmp_message_48(destino, texto_cifrado)
