#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Programa cliente que abre un socket a un servidor
"""

import socket
import sys

# Contenido que vamos a enviar
LINE = sys.argv[1] + ' ' + sys.argv[2]
LINE1 = 'INVITE sip:'
LINE2 = 'BYE sip:'
LINE3 = 'ACK sip:'

# Creamos el socket, lo configuramos y lo atamos a un servidor/puerto
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as my_socket:
    my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    PORT = int(LINE.split('@')[1].split(':')[1])
    SERVER = LINE.split('@')[1].split(':')[0]
    METHOD = sys.argv[1]
    LINE_SEND = ''.join(LINE).split(' ')[1]
    my_socket.connect((SERVER, PORT))
    if METHOD == 'INVITE':
        SEND = LINE1 + LINE_SEND
        print(SEND)
    elif METHOD == 'BYE':
        SEND = LINE2 + LINE_SEND
    else:
        SEND = LINE
    print("Enviando: " + SEND)
    my_socket.send(bytes(SEND + ' SIP/2.0', 'utf-8') + b'\r\n')
    data = my_socket.recv(1024)
    for receive in data.decode('utf-8').split():
        if receive == '200':
            SEND = LINE3 + LINE_SEND
            my_socket.send(bytes(SEND+ ' SIP/2.0', 'utf-8') + b'\r\n')
            data = my_socket.recv(1024)
    print(data.decode('utf-8'))
    print('Recibido -- ', data.decode('utf-8'))
    print("Terminando socket...")

print("Fin.")
