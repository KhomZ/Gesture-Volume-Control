# @author: Khom
import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)
# cap = cv2.VideoCapture(1)

mpHands = mp.solutions.hands
hands = mpHands.Hands()


while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    print(results.multi_hand_landmarks)  # check sth is detected or not

    cv2.imshow("Image", img)
    cv2.waitKey(1)
