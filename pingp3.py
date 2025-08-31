from scapy.all import IP, ICMP, send
import time

def send_icmp_message(host, message):
    print(f"[+] Enviando mensaje oculto a {host}")
    for char in message:
        # Padding típico de ping en Linux (56 bytes)
        default_padding = b"abcdefghijklmnopqrstuvwabcdefghi"
        
        # Construir payload: primer byte = carácter secreto, resto = padding normal
        payload = char.encode() + default_padding[1:]
        
        packet = IP(dst=host)/ICMP()/payload
        print(f"-> Enviando carácter: {char} ({ord(char)})")
        send(packet, verbose=False)
        time.sleep(0.5)
    print("[+] Envío completo.")
