from scapy.all import rdpcap, ICMP
import argparse
from colorama import Fore, Style

def cesar_decrypt(ciphertext: str, shift: int) -> str:
    resultado = ""
    for char in ciphertext:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            resultado += chr((ord(char) - base - shift) % 26 + base)
        else:
            resultado += char
    return resultado

def score_text(text: str) -> int:
    # Heurística simple: cuenta vocales + espacios como "legibles"
    score = sum(1 for c in text if c.lower() in "aeiou ")
    return score

def extract_message(pcap_file: str, dst_ip: str) -> str:
    packets = rdpcap(pcap_file)
    chars = []

    for pkt in packets:
        if pkt.haslayer(ICMP):
            icmp = pkt[ICMP]
            # Echo request con destino correcto y payload válido
            if icmp.type == 8 and pkt["IP"].dst == dst_ip and bytes(icmp.payload):
                payload = bytes(icmp.payload)
                if len(payload) >= 1:
                    chars.append(chr(payload[0]))  # Primer byte = carácter oculto

    return "".join(chars)

def main():
    parser = argparse.ArgumentParser(description="Decodificar mensaje oculto desde PCAP con fuerza bruta César.")
    parser.add_argument("--pcap", required=True, help="Archivo PCAP/PCAPNG con la captura de ICMP.")
    parser.add_argument("--dst", required=True, help="IP de destino de los paquetes ICMP (ej: 8.8.8.8).")
    args = parser.parse_args()

    ciphertext = extract_message(args.pcap, args.dst)
    if not ciphertext:
        print("No se extrajo ningún mensaje oculto.")
        return

    print(f"[+] Mensaje cifrado extraído: {ciphertext}")

    # Probar todos los shifts posibles
    candidates = []
    for shift in range(26):
        candidate = cesar_decrypt(ciphertext, shift)
        candidates.append((shift, candidate, score_text(candidate)))

    # Elegir el más probable
    best = max(candidates, key=lambda x: x[2])

    print("\nPosibles decodificaciones:")
    for shift, candidate, score in candidates:
        if candidate == best[1]:
            print(Fore.GREEN + f"Shift={shift}: {candidate}" + Style.RESET_ALL)
        else:
            print(f"Shift={shift}: {candidate}")

if __name__ == "__main__":
    main()
