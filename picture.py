import cv2

face_haar_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

image = cv2.imread(r"C:\Users\Daniel Terwase Ajayi\PycharmProjects\pythonProject33\Daniel.jpg")

grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

faces = face_haar_cascade.detectMultiScale(grey, 1.1, 4)
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 5)

cv2.imshow("Faces", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

