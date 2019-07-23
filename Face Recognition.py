import cv2

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

img = cv2.imread("IMG_20190210_221547.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray,
scaleFactor=1.6,
minNeighbors=5)

for x, y, w, h in faces:
    img = cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0, 0), 10)

print(faces)

rs = cv2.resize(img, (800, 400))

cv2.imshow("Gray", rs)
cv2.waitKey(0)
