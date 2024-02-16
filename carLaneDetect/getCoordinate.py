import cv2
from pylab import *
from PIL import Image
import sys
import copy


input_img = input("please input video path：")



# 例如E:\demo\1.jpg

def rgb2hex(rgb_list):
    # rgb_list = bgr_list[::-1]
    # print(rgb_list)
    res = "#"
    for a in rgb_list:
        a_hex = hex(a)
        if a < 16:
            res += "0"
            res += a_hex[2:]
        else:
            res += a_hex[2:]
    return res

def video_flag():
    frame = 0
    cap = cv2.VideoCapture(input_img)
    fps = cap.get(cv2.CAP_PROP_FPS)
    print("fps: ", fps)

    def on_EVENT_LBUTTONDOWN(event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:

            xy = "%d,%d" % (x, y)
            cv2.circle(frame, (x - 1, y - 1), 1, (255, 0, 0), thickness=-1)
            cv2.putText(frame, xy, (x + 10, y + 10), cv2.FONT_HERSHEY_PLAIN,
                        3.0, (0, 0, 0), thickness=3)
            print("x:{},y:{}".format(x, y))
            bgr_list = frame[y, x]
            rgb_list = bgr_list[::-1]
            print("RGB: ", rgb_list)
            print("colour：", rgb2hex(rgb_list))
            print("--" * 20)
            cv2.imshow("video", frame)

    cv2.namedWindow('video', cv2.WINDOW_NORMAL)
    cv2.setMouseCallback("video", on_EVENT_LBUTTONDOWN)

    while (True):
        ret, frame = cap.read()
        cv2.imshow("video", frame)
        c = cv2.waitKey(0)
        if c == 27:
            break
    cap.release()
    cv2.destroyAllWindows()





video_flag()



