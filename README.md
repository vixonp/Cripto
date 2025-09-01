# Proyecto Cripto

Este proyecto consiste en varios scripts de Python para tareas criptográficas y comunicación en red.

## Descripción

*   **[main.py](main.py)**: Script principal que solicita al usuario un texto, un valor de desplazamiento para el cifrado César y una dirección IP de destino. Cifra el texto utilizando el cifrado César y envía el texto cifrado como un mensaje ICMP a la dirección IP especificada.
*   **[cesar.py](cesar.py)**: Implementa el cifrado César.
*   **[pingp3.py](pingp3.py)**: Envía mensajes ICMP.
*   **captura1.pcapng, captura2.pcapng**: Archivos de captura de red.
*   **[MitM.py](MitM.py)**: Script para ataques de Man-in-the-Middle (funcionalidad no detallada).

## Uso

1.  Asegúrate de tener Python instalado.
2.  Instala las dependencias necesarias (si las hay) usando `pip install -r requirements.txt`.
3.  Ejecuta `main.py` para cifrar un mensaje y enviarlo a través de ICMP:

    ```bash
    python main.py
    ```

    Sigue las instrucciones para ingresar el texto, el valor de desplazamiento y la IP de destino.

## Scripts

*   **[main.py](main.py)**
    *   Solicita al usuario un texto para cifrar, un valor de desplazamiento para el cifrado César y una dirección IP de destino.
    *   Cifra el texto utilizando la función [`caesar_cipher`](cesar.py) de `cesar.py`.
    *   Imprime el texto cifrado en la consola.
    *   Envía el texto cifrado como un mensaje ICMP a la dirección IP de destino utilizando la función [`send_icmp_message_48`](pingp3.py) de `pingp3.py`.
*   **[cesar.py](cesar.py)**
    *   Implementa el algoritmo de cifrado César. La función [`caesar_cipher`](cesar.py) desplaza cada letra en el texto de entrada por un número específico de posiciones en el alfabeto.
*   **[pingp3.py](pingp3.py)**
    *   Implementa la funcionalidad para enviar mensajes ICMP. La función [`send_icmp_message_48`](pingp3.py) envía un mensaje ICMP a una dirección IP especificada.
*   **[MitM.py](MitM.py)**
    *   Implementa un ataque Man in the Middle para decodificar mensajes ICMP. El script extrae mensajes ocultos desde archivos PCAP utilizando la función [`extract_message`](MitM.py). Luego, intenta descifrar el mensaje por fuerza bruta usando la función [`cesar_decrypt`](MitM.py) y una heurística simple para puntuar el texto legible con la función [`score_text`](MitM.py).

## Notas

*   Asegúrate de tener los permisos necesarios para enviar mensajes ICMP.
*   Utiliza este software de manera responsable y ética.

## Estructura del proyecto

.
├── MitM.py
├── README.md
├── pycache/
│ ├── cesar.cpython-312.pyc
│ └── pingp3.cpython-312.pyc
├── captura1.pcapng
├── captura2.pcapng
├── cesar.py
├── main.py
└── pingp3.py