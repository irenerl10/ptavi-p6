#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import socketserver
import sys
import os

if len(sys.argv) < 4:
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
        while 1:
            line = self.rfile.read()
            if not line:
                break
            METHOD = line.decode('utf-8').split()[0]
            if METHOD == self.METHODS[0]:
                self.wfile.write(b"SIP/2.0 100 Trying\r\n\r\n")
                self.wfile.write(b"SIP/2.0 180 Ringing\r\n\r\n")
                self.wfile.write(b"SIP/2.0 SIP/2.0 200 OK\r\n\r\n")
            elif METHOD == self.METHODS[1]:
                self.wfile.write(b"SIP/2.0 200 OK \r\n\r\n")
            elif METHOD == self.METHODS[2]:
                aEjecutar = 'mp32rtp -i 127.0.0.1 -p 23032 <' + sys.argv[3]
                os.system(aEjecutar)
            elif METHOD != self.METHODS:
                self.wfile.write(b"SIP/2.0 405 Method Not Allowed\r\n\r\n")
            else:
                self.wfile.write(b"SIP/2.0 400 Bad Request\r\n\r\n")


if __name__ == "__main__":
    serv = socketserver.UDPServer(('', 6001), EchoHandler)
    print("Lanzando servidor UDP de eco...")
    if os.path.isfile(FILE):
        print("Listening...")
        serv.serve_forever()
    serv.serve_forever()
