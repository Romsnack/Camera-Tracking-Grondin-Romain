#!/usr/bin/env python3
import cv2
import sys
import mediapipe as mp

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

def detect_hand():
    cam = cv2.VideoCapture(0)
    mpHand = mp.solutions.hands
    hands = mpHand.Hands()
    while True:
        ret, frame = cam.read()
        if not ret:
            print("unable to open camera")
            break
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb)
        print(results.multi_hand_landmarks)
        cv2.imshow("Camera", frame)
        if cv2.waitKey(1) == ord('q'):
            break
    cv2.destroyAllWindows()

def draw_plan():
    cam = cv2.VideoCapture(0)
    mpHand = mp.solutions.hands
    hands = mpHand.Hands()
    mpDraw = mp.solutions.drawing_utils
    while True:
        ret, frame = cam.read()
        if not ret:
            print("unable to open camera")
            break
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb)
        # print(results.multi_hand_landmarks)
        if results.multi_hand_landmarks:
            for handlms in results.multi_hand_landmarks:
                for id, lm in enumerate(handlms.landmark):
                    h, w, c = frame.shape
                    x, y = int(lm.x * w), int(lm.y * h)
                mpDraw.draw_landmarks(frame, handlms)
                cv2.imshow("Camera", frame)
                if cv2.waitKey(1) == ord('q'):
                    break
        if cv2.waitKey(1) == ord('q'):
            break
    cv2.destroyAllWindows()

draw_plan()