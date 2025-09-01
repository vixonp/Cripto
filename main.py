from cesar import caesar_cipher
from pingp3 import send_icmp_message_48

if __name__ == "__main__":
    texto = input("Ingrese el texto a cifrar: ")
    corrimiento = int(input("Ingrese el corrimiento: "))
    destino = input("Ingrese la IP de destino: ")

    texto_cifrado = caesar_cipher(texto, corrimiento)
    print(f"\nTexto cifrado: {texto_cifrado}")

    send_icmp_message_48(destino, texto_cifrado)


