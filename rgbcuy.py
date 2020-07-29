import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # orange color
    low_orange = np.array([0, 50, 80])
    upper_orange = np.array([20,255,255])
    orange_mask = cv2.inRange(hsv_frame, low_orange, upper_orange)
    orange = cv2.bitwise_and(frame, frame, mask=orange_mask)

    cv2.imshow("Frame", frame)
    cv2.imshow("Orange", orange)
    key = cv2.waitKey(1)
    if key == 27:
        break
