import cv2
print(cv2.__version__)

class mpHands:
    import mediapipe as mp
    def __init__(self,maxHands=2,tol1=.5,tol2=.5):
        self.hands=self.mp.solutions.hands.Hands(static_image_mode=False,max_num_hands=maxHands,min_detection_confidence=tol1,min_tracking_confidence=tol2)
    def Marks(self,frame):
        myHands=[]
        handsType=[]
        frameRGB=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        results=self.hands.process(frameRGB)
        if results.multi_hand_landmarks != None:
            for hand in results.multi_handedness:
                handType=hand.classification[0].label
                handsType.append(handType)
            for handLandMarks in results.multi_hand_landmarks:
                myHand=[]
                for landMark in handLandMarks.landmark:
                    myHand.append((int(landMark.x*width),int(landMark.y*height)))
                myHands.append(myHand)
        return myHands,handsType

width=int(640*1.6)
height=int(360*1.6)

cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
# cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
# cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))
findHands=mpHands(2)
paddleWidth=25
paddleHeight=125
paddleColor=(255,0,255)
ballRadius=18
ballColor=(255,0,0)
xPos=int(width/2)
yPos=int(height/2)
deltaX=6
deltaY=6
font=cv2.FONT_HERSHEY_SIMPLEX
fontHeight=5
fontWeight=5
fontColor=(0,0,255)
yLeftFingerTip=0
yRightFingerTip=0
scoreLeft=0
scoreRight=0
while True:
    ignore,  frame = cam.read()
    frame=cv2.flip(frame,1)
    frame=cv2.resize(frame,(width,height))
    cv2.circle(frame,(xPos,yPos),ballRadius,ballColor,-1)
    cv2.putText(frame,str(scoreLeft),(50,125),font,fontHeight,fontColor,fontWeight)
    cv2.putText(frame,str(scoreRight),(width-150,125),font,fontHeight,fontColor,fontWeight)
    handData,handsType=findHands.Marks(frame)
    for hand,handType in zip(handData,handsType):
        if handType == 'Left':
            yLeftFingerTip=hand[8][1]
        if handType == 'Right':
            yRightFingerTip=hand[8][1]
    cv2.rectangle(frame,(0,int(yLeftFingerTip-paddleHeight/2)),(paddleWidth,int(yLeftFingerTip+paddleHeight/2)),paddleColor,-1)   
    cv2.rectangle(frame,(width-paddleWidth,int(yRightFingerTip-paddleHeight/2)),(width,int(yRightFingerTip+paddleHeight/2)),paddleColor,-1)   
    topBallEdge=yPos-ballRadius
    bottomBallEdge=yPos+ballRadius
    rightBallEdge=xPos+ballRadius
    leftBallEdge=xPos-ballRadius
    if topBallEdge <= 0:
        deltaY*=-1
    if bottomBallEdge >= height:
        deltaY*=-1
    if leftBallEdge <= paddleWidth:
        if yPos>=int(yLeftFingerTip-paddleHeight/2) and yPos<=int(yLeftFingerTip+paddleHeight/2):
            deltaX*=-1
        else:
            xPos=int(width/2)
            yPos=int(height/2)
            scoreRight+=1 
    if rightBallEdge >= width-paddleWidth:
        if yPos>=int(yRightFingerTip-paddleHeight/2) and yPos<=int(yRightFingerTip+paddleHeight/2):
            deltaX*=-1
        else:
            xPos=int(width/2)
            yPos=int(height/2)
            scoreLeft+=1                 
    xPos+=deltaX
    yPos+=deltaY                                 
    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam',0,0)
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
cam.release()