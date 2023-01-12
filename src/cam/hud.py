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

def drawRange(frame, range):
    height, width, channels = frame.shape
    L = 12
    R = 28
    B = 50
    Um = height - B
    min = 50
    max = 1000
    if (range > 1000):
        range=1000
    if (range < 50):
        range=50

    U = int((Um-B)*range/(max-min))
    color = (0, int(range/(max-min)*255), 255-int(range/(max-min)*255))
    frame = cv2.rectangle(frame, (L,B), (R, U), color, -1)
    return frame

def drawState(frame,state):
    height, width, channels = frame.shape
    text = ''
    if (state == 0x01):
        text = 'MAN'
    font = cv2.FONT_HERSHEY_SIMPLEX
    org = (width-150, height-50)
    fontScale = 1
    color = (255, 0, 0)
    thickness = 2
    frame = cv2.putText(frame, text, org, font, fontScale, color, thickness, cv2.LINE_AA)
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