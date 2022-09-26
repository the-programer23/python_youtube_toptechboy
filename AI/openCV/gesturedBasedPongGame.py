import cv2
import random
print(cv2.__version__)

screenWidth=640*2
screenHeight=360*2-50

paddleTopLeft=0
paddleWidth=125
paddleHeight=25
paddleTopRight=paddleWidth
lifesCount=4

ballWasShot=False
restarting=False
gameOver=False


class mpHands:
    import mediapipe as mp
    def __init__(self,maxHands=2,tol1=.5,tol2=.5):
        self.hands=self.mp.solutions.hands.Hands(static_image_mode=False,max_num_hands=maxHands,min_detection_confidence=tol1,min_tracking_confidence=tol2)
    def Marks(self,frame):
        myHands=[]
        frameRGB=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        results=self.hands.process(frameRGB)
        if results.multi_hand_landmarks != None:
            for handLandMarks in results.multi_hand_landmarks:
                myHand=[]
                for landMark in handLandMarks.landmark:
                    myHand.append((int(landMark.x*screenWidth),int(landMark.y*screenHeight)))
                myHands.append(myHand)
        return myHands

class ball:
    def __init__(self,ballRadius=8,deltaX=18,deltaY=18):
        self.deltaX=deltaX
        self.deltaY=deltaY
        self.ballRadius=ballRadius
        self.rightWallEdge=screenWidth
        self.leftWallEdge=0
        self.ceilingWallEdge=0
        self.bottomWallEdge=screenHeight
        self.ballColor=(140,100,140)
        self.initPos()

    def initPos(self):
        self.ballXPos=random.randint(self.ballRadius,screenWidth-self.ballRadius)
        self.ballYPos=screenHeight-self.ballRadius
        
    def restart(self,frame):
        global restarting
        self.initPos()
        self.show(frame) 
        restarting = False

    def move(self,frame):
        global ballWasShot
        global lifesCount
        global restarting
        global gameOver
        ballWasShot=True
        self.ballXPos+=self.deltaX 
        self.ballYPos-=self.deltaY  
        Xrbe=self.ballXPos+self.ballRadius 
        Xlbe=self.ballXPos-self.ballRadius
        Ytbe=self.ballYPos-self.ballRadius
        Ybbe=self.ballYPos+self.ballRadius

        hitSideWall=Xlbe<=self.leftWallEdge or Xrbe>=self.rightWallEdge
        hitBottom=Ybbe>=self.bottomWallEdge
        hitPaddle=(Ytbe <= paddleHeight and (self.ballXPos >= paddleTopLeft and self.ballXPos <= paddleTopRight))
    
        if hitSideWall:
            self.deltaX*=-1
        if hitBottom or hitPaddle:
            self.deltaY*=-1
        if Ytbe <= 0:
            lifesCount-=1
            if lifesCount == 0:
                gameOver = True
                return
            restarting = True
            ballWasShot = False
            self.restart(frame)
            return     
        self.show(frame)

    def show(self, frame):    
        cv2.circle(frame,(int(self.ballXPos),int(self.ballYPos)),self.ballRadius,self.ballColor,-1)

def drawPaddel():
    global paddleTopLeft
    global paddleTopRight
    paddleBottomLeft=0
    paddleBottomRight=paddleHeight
    paddleColor=(0,255,0)
    for hand in handsData:
        indexTipX=hand[8][0]
        paddleTopLeft=int(indexTipX-paddleWidth/2)
        paddleTopRight=int(indexTipX+paddleWidth/2)
        if paddleTopRight >= screenWidth:
            paddleTopRight=int(screenWidth)
            paddleTopLeft=paddleTopRight-paddleWidth
        if paddleTopLeft <= 0:
            paddleTopLeft=0
            paddleTopRight=paddleWidth
    cv2.rectangle(frame,(paddleTopLeft,paddleBottomLeft),(paddleTopRight,paddleBottomRight),paddleColor,-1)

cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))

findHands=mpHands(1)
ball1=ball()

while True:
    ignore,  frame = cam.read()
    frame=cv2.flip(frame,1)
    frame=cv2.resize(frame,(int(screenWidth),int(screenHeight)))
             
    handsData=findHands.Marks(frame)
    drawPaddel()
    if not ballWasShot: ball1.show(frame)
    if not gameOver:
        if handsData or ballWasShot and not restarting: ball1.move(frame)
    cv2.putText(frame,'x '+str(lifesCount),(0,int(screenHeight)),cv2.FONT_HERSHEY_PLAIN,4,(255,0,0),6)  
    if gameOver: 
        cv2.putText(frame,'GAME OVER',(int(screenWidth/4.8),int(screenHeight/2)),cv2.FONT_HERSHEY_TRIPLEX,4,(0,0,255),6)
    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam',0,0) 
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
cam.release()