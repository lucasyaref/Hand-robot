import cv2
import numpy as np

def empty(i):
    pass


cap = cv2.VideoCapture(0)
cv2.namedWindow("TrackedBars")
cv2.resizeWindow("TrackedBars", 640, 240)


def on_trackbar(val):
    hue_min = cv2.getTrackbarPos("Y Min", "TrackedBars")
    hue_max = cv2.getTrackbarPos("Y Max", "TrackedBars")
    sat_min = cv2.getTrackbarPos("Cr Min", "TrackedBars")
    sat_max = cv2.getTrackbarPos("Cr Max", "TrackedBars")
    val_min = cv2.getTrackbarPos("Cb Min", "TrackedBars")
    val_max = cv2.getTrackbarPos("Cb Max", "TrackedBars")

    lower = np.array([hue_min, sat_min, val_min])
    upper = np.array([hue_max, sat_max, val_max])

    imgMASK = cv2.inRange(imgHSV, lower, upper)

    cv2.imshow("Output1", img)
    cv2.imshow("Output2", imgHSV)
    cv2.imshow("Mask", imgMASK)


cv2.createTrackbar("Y Min", "TrackedBars", 0, 255, on_trackbar)
cv2.createTrackbar("Y Max", "TrackedBars", 255, 255, on_trackbar)
cv2.createTrackbar("Cr Min", "TrackedBars", 0, 255, on_trackbar)
cv2.createTrackbar("Cr Max", "TrackedBars", 255, 255, on_trackbar)
cv2.createTrackbar("Cb Min", "TrackedBars", 0, 255, on_trackbar)
cv2.createTrackbar("Cb Max", "TrackedBars", 255, 255, on_trackbar)

#img = cv2.imread(path)
while(cap.isOpened()):
    ret, img = cap.read()
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
    # Show some stuff
    on_trackbar(0)
    # Wait until user press some key
    cv2.waitKey()

