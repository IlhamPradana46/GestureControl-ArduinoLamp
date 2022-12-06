import cv2
import controller as cnt
from cvzone.HandTrackingModule import HandDetector

detector = HandDetector(detectionCon=0.6, maxHands=1)

video = cv2.VideoCapture(0)

while True:
    ret,frame=video.read()
    hands,img=detector.findHands(frame)

    if hands:
        
        lmList = hands[0]
        fingerUp = detector.fingersUp(lmList)

        finger = fingerUp

        cnt.ledActivate(finger)

    cv2.imshow("Frame", frame)
    k = cv2.waitKey(1)
    if k == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
