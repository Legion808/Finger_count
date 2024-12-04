import cv2
import mediapipe as mp
import time


class HandDetector:
    def __init__(self, mode=False, maxHands=2, detectioncon=0.5, trackcon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectioncon = detectioncon
        self.trackcon = trackcon

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(
            static_image_mode=self.mode,
            max_num_hands=self.maxHands,
            min_detection_confidence=self.detectioncon,
            min_tracking_confidence=self.trackcon
        )
        self.mpDraw = mp.solutions.drawing_utils

        # Qo'l nuqtalari tartibi (barmoqning bukilgan yoki ochilganligini aniqlash uchun)
        self.tipIds = [4, 8, 12, 16, 20]  # Bosh barmoq va boshqa barmoqlar uchlari

    def findHands(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)

        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)

        return img

    def findPosition(self, img, handNo=0, draw=True):
        lmList = []
        if self.results.multi_hand_landmarks and handNo < len(self.results.multi_hand_landmarks):
            myHand = self.results.multi_hand_landmarks[handNo]
            for id, lm in enumerate(myHand.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmList.append((id, cx, cy))
                if draw and id in self.tipIds:
                    cv2.circle(img, (cx, cy), 10, (255, 0, 255), cv2.FILLED)
        return lmList

    def fingersUp(self, lmList):
        fingers = []
        if not lmList:
            return fingers
        # Bosh barmoq
        if lmList[self.tipIds[0]][1] > lmList[self.tipIds[0] - 1][1]:
            fingers.append(1)  # Ochiq
        else:
            fingers.append(0)  # Yopiq

        # Qolgan to'rtta barmoq
        for id in range(1, 5):
            if lmList[self.tipIds[id]][2] < lmList[self.tipIds[id] - 2][2]:
                fingers.append(1)  # Ochiq
            else:
                fingers.append(0)  # Yopiq

        return fingers


def main():
    cap = cv2.VideoCapture(0)
    detector = HandDetector()
    pTime = 0

    while cap.isOpened():
        success, img = cap.read()
        if not success:
            print("Kamera ochilmadi!")
            break

        img = detector.findHands(img)
        totalFingers = 0

        if detector.results.multi_hand_landmarks:
            for handNo in range(len(detector.results.multi_hand_landmarks)):
                lmList = detector.findPosition(img, handNo)
                fingers = detector.fingersUp(lmList)
                totalFingers += sum(fingers)

        # Ekranga ko‘rsatilgan sonni chiqarish
        cv2.putText(img, str(totalFingers), (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 255, 0), 5)

        # FPS hisoblash
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        cv2.putText(img, f'FPS: {int(fps)}', (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

        cv2.imshow("Qo'l Aniqlash", img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
