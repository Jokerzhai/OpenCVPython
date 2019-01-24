import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(True):
    # capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame', gray)
    if cv2.waitkey(1) & 0xFF == ord('q'):
        break
    # when everything done,release the capture
    cap.release()
    cv2.destoryAllWindows()