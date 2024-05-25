#detecting selected color in video  

import cv2
import numpy as np

cap = cv2.VideoCapture(0)
while True:
    ret,frame = cap.read()
    frame = cv2.resize(frame,(400,400))
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
   
    l_v = np.array([21,70,80])
    u_v = np.array([61,255,255])
    
    #Creating Mask
    mask = cv2.inRange(hsv, l_v, u_v)
    #filter mask with image
    res = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("res", res)

    key = cv2.waitKey(25)
    if key == 27:
        break
cap.release()
cv2.destroyAllWindows()