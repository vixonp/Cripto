def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            # Para letras mayúsculas
            if char.isupper():
                result += chr((ord(char) - 65 + shift) % 26 + 65)
            # Para letras minúsculas
            else:
                result += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            # Si no es letra (espacios, números, símbolos) lo dejamos igual
            result += char
    return result


if __name__ == "__main__":
    texto = input("Ingrese el texto a cifrar: ")
    corrimiento = int(input("Ingrese el corrimiento (número entero): "))
    
    texto_cifrado = caesar_cipher(texto, corrimiento)
    print("\nTexto cifrado:", texto_cifrado)