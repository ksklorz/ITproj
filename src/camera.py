import cv2
from cam import hud
from cam.video_lib import *


def camThread():
    URL = "http://192.168.137.118"
    AWB = True
    phi=0
    theta=0
    cap = cv2.VideoCapture(0)
    # cap = cv2.VideoCapture(URL + ":81/stream")
    
    while True:
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

        elif key == ord('s'):
                cv2.imwrite('F:\PS\IT\image.jpg', frame) 

        elif key == 27:
                break