import cv2

#Image conversion project colored image into gray scale image
path = input("Enter the Path and name of an image===")
print("You Enter this===",path)

#Now read image 
img1 = cv2.imread(path,0) #convert image into grayscale
img1 = cv2.resize(img1,(560,700))
img1 = cv2.flip(img1,0)#it accept 3 parameters 0,-1,1
cv2.imshow("converted image==",img1)
k = cv2.waitKey(0)
if k == ord("q"):
    cv2.destroyAllWindows()
    
elif k == ord("s"):
    cv2.imwrite("name-and-location-of-folder-and-output.png",img1)  #it accept name of image and data
    cv2.destroyAllWindows()
