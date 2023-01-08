import struct
from dataclasses import dataclass
from numpy import int16, int8, uint16, uint8, uint32, int32

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
    range: int16 = 0
    # smiec: int16 = 0 #?????

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
    range: float = 0.0

@dataclass
class controlData:
    on: bool = True
    up: float = 0.0
    right: float = 0.0

@dataclass
class trackData:
    on: bool = True
    pitch: float = 0.0
    yaw: float = 0.0

@dataclass
class frame:
    cmd: uint8 = 0
    x: float = 0.0
    y: float = 0.0
    crc: uint8 = 0

def prepareControl(input):
    data = controlData
    data.cmd = 1
    data.x = input.up
    data.y = input.right
    data.cnt = 0
    data.crc = 0
    return data

def prepareTracking(input):
    data = trackData
    data.cmd = 2
    data.x = input.pitch
    data.y = input.yaw
    data.cnt = 1
    data.crc = 0
    return data