#detect color in image

import cv2
import numpy as np

frame = cv2.imread(r"C:\color_balls.jpg")

while True:
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    #l_v = np.array([110,50,50])  blue 
    #u_v = np.array([130,235,225])
    
    l_v = np.array([20,139,143]) #green and yellow
    u_v = np.array([48,255,248])
    
    #creating mask
    mask = cv2.inRange(hsv, l_v, u_v)
    
    #filter mask with image
    res = cv2.bitwise_and(frame, frame,mask = mask)
    
    cv2.imshow("Frame",frame)
    cv2.imshow("Mask",mask)
    cv2.imshow("res",res)
    
    key = cv2.waitKey(1)
    if key == 27:
        break

cv2.destroyAllWindows()
