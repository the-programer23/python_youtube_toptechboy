import cv2
import time
print(cv2.__version__)

width=640
height=360

cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))

faceCascade = cv2.CascadeClassifier('haar\haarcascade_frontalface_default.xml')
eyesCascade = cv2.CascadeClassifier('haar\haarcascade_eye.xml')
fps=10
timeStamp = time.time()

while True:
    ignore, frame = cam.read()
    grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces=faceCascade.detectMultiScale(grayFrame,1.3,5)

    for face in faces:
        x,y,w,h=face
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),3)
                #frame[startRow:endRow,startColumn,endColumn]
        frameROI=frame[y:y+h,x:x+w]
        frameROIGray=cv2.cvtColor(frameROI,cv2.COLOR_BGR2GRAY)
        eyes=eyesCascade.detectMultiScale(frameROIGray)
        for eye in eyes:
            xEye,yEye,wEye,hEye=eye
            cv2.rectangle(frame[y:y+h,x:x+w],(xEye,yEye),(xEye+wEye,yEye+hEye),(255,0,0),2)

    loopTime=time.time()-timeStamp
    timeStamp=time.time()
    fpsNew=1/loopTime
    #low pass filter
    fps=.9*fps+.1*fpsNew    
    fps=int(fps)

    cv2.putText(frame,str(fps)+' fps',(5,40),cv2.FONT_HERSHEY_PLAIN,2,(255,0,0),2)

    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam',0,0)
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
cam.release()