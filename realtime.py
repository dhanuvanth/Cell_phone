from cv2 import cv2
import time

cap = cv2.VideoCapture(0)

display_window = cv2.namedWindow("Cell phone")

face_cascade = cv2.CascadeClassifier(r'classifier\cell_phone.xml')

time.sleep(1)

while(True):
    
    ret,image = cap.read()

    #FACE DETECTION STUFF
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)

    #DISPLAY TO WINDOW
    cv2.imshow("Cell phone", image)
    key = cv2.waitKey(1)

    if key == 27:
        cap.release()
        cv2.destroyAllWindows()
        break
