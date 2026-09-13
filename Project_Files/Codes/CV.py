import cv2
import numpy as np

#cv2.resize('Bleu.mp4')
cap = cv2.VideoCapture('Bleu.mp4')

l = np.array([90,  0,   0])
u = np.array([125, 180, 100])
kernel = np.ones((5,5),np.uint8)

while cap.isOpened():

    ret, frame = cap.read()

    if ret:

        """frame = cv2.resize(frame, ...)  """      

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, l, u)

        M = cv2.moments(mask, True)
        if M["m00"] != 0:
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            cv2.circle(frame, (cX, cY), 10, (0, 0, 255), -1)

        mask = cv2.erode(mask, kernel)
        mask = cv2.dilate(mask, kernel)

        cv2.imshow("Test",mask)
   
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

#faire image 50% plus petite comblé les ... avec la page sur opéra(tcheker l'historique)