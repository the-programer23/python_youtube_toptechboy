import time
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
    #np.zeros creates an array pf zeros so np.zeros(ros,columns,typeOfNumbers)
    distMatrix = np.zeros([len(handData),len(handData)],dtype='float')
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

def findGesture(unknownGesture,knownGestures,keyPoints,gestNames,tol):
    errorArray=[]
    for i in range(0,len(gestNames),1):
        error=findError(knownGestures[i],unknownGesture,keyPoints)
        errorArray.append(error)
    errorMin=errorArray[0]
    minIndex=0
    for i in range(0,len(errorArray),1):
        if errorArray[i]<errorMin: 
            errorMin=errorArray[i]
            minIndex=i
    if errorMin<tol:
        gesture=gestNames[minIndex]
    if errorMin>=tol:
        gesture='Unknown'
    return gesture                


width=int(1280/1.4)
height=int(720/1.4)
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))
findHands=mpHands(1)

keyPoints=[0,4,5,9,13,17,8,12,16,20]
train=True
tol=1500
trainCount=0
knownGestures=[]
time.sleep(1)
numGest=int(input('How many gestures do you want? '))
gestNames=[]
for i in range(0,numGest,1):
    prompt='Name of gesture # '+str(i+1)+': '
    name=input(prompt)
    gestNames.append(name)
print(gestNames)    
while True:
    ignore,  frame = cam.read()
    frame=cv2.resize(frame,(width,height))
    handData=findHands.Marks(frame)
    if train==True:
        if handData!=[]:
            cv2.putText(frame,'Please, show gesture ' + gestNames[trainCount]+': Press t when ready',(30,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
            #cv2.waitKey(milliseconds)
            if cv2.waitKey(1) & 0xff==ord('t'):
                firstHand=handData[0]
                knownGesture=findDistances(firstHand)
                knownGestures.append(knownGesture)
                trainCount+=1
                if trainCount==numGest:
                    train=False
                
    if train==False:
        if handData!=[]:
            unkownGesture=findDistances(handData[0])
            # error=findError(knownGesture,unkownGesture,keyPoints)      
            myGesture=findGesture(unkownGesture,knownGestures,keyPoints,gestNames,tol)
            cv2.putText(frame,myGesture,(100,100),cv2.FONT_HERSHEY_SIMPLEX,2,(255,0,0),2)      
    for hand in handData:
        for ind in keyPoints :
            cv2.circle(frame,hand[ind],25,(255,0,255),3)
    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam',0,0)
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
cam.release()