# @author: Khom
# from operator import mod
# mediapipe is a framework used here developed by google
# here we are going to use handTracking Module consisting of Palm Detection and Hand Landmarks
import cv2
import mediapipe as mp
import time


# class findHands():
class handDetector():
    def __init__(self, mode=False, maxHands=2, modelComplex=1, detectionCon=0.5, trackCon = 0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.modelComplex = modelComplex
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands, self.modelComplex, self.detectionCon, self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils

    def findHands(self, img, draw=True):
        # send RGB image to hands
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)
        # print(results.multi_hand_landmarks)  # check sth is detected or not

        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:

                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
        return img

    def findPosition(self, img, handNo=0, draw=True):

        lmList = []
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]
            # get info now each id has a corresponding landmark and landmark has x, y and z
            for id, lm in enumerate(myHand.landmark):
                # print(id, lm)
                h, w, c  = img.shape  # height, weight and channels of the image
                cx, cy = int(lm.x*w), int(lm.y*h)  # find the position of the center
                # print(id, cx, cy)
                lmList.append([id, cx, cy])

                if draw:
                    cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)
                # cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)

        return lmList


    #     cTime = time.time()
    #     fps = 1 / (cTime - pTime)
    #     pTime = cTime

    #     cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,
    #                 (255, 0, 255), 3)

    # cv2.imshow("Image", img)
    # cv2.waitKey(1)


def main():
    pTime = 0  # previous time
    cTime = 0  # current time
    detector = handDetector()
    cap = cv2.VideoCapture(0)
    # cap = cv2.VideoCapture(1)  # for third party camera

    while True:
        success, img = cap.read()
        img = detector.findHands(img)
        lmList = detector.findPosition(img)
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


if __name__ == "__main__":
    main()





# import cv2
# import mediapipe as mp
# import time
#
# # class creation
# class handDetector():
#     def __init__(self, mode=False, maxHands=2, detectionCon=0.5, modelComplexity=1, trackCon=0.5):
#         self.mode = mode
#         self.maxHands = maxHands
#         self.detectionCon = detectionCon
#         self.modelComplex = modelComplexity
#         self.trackCon = trackCon
#         self.mpHands = mp.solutions.hands
#         self.hands = self.mpHands.Hands(self.mode, self.maxHands, self.modelComplex,
#                                         self.detectionCon, self.trackCon)
#         self.mpDraw = mp.solutions.drawing_utils  # it gives small dots onhands total 20 landmark points
#
#     def findHands(self, img, draw=True):
#         # Send rgb image to hands
#         imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#         self.results = self.hands.process(imgRGB)  # process the frame
#     #     print(results.multi_hand_landmarks)
#
#         if self.results.multi_hand_landmarks:
#             for handLms in self.results.multi_hand_landmarks:
#
#                 if draw:
#                     # Draw dots and connect them
#                     self.mpDraw.draw_landmarks(img, handLms,
#                                                self.mpHands.HAND_CONNECTIONS)
#
#         return img
#
#     def findPosition(self, img, handNo=0, draw=True):
#         """Lists the position/type of landmarks
#         we give in the list and in the list ww have stored
#         type and position of the landmarks.
#         List has all the lm position"""
#
#         lmlist = []
#
#         # check whether any landmark was detected
#         if self.results.multi_hand_landmarks:
#             # Which hand are we talking about
#             myHand = self.results.multi_hand_landmarks[handNo]
#             # Get id number and landmark information
#             for id, lm in enumerate(myHand.landmark):
#                 # id will give id of landmark in exact index number
#                 # height width and channel
#                 h, w, c = img.shape
#                 # find the position
#                 cx, cy = int(lm.x*w), int(lm.y*h) # center
#                 # print(id,cx,cy)
#                 lmlist.append([id, cx, cy])
#
#                 # Draw circle for 0th landmark
#                 if draw:
#                     cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)
#
#         return lmlist
#
# def main():
#     # Frame rates
#     pTime = 0
#     cTime = 0
#     cap = cv2.VideoCapture(0)
#     detector = handDetector()
#
#     while True:
#         success, img = cap.read()
#         img = detector.findHands(img)
#         lmList = detector.findPosition(img)
#         if len(lmList) != 0:
#             print(lmList[4])
#
#         cTime = time.time()
#         fps = 1/(cTime-pTime)
#         pTime = cTime
#
#         cv2.putText(img,str(int(fps)),(10,70), cv2.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
#
#         cv2.imshow("Video", img)
#         if cv2.waitKey(1) == ord('q'):
#             break
#
#     cap.release()
#     cv2.destroyAllWindows()
#
#
# if __name__ == "__main__":
#     main()


# import cv2
# import mediapipe as mp
# import time

# class findhand():
#     def __init__(self, mode=False, maxHands=2, detectionCon=0.5
#              ,trackCon=0.5):

#         self.mode = mode
#         self.maxHands = maxHands
#         self.detectionCon = detectionCon
#         self.trackCon = trackCon

#         self.mpHands = mp.solutions.hands

#         self.hands = self.mpHands.Hands(self.mode, self.maxHands
#                                         ,self.detectionCon
#                                         ,self.trackCon)
#         self.mpDraw = mp.solutions.drawing_utils

#     def findHands(self, img, draw=True):
#         imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#         self.results = self.hands.process(imgRGB)
#         if self.results.multi_hand_landmarks:
#             for handLms in self.results.multi_hand_landmarks:
#                 if draw:
#                     self.mpDraw.draw_landmarks(img, handLms,
#                                                self.mpHands.HAND_CONNECTIONS)

#         return img

# class findFace():
#     def __init__(self, mode=False, maxFaces=1, detectionCon=0.5
#                ,trackCon=0.5):
#         self.mode = mode
#         self.maxFaces = maxFaces
#         self.detectionCon = detectionCon
#         self.trackCon = trackCon
#         self.mpFaceMesh = mp.solutions.face_mesh

#         self.face_mesh = self.mpFaceMesh.FaceMesh(self.mode
#                                                  ,self.maxFaces
#                                                  ,self.detectionCon
#                                                  ,self.trackCon)

#         self.mpDraw = mp.solutions.drawing_utils


#     def findFace(self, img, draw=True):

#         imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#         self.results = self.face_mesh.process(imgRGB)

#         if self.results.multi_face_landmarks:
#             for faceLms in self.results.multi_face_landmarks:
#                 if draw:
#                     self.mpDraw.draw_landmarks(img, faceLms,
#                                                self.mpFaceMesh.FACE_CONNECTIONS)

#         return img

# class findPose():
#     def __init__(self, mode=False, complexity=1,detectionCon=0.5,landmarks=True
#                  ,trackCon=0.5):
#         self.mode = mode
#         self.maxFace = 1
#         self.detectionCon = 0.5
#         self.trackCon = 0.5
#         self.landmarks = landmarks
#         self.complexity = complexity
#         self.mpPose = mp.solutions.pose

#         self.pose = self.mpPose.Pose(self.mode, self.complexity
#                                          ,self.detectionCon
#                                          ,self.trackCon
#                                          ,self.landmarks)
#         self.mpDraw = mp.solutions.drawing_utils

#     def findPose(self, img, draw=True):
#         imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#         self.results = self.pose.process(imgRGB)

#         if self.result.pose_landmarks:
#             PoseLms = self.results.pose_landmarks
#             mpDraw.draw_landmarks(img, PoseLms, self.mpPose.POSE_CONNECTIONS,
#                                   drawSpec, drawSpec)

#         return img

# def main():

#     cTime, pTime = 0, 0

#     hand_detector = findhand()
#     face_detector = findFace()
#     pose_detector = findPose()

#     cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)

#     while True:

#         success, img = cap.read()
#         img = face_detector.findFace(img)
#         if not success:
#             print("GPU Didn't Success At Loading Video")
#             continue

#         handlmList = hand_detector.findHands(img)

#         cTime = time.time()
#         fps = 1 / (cTime - pTime)
#         pTime = cTime

#         cv2.putText(img, str(int(fps)), (10, 70),
#                     cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
#         cv2.imshow("Detector", img)

#         if cv2.waitKey(1) != -1:
#             cv2.destroyAllWindows()
#             break


# if __name__ == "__main__":
#     main()