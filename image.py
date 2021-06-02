import cv2
img = cv2.imread("C:\\Users\\Manvi Gupta\\Desktop\\python projects\\imageprocess\\shraddha.jpg",1)
#cv2.imshow("Camera",img)
#cv2.waitKey(20000)
#cv2.destroyAllWindows()
#resized = cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))
# resized = cv2.resize(img,(int(img.shape[1]*2),int(img.shape[2]*2)))
# cv2.imshow("image",img)
# cv2.waitKey(200000)
face_cascade = cv2.CascadeClassifier("C:\\Users\\Manvi Gupta\\Downloads\\haarcascade_frontalface_default.xml")
gray_imag = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray_imag, scaleFactor=2.05, minNeighbors=5)
print(type(faces))
print(faces)
for x,y,w,h in faces:
    img = cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0),3)
cv2.imshow("Gray",img)
cv2.waitKey(0)
cv2.destroyAllWindows()




