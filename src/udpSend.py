import socket
import queue
from cam import hud
import base64
import struct
import tlm

from globals import *



def udpSendThread():
    UDP_IP = "192.168.137.66"
    UDP_PORT = 31337
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(("192.168.137.1", 2222))
    sock.connect((UDP_IP, UDP_PORT))
    
    while True:
        data = udpSendQue.get()
        line = encodeCmdLine(data)
        try:
            sock.send(line)
        except:
            print("socket kaput");

def encodeCmdLine(data):
    tel = struct.pack('@?ff',data.on, data.up, data.right)
    line = base64.b64encode(tel)
    return line