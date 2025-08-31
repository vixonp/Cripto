from cesar import caesar_cipher
from pingp3 import send_icmp_message

if __name__ == "__main__":
    texto = input("Ingrese el texto a cifrar: ")
    corrimiento = int(input("Ingrese el corrimiento: "))
    destino = input("Ingrese la IP de destino: ")

    # Paso 1: cifrar
    texto_cifrado = caesar_cipher(texto, corrimiento)
    print(f"\nTexto cifrado: {texto_cifrado}")

    # Paso 2: enviar por ICMP
    send_icmp_message(destino, texto_cifrado)
