import numpy as np
import cv2

cap = cv2.VideoCapture(r'E:\gfdata\Video\09\29.mp4')

while (cap.isOpened()):
    ret, frame = cap.read()
    cv2.imshow('frame', frame)
    if cv2.waitKey(40) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
