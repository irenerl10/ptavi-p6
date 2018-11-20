#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import socketserver
import sys

if len(sys.argv)<4:
    sys.exit('Usage: python3 server.py IP port_audio_file')

SERVER = sys.argv[1]
PORT = sys.argv[2]
FILE = sys.argv[3]
class EchoHandler(socketserver.DatagramRequestHandler):
    """
    Echo server class
    """
    def handle(self):
        # Escribe dirección y puerto del cliente (de tupla client_address)
        self.wfile.write(b"Hemos recibido tu peticion")
        while 1:
            # Leyendo línea a línea lo que nos envía el cliente
            line = self.rfile.read()
            try:
                METHOD = line.decode('utf-8').split()[0]
            except:
                pass
            METHODS = ['INVITE', 'BYE', 'ACK']
            print('x', METHOD, METHODS)

            # Si no hay más líneas salimos del bucle infinito
            if not line:
                break

if __name__ == "__main__":
    # Creamos servidor de eco y escuchamos
    serv = socketserver.UDPServer(('', 6001), EchoHandler)
    print("Lanzando servidor UDP de eco...")
    serv.serve_forever()
