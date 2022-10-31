import requests
import cv2
import cmath
import numpy as np
import time


def set_resolution(url: str, index: int=1, verbose: bool=False):
    try:
        if verbose:
            resolutions = "10: UXGA(1600x1200)\n9: SXGA(1280x1024)\n8: XGA(1024x768)\n7: SVGA(800x600)\n6: VGA(640x480)\n5: CIF(400x296)\n4: QVGA(320x240)\n3: HQVGA(240x176)\n0: QQVGA(160x120)"
            print("available resolutions\n{}".format(resolutions))

        if index in [10, 9, 8, 7, 6, 5, 4, 3, 0]:
            requests.get(url + "/control?var=framesize&val={}".format(index))
        else:
            print("Wrong index")
    except:
        print("SET_RESOLUTION: something went wrong")

def set_quality(url: str, value: int=1, verbose: bool=False):
    try:
        if value >= 10 and value <=63:
            requests.get(url + "/control?var=quality&val={}".format(value))
    except:
        print("SET_QUALITY: something went wrong")

def set_awb(url: str, awb: int=1):
    try:
        awb = not awb
        requests.get(url + "/control?var=awb&val={}".format(1 if awb else 0))
    except:
        print("SET_QUALITY: something went wrong")
    return awb

def setTarget(tracker, frame):
    bbox = cv2.selectROI("Tracking", frame, False, True)
    ok = tracker.init(frame, bbox)
    return True

def rotate(frame, roll):
    (h, w) = frame.shape[:2]
    (cX, cY) = (w//2, h//2)
    M = cv2.getRotationMatrix2D((cX,cY), -roll * 180.0/cmath.pi, 1.0)
    return cv2.warpAffine(frame,M,(w,h))

def translate(frame, psi, theta):
    (h, w) = frame.shape[:2]
    x = psi*57.0/65.0*w
    y = theta*57.0/(65.0*3.0/4.0)*h
    M = np.array([
        [1,0,x],
        [0,1,y]
    ], dtype=np.float32)
    return cv2.warpAffine(frame,M,(w,h))

def stabilize(frame, ahrs, coeff):

    time_trans=time.time()
    psi_trans=0.0
    theta_trans=0.0


    now = time.time()
    ts = now - time_trans
    time_trans = now
    psi_trans += ahrs.R*ts
    psi_trans -= psi_trans*coeff
    theta_trans += ahrs.Q*ts
    theta_trans -= theta_trans*coeff

    frame = translate(frame,psi_trans,theta_trans)
    res = rotate(frame,-ahrs.phi)
    return res

