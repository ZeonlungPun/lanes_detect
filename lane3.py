import cv2
import numpy as np
from cvzone.ColorModule import ColorFinder



hsv_values={'hmin': 8, 'smin': 119, 'vmin': 106, 'hmax': 255, 'smax': 210, 'vmax': 206}
colorFinder=ColorFinder(True)
while True:

    frame=cv2.imread("E:\\opencv\\lanedetect\\test_image.jpg")

    imgColor,mask=colorFinder.update(frame,hsv_values)

    edges = cv2.Canny(mask, 200, 250)
    lines=cv2.HoughLinesP(edges,1,np.pi/180,50,maxLineGap=0)
    if lines is not None:
        for line in lines:
            x1,y1,x2,y2=line[0]
            cv2.line(frame,(x1,y1),(x2,y2),(0,255,0),5)

    cv2.imshow("frame", imgColor)
    cv2.imshow("mask",mask)

    key=cv2.waitKey(50)





