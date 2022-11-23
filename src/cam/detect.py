import cv2
import face_recognition
import numpy as np
import os

def getFile(path):
    DATA = []
    with open(path) as f:
        for line in f:
            data = line.strip().split(";")
            DATA.append(data)
    return DATA

def getImages(path, lines):
    images = []
    names = []
    for person in lines:
        photo = person[0]
        curImg = cv2.imread(path+photo)
        images.append(curImg)
        names.append(person[1])
    return images, names
    
def findEncodings(images):
    encodelist= []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodelist.append(encode)
    return encodelist

def recognition(frame, encode):
    # frame = cv2.resize(frame, (0,0), None, 0.25,0.25)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    facesCurFrame = face_recognition.face_locations(frame)
    if encode:
        encodesCurFrame = face_recognition.face_encodings(frame,facesCurFrame)
    else:
        encodesCurFrame = []
    return facesCurFrame, encodesCurFrame

def identification(encodeFace, knownFaces):
    matches = face_recognition.compare_faces(knownFaces,encodeFace)
    faceDis = face_recognition.face_distance(knownFaces,encodeFace)
    matchIndex = np.argmin(faceDis)
    return matchIndex, matches[matchIndex]

def drawRec(frame, loc, col):
    y1,x2,y2,x1 = loc
    cv2.rectangle(frame,(x1,y1),(x2,y2),col,2)


def importPhoto():
    # path = os.getcwd()
    path = "data\\"
    lines = getFile(path + "data.txt")
    images, names = getImages(path, lines)
    encodeList = findEncodings(images)
    print('Encoding Complete')
    return encodeList, names