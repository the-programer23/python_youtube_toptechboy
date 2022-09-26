import cv2
print(cv2.__version__)
import mediapipe as mp
width=1280
height=720
hands=mp.solutions.hands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.5, 
    min_tracking_confidence=0.5)
mpDraw=mp.solutions.drawing_utils
def parseLandmarks(frame):
    myHands=[]
    frameRGB=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    results=hands.process(frameRGB)
    if results.multi_hand_landmarks != None:
        for handLandmarks in results.multi_hand_landmarks:
            myHand=[]
            for landmark in handLandmarks.landmark:
                myHand.append((int(landmark.x*width),int(landmark.y*height)))
            myHands.append(myHand)
    return myHands                

cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))

while True:
    ignore,  frame = cam.read()
    myHands=parseLandmarks(frame)
    for myHand in myHands:
        for digit in [8,12,16,20]:
            cv2.circle(frame,myHand[digit],10,(255,0,255),1)
    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam',0,0)
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
cam.release()