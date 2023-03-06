import cv2
import numpy as np

#video=cv2.VideoCapture("E:\\opencv\\lanedetect\\videos\\dashcam6.mp4")
video = cv2.VideoCapture("E:\\opencv\\lanedetect\\videos\\test2.mp4")
def empty(a):
    pass

# cv2.namedWindow("HSV")
# cv2.createTrackbar("HUE Min","HSV",0,179,empty)
# cv2.createTrackbar("SAT Min","HSV",0,255,empty)
# cv2.createTrackbar("VALUE Min","HSV",0,255,empty)
# cv2.createTrackbar("HUE Max","HSV",0,179,empty)
# cv2.createTrackbar("SAT Max","HSV",0,255,empty)
# cv2.createTrackbar("VALUE Max","HSV",0,255,empty)

#yellow {'hmin': 5, 'smin': 140, 'vmin': 83, 'hmax': 14, 'smax': 224, 'vmax': 255}
#white {'hmin': 0, 'smin': 0, 'vmin': 141, 'hmax': 69, 'smax': 21, 'vmax': 255}
# {'hmin': 7, 'smin': 0, 'vmin': 96, 'hmax': 18, 'smax': 15, 'vmax': 206}
while True:
    ret,ori_frame=video.read()

    if not ret:
        video = cv2.VideoCapture("E:\\opencv\\lanedetect\\videos\\test2.mp4")
        #video = cv2.VideoCapture("E:\\opencv\\lanedetect\\videos\\dashcam6.mp4")
        continue
    frame=cv2.GaussianBlur(ori_frame,(5,5),0)




    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    low = np.array([7,0,96])
    up = np.array([18,15,206])
    mask = cv2.inRange(hsv, low, up)
    edges = cv2.Canny(mask, 300, 350)
    lines=cv2.HoughLinesP(edges,1,np.pi/180,50,maxLineGap=1000,minLineLength=150)
    if lines is not None:
        for line in lines:
            x1,y1,x2,y2=line[0]
            cv2.line(frame,(x1,y1),(x2,y2),(0,255,0),5)

    cv2.imshow("frame", frame)
    cv2.imshow("mask",mask)

    key=cv2.waitKey(20)
    if key==27:
        break
video.release()
cv2.destroyAllWindows()



