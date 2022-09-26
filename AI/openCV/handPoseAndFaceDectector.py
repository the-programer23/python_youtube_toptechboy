import cv2
import mediapipe as mp
print(cv2.__version__)

class mpFaces:
    def __init__(self):
        self.findFace=mp.solutions.face_detection.FaceDetection()
    def Marks(self,frame):
        frameRGB=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        results=self.findFace.process(frameRGB)
        faceBoundingBoxes=[]
        if results.detections != None:
            for face in results.detections:
                bBox=face.location_data.relative_bounding_box
                topLeft=(int(bBox.xmin*width),int(bBox.ymin*height))
                bottomRight=(int((bBox.xmin+bBox.width)*width),int((bBox.ymin+bBox.height)*height))
                faceBoundingBoxes.append((topLeft,bottomRight))
        return faceBoundingBoxes    
    

class mpPose:
    def __init__(self,still=False,tol1=.5, tol2=.5):
        # Setup the Pose function for images - independently for the images standalone processing.
        # pose=mp.solutions.pose.Pose(static_image_mode=True, min_detection_confidence=0.5)
        # Setup the Pose function for videos - for video processing.
        self.myPose=mp.solutions.pose.Pose(static_image_mode=still,min_detection_confidence=tol1,min_tracking_confidence=tol2)
    def Marks(self,frame):
        frameRGB=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        results=self.myPose.process(frameRGB)
        poseLandmarks=[]
        if results.pose_landmarks:
            for lm in results.pose_landmarks.landmark:            
                poseLandmarks.append((int(lm.x*width),int(lm.y*height)))
        return poseLandmarks

class mpHands:
    def __init__(self,maxHands=2,tol1=.5,tol2=.5):
        self.hands=mp.solutions.hands.Hands(static_image_mode=False,max_num_hands=maxHands,min_detection_confidence=tol1,min_tracking_confidence=tol2)

    def Marks(self,frame):
        myHands=[]
        handsType=[]
        frameRGB=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        results=self.hands.process(frameRGB)
        if results.multi_hand_landmarks != None:
            #print(results.multi_handedness)
            for hand in results.multi_handedness:
                #print(hand)
                #print(hand.classification)
                #print(hand.classification[0])
                handType=hand.classification[0].label
                handsType.append(handType)
            for handLandMarks in results.multi_hand_landmarks:
                myHand=[]
                for landMark in handLandMarks.landmark:
                    myHand.append((int(landMark.x*width),int(landMark.y*height)))
                myHands.append(myHand)
        return myHands,handsType

width=1280
height=720

circleRadius=8
circleColor=(0,0,255)
circleThickness=2

cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))

findHands=mpHands(2)
poseLandMarks=mpPose()
findFaces=mpFaces()

while True:
    ignore,  frame = cam.read()
    # frame=cv2.resize(frame,(width,height))
    # handData, handsType=findHands.Marks(frame)
    hands,handsType=findHands.Marks(frame)
    for hand,handType in zip(hands,handsType):
        if handType == 'Right':
            label='Right'
        if handType == 'Left':
            label='Left'
        cv2.putText(frame,label,hand[8],cv2.FONT_HERSHEY_SIMPLEX,2,(0,0,255),2)
    bodyLandmarks=poseLandMarks.Marks(frame)            
    if bodyLandmarks != None:
        for bodyPart in [13,14,15,16]:
            cv2.circle(frame,bodyLandmarks[bodyPart],circleRadius,circleColor,circleThickness)
    faceBoundingBoxes=findFaces.Marks(frame)
    for faceBB in faceBoundingBoxes:
        cv2.rectangle(frame,faceBB[0],faceBB[1],(255,0,0),3)            
    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam',0,0)
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
cam.release()