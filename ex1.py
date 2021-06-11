#!/usr/bin/env python3
import cv2
import sys

def open_image():
    image = cv2.imread(sys.argv[1])

    while True:
        cv2.imshow("My image", image)
        if (cv2.waitKey(1)) == ord('q'):
            break
    cv2.destroyAllWindows()

def open_video():
    video = cv2.VideoCapture(0)
    while True:
        ret, frame = video.read()
        if not ret:
            print("Unable to open camera")
            break
        cv2.imshow('CAMERA', frame)
        if cv2.waitKey(1) == ord('q'):
            break
    cv2.destroyAllWindows()

open_video()