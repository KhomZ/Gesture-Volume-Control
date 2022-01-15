# @author: Khom
import cv2
import mediapipe as mp
import time


cap = cv2.VideoCapture(0)


class handDetector():
    def __init__(self, mode=False, maxHands=2, detectionCon=0.5, trackCon=0.5):
    # def __init__(self, mode=False, maxHands=2, complexity=1, detectionCon=0.5, trackCon= 0.5):
        self.mode = mode
        self.maxHands = maxHands
        # self.complexity = complexity
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands,
                                        self.detectionCon, self.trackCon)
        # self.hands = self.mpHands.Hands(self.mode, self.maxHands, self.complexity,
        #                                 self.detectionCon, self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils


    def findHands(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = self.hands.process(imgRGB)
        # print(results.multi_hand_landmarks)  # check sth is detected or not

        if results.multi_hand_landmarks:
            for handLms in results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms,
                                               self.mpHands.HAND_CONNECTIONS)
        return img

                # # get info now each id has a corresponding landmark and landmark has x, y and z
                # for id, lm in enumerate(handLms.landmark):
                #     # print(id, lm)
                #     h, w, c = img.shape  # height, weight and channels of the image
                #     cx, cy = int(lm.x * w), int(lm.y * h)  # find the position of the center
                #     print(id, cx, cy)
                #     # if id == 0:
                #     #     cv2.circle(img, (cx, cy), 25, (255, 0, 255), cv2.FILLED)
                #     if id == 4:
                #         cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)
                #     # cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)


def main():
    pTime = 0  # previous time
    cTime = 0  # current time

    cap = cv2.VideoCapture(0)
    # cap = cv2.VideoCapture(1)

    detector = handDetector()

    while True:
        success, img = cap.read()
        img = detector.findHands(img)

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,
                    (255, 0, 255), 3)

        cv2.imshow("Image", img)
        if cv2.waitKey(1) == 13:
            break
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
