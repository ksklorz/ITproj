import socket
import queue
from cam import hud
import base64
import struct
import tlm
from dataclasses import dataclass
from numpy import int16, int8, uint16, uint8, uint32, int32

from globals import *
import crc8



UDP_IP = "192.168.137.66"
UDP_PORT = 31337
BIND_IP = "192.168.137.1"


def udpSendThread():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((BIND_IP, 2222))
    sock.connect((UDP_IP, UDP_PORT))
    
    while True:
        data = udpSendQue.get()
        line = encodeCmdLine(data)
        try:
            sock.send(line)
        except:
            print("socket error");


def encodeCmdLine(data):
    tel = struct.pack('@BffBB',data.cmd, data.x, data.y, data.cnt, data.crc)
    line = base64.b64encode(tel)
    return line

