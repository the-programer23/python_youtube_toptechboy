import cv2
print(cv2.__version__)
width=1280
height=720
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))


circleRadius=4
circleColor=(0,0,255)
circleThickness=-1

class mpPose:
    import mediapipe as mp
    def __init__(self,tol1=.7,tol2=.7):
        # Setup the Pose function for images - independently for the images standalone processing.
        # pose=mp.solutions.pose.Pose(static_image_mode=True, min_detection_confidence=0.5)
        # Setup the Pose function for videos - for video processing.
        self.pose=self.mp.solutions.pose.Pose(static_image_mode=False, min_detection_confidence=tol1,min_tracking_confidence=tol2)
        self.mpDraw=self.mp.solutions.drawing_utils
    def landMarks(self,frame):
        frameRGB=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        results=self.pose.process(frameRGB)
        landMarks=[]
        if results.pose_landmarks != None:
            # Draws landsmarks on the body
            # mpDraw.draw_landmarks(frame,results.pose_landmarks,mp.solutions.pose.POSE_CONNECTIONS)

            #prints 33 landmarks
            # print(results.pose_landmarks)
            # print(results.pose_landmarks.landmark)
            for landmark in results.pose_landmarks.landmark:
                landMarks.append((int(landmark.x*width),int(landmark.y*height)))
        return landMarks                     
findBody=mpPose()
while True:
    ignore,  frame = cam.read()
    bodyLandmarks=findBody.landMarks(frame)
    for landmark in bodyLandmarks:
        for bodyPart in [0,2,5]:
            cv2.circle(frame,bodyLandmarks[bodyPart],circleRadius,circleColor,circleThickness)
        
    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam',0,0)
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
cam.release()