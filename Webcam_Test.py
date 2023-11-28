import cv2

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
img = cv2.imread("news.jpg") 
#grayscale makes it easier to detect faces
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#converts image to grayscale while leaving original intact
faces =face_cascade.detectMultiScale(gray_img,
scaleFactor = 1.5,
minNeighbors = 5)
for x,y,w,h in faces:
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
cv2.imshow("Gray",img)
cv2.waitKey()
cv2.destroyAllWindows()