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