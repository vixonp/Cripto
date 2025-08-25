def caesar_cipher(text: str, shift: int) -> str:
    result = ""

    for char in text:
        # Si es mayúscula
        if char.isupper():
            result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        # Si es minúscula
        elif char.islower():
            result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            # Dejar otros caracteres tal cual (espacios, números, signos)
            result += char

    return result


# Ejemplo de uso
if __name__ == "__main__":
    texto = input("Ingrese el texto a cifrar: ")
    corrimiento = int(input("Ingrese el corrimiento César: "))
    
    cifrado = caesar_cipher(texto, corrimiento)
    print("Texto cifrado:", cifrado)
