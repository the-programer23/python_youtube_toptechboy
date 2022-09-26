import cv2
import mediapipe as mp
print(cv2.__version__)

width=640
height=360

cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))

#false is passed when we want to detect hands from the camera and we pass true to analize a a static image
#2 was passed because we want to detect 2 hands only
#.5 because 
#.5 level of confidence in tracking
# hands=mp.solutions.hands.Hands(False,2,.5,.5)
hands=mp.solutions.hands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.5, 
    min_tracking_confidence=0.5)
mpDraw=mp.solutions.drawing_utils

while True:
    myHands=[]
    ignore,  frame = cam.read()
    frameRGB=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    results=hands.process(frameRGB)
    # != None means that a hand was found
    if results.multi_hand_landmarks != None:
        # results.multi_hand_landmarks is an array with one element which has 21 landmark objects
        for handLandMarks in results.multi_hand_landmarks:
            # handLandMarks is a class with 21 objects
            myHand = []
            # mpDraw.draw_landmarks(frame,handLandMarks) to draw dots only
            # mpDraw.draw_landmarks(frame,handLandMarks,mp.solutions.hands.HAND_CONNECTIONS) # to draw dots and connections
            for Landmark in handLandMarks.landmark:
                myHand.append((int(Landmark.x*width),int(Landmark.y*height)))
            print(" ")
            cv2.circle(frame,myHand[17],6,(255,0,255),-1)
            cv2.circle(frame,myHand[18],6,(255,0,255),-1)
            cv2.circle(frame,myHand[19],6,(255,0,255),-1)
            cv2.circle(frame,myHand[20],6,(255,0,255),-1)
            myHands.append(myHand)
            print(myHands)
    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam',0,0)
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
cam.release()