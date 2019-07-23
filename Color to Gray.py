import cv2

img = cv2.imread("photo.jpg", 0)

resize_img = cv2.resize(img, (400, 600))
cv2.imshow("Gray Image", resize_img)
cv2.imwrite("Gray Image.jpg", resize_img)
cv2.waitKey(0)
