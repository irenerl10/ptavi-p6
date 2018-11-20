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
    METHODS = ['INVITE', 'BYE', 'ACK']
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
            if METHOD == self.METHODS[0]:
                self.wfile.write(b"\nSIP/2.0 100 Trying\nSIP/2.0 180 Ringing\nSIP/2.0 200 OK")
            elif METHOD == self.METHODS[1]:
                self.wfile.write(b"SIP/2.0 200 OK \n")
            elif METHOD == self.METHODS[2]:
                aEjecutar = 'mp32rtp -i 127.0.0.1 -p 23032 <' + sys.argv[3]
                os.system(aEjecutar)
            if METHOD != self.METHODS:
                self.wfile.write(b"SIP/2.0 405 Method Not Allowed \n")
            else:
                self.wfile.write(b"SIP/2.0 400 Bad Request \n")
           
            # Si no hay más líneas salimos del bucle infinito
            if not line:
                break
            else:
                print('line.decode('utf-8')')

if __name__ == "__main__":
    # Creamos servidor de eco y escuchamos
    serv = socketserver.UDPServer(('', 6001), EchoHandler)
    print("Lanzando servidor UDP de eco...")
	  if os.path.isfile(FICH_AUDIO):
        print("Listening...")
        serv.serve_forever()
    serv.serve_forever()
