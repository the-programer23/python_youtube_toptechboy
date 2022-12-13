import cv2
print(cv2.__version__)
import numpy as np

class mpHands:
    import mediapipe as mp
    def __init__(self,maxHands=2,tol1=.5,tol2=.5):
         self.hands=self.mp.solutions.hands.Hands(
            static_image_mode=False,
            max_num_hands=maxHands,
            min_detection_confidence=tol1,
            min_tracking_confidence=tol2)
    def Marks(self,frame):
        myHands=[]
        frameRGB=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        results=self.hands.process(frameRGB)
        if results.multi_hand_landmarks != None:
            for handLandMarks in results.multi_hand_landmarks:
                myHand=[]
                for landMark in handLandMarks.landmark:
                    myHand.append((int(landMark.x*width),int(landMark.y*height)))
                myHands.append(myHand)
        return myHands

def findDistances(handData):
    #np.zeros creates an array pf zeros so np.zeros(rows,columns,typeOfNumbers)
    distMatrix = np.zeros([len(handData),len(handData)],dtype='float')
    print(len(handData))
    print(distMatrix)
    for row in range(0,len(handData)):
        for column in range(0,len(handData)):
            # **2 = squared
            # **(1./2.) = square root 
            distMatrix[row][column]=((handData[row][0]-handData[column][0])**2+(handData[row][1]-handData[column][1])**2)**(1./2.)  
    return distMatrix

def findError(gestureMatrix,unknownMatrix,keyPoints):
    error=0
    for row in keyPoints:
        for column in keyPoints: 
            error+=abs(gestureMatrix[row][column]-unknownMatrix[row][column])
    return error        

width=1280
height=720
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))
findHands=mpHands(1)

keyPoints=[0,4,5,9,13,17,8,12,16,20]
train=True

while True:
    ignore,  frame = cam.read()
    frame=cv2.resize(frame,(width,height))
    handData=findHands.Marks(frame)
    print(handData)
    if train==True:
        if handData!=[]:
            cv2.putText(frame,'Show your gesture, press t when ready.',(30,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
            #cv2.waitKey(milliseconds)
            if cv2.waitKey(1) & 0xff==ord('t'):
                firstHand=handData[0]
                knownGesture=findDistances(firstHand)
                train=False
                print(knownGesture)
                print("==============")
    if train==False:
        if handData!=[]:
            unkownGesture=findDistances(handData[0])
                            #power to the ppl, power to the ppl, 
            error=findError(knownGesture,unkownGesture,keyPoints)      
            cv2.putText(frame,str(int(error)),(100,100),cv2.FONT_HERSHEY_SIMPLEX,2,(255,0,0),2)      
    for hand in handData:
        for ind in keyPoints :
            cv2.circle(frame,hand[ind],25,(255,0,255),3)
    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam',0,0)
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
cam.release()