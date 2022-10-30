# a python program to send an initial packet, then listen for packets from the ESP32
# the laptop/rasp pi that this code runs on can still be connected to the internet, but should also "share" its connection by creating its own mobile hotspot
# this version of the code allows your laptop to remain connected to the internet (which is a postive)
# but requires configuring your laptop to share its internet connection (which can be a negative because it is tricky to set up depending on your OS)
# for version that does not require sharing an internet connection, see https://gist.github.com/santolucito/70ecb94ce297eb1b8b8034f78683447b 
import cv2
import socket
import hud
from video_lib import * 
import sys

from types import DynamicClassAttribute
# UDP_IP = "192.168.137.72" 
UDP_PORT = 31337
UDP_REC_PORT = 31338
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Internet  # UDP
# sock.connect((UDP_IP, UDP_PORT))
sock.bind(('', UDP_REC_PORT))
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
sock.setblocking(0)


# camera:
URL = "http://192.168.137.118"
AWB = True


def main():
    x = 25
    y = 2
    dx = 0
    dy = 0
    phi=0
    theta=0
    cap = cv2.VideoCapture(0)
    cap = cv2.VideoCapture(URL + ":81/stream")
    while True:
        try:
            while True:
                line = sock.recv(1024)
        except:
            data = hud.tlmAHRS()
            data = hud.encodeTlm(line)
            phi = float(data.phi)/10000.0*57.0
            theta = float(data.theta)/10000.0*57.0
        
            phi=phi
            theta=theta

        if cap.isOpened():
            ret, frame = cap.read()
            frame = hud.drawHor(frame,-theta,-phi)
            cv2.imshow("frame", frame)
            
        key = cv2.waitKey(1)

        if key == ord('r'):
                idx = int(input("Select resolution index: "))
                set_resolution(URL, index=idx, verbose=True)

        elif key == ord('q'):
                val = int(input("Set quality (10 - 63): "))
                set_quality(URL, value=val)

        elif key == ord('a'):
                AWB = set_awb(URL, AWB)

        # elif key == ord('n'):
        #         tracking = setTarget(tracker, frame)
        elif key == ord('s'):
                cv2.imwrite('F:\PS\IT\image.jpg', frame) 

        elif key == 27:
                break








if __name__ == "__main__":
    # sock.send('Hello ESP32'.encode())
    main()