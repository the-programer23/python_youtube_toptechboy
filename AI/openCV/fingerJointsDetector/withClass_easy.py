from ntpath import join
import cv2
print(cv2.__version__)
width=1280
height=720

class mpHands:
    import mediapipe as mp
    #if the parameter maxHands is not received the default is 2
    def __init__(self,maxHands=2,tol1=.5,tol2=.5):
        self.hands=self.mp.solutions.hands.Hands(static_image_mode=False,max_num_hands=maxHands,min_detection_confidence=tol1,min_tracking_confidence=tol2)
    def Marks(self,frame):
        myHands=[]
        myFrameRGB=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB) 
        results=self.hands.process(myFrameRGB)
        if results.multi_hand_landmarks != None: 
            for handLandMark in results.multi_hand_landmarks:
                myHand=[]
                for landmark in handLandMark.landmark:
                    myHand.append((int(landmark.x*width),int(landmark.y*height)))
                myHands.append(myHand)    
        return myHands
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))

findHands=mpHands(1)

while True:
    ignore,  frame = cam.read()
    myHands=findHands.Marks(frame)
    for myHand in myHands:
        for joint in [0,5,6,7,8]:
            cv2.circle(frame,myHand[joint],12,(255,0,255),3)
    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam',0,0)
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
cam.release()