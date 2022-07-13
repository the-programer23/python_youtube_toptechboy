import cv2
import numpy as np

evt=0
xVal=0
yVal=0

def onMouseClick(event,xPos,yPos,flags,params):
    global evt
    global xVal
    global yVal
    if event==cv2.EVENT_LBUTTONDOWN:
        print(event)
        xVal=xPos
        yVal=yPos
        evt=event
    if event==cv2.EVENT_RBUTTONUP:
        print(event)
        evt=event    


width=640
height=360

cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))

cv2.namedWindow('my WEBcam')
cv2.setMouseCallback('my WEBcam',onMouseClick)

while True:
    ignore, frame = cam.read()

    if evt==1:
        x=np.zeros([250,250,3],dtype=np.uint8)
        hsvFrame=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        #hsvFrame[row][column] gets one pixel
        clr=hsvFrame[yVal][xVal]
        print(clr)
        #convert each pixel to clr
        x[:,:]=clr
        cv2.putText(x,str(clr),(0,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,0),1)
        cv2.imshow('Color Picker',x)
        cv2.moveWindow('Color Picker',width,0)
        evt=0
    
    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam',0,0)
    
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
cam.release()