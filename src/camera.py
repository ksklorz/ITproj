import cv2
from cam import hud
from cam.video_lib import *
from globals import *
from cam import video_lib
import tlm
from cam import detect

def camThread():
    URL = "http://192.168.137.77"
    AWB = True
    phi=0
    theta=0
    ahrs = tlm.dataAHRS(0,0,0,0,0,0,0,0,0,0)
#     cap = cv2.VideoCapture(0)
    cap = cv2.VideoCapture(URL + ":81/stream")
    set_resolution(URL, index=8, verbose=True)
    stab = video_lib.stabilization()
    target = video_lib.targetInd()

#     encodeListKnown, names = detect.importPhoto()

    while True:
        while not udpRecQue.empty():
            ahrs = udpRecQue.get()
            # ahrs = tlm.dataAHRS(ahrs)
            phi = ahrs.phi*57.0
            theta = ahrs.theta*57.0


        if cap.isOpened():
                ret, frame = cap.read()
                # frame = hud.drawHor(frame,-theta,-phi)

                        # frame2 = frame
                if (isRecognizing):
                        facesCurFrame, encodesCurFrame = detect.recognition(frame, isIdent)
                        for faceLoc in facesCurFrame:
                                detect.drawRec(frame, faceLoc, (0,255,0))
                        if isIdent:
                                for encodeFace,faceLoc in zip(encodesCurFrame,facesCurFrame):
                        
                                        id, tar = detect.identification(encodeFace, encodeListKnown)
                                        if tar:
                                                text = names[id].upper()
                                                print (text)
                                                detect.drawRec(frame,faceLoc,(255,0,0))
                                                # targetSet, tracker = setTarget(frame, faceLoc)
                                                break        
                
                frame2 = target.refresh(frame)
                if stabCoeff.isStab:
                        frame2 = stab.stabilize(frame2,ahrs,stabCoeff.coeff)
                # frame2 = frame

                cv2.imshow("frame", frame2)
            
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