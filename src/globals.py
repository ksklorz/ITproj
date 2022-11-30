import threading
import queue

cmdGui = queue.Queue(maxsize=20)

udpRecQue = queue.Queue(maxsize= 10)
udpSendQue = queue.Queue(maxsize= 20)
conVidQue = queue.Queue(maxsize= 50)

isRecognizing = False
isIdent = False


class stabCoeff:
    isStab = False
    coeff = .5
    def __init__(self):
        self.isStab = False
        self.coeff = .5
        self.lock = threading.Lock()


