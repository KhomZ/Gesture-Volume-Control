# @author: Khom
# from operator import mod
# mediapipe is a framework used here developed by google
# here we are going to use handTracking Module consisting of Palm Detection and Hand Landmarks

import os
import cv2
import mediapipe as mp
import time

wCam, hCam = 640, 480

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

folderPath = "FingerImages"
myList = os.listdir(folderPath)
print(myList)
# prints all ['0.png', '1.png', '2.png', '3.png', '4.png', '5.png']

overlayList = []
for imPath in myList:
    image = cv2.imread(f'{folderPath}/{imPath}')
    # print(f'{folderPath}/{imPath}')
    overlayList.append(image)

print(len(overlayList))

while True:

    success, img = cap.read()

    img[0:200, 0:200] = overlayList[0]  # slicing img[0:200,0:200] height and width

    cv2.imshow("Finger Counter", img)
    # cv2.waitKey(1)

    if cv2.waitKey(1) == 13:
        break
    cv2.destroyAllWindows()