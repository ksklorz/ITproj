import requests
import cv2
import cmath
import numpy as np
import time
from globals import *
from cam import tracker


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
class stabilization:
    def __init__(self):
        self.time_trans = time.time()
        self.psi_trans = 0.0
        self.theta_trans = 0.0


    def stabilize(self, frame, ahrs, coeff):
        now = time.time()
        ts = now - self.time_trans
        self.time_trans = now
        self.psi_trans += ahrs.R*ts
        self.psi_trans -= self.psi_trans*coeff
        self.theta_trans += ahrs.Q*ts
        self.theta_trans -= self.theta_trans*coeff

        frame = translate(frame,-self.psi_trans,self.theta_trans)
        res = rotate(frame,-ahrs.phi)
        return res

class targetInd:
    def __init__(self):
        self.x = 0.0
        self.y = 0.0
        self.w = .07
        self.h = self.w /3.0*4.0
        self.track = tracker.tracker()
        self.isTracking = False
    
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        self.x = min(self.x,1.0-self.w)
        self.x = max(self.x,-1.0+self.w)
        self.y = min(self.y,1.0-self.h)
        self.y = max(self.y,-1.0+self.h)

    def show(self, track, frame):
        (h, w) = frame.shape[:2]
        w = float(w)/2.0
        h = float(h)/2.0
        mX = w*self.x + w
        mY = h*self.y + h
        
        startP = (int(mX + self.w*w), int(mY + self.h*h))
        endP = (int(mX - self.w*w), int(mY - self.h*h))

        if True:#not track:
            frame = cv2.rectangle(frame, startP, endP, (0,255,0), 2)
        # else:
        #     frame = cv2.rectangle(frame, startP, endP, (0,255,0), 2)
        
        return frame

    def refresh(self, frame):
            coeff = .015
            track = False
            while not conVidQue.empty():
                data = conVidQue.get()

                if data.on:
                    self.isTracking = True
                    bbox = self.getbbox(frame)
                    self.track.setTarget(frame,bbox)
                # else:
                self.move(data.up*coeff, data.right*coeff)
                    # track = data.on
                
            if self.isTracking:
                track, bbox = self.track.update(frame)
                # if track:
                #     self.movebbox(frame,bbox)
                self.isTracking = track

            return self.show(self.isTracking, frame)

    def getbbox(self,frame):
        (h, w) = frame.shape[:2]
        w = float(w)/2.0
        h = float(h)/2.0
        mX = w*self.x + w
        mY = h*self.y + h
        L = int(mX-self.w*w)
        D = int(mY-self.h*h)
        WW = int(2*self.w*w)
        HH = int(2*self.h*h)
        bbox = (L,D,WW, HH)
        return bbox

    def movebbox(self,frame,bbox):
        (h, w) = frame.shape[:2]
        
        # (L,D,W,H) = bbox
        L= bbox[0]
        D = bbox[1]
        W = bbox[2]
        H = bbox[3]
        self.x = L/w
        self.h = D/h
        self.w = W/w
        self.h = H/h
