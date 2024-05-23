#Break video into multiple images and store in a folder
import cv2

vidcap = cv2.VideoCapture("C:\\Users\\LENOVO\\Desktop\\Image processing and Computer Vision\\test2.mp4")
ret,image=vidcap.read()
count=0
while True:
    if ret == True:
        cv2.imwrite("C:\\Users\\LENOVO\\Desktop\\Image processing and Computer Vision\\frames\\imgN%d.jpg"%count, image)
        vidcap.set(cv2.CAP_PROP_POS_MSEC,(count**100))
        ret,image = vidcap.read()
        cv2.imshow("ret", image)
        count+=1
        if cv2.waitKey(1)& 0xFF == ord("x"):
            break
            cv2.destroyAllWindows()
            
vidcap.release()
cv2.destroyAllWindows()