import cv2

cap = cv2.VideoCapture(0)#external cam 1 and laptop 0
print(cap)

fourcc = cv2.VideoWriter_fourcc(*"XVID") 
output = cv2.VideoWriter("C:\\Users\\LENOVO\\Desktop\\Image processing and Computer Vision\\output.avi",fourcc,20.0,(640,480))

while cap.isOpened():
    ret,frame = cap.read()#give two values one is bool and second is frame
    if ret == True:
        cv2.imshow("frame", frame)
        #frame = cv2.flip(frame,0)
        output.write(frame)
        if cv2.waitKey(1) & 0xFF == ord("x"):
            break
cap.release()
output.release()
cv2.destroyAllWindows()