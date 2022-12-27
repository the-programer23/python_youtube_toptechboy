import time
import cv2
print(cv2.__version__)
import numpy as np
import pickle

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
        #if there is a hand on the frame
        if results.multi_hand_landmarks != None:
            for handLandMarks in results.multi_hand_landmarks:
                myHand=[]
                for landMark in handLandMarks.landmark:
                    #landMark.x is the % of the widtd of the frame and 
                    # the result of landMark.x*width is the amount of pixes from the left side of the screen
                    # to the landMark 
                    myHand.append((int(landMark.x*width),int(landMark.y*height)))
                myHands.append(myHand)
        return myHands

def findDistances(handData):
    #np.zeros creates an array of zeros so np.zeros([rows,columns],typeOfNumbers)
    distMatrix = np.zeros([len(handData),len(handData)],dtype='float')
    # print(distMatrix)
    landMark0Xpos = handData[0][0] 
    landMark9Xpos = handData[9][0]
    landMark0Ypos = handData[0][1]
    landMark9Ypos = handData[9][1]
    #this is the equation in the equation.jpg  #((608-608)**2+(332-254)**2)**(1./2.) = ((0)+(6084))**(1./2.) = 78
    palmSize=((landMark0Xpos-landMark9Xpos)**2+(landMark0Ypos-landMark9Ypos)**2)**(1./2.)  
    for row in range(0,len(handData)):
        for column in range(0,len(handData)):
            # **2 = squared
            # **(1./2.) = square root 
            # (((626-588)**2+(336-318)**2)**(1./2.)) = (1444)+(324)**(1./2.)/palmSize
            x0 = handData[row][0]
            x1 = handData[column][0]
            y0 = handData[row][1]
            y1 = handData[column][1]
            distMatrixElement = (((x0-x1)**2+(y0-y1)**2)**(1./2.))/palmSize  
            distMatrix[row][column]=distMatrixElement
    return distMatrix

def findError(gestureMatrix,unknownMatrix,keyPoints):
    error=0
    for row in keyPoints:
        for column in keyPoints: 
            error+=abs(gestureMatrix[row][column]-unknownMatrix[row][column])
    print(error)        
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
# cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
# cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))

findHands=mpHands(1)

keyPoints=[0,4,5,9,13,17,8,12,16,20]
time.sleep(1)
train=int(input('Press 1 to train, press 0 to recognize '))

if train==1:
    trainCount=0
    knownGestures=[]
    #pauses the program for 1 second
    time.sleep(1) 
    numGest=int(input('How many gestures do you want? '))
    gestNames=[]
    for i in range(0,numGest,1):
        prompt='Name of gesture # '+str(i+1)+': '
        name=input(prompt)
        gestNames.append(name)
    # print(gestNames)  
    trainName=input('Filename for training data? (Press enter for default) ')
    if trainName=='':
        trainName='default'
    trainName+='.pkl'
if train==0:
    trainName=input('What training data do you want to use? (Press Enter for default) ')
    if trainName=='':
        trainName='default'
    trainName+='.pkl'    
    with open(trainName,'rb') as file:
        gestNames=pickle.load(file)    
        knownGestures=pickle.load(file)
tol=15

  

while True:
    ignore,  frame = cam.read()
    frame=cv2.resize(frame,(width,height))
    # handData is an array with 20 tuples, each tuple has the x and y coordinates of a landMark
    handData=findHands.Marks(frame)
    
    if train==1:
        if handData!=[]:
            print(handData)
            cv2.putText(frame,'Please, show gesture ' + gestNames[trainCount]+': Press t when ready',(20,20),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),1)
            #cv2.waitKey(milliseconds)
            if cv2.waitKey(1) & 0xff==ord('t'): #check if user pressed t
                firstHand=handData[0]
                knownGesture=findDistances(firstHand)
                knownGestures.append(knownGesture)
                trainCount+=1
                if trainCount==numGest:
                    train=0   
                    with open(trainName,'wb') as f:
                        pickle.dump(gestNames,f)
                        pickle.dump(knownGestures,f)
    if train==0:
        if handData!=[]:
            unkownGesture=findDistances(handData[0])
            # error=findError(knownGesture,unkownGesture,keyPoints)      
            myGesture=findGesture(unkownGesture,knownGestures,keyPoints,gestNames,tol)
            cv2.putText(frame,myGesture,(100,100),cv2.FONT_HERSHEY_SIMPLEX,2,(255,0,0),2)      
    
    
    for hand in handData:
        for ind in keyPoints :
            cv2.circle(frame,hand[ind],14,(255,0,255),3)
    
    
    cv2.imshow('my WEBcam', frame)
    # cv2.moveWindow('my WEBcam',0,0)
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
cam.release()