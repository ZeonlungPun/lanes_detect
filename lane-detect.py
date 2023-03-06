import cv2
import numpy as np
import matplotlib.pyplot as plt

def canny(img):
    gray=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    blur=cv2.GaussianBlur(gray,(5,5),0)
    canny=cv2.Canny(blur,50,150)
    return canny

def region_of_interest(img):
    height=int(img.shape[0])
    wdith=int(img.shape[1])
    triangle=np.array([[0,height],[1200,height],[647,400]],dtype=np.int32)
    mask=np.zeros_like(img)
    #input triangle :(1,3,2)
    cv2.fillPoly(mask,[triangle],255)
    mask=cv2.bitwise_and(img,mask)
    return mask

def display_lines(img,lines):
    line_img=np.zeros_like(img)
    if lines is not None:
        for line in lines:
            x1,y1,x2,y2=line.reshape(4)
            cv2.line(line_img,(x1,y1),(x2,y2),(255,0,0),10)
    return line_img

def make_coordinates(img,line_params):
    slope,intercept=line_params
    y1=img.shape[0]
    y2=int(y1*0.6)
    x1=int((y1-intercept)/slope)
    x2 = int((y2 - intercept) / slope)
    return np.array([x1,y1,x2,y2])


def average_slope_intercept(images,lines):
    left_fit=[]
    right_fit=[]
    for line in lines:
        x1,y1,x2,y2=line.reshape(4)
        parameters=np.polyfit((x1,x2),(y1,y2),1)
        slope=parameters[0]
        intercept=parameters[1]
        if slope<0:
            left_fit.append((slope,intercept))
        else:
            right_fit.append((slope,intercept))
    left_ave=np.average(left_fit,axis=0)
    right_ave=np.average(right_fit,axis=0)
    left_line=make_coordinates(images,left_ave)
    right_line=make_coordinates(images,right_ave)
    return np.array([left_line,right_line])



# img=cv2.imread("E:\\lanedetect\\images\\road4.png")
# lane_img=np.copy(img)
# can=canny(lane_img)
# cropped=region_of_interest(can)
# lines=cv2.HoughLinesP(cropped,1,np.pi/180,60,np.array([]),minLineLength=140,maxLineGap=150)
# ave_lines=average_slope_intercept(img,lines)
# line_img=display_lines(lane_img,ave_lines)
# combine=cv2.addWeighted(lane_img,0.8,line_img,1,1)
# plt.imshow(combine)
# plt.show()
# cv2.imshow('result',line_img)
# cv2.waitKey()

cap=cv2.VideoCapture("E:\\lanedetect\\videos\\dashcam2.mp4")
while True:
    _,frame=cap.read()
    lane_img=np.copy(frame)
    can = canny(lane_img)
    cropped = region_of_interest(can)
    lines = cv2.HoughLinesP(cropped, 1, np.pi / 180, 50, np.array([]), minLineLength=150, maxLineGap=120)
    ave_lines = average_slope_intercept(frame, lines)
    line_img = display_lines(lane_img, ave_lines)
    combine = cv2.addWeighted(lane_img, 0.8, line_img, 1, 1)
    cv2.imshow('result',combine)
    key=cv2.waitKey(1)
    if key==27:
        break




