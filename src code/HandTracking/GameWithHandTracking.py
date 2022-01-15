import cv2
import mediapipe as mp
import time
import HandTrackingModule as htm

pTime = 0  # previous time
cTime = 0  # current time
detector = htm.handDetector()
cap = cv2.VideoCapture(0)
# cap = cv2.VideoCapture(1)  # for third party camera

while True:
    success, img = cap.read()
    img = detector.findHands(img, draw=False)
    lmList = detector.findPosition(img, draw=False)
    if len(lmList) != 0:
        print(lmList[4])  # 4 is the tip of the Thumb

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,
                (255, 0, 255), 3)

    cv2.imshow("Image", img)
    if cv2.waitKey(1) == 13:
        break
cap.release()
cv2.destroyAllWindows()