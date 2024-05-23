import cv2
import numpy as np

img = cv2.imread("path of image.png")
img = cv2.resize(img,(600,700))

#Creating Blank Image/White Image---
#img = np.zeros([512, 512, 3], np.uint8)*255  #create window of an black screen
#img = np.ones([512,512,3], np.uint8)*255 #For white screen

#here line accept 5 parameters (img,starting,ending,color,thickness)
img = cv2.line(img, (0,0), (200,200), (254,7,31),8)

#here arrowedLine accept 5 parameters (img,starting,ending,color,thickness)
img = cv2.arrowedLine(img, (23,125), (380,300), (255,0,125),8)

#here rectangle accept 5 parameters (img,starting,ending,color,thickness)
img = cv2.rectangle(img, (384,10), (510,128), (254,7,254),8)

#here rectangle accept 5 parameters (img,starting,ending,color,fill)
img = cv2.rectangle(img, (520,138), (620,238), (254,7,254),-1)

#here circle accept 5 parameters (img,start_co,radius,color,thickness)
img = cv2.circle(img,(447,125),63,(214,255,0),5)

font = cv2.FONT_HERSHEY_COMPLEX
#putting text - puttext accept (img,text,start_co,font,fontsize,color,thickness,linetype)
img = cv2.putText(img, "Hello", (20,500), font, 4, (0,125,255),10,cv2.LINE_AA)

#ellipse-accept(img,start_cor,(length,height),color,thickness)
img = cv2.ellipse(img,(400,600),(100,50),0,0,270,155,5)

pts = np.array([[100,150],[200,30],[170,20],[50,10]], np.int32)
pts = pts.reshape((-1,1,2))
img = cv2.polylines(img,[pts],True,(0,255,155))

cv2.imshow("res",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
