import cv2 
import numpy as np
#convert frame to gray scale
#add color box to gray frame
#color box should bounce around
#the color box moves around and it's like a little window that colorises a portion of the gray frame

width=640
height=360

cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

swRowStart=150
swRowEnd=210

swColStart=250
swColEnd=390

deltaX=6
deltaY=6


while True:
    ignore, frame = cam.read()
    grayFrame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    grayFrameBGR=cv2.cvtColor(grayFrame,cv2.COLOR_GRAY2BGR)
    grayFrameBGR[swRowStart:swRowEnd,swColStart:swColEnd]=frame[swRowStart:swRowEnd,swColStart:swColEnd]

    cv2.rectangle(grayFrameBGR, (swColStart, swRowStart), (swColEnd, swRowEnd), (0,0,0), 2)

    cv2.imshow('my webcam', grayFrameBGR)
    cv2.moveWindow('my webcam',0,0)

    swRowStart += deltaY
    swRowEnd += deltaY

    swColStart += deltaX
    swColEnd += deltaX
    
    if swRowEnd >= height or swRowStart <= 0:
        deltaY*=-1
    if swColStart <= 0 or swColEnd >= width: 
        deltaX*=-1   

    if cv2.waitKey(1) & 0xff == ord('q'):
        break;
cam.release()    