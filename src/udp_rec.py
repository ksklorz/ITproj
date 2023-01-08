import socket
import queue
from cam import hud
import base64
import struct
import tlm

from globals import *



def udpRecThread():
    UDP_REC_PORT = 31338
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Internet  # UDP
    # sock.connect((UDP_IP, UDP_PORT))
    sock.bind(('', UDP_REC_PORT))
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    while True:
        line = sock.recv(256)
        data = decodeLine(line)
        udpRecQue.put(data)

def decodeLine(line):
    bytes = base64.b64decode(line)
    dataI = struct.unpack('@Lhhhhhhhhhh',bytes)
    dataI = tlm.tlmAHRS(dataI[0], dataI[1], dataI[2], dataI[3], dataI[4], dataI[5], dataI[6], dataI[7], dataI[8], dataI[9], dataI[10])
    dataF = tlm.dataAHRS(float(dataI.time)/10000.0,float(dataI.phi)/10000.0,float(dataI.theta)/10000.0,float(dataI.psi)/10000.0,float(dataI.P)/10000.0,float(dataI.Q)/10000.0,float(dataI.R)/10000.0,float(dataI.accX)/10000.0,float(dataI.accY)/10000.0,float(dataI.accZ)/10000.0,float(dataI.range) )
    return dataF