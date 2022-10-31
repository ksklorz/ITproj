from dataclasses import dataclass
import cv2
import math
import numpy as np
import base64
import struct
from numpy import int16, int8, uint16, uint8, uint32, int32

def drawHor(frame, theta, phi):
    widAngle = 65
    heiAngle = widAngle*3.0/4.0
    height, width, channels = frame.shape
    pm = (width/2, height/2)
    pm = (pm[0], pm[1]+theta/widAngle*height)
    r = width * .25
    p1 = (int(pm[0]-r*math.cos(phi/57.0)), int(pm[1]+r*math.sin(phi/57.0)))
    p2 = (int(pm[0]+r*math.cos(phi/57.0)), int(pm[1]-r*math.sin(phi/57.0)))
    cv2.line(frame,p1,p2,(0,255,0),3)
    return frame


@dataclass
class tlmAHRS:
    time: uint32 = 0
    phi: int16 = 0
    theta: int16 = 0
    psi: int16 = 0
    P: int16 = 0
    Q: int16 = 0
    R: int16 = 0
    accX: int16 = 0
    accY: int16 = 0
    accZ: int16 = 0
    smiec: int16 = 0 #?????

@dataclass
class dataAHRS:
    time: float = 0.0
    phi: float = 0.0
    theta: float = 0.0
    psi: float = 0.0
    P: float = 0.0
    Q: float = 0.0
    R: float = 0.0
    accX: float = 0.0
    accY: float = 0.0
    accZ: float = 0.0

def encodeTlm(line):
    bytes = base64.b64decode(line)
    tlm = struct.unpack('@Lhhhhhhhhhh',bytes)
    tlm = tlmAHRS(tlm[0], tlm[1], tlm[2], tlm[3], tlm[4], tlm[5], tlm[6], tlm[7], tlm[8], tlm[9], tlm[10])
    return tlm