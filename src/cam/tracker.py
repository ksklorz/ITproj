import cv2


class tracker:
    def __init__(self):
        self.tracker = cv2.TrackerCSRT_create()
        self.bbox = (0,0,0,0)

    def setTarget(self,frame, bbox):
        # y1,x2,y2,x1 = bbox
        # bbox= (x1,y1, x2-x1,y2-y1)
        ok = self.tracker.init(frame, bbox)
        return True

    def update(self,frame):
        isOK, bbox = self.tracker.update(frame)
        p1 = (int(bbox[0]), int(bbox[1]))
        p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
        pc= (int(bbox[0] + bbox[2]/2), int(bbox[1] + bbox[3]/2))
        cv2.rectangle(frame, p1, p2, (0,0,255), 2, 1)
        cv2.circle(frame,pc,radius=1, color = (0,0,255), thickness = -1)
        height, width = frame.shape[:2]
        x=pc[0]/width-0.5
        y=pc[1]/height-0.5
        return isOK, bbox
