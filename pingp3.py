from scapy.all import IP, ICMP, send
import time, os

# Padding fijo: 0x20–0x37 (ASCII " !"#$%&'()*+,-./01234567")
PADDING = bytes(range(0x20, 0x38))  # 24 bytes
PADDING_FULL = (PADDING * 2)[:40]   # 40 bytes exactos

def build_payload_48(char: str) -> bytes:
    """
    Construye payload ICMP de 48 bytes:
    - Byte 0 = carácter del mensaje
    - Bytes 1..7 = 0x00
    - Bytes 8..47 = patrón 0x20..0x37 repetido
    """
    msg_part = char.encode() + b"\x00" * 7
    payload = msg_part + PADDING_FULL
    assert len(payload) == 48
    return payload

def send_icmp_message_48(dst_ip: str, ciphertext: str, delay_s: float = 0.3):
    """
    Envía el texto cifrado en payloads ICMP de 48 bytes.
    Cada paquete lleva 1 carácter en el primer byte.
    """
    icmp_id = int.from_bytes(os.urandom(2), "big")
    ip_id = int.from_bytes(os.urandom(2), "big")

    print(f"[+] Destino {dst_ip}")
    print(f"[+] ICMP.id=0x{icmp_id:04x}, IP.id inicial=0x{ip_id:04x}")

    for i, c in enumerate(ciphertext):
        payload = build_payload_48(c)
        pkt = IP(dst=dst_ip, id=(ip_id + i)) / ICMP(id=icmp_id, seq=(i+1)) / payload

        # Log de evidencia
        print(f" -> pkt#{i+1} letra='{c}'  IP.id=0x{(ip_id+i):04x}  ICMP.seq={i+1}")
        print(f"    data[0:16] = {payload[:16].hex()}")

        send(pkt, verbose=False)
        time.sleep(delay_s)

    print("[+] Envío completo (48 bytes por paquete)")
