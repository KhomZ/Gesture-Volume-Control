# @author: Khom
# from operator import mod
# mediapipe is a framework used here developed by google
# here we are going to use handTracking Module consisting of Palm Detection and Hand Landmarks

import os
import cv2
import time
import HandTrackingModule as htm

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
pTime = 0

detector = htm.handDetector(detectionCon=0.75)

tipIds = [4, 8, 12, 16, 20]  # 4-8-12-16-20 thumb, index, middle, ring and pinky fingers resp


while True:

    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)
    # print(lmList)

    if len(lmList) != 0:
        fingers = []

        # Thumb
        if lmList[tipIds[0]][1] < lmList[tipIds[0] - 1][1]:
            fingers.append(1)
        else:
            fingers.append(0)

        # 4 Fingers except thumb
        for id in range(1, 5):
            if lmList[tipIds[id]][2] < lmList[tipIds[id]-2][2]:
                fingers.append(1)
            else:
                fingers.append(0)

            # if lmList[8][2] < lmList[6][2]:
            #     print("Index finger open")

        # print(fingers)
        totalFingers = fingers.count(1)
        print(totalFingers)

        h, w, c = overlayList[totalFingers].shape
        img[0:h, 0:w] = overlayList[totalFingers]

        # depends on where your finger images' are positioned in your directory
        # eg. [0]=>img of finger 1,
        # [1]=>img of finger 2,
        # [2]=>img of finger 3,
        # [3]=>img of finger 4,
        # [4]=>img of finger 5,
        # [5]=>img of finger 0 i.e. fist here
        # h, w, c = overlayList[totalFingers-1].shape
        # img[0:h, 0:w] = overlayList[totalFingers-1]

    # h, w, c = overlayList[2].shape
    # img[0:h, 0:w] = overlayList[2]
    # h, w, c = overlayList[0].shape
    # img[0:h, 0:w] = overlayList[0]

    # # img[0:200, 0:200] = overlayList[0]
    # img[0:228, 0:221] = overlayList[0]  # slicing img[0:200,0:200] height and width
    # # img[100:328, 100:321] = overlayList[0]

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, f'FPS: {int(fps)}', (400, 70), cv2.FONT_HERSHEY_PLAIN,
                3, (255, 0, 0), 3)  # font, scale, color, thickness
    cv2.imshow("Finger Counter", img)
    # cv2.waitKey(1)

    if cv2.waitKey(1) == 13:
        break
    # cv2.destroyAllWindows()
